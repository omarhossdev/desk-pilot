import json
from pathlib import Path
import subprocess
import os
import tempfile
from plyer import filechooser
from quo.prompt import Prompt

json_file = "src/utils/data.json"

def select_folder():
    path_list = filechooser.choose_dir(title="Select a Folder")

    folder_path = path_list[0] if isinstance(path_list, list) else path_list
    return folder_path


def play_sounds(sounds: list[str]):
    with tempfile.NamedTemporaryFile(mode='w', suffix='.m3u', delete=False) as f:
        for sound in sounds:
            f.write(str(sound) + '\n')
        playlist = f.name

    if os.name == 'nt':  # Windows
        os.startfile(playlist)
    else:  # macOS & Linux
        subprocess.Popen(
            ['xdg-open', playlist],
            stdout=subprocess.DEVNULL, # to disable conflicting between opening external apps and the tool 
            stderr=subprocess.DEVNULL
        )


def audio_app() -> None:    
    music_folder: str = ''

    with open(json_file) as f:
        music_folder = json.load(f)['music']

    while True:
        if music_folder:
            print("\n==========================")
            print("🔊 Audio Player")
            print("==========================")
            print("1. Play files")
            print("2. Play folder")
            print("3. Back..\n")

            opt = input("Select: ")

            if opt == '1':
                audio_files: list[str] = []
                filechooser.open_file(
                    title="Choose Music files",
                    multiple=True,
                    filters=[
                        ("Audio Files", "*.mp3", "*.wav", "*.ogg", "*.flac", "*.m4a", "*.aac")
                    ],
                    path=music_folder,
                    on_selection=lambda selection: audio_files.extend(selection)
                )

                play_sounds(audio_files)
            elif opt == '2':
                run_folder = select_folder()

                if os.path.exists(run_folder):
                    audio_extensions = {'.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a', '.wma', '.aiff'}

                    # Get all audio files recursively
                    audio_files = [str(f) for f in Path(run_folder).rglob("*") 
                    if f.is_file() and f.suffix.lower() in audio_extensions]

                    play_sounds(audio_files)

            return None
        else:
            
            if os.path.exists(select_folder()):

                with open(json_file, 'r') as f:
                    data = json.load(f)

                data['music'] = folder_path
                music_folder = folder_path

                with open(json_file, 'w') as f:
                    json.dump(data, f, indent=2)
            else:
                print("Selection cancelled.")
