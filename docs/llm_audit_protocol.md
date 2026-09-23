# LLM-Assisted Consistency Audit

The LLM audit is an auxiliary quality-control process and is **not** treated as human inter-annotator agreement.

A 200-command subset was evaluated with hosted LLM outputs and compared with the released gold labels under structural checks such as sequence-length and label-inventory validation. ChatGPT and Gemini form the main audit reported in the accompanying manuscript.

A preliminary DeepSeek run is retained in the repository for transparency, but schema-compliance problems prevented it from being treated as part of the main audit comparison. LLM agreement with the gold labels is therefore used only as a supplementary consistency signal, not as an independent gold standard.

Hosted model behavior can change over time, and the exact historical hosted model versions were not retained sufficiently to claim exact rerun reproducibility.
