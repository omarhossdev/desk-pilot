from datetime import datetime

def greet(name: str) -> str:
    h = datetime.now().hour

    if 5 <= h < 12:
        return f"Good morning, {name} 🌞"
    if 12 <= h < 17:
        return f"Good afternoon, {name} ☀️"
    if 17 <= h < 21:
        return f"Good evening, {name} 🌛"
    return f"Good night, {name} 🌚"

def chat() -> None:
    print("Chat..")
def todo_list() -> None:
    print("Todo list..")
def calendar() -> None:
    print("Calendar..")
def notes() -> None:
    print("Notes..")
def backup() -> None:
    print("Backup..")

home_options = [
{
    "title": "💬 Let's chat ",
    "method": chat
},
{
    "title": "✅ Todo list",
    "method": todo_list
},
{
    "title": "📅 Calendar",
    "method": calendar
},
{
    "title": "📝 Notes",
    "method": notes
},
{
    "title": "☁️  Backup",
    "method": backup
}
]

def print_home_options() -> None:
    print("")
    for i, opt in enumerate(home_options):
        print(f"{i + 1}. {opt["title"]}")
    print("")