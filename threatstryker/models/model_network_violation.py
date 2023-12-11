from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelNetworkViolation")


@_attrs_define
class ModelNetworkViolation:
    """
    Example:
        {'severity': 'severity', 'defenderd': 'defenderd', 'executed_at': 6, 'local_port': 1, 'policy_index': 5,
            'remote_port': 5, 'created_at': 0, 'node_policy_type': 'node_policy_type', 'ttl': 2, 'local_ip': 'local_ip',
            'event_type': 'event_type', 'remote_ip': 'remote_ip', 'config_id': 'config_id', 'alert_id': 'alert_id',
            'action': 'action', 'block_ip': 'block_ip', 'pod_id': 'pod_id', 'packet_direction': 'packet_direction',
            'container_id': 'container_id', 'host_name': 'host_name', 'direction': 'direction', 'node_id': 'node_id',
            'status': 'status'}

    Attributes:
        action (Union[Unset, str]):
        alert_id (Union[Unset, str]):
        block_ip (Union[Unset, str]):
        config_id (Union[Unset, str]):
        container_id (Union[Unset, str]):
        created_at (Union[Unset, int]):
        defenderd (Union[Unset, str]):
        direction (Union[Unset, str]):
        event_type (Union[Unset, str]):
        executed_at (Union[Unset, int]):
        host_name (Union[Unset, str]):
        local_ip (Union[Unset, str]):
        local_port (Union[Unset, int]):
        node_id (Union[Unset, str]):
        node_policy_type (Union[Unset, str]):
        packet_direction (Union[Unset, str]):
        pod_id (Union[Unset, str]):
        policy_index (Union[Unset, int]):
        remote_ip (Union[Unset, str]):
        remote_port (Union[Unset, int]):
        severity (Union[Unset, str]):
        status (Union[Unset, str]):
        ttl (Union[Unset, int]):
    """

    action: Union[Unset, str] = UNSET
    alert_id: Union[Unset, str] = UNSET
    block_ip: Union[Unset, str] = UNSET
    config_id: Union[Unset, str] = UNSET
    container_id: Union[Unset, str] = UNSET
    created_at: Union[Unset, int] = UNSET
    defenderd: Union[Unset, str] = UNSET
    direction: Union[Unset, str] = UNSET
    event_type: Union[Unset, str] = UNSET
    executed_at: Union[Unset, int] = UNSET
    host_name: Union[Unset, str] = UNSET
    local_ip: Union[Unset, str] = UNSET
    local_port: Union[Unset, int] = UNSET
    node_id: Union[Unset, str] = UNSET
    node_policy_type: Union[Unset, str] = UNSET
    packet_direction: Union[Unset, str] = UNSET
    pod_id: Union[Unset, str] = UNSET
    policy_index: Union[Unset, int] = UNSET
    remote_ip: Union[Unset, str] = UNSET
    remote_port: Union[Unset, int] = UNSET
    severity: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    ttl: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action = self.action
        alert_id = self.alert_id
        block_ip = self.block_ip
        config_id = self.config_id
        container_id = self.container_id
        created_at = self.created_at
        defenderd = self.defenderd
        direction = self.direction
        event_type = self.event_type
        executed_at = self.executed_at
        host_name = self.host_name
        local_ip = self.local_ip
        local_port = self.local_port
        node_id = self.node_id
        node_policy_type = self.node_policy_type
        packet_direction = self.packet_direction
        pod_id = self.pod_id
        policy_index = self.policy_index
        remote_ip = self.remote_ip
        remote_port = self.remote_port
        severity = self.severity
        status = self.status
        ttl = self.ttl

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if alert_id is not UNSET:
            field_dict["alert_id"] = alert_id
        if block_ip is not UNSET:
            field_dict["block_ip"] = block_ip
        if config_id is not UNSET:
            field_dict["config_id"] = config_id
        if container_id is not UNSET:
            field_dict["container_id"] = container_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if defenderd is not UNSET:
            field_dict["defenderd"] = defenderd
        if direction is not UNSET:
            field_dict["direction"] = direction
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if executed_at is not UNSET:
            field_dict["executed_at"] = executed_at
        if host_name is not UNSET:
            field_dict["host_name"] = host_name
        if local_ip is not UNSET:
            field_dict["local_ip"] = local_ip
        if local_port is not UNSET:
            field_dict["local_port"] = local_port
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if node_policy_type is not UNSET:
            field_dict["node_policy_type"] = node_policy_type
        if packet_direction is not UNSET:
            field_dict["packet_direction"] = packet_direction
        if pod_id is not UNSET:
            field_dict["pod_id"] = pod_id
        if policy_index is not UNSET:
            field_dict["policy_index"] = policy_index
        if remote_ip is not UNSET:
            field_dict["remote_ip"] = remote_ip
        if remote_port is not UNSET:
            field_dict["remote_port"] = remote_port
        if severity is not UNSET:
            field_dict["severity"] = severity
        if status is not UNSET:
            field_dict["status"] = status
        if ttl is not UNSET:
            field_dict["ttl"] = ttl

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        action = d.pop("action", UNSET)

        alert_id = d.pop("alert_id", UNSET)

        block_ip = d.pop("block_ip", UNSET)

        config_id = d.pop("config_id", UNSET)

        container_id = d.pop("container_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        defenderd = d.pop("defenderd", UNSET)

        direction = d.pop("direction", UNSET)

        event_type = d.pop("event_type", UNSET)

        executed_at = d.pop("executed_at", UNSET)

        host_name = d.pop("host_name", UNSET)

        local_ip = d.pop("local_ip", UNSET)

        local_port = d.pop("local_port", UNSET)

        node_id = d.pop("node_id", UNSET)

        node_policy_type = d.pop("node_policy_type", UNSET)

        packet_direction = d.pop("packet_direction", UNSET)

        pod_id = d.pop("pod_id", UNSET)

        policy_index = d.pop("policy_index", UNSET)

        remote_ip = d.pop("remote_ip", UNSET)

        remote_port = d.pop("remote_port", UNSET)

        severity = d.pop("severity", UNSET)

        status = d.pop("status", UNSET)

        ttl = d.pop("ttl", UNSET)

        model_network_violation = cls(
            action=action,
            alert_id=alert_id,
            block_ip=block_ip,
            config_id=config_id,
            container_id=container_id,
            created_at=created_at,
            defenderd=defenderd,
            direction=direction,
            event_type=event_type,
            executed_at=executed_at,
            host_name=host_name,
            local_ip=local_ip,
            local_port=local_port,
            node_id=node_id,
            node_policy_type=node_policy_type,
            packet_direction=packet_direction,
            pod_id=pod_id,
            policy_index=policy_index,
            remote_ip=remote_ip,
            remote_port=remote_port,
            severity=severity,
            status=status,
            ttl=ttl,
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
