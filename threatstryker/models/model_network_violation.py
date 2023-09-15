from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelNetworkViolation")


@_attrs_define
class ModelNetworkViolation:
    """
    Example:
        {'severity': 'severity', 'executed_at': 6, 'local_port': 1, 'policy_index': 5, 'remote_port': 2, 'created_at':
            0, 'node_policy_type': 'node_policy_type', 'type': 'type', 'ttl': 9, 'source_ip': 'source_ip', 'local_ip':
            'local_ip', 'remote_ip': 'remote_ip', 'config_id': 'config_id', 'port': 5, 'alert_id': 'alert_id',
            'source_port': 7, 'action': 'action', 'block_ip': 'block_ip', 'pod_id': 'pod_id', 'packet_direction':
            'packet_direction', 'container_id': 'container_id', 'host_name': 'host_name', 'direction': 'direction',
            'node_id': 'node_id'}

    Attributes:
        action (str):
        alert_id (str):
        block_ip (str):
        config_id (str):
        container_id (str):
        created_at (int):
        direction (str):
        executed_at (int):
        host_name (str):
        local_ip (str):
        local_port (int):
        node_id (str):
        node_policy_type (str):
        packet_direction (str):
        pod_id (str):
        policy_index (int):
        port (int):
        remote_ip (str):
        remote_port (int):
        severity (str):
        source_ip (str):
        source_port (int):
        ttl (int):
        type (str):
    """

    action: str
    alert_id: str
    block_ip: str
    config_id: str
    container_id: str
    created_at: int
    direction: str
    executed_at: int
    host_name: str
    local_ip: str
    local_port: int
    node_id: str
    node_policy_type: str
    packet_direction: str
    pod_id: str
    policy_index: int
    port: int
    remote_ip: str
    remote_port: int
    severity: str
    source_ip: str
    source_port: int
    ttl: int
    type: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action = self.action
        alert_id = self.alert_id
        block_ip = self.block_ip
        config_id = self.config_id
        container_id = self.container_id
        created_at = self.created_at
        direction = self.direction
        executed_at = self.executed_at
        host_name = self.host_name
        local_ip = self.local_ip
        local_port = self.local_port
        node_id = self.node_id
        node_policy_type = self.node_policy_type
        packet_direction = self.packet_direction
        pod_id = self.pod_id
        policy_index = self.policy_index
        port = self.port
        remote_ip = self.remote_ip
        remote_port = self.remote_port
        severity = self.severity
        source_ip = self.source_ip
        source_port = self.source_port
        ttl = self.ttl
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "alert_id": alert_id,
                "block_ip": block_ip,
                "config_id": config_id,
                "container_id": container_id,
                "created_at": created_at,
                "direction": direction,
                "executed_at": executed_at,
                "host_name": host_name,
                "local_ip": local_ip,
                "local_port": local_port,
                "node_id": node_id,
                "node_policy_type": node_policy_type,
                "packet_direction": packet_direction,
                "pod_id": pod_id,
                "policy_index": policy_index,
                "port": port,
                "remote_ip": remote_ip,
                "remote_port": remote_port,
                "severity": severity,
                "source_ip": source_ip,
                "source_port": source_port,
                "ttl": ttl,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        action = d.pop("action")

        alert_id = d.pop("alert_id")

        block_ip = d.pop("block_ip")

        config_id = d.pop("config_id")

        container_id = d.pop("container_id")

        created_at = d.pop("created_at")

        direction = d.pop("direction")

        executed_at = d.pop("executed_at")

        host_name = d.pop("host_name")

        local_ip = d.pop("local_ip")

        local_port = d.pop("local_port")

        node_id = d.pop("node_id")

        node_policy_type = d.pop("node_policy_type")

        packet_direction = d.pop("packet_direction")

        pod_id = d.pop("pod_id")

        policy_index = d.pop("policy_index")

        port = d.pop("port")

        remote_ip = d.pop("remote_ip")

        remote_port = d.pop("remote_port")

        severity = d.pop("severity")

        source_ip = d.pop("source_ip")

        source_port = d.pop("source_port")

        ttl = d.pop("ttl")

        type = d.pop("type")

        model_network_violation = cls(
            action=action,
            alert_id=alert_id,
            block_ip=block_ip,
            config_id=config_id,
            container_id=container_id,
            created_at=created_at,
            direction=direction,
            executed_at=executed_at,
            host_name=host_name,
            local_ip=local_ip,
            local_port=local_port,
            node_id=node_id,
            node_policy_type=node_policy_type,
            packet_direction=packet_direction,
            pod_id=pod_id,
            policy_index=policy_index,
            port=port,
            remote_ip=remote_ip,
            remote_port=remote_port,
            severity=severity,
            source_ip=source_ip,
            source_port=source_port,
            ttl=ttl,
            type=type,
        )

        model_network_violation.additional_properties = d
        return model_network_violation

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
