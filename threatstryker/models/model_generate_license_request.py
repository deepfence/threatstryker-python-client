from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelGenerateLicenseRequest")


@_attrs_define
class ModelGenerateLicenseRequest:
    """
    Attributes:
        company (str):
        email (str):
        first_name (str):
        last_name (str):
        resend_email (bool):
    """

    company: str
    email: str
    first_name: str
    last_name: str
    resend_email: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company = self.company

        email = self.email

        first_name = self.first_name

        last_name = self.last_name

        resend_email = self.resend_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "company": company,
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "resend_email": resend_email,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company = d.pop("company")

        email = d.pop("email")

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        resend_email = d.pop("resend_email")

        model_generate_license_request = cls(
            company=company,
            email=email,
            first_name=first_name,
            last_name=last_name,
            resend_email=resend_email,
        )

        model_generate_license_request.additional_properties = d
        return model_generate_license_request

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
