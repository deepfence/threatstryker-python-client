from enum import Enum


class ModelBulkDeleteScansRequestScanType(str, Enum):
    ALERT = "Alert"
    CLOUDCOMPLIANCE = "CloudCompliance"
    COMPLIANCE = "Compliance"
    MALWARE = "Malware"
    NETWORKPOLICYLOGS = "NetworkPolicyLogs"
    QUARANTINEPOLICYLOGS = "QuarantinePolicyLogs"
    SECRET = "Secret"
    VULNERABILITY = "Vulnerability"
    WORKLOADPOLICYLOGS = "WorkloadPolicyLogs"

    def __str__(self) -> str:
        return str(self.value)
