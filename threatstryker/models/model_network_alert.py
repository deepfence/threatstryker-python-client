from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelNetworkAlert")


@_attrs_define
class ModelNetworkAlert:
    """
    Attributes:
        category (str):
        cloud_account_id (str):
        cloud_provider (str):
        cloud_region (str):
        container_name (str):
        count (int):
        created_at (int):
        destination_ip (str):
        destination_port (int):
        direction (str):
        encrypted (bool):
        event_type (str):
        headers (str):
        host_name (str):
        http_type (str):
        kubernetes_cluster_id (str):
        kubernetes_cluster_name (str):
        masked (bool):
        node_id (str):
        node_type (str):
        pod_name (str):
        protocol (str):
        references (str):
        rule_id (str):
        severity (str):
        source_ip (str):
        source_port (int):
        summary (str):
        tactics (Union[None, list[str]]):
        tags (str):
        techniques (Union[None, list[str]]):
        updated_at (int):
        url (str):
        request (Union[Unset, str]):
        response (Union[Unset, str]):
    """

    category: str
    cloud_account_id: str
    cloud_provider: str
    cloud_region: str
    container_name: str
    count: int
    created_at: int
    destination_ip: str
    destination_port: int
    direction: str
    encrypted: bool
    event_type: str
    headers: str
    host_name: str
    http_type: str
    kubernetes_cluster_id: str
    kubernetes_cluster_name: str
    masked: bool
    node_id: str
    node_type: str
    pod_name: str
    protocol: str
    references: str
    rule_id: str
    severity: str
    source_ip: str
    source_port: int
    summary: str
    tactics: Union[None, list[str]]
    tags: str
    techniques: Union[None, list[str]]
    updated_at: int
    url: str
    request: Union[Unset, str] = UNSET
    response: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        cloud_account_id = self.cloud_account_id

        cloud_provider = self.cloud_provider

        cloud_region = self.cloud_region

        container_name = self.container_name

        count = self.count

        created_at = self.created_at

        destination_ip = self.destination_ip

        destination_port = self.destination_port

        direction = self.direction

        encrypted = self.encrypted

        event_type = self.event_type

        headers = self.headers

        host_name = self.host_name

        http_type = self.http_type

        kubernetes_cluster_id = self.kubernetes_cluster_id

        kubernetes_cluster_name = self.kubernetes_cluster_name

        masked = self.masked

        node_id = self.node_id

        node_type = self.node_type

        pod_name = self.pod_name

        protocol = self.protocol

        references = self.references

        rule_id = self.rule_id

        severity = self.severity

        source_ip = self.source_ip

        source_port = self.source_port

        summary = self.summary

        tactics: Union[None, list[str]]
        if isinstance(self.tactics, list):
            tactics = self.tactics

        else:
            tactics = self.tactics

        tags = self.tags

        techniques: Union[None, list[str]]
        if isinstance(self.techniques, list):
            techniques = self.techniques

        else:
            techniques = self.techniques

        updated_at = self.updated_at

        url = self.url

        request = self.request

        response = self.response

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "cloud_account_id": cloud_account_id,
                "cloud_provider": cloud_provider,
                "cloud_region": cloud_region,
                "container_name": container_name,
                "count": count,
                "created_at": created_at,
                "destination_ip": destination_ip,
                "destination_port": destination_port,
                "direction": direction,
                "encrypted": encrypted,
                "event_type": event_type,
                "headers": headers,
                "host_name": host_name,
                "http_type": http_type,
                "kubernetes_cluster_id": kubernetes_cluster_id,
                "kubernetes_cluster_name": kubernetes_cluster_name,
                "masked": masked,
                "node_id": node_id,
                "node_type": node_type,
                "pod_name": pod_name,
                "protocol": protocol,
                "references": references,
                "rule_id": rule_id,
                "severity": severity,
                "source_ip": source_ip,
                "source_port": source_port,
                "summary": summary,
                "tactics": tactics,
                "tags": tags,
                "techniques": techniques,
                "updated_at": updated_at,
                "url": url,
            }
        )
        if request is not UNSET:
            field_dict["request"] = request
        if response is not UNSET:
            field_dict["response"] = response

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category")

        cloud_account_id = d.pop("cloud_account_id")

        cloud_provider = d.pop("cloud_provider")

        cloud_region = d.pop("cloud_region")

        container_name = d.pop("container_name")

        count = d.pop("count")

        created_at = d.pop("created_at")

        destination_ip = d.pop("destination_ip")

        destination_port = d.pop("destination_port")

        direction = d.pop("direction")

        encrypted = d.pop("encrypted")

        event_type = d.pop("event_type")

        headers = d.pop("headers")

        host_name = d.pop("host_name")

        http_type = d.pop("http_type")

        kubernetes_cluster_id = d.pop("kubernetes_cluster_id")

        kubernetes_cluster_name = d.pop("kubernetes_cluster_name")

        masked = d.pop("masked")

        node_id = d.pop("node_id")

        node_type = d.pop("node_type")

        pod_name = d.pop("pod_name")

        protocol = d.pop("protocol")

        references = d.pop("references")

        rule_id = d.pop("rule_id")

        severity = d.pop("severity")

        source_ip = d.pop("source_ip")

        source_port = d.pop("source_port")

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

        tags = d.pop("tags")

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

        updated_at = d.pop("updated_at")

        url = d.pop("url")

        request = d.pop("request", UNSET)

        response = d.pop("response", UNSET)

        model_network_alert = cls(
            category=category,
            cloud_account_id=cloud_account_id,
            cloud_provider=cloud_provider,
            cloud_region=cloud_region,
            container_name=container_name,
            count=count,
            created_at=created_at,
            destination_ip=destination_ip,
            destination_port=destination_port,
            direction=direction,
            encrypted=encrypted,
            event_type=event_type,
            headers=headers,
            host_name=host_name,
            http_type=http_type,
            kubernetes_cluster_id=kubernetes_cluster_id,
            kubernetes_cluster_name=kubernetes_cluster_name,
            masked=masked,
            node_id=node_id,
            node_type=node_type,
            pod_name=pod_name,
            protocol=protocol,
            references=references,
            rule_id=rule_id,
            severity=severity,
            source_ip=source_ip,
            source_port=source_port,
            summary=summary,
            tactics=tactics,
            tags=tags,
            techniques=techniques,
            updated_at=updated_at,
            url=url,
            request=request,
            response=response,
        )

        model_network_alert.additional_properties = d
        return model_network_alert

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
