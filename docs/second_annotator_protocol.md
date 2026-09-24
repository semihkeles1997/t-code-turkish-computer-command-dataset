# Second Annotator Protocol

A second annotator blindly re-annotated a subset of 300 commands from the final resource.


The second annotator had a computer-engineering background and technical familiarity with computer systems and the operations represented in the resource.

The released 300-command subset was selected with random seed 42 and contains 75 commands from each of the four domains. The released summary also records the distribution by task count.

The annotator received only:

- `id`
- `domain`
- `raw_command`
- `tokens`

The annotator did not receive:

- `normalized_command`
- `task_segments`
- `task_labels`
- `boundary_labels`
- `task_token_labels`

Agreement was calculated at token level, separately for boundary labels and task-token labels, using Cohen's kappa. The blind material, gold material, anonymized completed annotations, and summary metadata are retained under `data/second_annotator/`.
