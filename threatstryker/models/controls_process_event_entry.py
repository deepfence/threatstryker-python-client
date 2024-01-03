from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.controls_process_event_entry_event import ControlsProcessEventEntryEvent
from ..types import UNSET, Unset

T = TypeVar("T", bound="ControlsProcessEventEntry")


@_attrs_define
class ControlsProcessEventEntry:
    """
    Example:
        {'skip_path_list': ['skip_path_list', 'skip_path_list'], 'failure_severity': 'failure_severity',
            'success_severity': 'success_severity', 'event': 'bin-execution', 'skip_comm_list': ['skip_comm_list',
            'skip_comm_list']}

    Attributes:
        event (ControlsProcessEventEntryEvent):
        failure_severity (str):
        success_severity (str):
        skip_comm_list (Union[Unset, None, List[str]]):
        skip_path_list (Union[Unset, None, List[str]]):
    """

    event: ControlsProcessEventEntryEvent
    failure_severity: str
    success_severity: str
    skip_comm_list: Union[Unset, None, List[str]] = UNSET
    skip_path_list: Union[Unset, None, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event = self.event.value

        failure_severity = self.failure_severity
        success_severity = self.success_severity
        skip_comm_list: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.skip_comm_list, Unset):
            if self.skip_comm_list is None:
                skip_comm_list = None
            else:
                skip_comm_list = self.skip_comm_list

        skip_path_list: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.skip_path_list, Unset):
            if self.skip_path_list is None:
                skip_path_list = None
            else:
                skip_path_list = self.skip_path_list

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event": event,
                "failure_severity": failure_severity,
                "success_severity": success_severity,
            }
        )
        if skip_comm_list is not UNSET:
            field_dict["skip_comm_list"] = skip_comm_list
        if skip_path_list is not UNSET:
            field_dict["skip_path_list"] = skip_path_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        event = ControlsProcessEventEntryEvent(d.pop("event"))

        failure_severity = d.pop("failure_severity")

        success_severity = d.pop("success_severity")

        skip_comm_list = cast(List[str], d.pop("skip_comm_list", UNSET))

        skip_path_list = cast(List[str], d.pop("skip_path_list", UNSET))

        controls_process_event_entry = cls(
            event=event,
            failure_severity=failure_severity,
            success_severity=success_severity,
            skip_comm_list=skip_comm_list,
            skip_path_list=skip_path_list,
        )

        controls_process_event_entry.additional_properties = d
        return controls_process_event_entry

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
