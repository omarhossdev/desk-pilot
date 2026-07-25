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

            session = Prompt()
            print("Play: Audio(a)")
            inp = session.prompt(
                "#=> ",
                placeholder='<gray>Message AI or select opt above (1-5)...</gray>'
            )

            if inp == 'a':
                audio_app()
    except KeyboardInterrupt:
        print("Bye Bye :)")
if __name__ == "__main__":
    main()
