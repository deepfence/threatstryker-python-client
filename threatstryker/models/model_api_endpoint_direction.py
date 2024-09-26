from enum import Enum


class ModelAPIEndpointDirection(str, Enum):
    EGRESS = "egress"
    INGRESS = "ingress"

    def __str__(self) -> str:
        return str(self.value)
