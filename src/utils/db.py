from src.utils.vars import DB_FILE
import sqlite_utils
from sqlite_utils import Database


def init_db() -> None:
    db: Database = sqlite_utils.Database(DB_FILE)

    if "todos" not in db.table_names():
        db["todos"].create(
            {
                "id": int,
                "title": str,
                "description": str,
                "added_at": str,
                "last_update_at": str,
                "urgent": str,
                "is_in_calendar": bool,
                "is_sent_to_someone": bool,
                "completed": bool,
                "tag": str,
            },
            pk="id",
        )

    return db
