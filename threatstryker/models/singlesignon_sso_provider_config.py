from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.singlesignon_sso_provider_config_sso_provider_type import SinglesignonSSOProviderConfigSsoProviderType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SinglesignonSSOProviderConfig")


@_attrs_define
class SinglesignonSSOProviderConfig:
    """
    Attributes:
        client_id (str):
        client_secret (str):
        disable_password_login (bool):
        sso_provider_type (SinglesignonSSOProviderConfigSsoProviderType):
        host_name (Union[Unset, str]):
        issuer_alias_url (Union[Unset, str]):
        issuer_url (Union[Unset, str]):
    """

    client_id: str
    client_secret: str
    disable_password_login: bool
    sso_provider_type: SinglesignonSSOProviderConfigSsoProviderType
    host_name: Union[Unset, str] = UNSET
    issuer_alias_url: Union[Unset, str] = UNSET
    issuer_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_id = self.client_id

        client_secret = self.client_secret

        disable_password_login = self.disable_password_login

        sso_provider_type = self.sso_provider_type.value

        host_name = self.host_name

        issuer_alias_url = self.issuer_alias_url

        issuer_url = self.issuer_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "client_id": client_id,
                "client_secret": client_secret,
                "disable_password_login": disable_password_login,
                "sso_provider_type": sso_provider_type,
            }
        )
        if host_name is not UNSET:
            field_dict["host_name"] = host_name
        if issuer_alias_url is not UNSET:
            field_dict["issuer_alias_url"] = issuer_alias_url
        if issuer_url is not UNSET:
            field_dict["issuer_url"] = issuer_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_id = d.pop("client_id")

        client_secret = d.pop("client_secret")

        disable_password_login = d.pop("disable_password_login")

        sso_provider_type = SinglesignonSSOProviderConfigSsoProviderType(d.pop("sso_provider_type"))

        host_name = d.pop("host_name", UNSET)

        issuer_alias_url = d.pop("issuer_alias_url", UNSET)

        issuer_url = d.pop("issuer_url", UNSET)

        singlesignon_sso_provider_config = cls(
            client_id=client_id,
            client_secret=client_secret,
            disable_password_login=disable_password_login,
            sso_provider_type=sso_provider_type,
            host_name=host_name,
            issuer_alias_url=issuer_alias_url,
            issuer_url=issuer_url,
        )

        singlesignon_sso_provider_config.additional_properties = d
        return singlesignon_sso_provider_config

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
