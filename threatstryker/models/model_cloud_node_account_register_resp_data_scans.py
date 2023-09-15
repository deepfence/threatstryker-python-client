from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_cloud_compliance_scan_details import ModelCloudComplianceScanDetails


T = TypeVar("T", bound="ModelCloudNodeAccountRegisterRespDataScans")


@_attrs_define
class ModelCloudNodeAccountRegisterRespDataScans:
    """ """

    additional_properties: Dict[str, "ModelCloudComplianceScanDetails"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pass

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_cloud_compliance_scan_details import ModelCloudComplianceScanDetails

        d = src_dict.copy()
        model_cloud_node_account_register_resp_data_scans = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ModelCloudComplianceScanDetails.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        model_cloud_node_account_register_resp_data_scans.additional_properties = additional_properties
        return model_cloud_node_account_register_resp_data_scans

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "ModelCloudComplianceScanDetails":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "ModelCloudComplianceScanDetails") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
