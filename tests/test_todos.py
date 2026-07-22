from src.types.models import Todo, Urgent
from src.todos.main import addTodo, editTodo, removeTodo
from datetime import datetime

todos: list[Todo] = [
    {
        "title": "learn combinatorics in math",
        "description": "something should go here..........",
        "added_at": datetime.now(),
        "last_update_at": datetime.now(),
        "is_in_calendar": False,
        "is_sent_to_someone": False,
        "urgent": Urgent.NOW,
    }
]


def test_add_todo() -> None:
    assert (
        addTodo(
            todos,
            "Learn pytest",
            "lorem ipsum, lorem ipsum 390 jkasjuiq n mnzcxjkj \n uiquiweczxkj",
            Urgent.NOW,
        )
        is None
    )


def test_remove_todo() -> None:
    assert removeTodo(todos, 0) is None


def test_edit_todo() -> None:
    assert editTodo(todos, 0, "Learn German", None, Urgent.SCHEDULE) is None
