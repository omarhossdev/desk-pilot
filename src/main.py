from utils.ui.globals import clear_terminal, typewriter, draw_logo
from utils.ui.home import greet, home_options, print_home_options
import sys


def main() -> None:
    clear_terminal()
    #draw_logo()
    #typewriter(f"AI: {greet("Omar")}  How can I help you today? ☺️")
    
    while True:
        print_home_options()

        try:
            sys.stdout.write("Select option (1-5): ")
            sys.stdout.flush()
            opt = int(sys.stdin.buffer.readline()) - 1
            home_options[opt]["method"]()

        except (ValueError, IndexError):
            sys.stdout.write("\nOops, wrong number! No worries 😄\n")
            continue
        break

if __name__ == "__main__":
    main()
