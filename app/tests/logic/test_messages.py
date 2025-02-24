import pytest
from domain.entities.messages import Chat
from domain.values.messages import Title
from faker import Faker
from infrastructure.repositories.messages import BaseChatRepository
from logic.commands.messages import CreateChatCommand
from logic.exceptions.messages import ChatWithThatTitleAlreadyExists
from logic.mediator import Mediator


@pytest.mark.asyncio
async def test_create_chat_command_success(chat_repository: BaseChatRepository, mediator: Mediator, faker: Faker):
    chat: Chat
    chat, *_ = await mediator.handle_command(CreateChatCommand(title=faker.text(max_nb_chars=Title.MAX_LENGTH)))

    assert await chat_repository.check_chat_exists_by_title(title=chat.title.as_generic_type())


@pytest.mark.asyncio
async def test_create_chat_command_title_already_exists(
    chat_repository: BaseChatRepository, mediator: Mediator, faker: Faker
):
    title_text = faker.text(max_nb_chars=Title.MAX_LENGTH)
    chat = Chat(title=Title(title_text))
    await chat_repository.add_chat(chat)
    with pytest.raises(ChatWithThatTitleAlreadyExists):
        await mediator.handle_command(CreateChatCommand(title=title_text))

    assert len(chat_repository._saved_chats) == 1  # noqa
