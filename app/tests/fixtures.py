from infrastructure.repositories.messages import BaseChatRepository, MemoryChatRepository
from logic.init import init_new_container
from punq import Container, Scope


def init_dummy_container() -> Container:
    container = init_new_container()
    container.register(BaseChatRepository, MemoryChatRepository, scope=Scope.singleton)
    return container
