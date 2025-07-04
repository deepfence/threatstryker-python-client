from enum import Enum


class ModelCommonAlertEventType(str, Enum):
    FILE_ANOMALY = "file_anomaly"
    MALICIOUS_IP = "malicious_ip"
    NETWORK_ANOMALY = "network_anomaly"
    PROCESS_ANOMALY = "process_anomaly"

    def __str__(self) -> str:
        return str(self.value)
