from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def read_jsonl(path: Path) -> list[dict]:
    records: list[dict] = []
    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON on line {line_no} of {path}: {exc}") from exc
    return records


def load_inventory(path: Path) -> set[str]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    labels = payload.get("labels", [])
    if payload.get("label_count") != len(labels):
        raise ValueError(f"label_count does not match labels in {path}")
    return set(labels)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/final/tcode_v4_2700.jsonl")
    parser.add_argument("--boundary-labels", default="data/labels/boundary_labels_3.json")
    parser.add_argument("--task-labels", default="data/labels/task_token_labels_33.json")
    parser.add_argument("--out", default="results/dataset_validation_summary.json")
    args = parser.parse_args()

    records = read_jsonl(Path(args.input))
    boundary_inventory = load_inventory(Path(args.boundary_labels))
    task_inventory = load_inventory(Path(args.task_labels))

    errors: list[dict] = []
    ids: list[str | None] = []
    raws: list[str | None] = []

    required_fields = {
        "id",
        "raw_command",
        "task_count",
        "task_segments",
        "task_labels",
        "tokens",
        "boundary_labels",
        "task_token_labels",
        "domain",
    }

    for record in records:
        rec_id = record.get("id")
        ids.append(rec_id)
        raws.append(record.get("raw_command"))

        missing = sorted(required_fields.difference(record))
        if missing:
            errors.append({"id": rec_id, "error": "missing_required_fields", "fields": missing})

        tokens = record.get("tokens", [])
        boundary = record.get("boundary_labels", [])
        task_tokens = record.get("task_token_labels", [])
        segments = record.get("task_segments", [])
        task_labels = record.get("task_labels", [])

        if len(tokens) != len(boundary):
            errors.append({"id": rec_id, "error": "tokens_boundary_length_mismatch"})
        if len(tokens) != len(task_tokens):
            errors.append({"id": rec_id, "error": "tokens_task_token_length_mismatch"})
        if len(segments) != len(task_labels):
            errors.append({"id": rec_id, "error": "segments_task_labels_length_mismatch"})
        if record.get("task_count") != len(task_labels):
            errors.append({"id": rec_id, "error": "task_count_mismatch"})

        invalid_boundary = sorted(set(boundary).difference(boundary_inventory))
        if invalid_boundary:
            errors.append({"id": rec_id, "error": "invalid_boundary_labels", "labels": invalid_boundary})

        invalid_task_tokens = sorted(set(task_tokens).difference(task_inventory))
        if invalid_task_tokens:
            errors.append({"id": rec_id, "error": "invalid_task_token_labels", "labels": invalid_task_tokens})

        invalid_task_labels = sorted(set(task_labels).difference(task_inventory - {"O"}))
        if invalid_task_labels:
            errors.append({"id": rec_id, "error": "invalid_task_labels", "labels": invalid_task_labels})

    summary = {
        "record_count": len(records),
        "domain_distribution": dict(Counter(record.get("domain", "unknown") for record in records)),
        "task_count_distribution": dict(Counter(str(record.get("task_count", "unknown")) for record in records)),
        "duplicate_id_count": sum(1 for count in Counter(ids).values() if count > 1),
        "duplicate_raw_command_count": sum(1 for count in Counter(raws).values() if count > 1),
        "boundary_label_count": len(boundary_inventory),
        "task_token_label_count": len(task_inventory),
        "error_count": len(errors),
        "errors_preview": errors[:50],
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
