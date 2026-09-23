# T-Code v4 Label Descriptions

These descriptions document the action ontology used in T-Code v4. They are intended to clarify the released benchmark labels rather than define a universal taxonomy of computer interaction.

## Task-token labels

| Label | Description |
|---|---|
| `O` | Token outside an executable task segment. |
| `ARA` | Performs a search or query operation, typically through a search field or search interface. |
| `ARTIR` | Increases a value, level, size, volume, or similar adjustable property. |
| `AZALT` | Decreases a value, level, size, volume, or similar adjustable property. |
| `AÇ` | Opens an existing file, application, window, page, or interface element. |
| `BOŞLUK` | Inserts or leaves a space in text. |
| `BUL` | Locates a specified item, text, file, result, or target within the current context. |
| `BÜYÜT` | Enlarges or zooms in on displayed content or an interface element. |
| `DEĞİŞTİR` | Changes an existing value, setting, format, or content. |
| `DİĞER` | Executable operation that is not covered by a more specific T-Code v4 action class. |
| `ENTER` | Performs an Enter/Return key action. |
| `GEÇ` | Transitions to another window, field, panel, slide, or interface area. |
| `GÖNDER` | Sends a message, form, request, or other content. |
| `GİT` | Navigates to a specified location, directory, section, or destination. |
| `KAPAT` | Closes an application, window, tab, panel, or other interface element. |
| `KAYDET` | Saves the current file, document, state, or content. |
| `KAYDIR` | Scrolls or shifts the current view in a specified direction. |
| `KES` | Performs a cut operation on selected or specified content. |
| `KOPYALA` | Copies selected or specified content. |
| `KÜÇÜLT` | Reduces the size or zoom level of displayed content or an interface element. |
| `SEKME_DEĞİŞTİR` | Switches from the current browser or application tab to another tab. |
| `SEÇ` | Selects a specified item, region, text, cell, or interface element. |
| `SİL` | Deletes or removes specified content or an item. |
| `TAŞI` | Moves an item or interface element to another position or location. |
| `TIKLA` | Activates an interface element by clicking or pressing it. |
| `YAPIŞTIR` | Pastes previously copied or cut content. |
| `YAZ` | Types or enters specified textual content. |
| `YAZDIR` | Prints a document, file, page, or other printable content. |
| `YENİDEN_ADLANDIR` | Changes the name of an existing item. |
| `YENİ_OLUŞTUR` | Creates a new file, document, folder, object, or similar item. |
| `YÜKLE` | Uploads a file or other content. |
| `YİNELE` | Repeats or reruns an operation, including page refresh/reload where applicable. |
| `İNDİR` | Downloads a file or other content. |

## Boundary labels

| Label | Description |
|---|---|
| `B-TASK` | Beginning token of an executable task segment. |
| `I-TASK` | Continuation token of the same executable task segment. |
| `O` | Token outside an executable task segment. |
