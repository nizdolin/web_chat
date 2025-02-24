from datetime import datetime

import pytest
from domain.entities.messages import Chat, Message
from domain.events.messages import NewMessageReceivedEvent
from domain.exceptions.messages import TitleTooLongException
from domain.values.messages import Text, Title


def test_create_message_success_short_text():
    text = Text("Some valid text")
    message = Message(text=text)

    assert message.text == text
    assert message.created_at.date() == datetime.today().date()


def test_create_message_success_long_text():
    text = Text("Text" * 100)
    message = Message(text=text)

    assert message.text == text
    assert message.created_at.date() == datetime.today().date()


def test_create_chat_success():
    title = Title("title")
    chat = Chat(title=title)

    assert chat.title == title
    assert not chat.messages
    assert chat.created_at.date() == datetime.today().date()


def test_create_chat_title_too_long():
    with pytest.raises(TitleTooLongException):
        title = Title("t" * (Title.MAX_LENGTH + 1))


def test_add_message_to_chat():
    text = Text("Some valid text")
    message = Message(text=text)

    title = Title("title")
    chat = Chat(title=title)

    chat.add_message(message)

    assert message in chat.messages


def test_new_message_events():
    text = Text("Some valid text")
    message = Message(text=text)

    title = Title("title")
    chat = Chat(title=title)

    chat.add_message(message)
    events = chat.pull_events()
    empty_events = chat.pull_events()

    assert not empty_events, empty_events
    assert len(events) == 1, events

    new_event = events[0]

    assert isinstance(new_event, NewMessageReceivedEvent), new_event
    assert new_event.message_id == message.id
    assert new_event.message_text == message.text.as_generic_type()
    assert new_event.chat_id == chat.id
