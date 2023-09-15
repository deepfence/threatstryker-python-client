from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ControlsProcessEventConfig")


@_attrs_define
class ControlsProcessEventConfig:
    """
    Example:
        {'event_name': 'event_name', 'weight': 'weight'}

    Attributes:
        event_name (str):
        weight (str):
    """

    event_name: str
    weight: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_name = self.event_name
        weight = self.weight

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_name": event_name,
                "weight": weight,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        event_name = d.pop("event_name")

        weight = d.pop("weight")

        controls_process_event_config = cls(
            event_name=event_name,
            weight=weight,
        )

        controls_process_event_config.additional_properties = d
        return controls_process_event_config

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
