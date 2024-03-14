from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelFileAlert")


@_attrs_define
class ModelFileAlert:
    """
    Attributes:
        category (str):
        container_id (str):
        container_image (str):
        container_ip (str):
        container_name (str):
        count (int):
        created_at (int):
        event_type (str):
        filepath (str):
        fstat (str):
        host_name (str):
        kubernetes_cluster_id (str):
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
        rule_id (str):
        severity (str):
        summary (str):
        tactics (Union[List[str], None]):
        techniques (Union[List[str], None]):
        top (str):
        updated_at (int):
        users (str):
    """

    category: str
    container_id: str
    container_image: str
    container_ip: str
    container_name: str
    count: int
    created_at: int
    event_type: str
    filepath: str
    fstat: str
    host_name: str
    kubernetes_cluster_id: str
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
    rule_id: str
    severity: str
    summary: str
    tactics: Union[List[str], None]
    techniques: Union[List[str], None]
    top: str
    updated_at: int
    users: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category = self.category

        container_id = self.container_id

        container_image = self.container_image

        container_ip = self.container_ip

        container_name = self.container_name

        count = self.count

        created_at = self.created_at

        event_type = self.event_type

        filepath = self.filepath

        fstat = self.fstat

        host_name = self.host_name

        kubernetes_cluster_id = self.kubernetes_cluster_id

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

        rule_id = self.rule_id

        severity = self.severity

        summary = self.summary

        tactics: Union[List[str], None]
        if isinstance(self.tactics, list):
            tactics = self.tactics

        else:
            tactics = self.tactics

        techniques: Union[List[str], None]
        if isinstance(self.techniques, list):
            techniques = self.techniques

        else:
            techniques = self.techniques

        top = self.top

        updated_at = self.updated_at

        users = self.users

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
                "event_type": event_type,
                "filepath": filepath,
                "fstat": fstat,
                "host_name": host_name,
                "kubernetes_cluster_id": kubernetes_cluster_id,
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
                "rule_id": rule_id,
                "severity": severity,
                "summary": summary,
                "tactics": tactics,
                "techniques": techniques,
                "top": top,
                "updated_at": updated_at,
                "users": users,
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

        event_type = d.pop("event_type")

        filepath = d.pop("filepath")

        fstat = d.pop("fstat")

        host_name = d.pop("host_name")

        kubernetes_cluster_id = d.pop("kubernetes_cluster_id")

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

        rule_id = d.pop("rule_id")

        severity = d.pop("severity")

        summary = d.pop("summary")

        def _parse_tactics(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tactics_type_0 = cast(List[str], data)

                return tactics_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

        tactics = _parse_tactics(d.pop("tactics"))

        def _parse_techniques(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                techniques_type_0 = cast(List[str], data)

                return techniques_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

        techniques = _parse_techniques(d.pop("techniques"))

        top = d.pop("top")

        updated_at = d.pop("updated_at")

        users = d.pop("users")

        model_file_alert = cls(
            category=category,
            container_id=container_id,
            container_image=container_image,
            container_ip=container_ip,
            container_name=container_name,
            count=count,
            created_at=created_at,
            event_type=event_type,
            filepath=filepath,
            fstat=fstat,
            host_name=host_name,
            kubernetes_cluster_id=kubernetes_cluster_id,
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
            rule_id=rule_id,
            severity=severity,
            summary=summary,
            tactics=tactics,
            techniques=techniques,
            top=top,
            updated_at=updated_at,
            users=users,
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
