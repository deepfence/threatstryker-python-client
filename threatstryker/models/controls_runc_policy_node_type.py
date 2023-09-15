from enum import Enum


class ControlsRuncPolicyNodeType(str, Enum):
    CONTAINER = "container"
    POD = "pod"

    def __str__(self) -> str:
        return str(self.value)
