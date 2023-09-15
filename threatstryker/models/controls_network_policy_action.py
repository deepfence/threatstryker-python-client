from enum import Enum


class ControlsNetworkPolicyAction(str, Enum):
    BLOCK = "block"

    def __str__(self) -> str:
        return str(self.value)
