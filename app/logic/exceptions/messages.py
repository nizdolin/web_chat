from dataclasses import dataclass

from logic.exceptions.base import LogicException


@dataclass(eq=False)
class ChatWithThatTitleAlreadyExists(LogicException):
    title: str

    @property
    def message(self) -> str:
        return f'Chat with this title already exists: "{self.title}".'
