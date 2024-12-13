from dataclasses import dataclass, field

from domain.entities.base import BaseImmutableEntity, BaseMutableEntity
from domain.values.messages import Text, Title


@dataclass(frozen=True)
class Message(BaseImmutableEntity):
    text: Text


@dataclass
class Chat(BaseMutableEntity):
    title: Title
    messages: set[Message] = field(default_factory=set, kw_only=True)

    def add_message(self, message: Message):
        self.messages.add(message)
