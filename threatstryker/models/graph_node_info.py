from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GraphNodeInfo")


@_attrs_define
class GraphNodeInfo:
    """
    Attributes:
        alerts_count (int):
        cloud_compliance_count (int):
        cloud_warn_alarm_count (int):
        compliance_count (int):
        exploitable_secrets_count (int):
        exploitable_vulnerabilities_count (int):
        name (str):
        node_id (str):
        secrets_count (int):
        vulnerability_count (int):
        warn_alarm_count (int):
    """

    alerts_count: int
    cloud_compliance_count: int
    cloud_warn_alarm_count: int
    compliance_count: int
    exploitable_secrets_count: int
    exploitable_vulnerabilities_count: int
    name: str
    node_id: str
    secrets_count: int
    vulnerability_count: int
    warn_alarm_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alerts_count = self.alerts_count

        cloud_compliance_count = self.cloud_compliance_count

        cloud_warn_alarm_count = self.cloud_warn_alarm_count

        compliance_count = self.compliance_count

        exploitable_secrets_count = self.exploitable_secrets_count

        exploitable_vulnerabilities_count = self.exploitable_vulnerabilities_count

        name = self.name

        node_id = self.node_id

        secrets_count = self.secrets_count

        vulnerability_count = self.vulnerability_count

        warn_alarm_count = self.warn_alarm_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alerts_count": alerts_count,
                "cloud_compliance_count": cloud_compliance_count,
                "cloud_warn_alarm_count": cloud_warn_alarm_count,
                "compliance_count": compliance_count,
                "exploitable_secrets_count": exploitable_secrets_count,
                "exploitable_vulnerabilities_count": exploitable_vulnerabilities_count,
                "name": name,
                "node_id": node_id,
                "secrets_count": secrets_count,
                "vulnerability_count": vulnerability_count,
                "warn_alarm_count": warn_alarm_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        alerts_count = d.pop("alerts_count")

        cloud_compliance_count = d.pop("cloud_compliance_count")

        cloud_warn_alarm_count = d.pop("cloud_warn_alarm_count")

        compliance_count = d.pop("compliance_count")

        exploitable_secrets_count = d.pop("exploitable_secrets_count")

        exploitable_vulnerabilities_count = d.pop("exploitable_vulnerabilities_count")

        name = d.pop("name")

        node_id = d.pop("node_id")

        secrets_count = d.pop("secrets_count")

        vulnerability_count = d.pop("vulnerability_count")

        warn_alarm_count = d.pop("warn_alarm_count")

        graph_node_info = cls(
            alerts_count=alerts_count,
            cloud_compliance_count=cloud_compliance_count,
            cloud_warn_alarm_count=cloud_warn_alarm_count,
            compliance_count=compliance_count,
            exploitable_secrets_count=exploitable_secrets_count,
            exploitable_vulnerabilities_count=exploitable_vulnerabilities_count,
            name=name,
            node_id=node_id,
            secrets_count=secrets_count,
            vulnerability_count=vulnerability_count,
            warn_alarm_count=warn_alarm_count,
        )

        graph_node_info.additional_properties = d
        return graph_node_info

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
