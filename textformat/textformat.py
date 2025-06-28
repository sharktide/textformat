import os

def enable_windows_ansi_support() -> None:
    """
    Enables ANSI escape sequence support in Windows terminals (safe version).
    """
    if os.name == 'nt':
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            handle = kernel32.GetStdHandle(-11)
            mode = ctypes.c_ulong()
            if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
                mode.value |= 0x0004
                kernel32.SetConsoleMode(handle, mode)
        except Exception:
            pass

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    NOTE = '\x1b[35m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
class TextFormat:
    """ ANSI Escape Code Formatting for Python CLI Output """
    RESET = "\x1b[0m"

    BOLD = "\x1b[1m"  # Basic bold without a color

    UNDERLINE = "\x1b[4m"  # Add this line for underline support

    COLORS = {
        "black": "\x1b[30m", "blue": "\x1b[34m", "cyan": "\x1b[36m",
        "green": "\x1b[32m", "grey": "\x1b[90m", "magenta": "\x1b[35m",
        "red": "\x1b[31m", "white": "\x1b[37m", "yellow": "\x1b[33m"
    }

    BOLD_COLORS = {
        "black": "\x1b[1;30m", "blue": "\x1b[1;34m", "cyan": "\x1b[1;36m",
        "green": "\x1b[1;32m", "magenta": "\x1b[1;35m", "red": "\x1b[1;31m",
        "white": "\x1b[1;37m", "yellow": "\x1b[1;33m"
    }

    @staticmethod
    def style(text, *styles):
        """ Applies ANSI styles to text """
        return "".join(styles) + text + TextFormat.RESET
