from dataclasses import dataclass, field
from datetime import datetime

from domain.entities.base import BaseEntity
from domain.events.messages import NewChatCreatedEvent, NewMessageReceivedEvent
from domain.values.messages import Text, Title


@dataclass(eq=False)
class Message(BaseEntity):
    created_at: datetime = field(default_factory=datetime.now, kw_only=True)
    text: Text


@dataclass(eq=False)
class Chat(BaseEntity):
    created_at: datetime = field(default_factory=datetime.now, kw_only=True)
    title: Title
    messages: set[Message] = field(default_factory=set, kw_only=True)

    @classmethod
    def create(cls, title: Title) -> "Chat":
        new_chat = cls(title=title)
        new_chat.register_event(NewChatCreatedEvent(chat_id=new_chat.id, chat_title=new_chat.title.as_generic_type()))
        return new_chat

    def add_message(self, message: Message):
        self.messages.add(message)
        self.register_event(
            NewMessageReceivedEvent(
                message_id=message.id,
                message_text=message.text.as_generic_type(),
                chat_id=self.id,
            )
        )
