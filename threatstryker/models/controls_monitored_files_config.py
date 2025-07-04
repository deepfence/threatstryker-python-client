from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ControlsMonitoredFilesConfig")


@_attrs_define
class ControlsMonitoredFilesConfig:
    """
    Attributes:
        accesstypes (Union[None, list[str]]):
        exclude (Union[None, list[str]]):
        recursive (bool):
        root (str):
        severity (str):
    """

    accesstypes: Union[None, list[str]]
    exclude: Union[None, list[str]]
    recursive: bool
    root: str
    severity: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accesstypes: Union[None, list[str]]
        if isinstance(self.accesstypes, list):
            accesstypes = self.accesstypes

        else:
            accesstypes = self.accesstypes

        exclude: Union[None, list[str]]
        if isinstance(self.exclude, list):
            exclude = self.exclude

        else:
            exclude = self.exclude

        recursive = self.recursive

        root = self.root

        severity = self.severity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accesstypes": accesstypes,
                "exclude": exclude,
                "recursive": recursive,
                "root": root,
                "severity": severity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_accesstypes(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                accesstypes_type_0 = cast(list[str], data)

                return accesstypes_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        accesstypes = _parse_accesstypes(d.pop("accesstypes"))

        def _parse_exclude(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exclude_type_0 = cast(list[str], data)

                return exclude_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        exclude = _parse_exclude(d.pop("exclude"))

        recursive = d.pop("recursive")

        root = d.pop("root")

        severity = d.pop("severity")

        controls_monitored_files_config = cls(
            accesstypes=accesstypes,
            exclude=exclude,
            recursive=recursive,
            root=root,
            severity=severity,
        )

        controls_monitored_files_config.additional_properties = d
        return controls_monitored_files_config

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
