from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import File

T = TypeVar("T", bound="FormDataModelRegistryGCRAddReq")


@_attrs_define
class FormDataModelRegistryGCRAddReq:
    """
    Attributes:
        name (str):
        registry_url (str):
        service_account_json (File):
    """

    name: str
    registry_url: str
    service_account_json: File
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        registry_url = self.registry_url

        service_account_json = self.service_account_json.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "registry_url": registry_url,
                "service_account_json": service_account_json,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        files.append(("registry_url", (None, str(self.registry_url).encode(), "text/plain")))

        files.append(("service_account_json", self.service_account_json.to_tuple()))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        registry_url = d.pop("registry_url")

        service_account_json = File(payload=BytesIO(d.pop("service_account_json")))

        form_data_model_registry_gcr_add_req = cls(
            name=name,
            registry_url=registry_url,
            service_account_json=service_account_json,
        )

        form_data_model_registry_gcr_add_req.additional_properties = d
        return form_data_model_registry_gcr_add_req

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
