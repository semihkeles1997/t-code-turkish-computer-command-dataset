# T-Code v4: Turkish Computer-Control Command Dataset

This repository contains the T-Code v4 dataset and retained experimental materials for token-level decomposition of compound Turkish computer-control commands.

## Overview

T-Code v4 contains 2,700 designed textual command records across four balanced domains (675 records per domain):

- `temel_bilgisayar`
- `tarayıcı_internet`
- `ofis_metin_düzenleme`
- `dosya_yazılım_geliştirme`

Each record includes the command text together with task segments, task labels, tokens, boundary labels, and task-token labels. The task-token inventory contains 33 classes including `O`; the boundary inventory contains `B-TASK`, `I-TASK`, and `O`.

The resource consists of designed textual examples rather than deployed-user interaction logs. It should therefore be treated as a purpose-built research benchmark, not as a population sample of naturally occurring Turkish computer-control traffic.

## Canonical data files

- `data/final/tcode_v4_2700.jsonl` — final 2,700-record resource
- `data/intermediate/t_code_dataset_v4_1600.jsonl` — development-stage 1,600-record version
- `data/intermediate/t_code_dataset_v4_2500.jsonl` — 2,500-record main resource before final augmentation
- `data/augmentation/tcode_v4_aug_200_clean_CK3703_CK3902.jsonl` — 200-record final training augmentation block
- `data/challenge/challenge_gold_100.jsonl` — separately prepared 100-command human-written challenge set
- `data/challenge/challenge_filtered_99_excluding_identified_neardup.jsonl` — 99-command challenge variant excluding one pre-identified near-duplicate
- `data/labels/task_token_labels_33.json` — final task-token label inventory
- `data/labels/boundary_labels_3.json` — boundary-label inventory

The 99-command challenge variant removes the one near-duplicate identified during the pre-augmentation review. Because later augmentation was informed by challenge-set error patterns, this variant should not be interpreted as proof of complete decontamination relative to the final augmented training data.

## Final benchmark partitions

The final resource contains 2,200 training records, 250 validation records, and 250 internal-test records. The 100-command and 99-command challenge sets are separate evaluation material and are not part of the 2,700-record resource. See `docs/data_splits.md` for the retained ID information and interpretation notes.

## Main experiments

The accompanying manuscript compares:

- BiLSTM-CRF
- mBERT
- XLM-RoBERTa-base
- BERTurk

Retained outputs for the final internal test and challenge evaluations are stored under `results/`. The repository also contains the development-stage challenge analysis, human inter-annotator agreement material, and the LLM-assisted consistency audit described in the manuscript.

## Reproducibility scope

This repository preserves the released datasets, fixed evaluation material, result files, documentation, and utility scripts that were retained from the study. It does **not** provide a complete reconstruction of every historical model-training environment. Some low-level training settings from the original runs were not retained consistently and are therefore not reconstructed from assumed defaults.

The scripts under `scripts/` support structural dataset validation and inter-annotator agreement calculations; they should not be interpreted as the complete original training pipeline.

## Repository structure

- `data/final` — final 2,700-record dataset
- `data/intermediate` — 1,600- and 2,500-record development-stage datasets
- `data/challenge` — challenge evaluation material
- `data/augmentation` — final 200-record augmentation material
- `data/labels` — final label inventories and descriptions
- `data/second_annotator` — final 300-command blind re-annotation material
- `scripts` — structural validation and inter-annotator agreement utilities
- `results` — retained benchmark and analysis outputs
- `llm_audit` — supplementary LLM-assisted consistency-audit material
- `models` — notes about model checkpoints
- `docs` — annotation, split, audit, and dataset documentation

## Safety and intended use

T-Code is intended for research on command decomposition and sequence labelling. A predicted command decomposition should not itself be treated as authorization to execute destructive or consequential computer actions. Any downstream execution system requires its own confirmation, permission, state-tracking, and recovery mechanisms.

## Citation

Please cite the accompanying manuscript if you use this dataset or the retained benchmark materials. Repository citation metadata are provided in `CITATION.cff`.
