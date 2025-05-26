# test_textfmt.py

from textformat import TextFormat, WordArt, TableFormatter

def test_text_formatting():
    print(TextFormat.style("Bold Text", TextFormat.BOLD))
    print(TextFormat.style("Red Warning", TextFormat.COLORS["red"]))
    print(TextFormat.style("Blue Underline", TextFormat.UNDERLINE, TextFormat.COLORS["blue"]))

def test_word_art():
    print(WordArt.banner("TEXTFMT", char="*", width=40))

def test_table():
    headers = ["Feature", "Color", "Effect"]
    data = [
        ["Bold", "White", "Strong emphasis"],
        ["Underline", "Blue", "Text decoration"],
        ["Warning", "Yellow", "Cautionary message"],
    ]
    print(TableFormatter.generate(headers, data))

if __name__ == "__main__":
    print("Running textfmt tests...\n")
    test_text_formatting()
    print("\n")
    test_word_art()
    print("\n")
    test_table()
    print("\nTests completed successfully!")
