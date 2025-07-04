from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.diagnosis_diagnostic_logs_link import DiagnosisDiagnosticLogsLink


T = TypeVar("T", bound="DiagnosisGetDiagnosticLogsResponse")


@_attrs_define
class DiagnosisGetDiagnosticLogsResponse:
    """
    Attributes:
        agent_logs (Union[None, Unset, list['DiagnosisDiagnosticLogsLink']]):
        console_logs (Union[None, Unset, list['DiagnosisDiagnosticLogsLink']]):
    """

    agent_logs: Union[None, Unset, list["DiagnosisDiagnosticLogsLink"]] = UNSET
    console_logs: Union[None, Unset, list["DiagnosisDiagnosticLogsLink"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_logs: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.agent_logs, Unset):
            agent_logs = UNSET
        elif isinstance(self.agent_logs, list):
            agent_logs = []
            for agent_logs_type_0_item_data in self.agent_logs:
                agent_logs_type_0_item = agent_logs_type_0_item_data.to_dict()
                agent_logs.append(agent_logs_type_0_item)

        else:
            agent_logs = self.agent_logs

        console_logs: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.console_logs, Unset):
            console_logs = UNSET
        elif isinstance(self.console_logs, list):
            console_logs = []
            for console_logs_type_0_item_data in self.console_logs:
                console_logs_type_0_item = console_logs_type_0_item_data.to_dict()
                console_logs.append(console_logs_type_0_item)

        else:
            console_logs = self.console_logs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agent_logs is not UNSET:
            field_dict["agent_logs"] = agent_logs
        if console_logs is not UNSET:
            field_dict["console_logs"] = console_logs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.diagnosis_diagnostic_logs_link import DiagnosisDiagnosticLogsLink

        d = dict(src_dict)

        def _parse_agent_logs(data: object) -> Union[None, Unset, list["DiagnosisDiagnosticLogsLink"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                agent_logs_type_0 = []
                _agent_logs_type_0 = data
                for agent_logs_type_0_item_data in _agent_logs_type_0:
                    agent_logs_type_0_item = DiagnosisDiagnosticLogsLink.from_dict(agent_logs_type_0_item_data)

                    agent_logs_type_0.append(agent_logs_type_0_item)

                return agent_logs_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["DiagnosisDiagnosticLogsLink"]], data)

        agent_logs = _parse_agent_logs(d.pop("agent_logs", UNSET))

        def _parse_console_logs(data: object) -> Union[None, Unset, list["DiagnosisDiagnosticLogsLink"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                console_logs_type_0 = []
                _console_logs_type_0 = data
                for console_logs_type_0_item_data in _console_logs_type_0:
                    console_logs_type_0_item = DiagnosisDiagnosticLogsLink.from_dict(console_logs_type_0_item_data)

                    console_logs_type_0.append(console_logs_type_0_item)

                return console_logs_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["DiagnosisDiagnosticLogsLink"]], data)

        console_logs = _parse_console_logs(d.pop("console_logs", UNSET))

        diagnosis_get_diagnostic_logs_response = cls(
            agent_logs=agent_logs,
            console_logs=console_logs,
        )

        diagnosis_get_diagnostic_logs_response.additional_properties = d
        return diagnosis_get_diagnostic_logs_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
