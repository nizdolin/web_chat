from dataclasses import dataclass

from domain.entities.messages import Chat
from domain.values.messages import Title
from infrastructure.repositories.messages import BaseChatRepository
from logic.commands.base import BaseCommand, CommandHandler
from logic.exceptions.messages import ChatWithThatTitleAlreadyExists


@dataclass(frozen=True)
class CreateChatCommand(BaseCommand):
    title: str


@dataclass(frozen=True)
class CreateChatCommandHandler(CommandHandler[CreateChatCommand, Chat]):
    chat_repository: BaseChatRepository

    async def handle(self, command: CreateChatCommand) -> Chat:
        if await self.chat_repository.check_chat_exists_by_title(command.title):
            raise ChatWithThatTitleAlreadyExists(command.title)

        title = Title(value=command.title)

        new_chat = Chat.create(title=title)
        # TODO: считать эвенты
        await self.chat_repository.add_chat(new_chat)

        return new_chat
