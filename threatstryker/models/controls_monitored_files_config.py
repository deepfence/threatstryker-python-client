from typing import Any, Dict, List, Optional, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ControlsMonitoredFilesConfig")


@_attrs_define
class ControlsMonitoredFilesConfig:
    """
    Example:
        {'severity': 'severity', 'accesstypes': ['accesstypes', 'accesstypes'], 'root': 'root', 'recursive': True}

    Attributes:
        recursive (bool):
        root (str):
        severity (str):
        accesstypes (Optional[List[str]]):
    """

    recursive: bool
    root: str
    severity: str
    accesstypes: Optional[List[str]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        recursive = self.recursive
        root = self.root
        severity = self.severity
        if self.accesstypes is None:
            accesstypes = None
        else:
            accesstypes = self.accesstypes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "recursive": recursive,
                "root": root,
                "severity": severity,
                "accesstypes": accesstypes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        recursive = d.pop("recursive")

        root = d.pop("root")

        severity = d.pop("severity")

        accesstypes = cast(List[str], d.pop("accesstypes"))

        controls_monitored_files_config = cls(
            recursive=recursive,
            root=root,
            severity=severity,
            accesstypes=accesstypes,
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
