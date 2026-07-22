import os
import subprocess
import sys
import time
import pyfiglet
from colorama import Fore, Style, init


def clear_terminal() -> None:
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)


def draw_logo() -> None:
    init(autoreset=True)

    ascii_art = pyfiglet.figlet_format("AI Partner", font="smslant", width=80)
    print(Fore.BLUE + Style.BRIGHT + ascii_art)


def typewriter(text: str, delay: float = 0.03) -> None:
    """Prints text letter by letter.
    
    :param text: The string to print
    :param delay: Time to wait between characters in seconds
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()  # Forces character to render immediately
        time.sleep(delay)
    print()  # Add final newline at the end

