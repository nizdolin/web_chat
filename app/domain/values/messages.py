from dataclasses import dataclass

from domain.exceptions.messages import EmptyTextException, TitleTooLongException
from domain.values.base import BaseValueObject


@dataclass(frozen=True)
class Text(BaseValueObject):
    value: str

    def validate(self) -> None:
        if not self.value:
            raise EmptyTextException()

    def as_generic_type(self) -> str:
        return self.value


@dataclass(frozen=True)
class Title(Text):
    MAX_LENGTH = 255

    def validate(self) -> None:
        super().validate()
        if len(self.value) > self.MAX_LENGTH:
            raise TitleTooLongException(self.value, self.MAX_LENGTH)
