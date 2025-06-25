from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelQuarantineViolation")


@_attrs_define
class ModelQuarantineViolation:
    """
    Attributes:
        action (str):
        alert_id (str):
        config_id (str):
        container_id (str):
        created_at (int):
        executed_at (int):
        host_name (str):
        node_id (str):
        pod_id (str):
        policy_index (int):
        severity (str):
        ttl (int):
        type_ (str):
    """

    action: str
    alert_id: str
    config_id: str
    container_id: str
    created_at: int
    executed_at: int
    host_name: str
    node_id: str
    pod_id: str
    policy_index: int
    severity: str
    ttl: int
    type_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        alert_id = self.alert_id

        config_id = self.config_id

        container_id = self.container_id

        created_at = self.created_at

        executed_at = self.executed_at

        host_name = self.host_name

        node_id = self.node_id

        pod_id = self.pod_id

        policy_index = self.policy_index

        severity = self.severity

        ttl = self.ttl

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "alert_id": alert_id,
                "config_id": config_id,
                "container_id": container_id,
                "created_at": created_at,
                "executed_at": executed_at,
                "host_name": host_name,
                "node_id": node_id,
                "pod_id": pod_id,
                "policy_index": policy_index,
                "severity": severity,
                "ttl": ttl,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action")

        alert_id = d.pop("alert_id")

        config_id = d.pop("config_id")

        container_id = d.pop("container_id")

        created_at = d.pop("created_at")

        executed_at = d.pop("executed_at")

        host_name = d.pop("host_name")

        node_id = d.pop("node_id")

        pod_id = d.pop("pod_id")

        policy_index = d.pop("policy_index")

        severity = d.pop("severity")

        ttl = d.pop("ttl")

        type_ = d.pop("type")

        model_quarantine_violation = cls(
            action=action,
            alert_id=alert_id,
            config_id=config_id,
            container_id=container_id,
            created_at=created_at,
            executed_at=executed_at,
            host_name=host_name,
            node_id=node_id,
            pod_id=pod_id,
            policy_index=policy_index,
            severity=severity,
            ttl=ttl,
            type_=type_,
        )

        model_quarantine_violation.additional_properties = d
        return model_quarantine_violation

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
