from abc import ABC
from dataclasses import dataclass
from typing import Any, TypeVar

from black.nodes import Generic
from domain.events.base import BaseEvent

ET = TypeVar(name="ET", bound=BaseEvent)
ER = TypeVar(name="ER", bound=Any)


@dataclass
class EventHandler(ABC, Generic[ET, ER]):
    async def handle(self, event: ET) -> ER: ...
