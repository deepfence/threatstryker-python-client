from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import File, Unset

T = TypeVar("T", bound="FormDataModelImportAgentPolicyConfigReq")


@_attrs_define
class FormDataModelImportAgentPolicyConfigReq:
    """
    Attributes:
        config_id (str):
        network_policy_json (File):
    """

    config_id: str
    network_policy_json: File
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        config_id = self.config_id

        network_policy_json = self.network_policy_json.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config_id": config_id,
                "network_policy_json": network_policy_json,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        config_id = (
            self.config_id if isinstance(self.config_id, Unset) else (None, str(self.config_id).encode(), "text/plain")
        )

        network_policy_json = self.network_policy_json.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "config_id": config_id,
                "network_policy_json": network_policy_json,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        config_id = d.pop("config_id")

        network_policy_json = File(payload=BytesIO(d.pop("network_policy_json")))

        form_data_model_import_agent_policy_config_req = cls(
            config_id=config_id,
            network_policy_json=network_policy_json,
        )

        form_data_model_import_agent_policy_config_req.additional_properties = d
        return form_data_model_import_agent_policy_config_req

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
