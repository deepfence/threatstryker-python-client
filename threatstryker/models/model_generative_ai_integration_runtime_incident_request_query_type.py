from enum import Enum


class ModelGenerativeAiIntegrationRuntimeIncidentRequestQueryType(str, Enum):
    REMEDIATION = "remediation"

    def __str__(self) -> str:
        return str(self.value)
