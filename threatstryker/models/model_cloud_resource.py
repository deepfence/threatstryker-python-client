from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_cloud_resource_agent_install_availability import ModelCloudResourceAgentInstallAvailability
from ..models.model_cloud_resource_cloud_provider import ModelCloudResourceCloudProvider

T = TypeVar("T", bound="ModelCloudResource")


@_attrs_define
class ModelCloudResource:
    """
    Attributes:
        account_id (str):
        agent_install_availability (ModelCloudResourceAgentInstallAvailability):
        cloud_compliance_latest_scan_id (str):
        cloud_compliance_scan_status (str):
        cloud_compliances_count (int):
        cloud_provider (ModelCloudResourceCloudProvider):
        cloud_region (str):
        cloud_warn_alarm_count (int):
        node_id (str):
        node_name (str):
        node_type (str):
        type_label (str):
    """

    account_id: str
    agent_install_availability: ModelCloudResourceAgentInstallAvailability
    cloud_compliance_latest_scan_id: str
    cloud_compliance_scan_status: str
    cloud_compliances_count: int
    cloud_provider: ModelCloudResourceCloudProvider
    cloud_region: str
    cloud_warn_alarm_count: int
    node_id: str
    node_name: str
    node_type: str
    type_label: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        agent_install_availability = self.agent_install_availability.value

        cloud_compliance_latest_scan_id = self.cloud_compliance_latest_scan_id

        cloud_compliance_scan_status = self.cloud_compliance_scan_status

        cloud_compliances_count = self.cloud_compliances_count

        cloud_provider = self.cloud_provider.value

        cloud_region = self.cloud_region

        cloud_warn_alarm_count = self.cloud_warn_alarm_count

        node_id = self.node_id

        node_name = self.node_name

        node_type = self.node_type

        type_label = self.type_label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "agent_install_availability": agent_install_availability,
                "cloud_compliance_latest_scan_id": cloud_compliance_latest_scan_id,
                "cloud_compliance_scan_status": cloud_compliance_scan_status,
                "cloud_compliances_count": cloud_compliances_count,
                "cloud_provider": cloud_provider,
                "cloud_region": cloud_region,
                "cloud_warn_alarm_count": cloud_warn_alarm_count,
                "node_id": node_id,
                "node_name": node_name,
                "node_type": node_type,
                "type_label": type_label,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id")

        agent_install_availability = ModelCloudResourceAgentInstallAvailability(d.pop("agent_install_availability"))

        cloud_compliance_latest_scan_id = d.pop("cloud_compliance_latest_scan_id")

        cloud_compliance_scan_status = d.pop("cloud_compliance_scan_status")

        cloud_compliances_count = d.pop("cloud_compliances_count")

        cloud_provider = ModelCloudResourceCloudProvider(d.pop("cloud_provider"))

        cloud_region = d.pop("cloud_region")

        cloud_warn_alarm_count = d.pop("cloud_warn_alarm_count")

        node_id = d.pop("node_id")

        node_name = d.pop("node_name")

        node_type = d.pop("node_type")

        type_label = d.pop("type_label")

        model_cloud_resource = cls(
            account_id=account_id,
            agent_install_availability=agent_install_availability,
            cloud_compliance_latest_scan_id=cloud_compliance_latest_scan_id,
            cloud_compliance_scan_status=cloud_compliance_scan_status,
            cloud_compliances_count=cloud_compliances_count,
            cloud_provider=cloud_provider,
            cloud_region=cloud_region,
            cloud_warn_alarm_count=cloud_warn_alarm_count,
            node_id=node_id,
            node_name=node_name,
            node_type=node_type,
            type_label=type_label,
        )

        model_cloud_resource.additional_properties = d
        return model_cloud_resource

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
