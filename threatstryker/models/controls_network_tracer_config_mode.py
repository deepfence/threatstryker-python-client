from enum import Enum


class ControlsNetworkTracerConfigMode(str, Enum):
    ALL = "all"
    ALLOW = "allow"
    DENY = "deny"

    def __str__(self) -> str:
        return str(self.value)
