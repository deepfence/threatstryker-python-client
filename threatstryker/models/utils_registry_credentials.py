from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UtilsRegistryCredentials")


@_attrs_define
class UtilsRegistryCredentials:
    """
    Attributes:
        password (Union[Unset, str]):
        registry_url (Union[Unset, str]):
        username (Union[Unset, str]):
    """

    password: Union[Unset, str] = UNSET
    registry_url: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        password = self.password

        registry_url = self.registry_url

        username = self.username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if password is not UNSET:
            field_dict["password"] = password
        if registry_url is not UNSET:
            field_dict["registry_url"] = registry_url
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        password = d.pop("password", UNSET)

        registry_url = d.pop("registry_url", UNSET)

        username = d.pop("username", UNSET)

        utils_registry_credentials = cls(
            password=password,
            registry_url=registry_url,
            username=username,
        )

        utils_registry_credentials.additional_properties = d
        return utils_registry_credentials

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
