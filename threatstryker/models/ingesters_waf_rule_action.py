from enum import Enum


class IngestersWAFRuleAction(str, Enum):
    BLOCK = "block"
    UNBLOCK = "unblock"

    def __str__(self) -> str:
        return str(self.value)
