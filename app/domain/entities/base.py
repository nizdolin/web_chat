from abc import ABC
from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass
class BaseMutableEntity(ABC):
    id: str = field(default_factory=lambda: str(uuid4()), kw_only=True)
    created_at: datetime = field(default_factory=datetime.now, kw_only=True)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BaseMutableEntity):
            return NotImplemented
        return self.id == other.id


@dataclass(frozen=True)
class BaseImmutableEntity(ABC):
    id: str = field(default_factory=lambda: str(uuid4()), kw_only=True)
    created_at: datetime = field(default_factory=datetime.now, kw_only=True)

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BaseImmutableEntity):
            return NotImplemented
        return self.id == other.id
