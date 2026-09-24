# Reproducibility Notes

This repository preserves fixed data, evaluation material, prediction/error files, and retained model metadata. It does not claim byte-for-byte reconstruction of every historical training environment.

## Final BERTurk run

The following settings were recovered from the archived final BERTurk checkpoint metadata:

- base model: `dbmdz/bert-base-turkish-cased`
- task: 33-class `task_token_labels` token classification
- train / validation / internal test: 2,200 / 250 / 250 records
- epochs: 5
- tokenizer truncation length: 128
- learning rate: `2e-5`
- train batch size: 16
- evaluation batch size: 32
- optimizer: `adamw_torch_fused`
- weight decay: 0.01
- Adam beta1 / beta2 / epsilon: 0.9 / 0.999 / `1e-8`
- scheduler: linear
- warm-up steps: 0
- gradient accumulation: 1
- max gradient norm: 1.0
- FP16: enabled
- random seed: 42
- evaluation strategy: once per epoch
- best-model metric: `macro_f1`
- `load_best_model_at_end`: true
- archived Transformers version: 5.8.1
- hardware: Tesla T4 GPU

A machine-readable copy is stored in `results/berturk_final_2700/training_configuration.json`.

## BiLSTM-CRF

The archived model configuration preserves:

- vocabulary size: 2,235
- embedding dimension: 128
- BiLSTM hidden dimension: 256
- dropout: 0.35
- output labels: 33
- maximum observed training history: 40 epochs
- retained best epoch: 32
- validation macro-F1 at retained best epoch: 0.9352494598

A machine-readable copy is stored in `models/bilstm_crf_model_config.json`.

## mBERT and XLM-RoBERTa-base

The retained results identify the base checkpoints as `bert-base-multilingual-cased` and `xlm-roberta-base`, respectively, and record five-epoch fine-tuning on the same benchmark partitions. Complete low-level optimizer/scheduler metadata were not retained uniformly for these reruns and are therefore not reconstructed from assumed defaults.
