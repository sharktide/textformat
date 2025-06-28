# textfmt/__init__.py
from .textformat import TextFormat, bcolors, enable_windows_ansi_support
from .word_art import WordArt
from .table import TableFormatter
import os

enable_windows_ansi_support()

__all__ = ["TextFormat", "bcolors", "WordArt", "TableFormatter", "enable_windows_ansi_support"]
