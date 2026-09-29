# PDF libraries

Checked for ObzueAI Professor scripts, which must download from the browser and keep the language the room is using.

| Library | Fit |
|---|---|
| pdf-lib | Use this. It is already installed. It runs in the window, so a published app can still make a PDF. Its built-in fonts are Latin-only, so the script is drawn by the browser and embedded as pages. |
| jsPDF | Smaller, and Unicode needs a font file you ship. Easy to break on Chinese, Arabic, and Hindi. |
| PDFKit | A Node tool. It does not belong in the window. |
| Chromium print | The sharpest print in this workspace, and it is not available after the app is published. |

pdf-lib reads the shell of a PDF: page count, title, author, and form-field names. It does not read the sentences on the page. Those come from PDF.js. ObzueAI Professor uses both. A scanned page with no text layer still opens, and the reading stays empty until someone types the passage.

A script download still uses pdf-lib. The title is ObzueAI Professor, the author is Corta, and the pages are numbered. The words are drawn by the browser first, then embedded, so the lesson language survives.
