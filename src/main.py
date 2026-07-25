from utils.ui.globals import clear_terminal, typewriter, draw_logo
from utils.ui.home import greet, home_options, print_home_options
from utils.applications import audio_app
import sys
from quo.prompt import Prompt

def main() -> None:
    try:
        clear_terminal()
        draw_logo()
        typewriter(f"AI: {greet('Omar')}  How can I help you today? ☺️")

        while True:
            print_home_options()
            print("hint: press Ctrl+C to quit\n")

            session = Prompt()
            inp = session.prompt(
                "#=> ",
                placeholder='<gray>Message AI or select number above (1-6)...</gray>'
            )

            if inp.lower() == '4':
                audio_app()
            else:
                print("Goodbye 👋")
                break
    except KeyboardInterrupt:
        print("Goodbye 👋")
if __name__ == "__main__":
    main()
