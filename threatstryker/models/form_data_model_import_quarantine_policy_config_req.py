from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import File

T = TypeVar("T", bound="FormDataModelImportQuarantinePolicyConfigReq")


@_attrs_define
class FormDataModelImportQuarantinePolicyConfigReq:
    """
    Attributes:
        config_id (str):
        quarantine_policy_json (File):
    """

    config_id: str
    quarantine_policy_json: File
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config_id = self.config_id

        quarantine_policy_json = self.quarantine_policy_json.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config_id": config_id,
                "quarantine_policy_json": quarantine_policy_json,
            }
        )

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("config_id", (None, str(self.config_id).encode(), "text/plain")))

        files.append(("quarantine_policy_json", self.quarantine_policy_json.to_tuple()))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        config_id = d.pop("config_id")

        quarantine_policy_json = File(payload=BytesIO(d.pop("quarantine_policy_json")))

        form_data_model_import_quarantine_policy_config_req = cls(
            config_id=config_id,
            quarantine_policy_json=quarantine_policy_json,
        )

        form_data_model_import_quarantine_policy_config_req.additional_properties = d
        return form_data_model_import_quarantine_policy_config_req

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
