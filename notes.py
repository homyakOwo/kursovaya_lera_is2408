"""Small training module for a collaborative live coding session.

No external dependencies or real user data are required.
"""
from dataclasses import dataclass, replace


@dataclass(frozen=True)
class Note:
    identifier: int
    title: str
    completed: bool = False


def add_note(notes: tuple[Note, ...], title: str) -> tuple[Note, ...]:
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Название заметки не должно быть пустым")
    new_id = max((item.identifier for item in notes), default=0) + 1
    return (*notes, Note(new_id, title.strip()))


def complete_note(notes: tuple[Note, ...], identifier: int) -> tuple[Note, ...]:
    if not any(n.identifier == identifier for n in notes):
        raise ValueError("Заметка не найдена")
    return tuple(replace(n, completed=True) if n.identifier == identifier else n for n in notes)


def pending_titles(notes: tuple[Note, ...]) -> list[str]:
    return [n.title for n in notes if not n.completed]


def summary(notes: tuple[Note, ...]) -> str:
    done = sum(n.completed for n in notes)
    return f"Всего: {len(notes)}, выполнено: {done}"
