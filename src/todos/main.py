from datetime import datetime
from src.types.models import Todo, Urgent
from typing import Union


def addTodo(
    todos: list[Todo], title: str, description: str, urgent: Urgent
) -> Union[None, ValueError]:
    if not title or not description or not urgent:
        return ValueError("Parameters should be valid strings and have length > 0")

    todos.append(
        {
            "title": title,
            "description": description,
            "urgent": urgent,
            "is_in_calendar": False,
            "is_sent_to_someone": False,
            "added_at": datetime.now(),
            "last_update_at": datetime.now(),
        }
    )

    return None


def editTodo(
    todos: list[Todo],
    index: int,
    title: str | None = None,  # string or None, default is None
    description: str | None = None,
    urgent: Urgent | None = None,
) -> Union[None, KeyError]:
    try:
        updated = False

        if title is not None:
            todos[index]["title"] = title
            updated = True

        if description is not None:
            todos[index]["description"] = description
            updated = True

        if urgent is not None:
            todos[index]["urgent"] = urgent
            updated = True

        if updated:
            todos[index]["last_update_at"] = datetime.now()

    except KeyError:
        return KeyError("'index' is out of range")

    return None


def removeTodo(todos: list[Todo], index: int) -> Union[None, KeyError]:
    try:
        todos.pop(index)
    except KeyError:
        return KeyError("'index' is out of range")
    return None


def printTodos(todos: list[Todo]) -> Union[None, ValueError]:
    try:
        for i, todo in enumerate(todos):
            print(f"{i}. {todo['title']} [{todo['urgent']}]")
    except ValueError:
        return ValueError("'todos' cannot be None and must be a list")
    return None


def printTodoInfo(todo: Todo) -> Union[None, ValueError]:
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
