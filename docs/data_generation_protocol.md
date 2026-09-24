# Data Generation and Provenance

## Main 2,500-record resource

The main T-Code resource was created through an AI-assisted, human-curated synthetic workflow.

- Approximate date of candidate generation: around 20 May 2026
- Tool: OpenAI GPT-5.0
- Access: ChatGPT web application
- Role of the model: generation of candidate Turkish computer-control command text
- Human role: screening, rejection, rewriting, and enrichment of candidate commands
- Gold annotation role: all structured annotations were created and verified manually

The retained command set was not accepted automatically from model output. Unnatural, unsuitable, repetitive, or task-inconsistent candidates were rejected or rewritten. During iterative curation, colloquial and regional wording, correction patterns, negation, disfluency-like forms, and simulated speech-recognition-style surface variation were introduced or revised manually.

The original exact candidate-generation prompt transcript was not retained. No replacement prompt is reconstructed here.

## Gold annotations

GPT-5.0 was not used to create the final gold structured annotation fields. Task segmentation, task labels, tokens, boundary labels, and task-token labels were created and checked manually.

## Human-authored material

The following materials were manually authored rather than generated with GPT:

- the 200-record error-driven augmentation block;
- the 100-command human-written challenge set.

The augmentation block was created after challenge-set error analysis and was added only to the training partition. Challenge records themselves were not inserted into training.

## Interpretation

T-Code should be treated as an AI-assisted, human-curated synthetic benchmark, not as a population sample of naturally occurring Turkish user traffic. The `source_type` field records construction categories and should not be interpreted as observed population frequencies.
