import uuid
from abc import ABC
from dataclasses import dataclass, field


@dataclass
class IdEntity(ABC):
    id: str = field(default_factory=lambda: str(uuid.uuid4()), kw_only=True)
