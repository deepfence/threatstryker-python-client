from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelListAgentVersionResp")


@_attrs_define
class ModelListAgentVersionResp:
    """
    Attributes:
        versions (Union[None, list[str]]):
    """

    versions: Union[None, list[str]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        versions: Union[None, list[str]]
        if isinstance(self.versions, list):
            versions = self.versions

        else:
            versions = self.versions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "versions": versions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_versions(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                versions_type_0 = cast(list[str], data)

                return versions_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        versions = _parse_versions(d.pop("versions"))

        model_list_agent_version_resp = cls(
            versions=versions,
        )

        model_list_agent_version_resp.additional_properties = d
        return model_list_agent_version_resp

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
