# Data Splits

The final T-Code v4 resource contains 2,700 records. The retained benchmark protocol uses the following partitions:

| Split | Records | Retained ID information | Role |
|---|---:|---|---|
| Training | 2,200 | 2,000 main-resource training records plus `CK-3703`–`CK-3902` augmentation | Model training |
| Validation | 250 | `CK-3203`–`CK-3452` | Model selection / early stopping |
| Internal test | 250 | `CK-3453`–`CK-3702` | Fixed ID/batch holdout evaluation |
| Challenge test | 100 | `CH-0001`–`CH-0100` | Separately prepared wording-shift evaluation |
| Filtered challenge variant | 99 | Challenge set with one pre-identified near-duplicate removed | Sensitivity check |

The 2,000-record main-resource training partition is not described as one continuous ID interval because the historical ID sequence contains gaps. The validation and internal-test ranges above are retained explicitly and are not part of training.

The 100-command and 99-command challenge sets are outside the 2,700-record resource. Challenge-set error patterns later informed the construction of the 200-record augmentation block, although challenge records themselves were not added to training. Post-augmentation challenge results should therefore be interpreted as error-informed stress-test results rather than as pristine once-only external validation.
