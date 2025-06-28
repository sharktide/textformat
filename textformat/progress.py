import requests
import time
from pathlib import Path
import sys

# Define color codes for terminal (ANSI escape codes)
class Colors:
    RESET = "\033[0m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    LIGHT_GREEN = "\033[92m"
    LIGHT_BLUE = "\033[94m"
    LIGHT_RED = "\033[91m"
    LIGHT_YELLOW = "\033[93m"
    LIGHT_MAGENTA = "\033[95m"
    LIGHT_CYAN = "\033[96m"

    ALL_COLORS = [
        GREEN, BLUE, RED, YELLOW, MAGENTA, CYAN, WHITE,
        LIGHT_GREEN, LIGHT_BLUE, LIGHT_RED, LIGHT_YELLOW, LIGHT_MAGENTA, LIGHT_CYAN
    ]

class DownloadProgressBar:
    def __init__(self, total, prefix='', length=40, fill='━', empty=' ', print_end="\r",
                 download_color=Colors.GREEN, complete_color=Colors.BLUE):
        self.total = total
        self.prefix = prefix
        self.length = length
        self.fill = fill
        self.empty = empty
        self.print_end = print_end
        self.download_color = download_color
        self.complete_color = complete_color
        self.start_time = time.time()
        self.downloaded = 0

    def update(self, downloaded):
        now = time.time()
        self.downloaded = downloaded

        if self.total > 0:
            percent = 100 * (self.downloaded / float(self.total))
            filled_length = int(self.length * self.downloaded // self.total)
            total_size = self.format_size(self.total)
        else:
            percent = 100
            filled_length = 40
            total_size = "?"

        bar = self.fill * filled_length + self.empty * (self.length - filled_length)
        current_size = self.format_size(self.downloaded)

        # Speed (bytes per second)
        elapsed = now - self.start_time
        speed_bps = self.downloaded / elapsed if elapsed > 0 else 0
        speed_str = self.format_size(speed_bps) + "/s" if speed_bps > 0 else "?"

        # ETA
        remaining = self.total - self.downloaded if self.total > 0 else 0
        eta_seconds = remaining / speed_bps if self.total > 0 and speed_bps > 0 else 0
        eta_str = self.format_time(eta_seconds) if self.total > 0 else "?"

        # Choose color
        color = self.complete_color if self.downloaded == self.total and self.total > 0 else self.download_color

        # Print
        sys.stdout.write(
            f'\r{self.prefix} {color}{bar}{Colors.RESET} {percent:5.1f}% • '
            f'{current_size}/{total_size} • {speed_str} • {eta_str}'
        )
        sys.stdout.flush()

        if self.downloaded == self.total and self.total > 0:
            sys.stdout.write(self.print_end)
            sys.stdout.flush()

    @staticmethod
    def format_size(size_in_bytes):
        """Format the size in a human-readable format."""
        for unit in ['B', 'KiB', 'MiB', 'GiB', 'TiB']:
            if size_in_bytes < 1024:
                return f"{size_in_bytes:.1f} {unit}"
            size_in_bytes /= 1024
        return f"{size_in_bytes:.1f} PiB"

    @staticmethod
    def format_time(seconds):
        """Format seconds into H:MM:SS or M:SS."""
        if seconds < 0.1:
            return "0:00"
        m, s = divmod(int(seconds + 0.5), 60)
        h, m = divmod(m, 60)
        return f"{h}:{m:02}:{s:02}" if h else f"{m}:{s:02}"
