from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_cloud_node_control_req_cloud_provider import ModelCloudNodeControlReqCloudProvider
from ..models.model_cloud_node_control_req_compliance_type import ModelCloudNodeControlReqComplianceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelCloudNodeControlReq")


@_attrs_define
class ModelCloudNodeControlReq:
    """
    Attributes:
        cloud_provider (ModelCloudNodeControlReqCloudProvider):
        compliance_type (ModelCloudNodeControlReqComplianceType):
        node_id (Union[Unset, str]):
    """

    cloud_provider: ModelCloudNodeControlReqCloudProvider
    compliance_type: ModelCloudNodeControlReqComplianceType
    node_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cloud_provider = self.cloud_provider.value

        compliance_type = self.compliance_type.value

        node_id = self.node_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cloud_provider": cloud_provider,
                "compliance_type": compliance_type,
            }
        )
        if node_id is not UNSET:
            field_dict["node_id"] = node_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cloud_provider = ModelCloudNodeControlReqCloudProvider(d.pop("cloud_provider"))

        compliance_type = ModelCloudNodeControlReqComplianceType(d.pop("compliance_type"))

        node_id = d.pop("node_id", UNSET)

        model_cloud_node_control_req = cls(
            cloud_provider=cloud_provider,
            compliance_type=compliance_type,
            node_id=node_id,
        )

        model_cloud_node_control_req.additional_properties = d
        return model_cloud_node_control_req

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
