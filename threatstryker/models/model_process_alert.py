from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelProcessAlert")


@_attrs_define
class ModelProcessAlert:
    """
    Attributes:
        category (str):
        cloud_account_id (str):
        cloud_provider (str):
        cloud_region (str):
        command (str):
        container_id (str):
        container_image (str):
        container_ip (str):
        container_name (str):
        count (int):
        cpu_time (float):
        created_at (int):
        event_type (str):
        exec_path (str):
        group (str):
        kubernetes_cluster_id (str):
        kubernetes_cluster_name (str):
        masked (bool):
        netstat (str):
        node_id (str):
        node_type (str):
        num_threads (int):
        pid (int):
        pod_name (str):
        priority (int):
        proc_status (str):
        return_ (int):
        rss (int):
        rule_id (str):
        session (int):
        severity (str):
        state (str):
        summary (str):
        tactics (Union[None, list[str]]):
        techniques (Union[None, list[str]]):
        top (str):
        updated_at (int):
        user (str):
        user_name (str):
        users (str):
        vsize (int):
    """

    category: str
    cloud_account_id: str
    cloud_provider: str
    cloud_region: str
    command: str
    container_id: str
    container_image: str
    container_ip: str
    container_name: str
    count: int
    cpu_time: float
    created_at: int
    event_type: str
    exec_path: str
    group: str
    kubernetes_cluster_id: str
    kubernetes_cluster_name: str
    masked: bool
    netstat: str
    node_id: str
    node_type: str
    num_threads: int
    pid: int
    pod_name: str
    priority: int
    proc_status: str
    return_: int
    rss: int
    rule_id: str
    session: int
    severity: str
    state: str
    summary: str
    tactics: Union[None, list[str]]
    techniques: Union[None, list[str]]
    top: str
    updated_at: int
    user: str
    user_name: str
    users: str
    vsize: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        cloud_account_id = self.cloud_account_id

        cloud_provider = self.cloud_provider

        cloud_region = self.cloud_region

        command = self.command

        container_id = self.container_id

        container_image = self.container_image

        container_ip = self.container_ip

        container_name = self.container_name

        count = self.count

        cpu_time = self.cpu_time

        created_at = self.created_at

        event_type = self.event_type

        exec_path = self.exec_path

        group = self.group

        kubernetes_cluster_id = self.kubernetes_cluster_id

        kubernetes_cluster_name = self.kubernetes_cluster_name

        masked = self.masked

        netstat = self.netstat

        node_id = self.node_id

        node_type = self.node_type

        num_threads = self.num_threads

        pid = self.pid

        pod_name = self.pod_name

        priority = self.priority

        proc_status = self.proc_status

        return_ = self.return_

        rss = self.rss

        rule_id = self.rule_id

        session = self.session

        severity = self.severity

        state = self.state

        summary = self.summary

        tactics: Union[None, list[str]]
        if isinstance(self.tactics, list):
            tactics = self.tactics

        else:
            tactics = self.tactics

        techniques: Union[None, list[str]]
        if isinstance(self.techniques, list):
            techniques = self.techniques

        else:
            techniques = self.techniques

        top = self.top

        updated_at = self.updated_at

        user = self.user

        user_name = self.user_name

        users = self.users

        vsize = self.vsize

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "cloud_account_id": cloud_account_id,
                "cloud_provider": cloud_provider,
                "cloud_region": cloud_region,
                "command": command,
                "container_id": container_id,
                "container_image": container_image,
                "container_ip": container_ip,
                "container_name": container_name,
                "count": count,
                "cpu_time": cpu_time,
                "created_at": created_at,
                "event_type": event_type,
                "exec_path": exec_path,
                "group": group,
                "kubernetes_cluster_id": kubernetes_cluster_id,
                "kubernetes_cluster_name": kubernetes_cluster_name,
                "masked": masked,
                "netstat": netstat,
                "node_id": node_id,
                "node_type": node_type,
                "num_threads": num_threads,
                "pid": pid,
                "pod_name": pod_name,
                "priority": priority,
                "proc_status": proc_status,
                "return": return_,
                "rss": rss,
                "rule_id": rule_id,
                "session": session,
                "severity": severity,
                "state": state,
                "summary": summary,
                "tactics": tactics,
                "techniques": techniques,
                "top": top,
                "updated_at": updated_at,
                "user": user,
                "user_name": user_name,
                "users": users,
                "vsize": vsize,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category")

        cloud_account_id = d.pop("cloud_account_id")

        cloud_provider = d.pop("cloud_provider")

        cloud_region = d.pop("cloud_region")

        command = d.pop("command")

        container_id = d.pop("container_id")

        container_image = d.pop("container_image")

        container_ip = d.pop("container_ip")

        container_name = d.pop("container_name")

        count = d.pop("count")

        cpu_time = d.pop("cpu_time")

        created_at = d.pop("created_at")

        event_type = d.pop("event_type")

        exec_path = d.pop("exec_path")

        group = d.pop("group")

        kubernetes_cluster_id = d.pop("kubernetes_cluster_id")

        kubernetes_cluster_name = d.pop("kubernetes_cluster_name")

        masked = d.pop("masked")

        netstat = d.pop("netstat")

        node_id = d.pop("node_id")

        node_type = d.pop("node_type")

        num_threads = d.pop("num_threads")

        pid = d.pop("pid")

        pod_name = d.pop("pod_name")

        priority = d.pop("priority")

        proc_status = d.pop("proc_status")

        return_ = d.pop("return")

        rss = d.pop("rss")

        rule_id = d.pop("rule_id")

        session = d.pop("session")

        severity = d.pop("severity")

        state = d.pop("state")

        summary = d.pop("summary")

        def _parse_tactics(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tactics_type_0 = cast(list[str], data)

                return tactics_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        tactics = _parse_tactics(d.pop("tactics"))

        def _parse_techniques(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                techniques_type_0 = cast(list[str], data)

                return techniques_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        techniques = _parse_techniques(d.pop("techniques"))

        top = d.pop("top")

        updated_at = d.pop("updated_at")

        user = d.pop("user")

        user_name = d.pop("user_name")

        users = d.pop("users")

        vsize = d.pop("vsize")

        model_process_alert = cls(
            category=category,
            cloud_account_id=cloud_account_id,
            cloud_provider=cloud_provider,
            cloud_region=cloud_region,
            command=command,
            container_id=container_id,
            container_image=container_image,
            container_ip=container_ip,
            container_name=container_name,
            count=count,
            cpu_time=cpu_time,
            created_at=created_at,
            event_type=event_type,
            exec_path=exec_path,
            group=group,
            kubernetes_cluster_id=kubernetes_cluster_id,
            kubernetes_cluster_name=kubernetes_cluster_name,
            masked=masked,
            netstat=netstat,
            node_id=node_id,
            node_type=node_type,
            num_threads=num_threads,
            pid=pid,
            pod_name=pod_name,
            priority=priority,
            proc_status=proc_status,
            return_=return_,
            rss=rss,
            rule_id=rule_id,
            session=session,
            severity=severity,
            state=state,
            summary=summary,
            tactics=tactics,
            techniques=techniques,
            top=top,
            updated_at=updated_at,
            user=user,
            user_name=user_name,
            users=users,
            vsize=vsize,
        )

        model_process_alert.additional_properties = d
        return model_process_alert

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
