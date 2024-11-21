from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ControlsMonitoredFilesConfig")


@_attrs_define
class ControlsMonitoredFilesConfig:
    """
    Example:
        {'severity': 'severity', 'accesstypes': ['accesstypes', 'accesstypes'], 'root': 'root', 'recursive': True}

    Attributes:
        accesstypes (Union[List[str], None]):
        recursive (bool):
        root (str):
        severity (str):
    """

    accesstypes: Union[List[str], None]
    recursive: bool
    root: str
    severity: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        accesstypes: Union[List[str], None]
        if isinstance(self.accesstypes, list):
            accesstypes = self.accesstypes

        else:
            accesstypes = self.accesstypes

        recursive = self.recursive

        root = self.root

        severity = self.severity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accesstypes": accesstypes,
                "recursive": recursive,
                "root": root,
                "severity": severity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_accesstypes(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                accesstypes_type_0 = cast(List[str], data)

                return accesstypes_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

        accesstypes = _parse_accesstypes(d.pop("accesstypes"))

        recursive = d.pop("recursive")

        root = d.pop("root")

        severity = d.pop("severity")

        controls_monitored_files_config = cls(
            accesstypes=accesstypes,
            recursive=recursive,
            root=root,
            severity=severity,
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
