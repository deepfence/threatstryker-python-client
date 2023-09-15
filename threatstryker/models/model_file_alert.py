from typing import Any, Dict, List, Optional, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelFileAlert")


@_attrs_define
class ModelFileAlert:
    """
    Example:
        {'container_ip': 'container_ip', 'kubernetes_cluster_name': 'kubernetes_cluster_name', 'masked': True,
            'created_at': 6, 'pid': 1, 'signature_id': 5, 'event_type': 'event_type', 'node_type': 'node_type', 'filepath':
            'filepath', 'top': 'top', 'updated_at': 2, 'process_name': 'process_name', 'direction': 'direction', 'severity':
            'severity', 'summary': 'summary', 'count': 0, 'resource_type': 'resource_type', 'fstat': 'fstat',
            'container_image': 'container_image', 'netstat': 'netstat', 'users': 'users', 'pod_name': 'pod_name',
            'container_name': 'container_name', 'techniques': ['techniques', 'techniques'], 'w': 7, 'tactics': ['tactics',
            'tactics'], 'proc_status': 'proc_status', 'category': 'category', 'container_id': 'container_id', 'host_name':
            'host_name', 'node_id': 'node_id', 'severity_score': 5.962133916683182}

    Attributes:
        category (str):
        container_id (str):
        container_image (str):
        container_ip (str):
        container_name (str):
        count (int):
        created_at (int):
        direction (str):
        event_type (str):
        filepath (str):
        fstat (str):
        host_name (str):
        kubernetes_cluster_name (str):
        masked (bool):
        netstat (str):
        node_id (str):
        node_type (str):
        pid (int):
        pod_name (str):
        proc_status (str):
        process_name (str):
        resource_type (str):
        severity (str):
        severity_score (float):
        signature_id (int):
        summary (str):
        top (str):
        updated_at (int):
        users (str):
        w (int):
        tactics (Optional[List[str]]):
        techniques (Optional[List[str]]):
    """

    category: str
    container_id: str
    container_image: str
    container_ip: str
    container_name: str
    count: int
    created_at: int
    direction: str
    event_type: str
    filepath: str
    fstat: str
    host_name: str
    kubernetes_cluster_name: str
    masked: bool
    netstat: str
    node_id: str
    node_type: str
    pid: int
    pod_name: str
    proc_status: str
    process_name: str
    resource_type: str
    severity: str
    severity_score: float
    signature_id: int
    summary: str
    top: str
    updated_at: int
    users: str
    w: int
    tactics: Optional[List[str]]
    techniques: Optional[List[str]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category = self.category
        container_id = self.container_id
        container_image = self.container_image
        container_ip = self.container_ip
        container_name = self.container_name
        count = self.count
        created_at = self.created_at
        direction = self.direction
        event_type = self.event_type
        filepath = self.filepath
        fstat = self.fstat
        host_name = self.host_name
        kubernetes_cluster_name = self.kubernetes_cluster_name
        masked = self.masked
        netstat = self.netstat
        node_id = self.node_id
        node_type = self.node_type
        pid = self.pid
        pod_name = self.pod_name
        proc_status = self.proc_status
        process_name = self.process_name
        resource_type = self.resource_type
        severity = self.severity
        severity_score = self.severity_score
        signature_id = self.signature_id
        summary = self.summary
        top = self.top
        updated_at = self.updated_at
        users = self.users
        w = self.w
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
                "container_id": container_id,
                "container_image": container_image,
                "container_ip": container_ip,
                "container_name": container_name,
                "count": count,
                "created_at": created_at,
                "direction": direction,
                "event_type": event_type,
                "filepath": filepath,
                "fstat": fstat,
                "host_name": host_name,
                "kubernetes_cluster_name": kubernetes_cluster_name,
                "masked": masked,
                "netstat": netstat,
                "node_id": node_id,
                "node_type": node_type,
                "pid": pid,
                "pod_name": pod_name,
                "proc_status": proc_status,
                "process_name": process_name,
                "resource_type": resource_type,
                "severity": severity,
                "severity_score": severity_score,
                "signature_id": signature_id,
                "summary": summary,
                "top": top,
                "updated_at": updated_at,
                "users": users,
                "w": w,
                "tactics": tactics,
                "techniques": techniques,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        category = d.pop("category")

        container_id = d.pop("container_id")

        container_image = d.pop("container_image")

        container_ip = d.pop("container_ip")

        container_name = d.pop("container_name")

        count = d.pop("count")

        created_at = d.pop("created_at")

        direction = d.pop("direction")

        event_type = d.pop("event_type")

        filepath = d.pop("filepath")

        fstat = d.pop("fstat")

        host_name = d.pop("host_name")

        kubernetes_cluster_name = d.pop("kubernetes_cluster_name")

        masked = d.pop("masked")

        netstat = d.pop("netstat")

        node_id = d.pop("node_id")

        node_type = d.pop("node_type")

        pid = d.pop("pid")

        pod_name = d.pop("pod_name")

        proc_status = d.pop("proc_status")

        process_name = d.pop("process_name")

        resource_type = d.pop("resource_type")

        severity = d.pop("severity")

        severity_score = d.pop("severity_score")

        signature_id = d.pop("signature_id")

        summary = d.pop("summary")

        top = d.pop("top")

        updated_at = d.pop("updated_at")

        users = d.pop("users")

        w = d.pop("w")

        tactics = cast(List[str], d.pop("tactics"))

        techniques = cast(List[str], d.pop("techniques"))

        model_file_alert = cls(
            category=category,
            container_id=container_id,
            container_image=container_image,
            container_ip=container_ip,
            container_name=container_name,
            count=count,
            created_at=created_at,
            direction=direction,
            event_type=event_type,
            filepath=filepath,
            fstat=fstat,
            host_name=host_name,
            kubernetes_cluster_name=kubernetes_cluster_name,
            masked=masked,
            netstat=netstat,
            node_id=node_id,
            node_type=node_type,
            pid=pid,
            pod_name=pod_name,
            proc_status=proc_status,
            process_name=process_name,
            resource_type=resource_type,
            severity=severity,
            severity_score=severity_score,
            signature_id=signature_id,
            summary=summary,
            top=top,
            updated_at=updated_at,
            users=users,
            w=w,
            tactics=tactics,
            techniques=techniques,
        )

        model_file_alert.additional_properties = d
        return model_file_alert

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
