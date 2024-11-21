from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SinglesignonUpdateSSOProviderConfig")


@_attrs_define
class SinglesignonUpdateSSOProviderConfig:
    """
    Example:
        {'issuer_alias_url': 'issuer_alias_url', 'issuer_url': 'issuer_url', 'disable_password_login': True,
            'client_secret': 'client_secret', 'client_id': 'client_id'}

    Attributes:
        client_id (str):
        disable_password_login (bool):
        client_secret (Union[Unset, str]):
        issuer_alias_url (Union[Unset, str]):
        issuer_url (Union[Unset, str]):
    """

    client_id: str
    disable_password_login: bool
    client_secret: Union[Unset, str] = UNSET
    issuer_alias_url: Union[Unset, str] = UNSET
    issuer_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_id = self.client_id

        disable_password_login = self.disable_password_login

        client_secret = self.client_secret

        issuer_alias_url = self.issuer_alias_url

        issuer_url = self.issuer_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "client_id": client_id,
                "disable_password_login": disable_password_login,
            }
        )
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret
        if issuer_alias_url is not UNSET:
            field_dict["issuer_alias_url"] = issuer_alias_url
        if issuer_url is not UNSET:
            field_dict["issuer_url"] = issuer_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        client_id = d.pop("client_id")

        disable_password_login = d.pop("disable_password_login")

        client_secret = d.pop("client_secret", UNSET)

        issuer_alias_url = d.pop("issuer_alias_url", UNSET)

        issuer_url = d.pop("issuer_url", UNSET)

        singlesignon_update_sso_provider_config = cls(
            client_id=client_id,
            disable_password_login=disable_password_login,
            client_secret=client_secret,
            issuer_alias_url=issuer_alias_url,
            issuer_url=issuer_url,
        )

        singlesignon_update_sso_provider_config.additional_properties = d
        return singlesignon_update_sso_provider_config

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
