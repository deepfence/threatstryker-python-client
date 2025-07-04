from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelUserRegisterRequest")


@_attrs_define
class ModelUserRegisterRequest:
    """
    Attributes:
        company (str):
        console_url (str):
        email (str):
        first_name (str):
        last_name (str):
        password (str):
        is_temporary_password (Union[Unset, bool]):
        namespace (Union[Unset, str]):
    """

    company: str
    console_url: str
    email: str
    first_name: str
    last_name: str
    password: str
    is_temporary_password: Union[Unset, bool] = UNSET
    namespace: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company = self.company

        console_url = self.console_url

        email = self.email

        first_name = self.first_name

        last_name = self.last_name

        password = self.password

        is_temporary_password = self.is_temporary_password

        namespace = self.namespace

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "company": company,
                "console_url": console_url,
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "password": password,
            }
        )
        if is_temporary_password is not UNSET:
            field_dict["is_temporary_password"] = is_temporary_password
        if namespace is not UNSET:
            field_dict["namespace"] = namespace

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company = d.pop("company")

        console_url = d.pop("console_url")

        email = d.pop("email")

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        password = d.pop("password")

        is_temporary_password = d.pop("is_temporary_password", UNSET)

        namespace = d.pop("namespace", UNSET)

        model_user_register_request = cls(
            company=company,
            console_url=console_url,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_temporary_password=is_temporary_password,
            namespace=namespace,
        )

        model_user_register_request.additional_properties = d
        return model_user_register_request

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
