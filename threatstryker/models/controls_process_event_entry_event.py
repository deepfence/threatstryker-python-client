from enum import Enum


class ControlsProcessEventEntryEvent(str, Enum):
    BIN_EXECUTION = "bin-execution"
    ROOT_ESCALATION = "root-escalation"
    TERMINATION_FAILURE = "termination-failure"

    def __str__(self) -> str:
        return str(self.value)
