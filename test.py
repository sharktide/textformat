# test_textfmt.py

from textformat import TextFormat, WordArt, TableFormatter, bcolors, progress

def test_text_formatting():
    print(TextFormat.style("Bold Text", TextFormat.BOLD))
    print(TextFormat.style("Red Warning", TextFormat.COLORS["red"]))
    print(TextFormat.style("Blue Underline", TextFormat.UNDERLINE, TextFormat.COLORS["blue"]))
    print(f"{bcolors.OKGREEN}Simple mode{bcolors.ENDC}")

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

from textformat.progress import Colors, DownloadProgressBar
from pathlib import Path
import requests

def download_with_progress(url: str, output_path: Path, download_color, complete_color):
    response = requests.get(url, stream=True)
    total = int(response.headers.get('content-length', 0))

    if response.status_code != 200:
        raise Exception(f"Failed to download from {url}. HTTP status: {response.status_code}")

    progress = DownloadProgressBar(total, prefix=output_path.name, 
                           download_color=download_color, complete_color=complete_color)
    with open(output_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
                progress.update(progress.downloaded + len(chunk))
    print()

if __name__ == "__main__":
    print("Running textfmt tests...\n")
    test_text_formatting()
    print("\n")
    test_word_art()
    print("\n")
    test_table()
    print("\n")
    download_with_progress('https://huggingface.co/sharktide/recyclebot0/resolve/main/tf_model.h5', Path("example/tf_model.h5"), Colors.CYAN, Colors.GREEN)
    print("\nTests completed successfully!")


