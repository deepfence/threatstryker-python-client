from enum import Enum


class ModelGenerateReportReqReportType(str, Enum):
    PDF = "pdf"
    XLSX = "xlsx"

    def __str__(self) -> str:
        return str(self.value)
