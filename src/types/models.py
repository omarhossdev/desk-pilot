from typing import TypedDict
from datetime import datetime
from enum import Enum


class Urgent(Enum):
    NOW = "🔥 DO FIRST"
    SCHEDULE = "📅 SCHEDULE"
    DELEGATE = "🙅 DELEGATE"
    DELETE = "🗑️ DELETE"


class Todo(TypedDict):
    title: str
    description: str
    added_at: datetime
    last_update_at: datetime
    urgent: Urgent
    is_in_calendar: bool
    is_sent_to_someone: bool
    completed: bool
    tag: str
