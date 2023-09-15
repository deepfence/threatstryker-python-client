from typing import Any, Dict, List, Optional, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ControlsMonitoredFilesConfig")


@_attrs_define
class ControlsMonitoredFilesConfig:
    """
    Example:
        {'path': 'path', 'weight': 'weight', 'access_types': ['access_types', 'access_types']}

    Attributes:
        path (str):
        weight (str):
        access_types (Optional[List[str]]):
    """

    path: str
    weight: str
    access_types: Optional[List[str]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path = self.path
        weight = self.weight
        if self.access_types is None:
            access_types = None
        else:
            access_types = self.access_types

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
                "weight": weight,
                "access_types": access_types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("path")

        weight = d.pop("weight")

        access_types = cast(List[str], d.pop("access_types"))

        controls_monitored_files_config = cls(
            path=path,
            weight=weight,
            access_types=access_types,
        )

        controls_monitored_files_config.additional_properties = d
        return controls_monitored_files_config

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
