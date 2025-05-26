# textfmt

A lightweight Python module for ANSI text formatting, customizable word art, and table rendering in CLI applications.

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
import textfmt

print(textfmt.TextFmt.style("Hello, World!", textfmt.TextFmt.BOLD, textfmt.TextFmt.COLORS["blue"]))
```

Custom Word Art Banner
```python
import textfmt.word_art

print(textfmt.word_art.WordArt.banner("TEXTFMT", char="*", width=40))
```

Table Rendering
```python
import textfmt.table

headers = ["Name", "Color", "Effect"]
data = [
    ["Bold", "White", "Strong emphasis"],
    ["Underline", "Blue", "Text decoration"],
    ["Warning", "Yellow", "Cautionary message"],
]

print(textfmt.table.TableFormatter.generate(headers, data))
```
## License
MIT License – Free to use and modify.