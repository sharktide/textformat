# TextFormat

TextFormat is a lightweight Python module for ANSI text formatting, customizable word art, and table rendering in CLI applications.

## Features
- **ANSI Colors & Styles** – Easily format text using intuitive color mappings.
- **Customizable Word Art** – Generate banners with adjustable characters and widths.
- **Table Formatting** – Display structured data in a clean, readable format.

## Installation
Install via PyPI:
```sh
pip install textformat
```

## Usage
Basic Text Formatting
```python
from textformat import TextFormat

print(TextFormat.style("Hello, World!", TextFormat.BOLD, TextFormat.COLORS["blue"]))
```

Custom Word Art Banner

```python
from textformat.word_art import WordArt

print(WordArt.banner("TEXTFORMAT", char="*", width=40))
```

Table Rendering
```python
from textformat.table import TableFormatter

headers = ["Feature", "Color", "Effect"]
data = [
    ["Bold", "White", "Strong emphasis"],
    ["Underline", "Blue", "Text decoration"],
    ["Warning", "Yellow", "Cautionary message"],
]

print(TableFormatter.generate(headers, data))
```

## License

MIT License – Free to use and modify.
