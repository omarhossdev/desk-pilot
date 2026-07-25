# 🧭 Desk Pilot

**Command your digital workspace. Todos, notes, calendar, encrypted backups, audio playback, and local AI – no memorization required.**

Desk Pilot is a cross-platform desktop assistant that brings all your digital tools under one roof. No more juggling apps – just a clean terminal interface with helpful GUI dialogs when you need them.

---

## ✨ Features

- 📝 **Task Management** – Add, list, and complete todos with natural language
- 📔 **Note Taking:** Take your notes here and connect them with other desk pilot tools or share them with friends!
- 📅 **Calendar Integration** – Schedule events with a visual date picker
- ☁️ **Encrypted Backups** – Secure your folders and upload to Google Drive, Dropbox, or your own cloud
- 🔊 **Audio Playback** – Select any audio file via GUI picker and play it with your default player
- 🤖 **Local AI Chat** – Privacy-first conversations using Ollama (no data leaves your machine)
- 🔄 **Cross-Platform** – Works on Windows, macOS, and Linux
- 🎯 **Zero Memorization** – Navigate with menus, file dialogs, and natural language

---

## 🚀 Quick Start

1. Clone the repo and move there:
```bash
# Clone the repository
git clone https://github.com/omarhossdev/desk-pilot.git
cd desk-pilot
```
2. Make sure you have [uv package manager](https://docs.astral.sh/uv/)
3. Make sure you have [just command runner](https://github.com/casey/just) to run commands from `justfile`
4. open the terminal and run `just install` to install the dependencies.
5. Run the project using `just run` and *Volia!*

---

## 💡 Why Desk Pilot?

**Most CLI tools:** "Read the 50-page manual!"
**Most GUI apps:** "Click through 15 menus!"

**Desk Pilot:** "Press 2, pick your files, done."

It's the sweet spot – powerful enough for developers, *simple enough for everyone else.*

---

## 🔒 Privacy First

- All data stays **local** on your machine
- Optional cloud backups are **end-to-end encrypted**
- AI runs **locally** – no API calls, no tracking

--- 

## 🔨 Tech Stack

1. Python +3.13
2. `uv` modern easy to use package manager
3. `just` to run justfile so you can easily run `just install` to install packages or `just test` to test etc..
4. `ruff` for code linting and formating
5. `pyright` to add static typing and strict type check to ensure everything is working as expected
6. `plyer` simple GUI tool to easily select files and folders
7. `pytest` testing

---

## ⚖️ LICENSE

This project is under MIT License

---

This README is not done yet so stay tuned!
If you found this tool useful, give it a star to help it grow ⭐