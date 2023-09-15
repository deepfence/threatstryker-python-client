from enum import Enum


class IngestersCloudWafConfigCloudProvider(str, Enum):
    AWS = "aws"

    def __str__(self) -> str:
        return str(self.value)
