from datetime import datetime
from src.types.models import Todo, Urgent
from typing import Union
from sqlite_utils import Database


def add_todo(
    db: Database,
    title: str,
    description: str | None = None,
    urgent: Urgent | None = None,
    tag: str | None = None,
) -> Union[None, ValueError]:
    if not title:
        return ValueError("Parameters should be valid strings and have length > 0")

    new_todo = {
        "title": title,
        "is_in_calendar": False,
        "is_sent_to_someone": False,
        "completed": False,
        "added_at": datetime.now(),
        "last_update_at": datetime.now(),
    }

    if description:
        new_todo["description"] = description
    if urgent:
        new_todo["urgent"] = urgent
    if tag:
        new_todo["tag"] = tag

    db["todos"].insert(new_todo, pk="id")

    return None


def edit_todo(
    db: Database,
    todo_id: int,
    title: str | None = None,  # string or None, default is None
    description: str | None = None,
    urgent: Urgent | None = None,
    tag: str | None = None,
) -> Union[None, KeyError]:
    try:
        cols_to_update = {}

        if title is not None:
            cols_to_update["title"] = title

        if description is not None:
            cols_to_update["description"] = description

        if urgent is not None:
            cols_to_update["urgent"] = urgent

        if tag is not None:
            cols_to_update["tag"] = tag

        if cols_to_update:
            cols_to_update["last_update_at"] = datetime.now().isoformat()
            db["todos"].update(todo_id, cols_to_update)

    except KeyError:
        return KeyError("'index' is out of range")

    return None


def complete_todo(db: Database, todo_id: int) -> Union[None, KeyError]:
    db["todos"].update(todo_id, {"completed": True})


def remove_todo(db: Database, todo_id: int) -> Union[None, KeyError]:
    try:
        db["todos"].delete(todo_id)
    except KeyError:
        return KeyError("'index' is out of range")
    return None


def get_todo(db: Database, todo_id: int) -> Todo:
    return db["todos"].get(todo_id)


def print_todos(db: Database) -> Union[None, ValueError]:
    try:
        for i, todo in enumerate(db["todos"].rows):
            print(f"{i}. {todo['title']} [{todo['urgent']}]")
    except ValueError:
        return ValueError("'todos' cannot be None and must be a list")
    return None


def print_todo_info(todo: Todo) -> Union[None, ValueError]:
    try:
        print(f"Title:\n{todo['title']}\n")
        print(f"Description:\n{todo['description']}\n")
        print(f"Urgent: {todo['urgent']}\n")
        print(f"Added at: {todo['added_at']}")
        print(f"Last update at: {todo['last_update_at']}\n")
        print(f"Is connected with Calendar? {todo['is_in_calendar']}\n")
        print(f"Is sent to someone: {todo['is_sent_to_someone']}")
    except ValueError:
        return ValueError("todo doesn't follow Todos in structure")
    return None
