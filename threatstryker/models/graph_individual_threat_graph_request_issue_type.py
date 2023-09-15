from enum import Enum


class GraphIndividualThreatGraphRequestIssueType(str, Enum):
    ALERT = "alert"
    CLOUD_COMPLIANCE = "cloud_compliance"
    COMPLIANCE = "compliance"
    MALWARE = "malware"
    SECRET = "secret"
    VULNERABILITY = "vulnerability"

    def __str__(self) -> str:
        return str(self.value)
