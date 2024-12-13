from dataclasses import dataclass

from domain.entities.base import IdEntity
from domain.values.messages import Text


@dataclass
class Message(IdEntity):
    text: Text
