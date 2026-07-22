from src.todos.main import add_todo, edit_todo, remove_todo
from datetime import datetime
import sqlite_utils

# None means success*

db = sqlite_utils.Database(":memory:")

db["todos"].insert(
    {
        "title": "learn combinatorics in math",
        "description": "something should go here..........",
        "added_at": datetime.now(),
        "last_update_at": datetime.now(),
        "is_in_calendar": False,
        "is_sent_to_someone": False,
        "urgent": None,
        "completed": False,
        "tag": "coding",
    },
    pk="id",
)


def test_add_todo() -> None:
    assert (
        add_todo(
            db,
            "Learn pytest",
            "lorem ipsum, lorem ipsum 390 jkasjuiq n mnzcxjkj \n uiquiweczxkj",
            None,
            None,
        )
        is None
    )


def test_remove_todo() -> None:
    assert remove_todo(db, 1) is None


def test_edit_todo() -> None:
    assert edit_todo(db, 2, "Learn German") is None
