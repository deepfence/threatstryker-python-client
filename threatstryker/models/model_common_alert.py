from typing import Any, Dict, List, Optional, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelCommonAlert")


@_attrs_define
class ModelCommonAlert:
    """
    Example:
        {'severity': 'severity', 'summary': 'summary', 'geoip': 'geoip', 'kubernetes_cluster_name':
            'kubernetes_cluster_name', 'masked': True, 'count': 0, 'created_at': 6, 'pod_name': 'pod_name', 'rule_id':
            'rule_id', 'event_type': 'event_type', 'node_type': 'node_type', 'container_name': 'container_name',
            'updated_at': 1, 'techniques': ['techniques', 'techniques'], 'tactics': ['tactics', 'tactics'], 'matched':
            'matched', 'category': 'category', 'host_name': 'host_name', 'node_id': 'node_id'}

    Attributes:
        category (str):
        container_name (str):
        count (int):
        created_at (int):
        event_type (str):
        geoip (str):
        host_name (str):
        kubernetes_cluster_name (str):
        masked (bool):
        matched (str):
        node_id (str):
        node_type (str):
        pod_name (str):
        rule_id (str):
        severity (str):
        summary (str):
        updated_at (int):
        tactics (Optional[List[str]]):
        techniques (Optional[List[str]]):
    """

    category: str
    container_name: str
    count: int
    created_at: int
    event_type: str
    geoip: str
    host_name: str
    kubernetes_cluster_name: str
    masked: bool
    matched: str
    node_id: str
    node_type: str
    pod_name: str
    rule_id: str
    severity: str
    summary: str
    updated_at: int
    tactics: Optional[List[str]]
    techniques: Optional[List[str]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category = self.category
        container_name = self.container_name
        count = self.count
        created_at = self.created_at
        event_type = self.event_type
        geoip = self.geoip
        host_name = self.host_name
        kubernetes_cluster_name = self.kubernetes_cluster_name
        masked = self.masked
        matched = self.matched
        node_id = self.node_id
        node_type = self.node_type
        pod_name = self.pod_name
        rule_id = self.rule_id
        severity = self.severity
        summary = self.summary
        updated_at = self.updated_at
        if self.tactics is None:
            tactics = None
        else:
            tactics = self.tactics

        if self.techniques is None:
            techniques = None
        else:
            techniques = self.techniques

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "container_name": container_name,
                "count": count,
                "created_at": created_at,
                "event_type": event_type,
                "geoip": geoip,
                "host_name": host_name,
                "kubernetes_cluster_name": kubernetes_cluster_name,
                "masked": masked,
                "matched": matched,
                "node_id": node_id,
                "node_type": node_type,
                "pod_name": pod_name,
                "rule_id": rule_id,
                "severity": severity,
                "summary": summary,
                "updated_at": updated_at,
                "tactics": tactics,
                "techniques": techniques,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        category = d.pop("category")

        container_name = d.pop("container_name")

        count = d.pop("count")

        created_at = d.pop("created_at")

        event_type = d.pop("event_type")

        geoip = d.pop("geoip")

        host_name = d.pop("host_name")

        kubernetes_cluster_name = d.pop("kubernetes_cluster_name")

        masked = d.pop("masked")

        matched = d.pop("matched")

        node_id = d.pop("node_id")

        node_type = d.pop("node_type")

        pod_name = d.pop("pod_name")

        rule_id = d.pop("rule_id")

        severity = d.pop("severity")

        summary = d.pop("summary")

        updated_at = d.pop("updated_at")

        tactics = cast(List[str], d.pop("tactics"))

        techniques = cast(List[str], d.pop("techniques"))

        model_common_alert = cls(
            category=category,
            container_name=container_name,
            count=count,
            created_at=created_at,
            event_type=event_type,
            geoip=geoip,
            host_name=host_name,
            kubernetes_cluster_name=kubernetes_cluster_name,
            masked=masked,
            matched=matched,
            node_id=node_id,
            node_type=node_type,
            pod_name=pod_name,
            rule_id=rule_id,
            severity=severity,
            summary=summary,
            updated_at=updated_at,
            tactics=tactics,
            techniques=techniques,
        )

        model_common_alert.additional_properties = d
        return model_common_alert

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
