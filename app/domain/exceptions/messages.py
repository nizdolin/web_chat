from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class EmptyTextException(ApplicationException):
    @property
    def message(self):
        return "Text can not be empty"


@dataclass(eq=False)
class TitleTooLongException(ApplicationException):
    text: str
    length: int

    @property
    def message(self):
        return f'Message text is too long: "{self.text[:self.length]}..."'
