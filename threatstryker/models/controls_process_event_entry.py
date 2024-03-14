from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.controls_process_event_entry_event import ControlsProcessEventEntryEvent
from ..types import UNSET, Unset

T = TypeVar("T", bound="ControlsProcessEventEntry")


@_attrs_define
class ControlsProcessEventEntry:
    """
    Attributes:
        event (ControlsProcessEventEntryEvent):
        failure_severity (str):
        success_severity (str):
        skip_comm_list (Union[List[str], None, Unset]):
        skip_path_list (Union[List[str], None, Unset]):
        skip_user_list (Union[List[str], None, Unset]):
    """

    event: ControlsProcessEventEntryEvent
    failure_severity: str
    success_severity: str
    skip_comm_list: Union[List[str], None, Unset] = UNSET
    skip_path_list: Union[List[str], None, Unset] = UNSET
    skip_user_list: Union[List[str], None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event = self.event.value

        failure_severity = self.failure_severity

        success_severity = self.success_severity

        skip_comm_list: Union[List[str], None, Unset]
        if isinstance(self.skip_comm_list, Unset):
            skip_comm_list = UNSET
        elif isinstance(self.skip_comm_list, list):
            skip_comm_list = self.skip_comm_list

        else:
            skip_comm_list = self.skip_comm_list

        skip_path_list: Union[List[str], None, Unset]
        if isinstance(self.skip_path_list, Unset):
            skip_path_list = UNSET
        elif isinstance(self.skip_path_list, list):
            skip_path_list = self.skip_path_list

        else:
            skip_path_list = self.skip_path_list

        skip_user_list: Union[List[str], None, Unset]
        if isinstance(self.skip_user_list, Unset):
            skip_user_list = UNSET
        elif isinstance(self.skip_user_list, list):
            skip_user_list = self.skip_user_list

        else:
            skip_user_list = self.skip_user_list

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
        if skip_user_list is not UNSET:
            field_dict["skip_user_list"] = skip_user_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        event = ControlsProcessEventEntryEvent(d.pop("event"))

        failure_severity = d.pop("failure_severity")

        success_severity = d.pop("success_severity")

        def _parse_skip_comm_list(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                skip_comm_list_type_0 = cast(List[str], data)

                return skip_comm_list_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        skip_comm_list = _parse_skip_comm_list(d.pop("skip_comm_list", UNSET))

        def _parse_skip_path_list(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                skip_path_list_type_0 = cast(List[str], data)

                return skip_path_list_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        skip_path_list = _parse_skip_path_list(d.pop("skip_path_list", UNSET))

        def _parse_skip_user_list(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                skip_user_list_type_0 = cast(List[str], data)

                return skip_user_list_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        skip_user_list = _parse_skip_user_list(d.pop("skip_user_list", UNSET))

        controls_process_event_entry = cls(
            event=event,
            failure_severity=failure_severity,
            success_severity=success_severity,
            skip_comm_list=skip_comm_list,
            skip_path_list=skip_path_list,
            skip_user_list=skip_user_list,
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
