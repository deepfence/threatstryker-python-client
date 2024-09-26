from enum import Enum


class ModelAgentInstallCloudProvider(str, Enum):
    AWS = "aws"

    def __str__(self) -> str:
        return str(self.value)
