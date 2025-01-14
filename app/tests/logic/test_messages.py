import pytest
from infrastructure.repositories.messages import BaseChatRepository
from logic.commands.messages import CreateChatCommand
from logic.mediator import Mediator


@pytest.mark.asyncio
async def test_create_chat_command_success(chat_repository: BaseChatRepository, mediator: Mediator):
    chat = (await mediator.handle_command(CreateChatCommand(title="Some title")))[0]

    assert chat_repository.check_chat_exists_by_title(title=chat.title.as_generic_type())
