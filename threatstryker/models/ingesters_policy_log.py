from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ingesters_policy_log_direction import IngestersPolicyLogDirection

T = TypeVar("T", bound="IngestersPolicyLog")


@_attrs_define
class IngestersPolicyLog:
    """
    Attributes:
        alert_id (str):
        config_id (str):
        created_at (int):
        direction (IngestersPolicyLogDirection):
        host_name (str):
        incident (str):
        local_ip (str):
        local_port (int):
        policy_index (int):
        remote_ip (str):
        remote_port (int):
        severity (str):
    """

    alert_id: str
    config_id: str
    created_at: int
    direction: IngestersPolicyLogDirection
    host_name: str
    incident: str
    local_ip: str
    local_port: int
    policy_index: int
    remote_ip: str
    remote_port: int
    severity: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alert_id = self.alert_id

        config_id = self.config_id

        created_at = self.created_at

        direction = self.direction.value

        host_name = self.host_name

        incident = self.incident

        local_ip = self.local_ip

        local_port = self.local_port

        policy_index = self.policy_index

        remote_ip = self.remote_ip

        remote_port = self.remote_port

        severity = self.severity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alert_id": alert_id,
                "config_id": config_id,
                "created_at": created_at,
                "direction": direction,
                "host_name": host_name,
                "incident": incident,
                "local_ip": local_ip,
                "local_port": local_port,
                "policy_index": policy_index,
                "remote_ip": remote_ip,
                "remote_port": remote_port,
                "severity": severity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        alert_id = d.pop("alert_id")

        config_id = d.pop("config_id")

        created_at = d.pop("created_at")

        direction = IngestersPolicyLogDirection(d.pop("direction"))

        host_name = d.pop("host_name")

        incident = d.pop("incident")

        local_ip = d.pop("local_ip")

        local_port = d.pop("local_port")

        policy_index = d.pop("policy_index")

        remote_ip = d.pop("remote_ip")

        remote_port = d.pop("remote_port")

        severity = d.pop("severity")

        ingesters_policy_log = cls(
            alert_id=alert_id,
            config_id=config_id,
            created_at=created_at,
            direction=direction,
            host_name=host_name,
            incident=incident,
            local_ip=local_ip,
            local_port=local_port,
            policy_index=policy_index,
            remote_ip=remote_ip,
            remote_port=remote_port,
            severity=severity,
        )

        ingesters_policy_log.additional_properties = d
        return ingesters_policy_log

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
