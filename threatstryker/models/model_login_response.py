from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelLoginResponse")


@_attrs_define
class ModelLoginResponse:
    """
    Attributes:
        access_token (str):
        email_domain (str):
        license_key (str):
        license_registered (bool):
        onboarding_required (bool):
        password_invalidated (bool):
        refresh_token (str):
    """

    access_token: str
    email_domain: str
    license_key: str
    license_registered: bool
    onboarding_required: bool
    password_invalidated: bool
    refresh_token: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_token = self.access_token

        email_domain = self.email_domain

        license_key = self.license_key

        license_registered = self.license_registered

        onboarding_required = self.onboarding_required

        password_invalidated = self.password_invalidated

        refresh_token = self.refresh_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "access_token": access_token,
                "email_domain": email_domain,
                "license_key": license_key,
                "license_registered": license_registered,
                "onboarding_required": onboarding_required,
                "password_invalidated": password_invalidated,
                "refresh_token": refresh_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_token = d.pop("access_token")

        email_domain = d.pop("email_domain")

        license_key = d.pop("license_key")

        license_registered = d.pop("license_registered")

        onboarding_required = d.pop("onboarding_required")

        password_invalidated = d.pop("password_invalidated")

        refresh_token = d.pop("refresh_token")

        model_login_response = cls(
            access_token=access_token,
            email_domain=email_domain,
            license_key=license_key,
            license_registered=license_registered,
            onboarding_required=onboarding_required,
            password_invalidated=password_invalidated,
            refresh_token=refresh_token,
        )

        model_login_response.additional_properties = d
        return model_login_response

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
