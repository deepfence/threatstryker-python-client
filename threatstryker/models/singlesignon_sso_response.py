import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="SinglesignonSSOResponse")


@_attrs_define
class SinglesignonSSOResponse:
    """
    Attributes:
        client_id (str):
        created_at (datetime.datetime):
        disable_password_login (bool):
        id (int):
        issuer_alias_url (str):
        issuer_url (str):
        label (str):
        sso_provider_type (str):
        updated_at (datetime.datetime):
    """

    client_id: str
    created_at: datetime.datetime
    disable_password_login: bool
    id: int
    issuer_alias_url: str
    issuer_url: str
    label: str
    sso_provider_type: str
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_id = self.client_id

        created_at = self.created_at.isoformat()

        disable_password_login = self.disable_password_login

        id = self.id

        issuer_alias_url = self.issuer_alias_url

        issuer_url = self.issuer_url

        label = self.label

        sso_provider_type = self.sso_provider_type

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "client_id": client_id,
                "created_at": created_at,
                "disable_password_login": disable_password_login,
                "id": id,
                "issuer_alias_url": issuer_alias_url,
                "issuer_url": issuer_url,
                "label": label,
                "sso_provider_type": sso_provider_type,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_id = d.pop("client_id")

        created_at = isoparse(d.pop("created_at"))

        disable_password_login = d.pop("disable_password_login")

        id = d.pop("id")

        issuer_alias_url = d.pop("issuer_alias_url")

        issuer_url = d.pop("issuer_url")

        label = d.pop("label")

        sso_provider_type = d.pop("sso_provider_type")

        updated_at = isoparse(d.pop("updated_at"))

        singlesignon_sso_response = cls(
            client_id=client_id,
            created_at=created_at,
            disable_password_login=disable_password_login,
            id=id,
            issuer_alias_url=issuer_alias_url,
            issuer_url=issuer_url,
            label=label,
            sso_provider_type=sso_provider_type,
            updated_at=updated_at,
        )

        singlesignon_sso_response.additional_properties = d
        return singlesignon_sso_response

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
