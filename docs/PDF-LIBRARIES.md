# PDF libraries

Checked for ObzueAI Professor scripts, which must download from the browser and keep the language the room is using.

| Library | Fit |
|---|---|
| pdf-lib | Use this. It is already installed. It runs in the window, so a published app can still make a PDF. Its built-in fonts are Latin-only, so the script is drawn by the browser and embedded as pages. |
| jsPDF | Smaller, and Unicode needs a font file you ship. Easy to break on Chinese, Arabic, and Hindi. |
| PDFKit | A Node tool. It does not belong in the window. |
| Chromium print | The sharpest print in this workspace, and it is not available after the app is published. |

Do not add a second PDF library unless pdf-lib cannot draw the page.
