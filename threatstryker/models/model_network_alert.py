from typing import Any, Dict, List, Optional, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelNetworkAlert")


@_attrs_define
class ModelNetworkAlert:
    """
    Example:
        {'internal': 'internal', 'destination_port': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name', 'masked':
            True, 'created_at': 6, 'description': 'description', 'request_method': 'request_method', 'http_user_agent':
            'http_user_agent', 'source_ip': 'source_ip', 'protocol': 5, 'signature_id': 7, 'destination_ip':
            'destination_ip', 'event_type': 'event_type', 'node_type': 'node_type', 'http_content_type': '', 'updated_at':
            3, 'ip_reputation': 'ip_reputation', 'source_port': 9, 'direction': 'direction', 'request_printable_payload':
            'request_printable_payload', 'severity': 'severity', 'summary': 'summary', 'headers': 'headers', 'geoip':
            'geoip', 'local_port': 5, 'count': 0, 'length': '', 'resource_type': 'resource_type', 'http_type': 'http_type',
            'response_printable_payload': '', 'app_proto': 'app_proto', 'url': 'url', 'pod_name': 'pod_name', 'tags':
            'tags', 'rule_id': 'rule_id', 'container_name': 'container_name', 'encrypted': 'encrypted', 'techniques':
            ['techniques', 'techniques'], 'request_path': 'request_path', 'tactics': ['tactics', 'tactics'], 'matched':
            'matched', 'category': 'category', 'request_payload': 'request_payload', 'host_name': 'host_name',
            'response_payload': '', 'node_id': 'node_id', 'severity_score': 2.3021358869347655, 'status': ''}

    Attributes:
        app_proto (str):
        category (str):
        container_name (str):
        count (int):
        created_at (int):
        description (str):
        destination_ip (str):
        destination_port (int):
        direction (str):
        encrypted (str):
        event_type (str):
        geoip (str):
        headers (str):
        host_name (str):
        http_content_type (Any):
        http_type (str):
        http_user_agent (str):
        internal (str):
        ip_reputation (str):
        kubernetes_cluster_name (str):
        length (Any):
        local_port (int):
        masked (bool):
        matched (str):
        node_id (str):
        node_type (str):
        pod_name (str):
        protocol (int):
        request_method (str):
        request_path (str):
        request_payload (str):
        request_printable_payload (str):
        resource_type (str):
        response_payload (Any):
        response_printable_payload (Any):
        rule_id (str):
        severity (str):
        severity_score (float):
        signature_id (int):
        source_ip (str):
        source_port (int):
        status (Any):
        summary (str):
        tags (str):
        updated_at (int):
        url (str):
        tactics (Optional[List[str]]):
        techniques (Optional[List[str]]):
    """

    app_proto: str
    category: str
    container_name: str
    count: int
    created_at: int
    description: str
    destination_ip: str
    destination_port: int
    direction: str
    encrypted: str
    event_type: str
    geoip: str
    headers: str
    host_name: str
    http_content_type: Any
    http_type: str
    http_user_agent: str
    internal: str
    ip_reputation: str
    kubernetes_cluster_name: str
    length: Any
    local_port: int
    masked: bool
    matched: str
    node_id: str
    node_type: str
    pod_name: str
    protocol: int
    request_method: str
    request_path: str
    request_payload: str
    request_printable_payload: str
    resource_type: str
    response_payload: Any
    response_printable_payload: Any
    rule_id: str
    severity: str
    severity_score: float
    signature_id: int
    source_ip: str
    source_port: int
    status: Any
    summary: str
    tags: str
    updated_at: int
    url: str
    tactics: Optional[List[str]]
    techniques: Optional[List[str]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        app_proto = self.app_proto
        category = self.category
        container_name = self.container_name
        count = self.count
        created_at = self.created_at
        description = self.description
        destination_ip = self.destination_ip
        destination_port = self.destination_port
        direction = self.direction
        encrypted = self.encrypted
        event_type = self.event_type
        geoip = self.geoip
        headers = self.headers
        host_name = self.host_name
        http_content_type = self.http_content_type
        http_type = self.http_type
        http_user_agent = self.http_user_agent
        internal = self.internal
        ip_reputation = self.ip_reputation
        kubernetes_cluster_name = self.kubernetes_cluster_name
        length = self.length
        local_port = self.local_port
        masked = self.masked
        matched = self.matched
        node_id = self.node_id
        node_type = self.node_type
        pod_name = self.pod_name
        protocol = self.protocol
        request_method = self.request_method
        request_path = self.request_path
        request_payload = self.request_payload
        request_printable_payload = self.request_printable_payload
        resource_type = self.resource_type
        response_payload = self.response_payload
        response_printable_payload = self.response_printable_payload
        rule_id = self.rule_id
        severity = self.severity
        severity_score = self.severity_score
        signature_id = self.signature_id
        source_ip = self.source_ip
        source_port = self.source_port
        status = self.status
        summary = self.summary
        tags = self.tags
        updated_at = self.updated_at
        url = self.url
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
                "app_proto": app_proto,
                "category": category,
                "container_name": container_name,
                "count": count,
                "created_at": created_at,
                "description": description,
                "destination_ip": destination_ip,
                "destination_port": destination_port,
                "direction": direction,
                "encrypted": encrypted,
                "event_type": event_type,
                "geoip": geoip,
                "headers": headers,
                "host_name": host_name,
                "http_content_type": http_content_type,
                "http_type": http_type,
                "http_user_agent": http_user_agent,
                "internal": internal,
                "ip_reputation": ip_reputation,
                "kubernetes_cluster_name": kubernetes_cluster_name,
                "length": length,
                "local_port": local_port,
                "masked": masked,
                "matched": matched,
                "node_id": node_id,
                "node_type": node_type,
                "pod_name": pod_name,
                "protocol": protocol,
                "request_method": request_method,
                "request_path": request_path,
                "request_payload": request_payload,
                "request_printable_payload": request_printable_payload,
                "resource_type": resource_type,
                "response_payload": response_payload,
                "response_printable_payload": response_printable_payload,
                "rule_id": rule_id,
                "severity": severity,
                "severity_score": severity_score,
                "signature_id": signature_id,
                "source_ip": source_ip,
                "source_port": source_port,
                "status": status,
                "summary": summary,
                "tags": tags,
                "updated_at": updated_at,
                "url": url,
                "tactics": tactics,
                "techniques": techniques,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        app_proto = d.pop("app_proto")

        category = d.pop("category")

        container_name = d.pop("container_name")

        count = d.pop("count")

        created_at = d.pop("created_at")

        description = d.pop("description")

        destination_ip = d.pop("destination_ip")

        destination_port = d.pop("destination_port")

        direction = d.pop("direction")

        encrypted = d.pop("encrypted")

        event_type = d.pop("event_type")

        geoip = d.pop("geoip")

        headers = d.pop("headers")

        host_name = d.pop("host_name")

        http_content_type = d.pop("http_content_type")

        http_type = d.pop("http_type")

        http_user_agent = d.pop("http_user_agent")

        internal = d.pop("internal")

        ip_reputation = d.pop("ip_reputation")

        kubernetes_cluster_name = d.pop("kubernetes_cluster_name")

        length = d.pop("length")

        local_port = d.pop("local_port")

        masked = d.pop("masked")

        matched = d.pop("matched")

        node_id = d.pop("node_id")

        node_type = d.pop("node_type")

        pod_name = d.pop("pod_name")

        protocol = d.pop("protocol")

        request_method = d.pop("request_method")

        request_path = d.pop("request_path")

        request_payload = d.pop("request_payload")

        request_printable_payload = d.pop("request_printable_payload")

        resource_type = d.pop("resource_type")

        response_payload = d.pop("response_payload")

        response_printable_payload = d.pop("response_printable_payload")

        rule_id = d.pop("rule_id")

        severity = d.pop("severity")

        severity_score = d.pop("severity_score")

        signature_id = d.pop("signature_id")

        source_ip = d.pop("source_ip")

        source_port = d.pop("source_port")

        status = d.pop("status")

        summary = d.pop("summary")

        tags = d.pop("tags")

        updated_at = d.pop("updated_at")

        url = d.pop("url")

        tactics = cast(List[str], d.pop("tactics"))

        techniques = cast(List[str], d.pop("techniques"))

        model_network_alert = cls(
            app_proto=app_proto,
            category=category,
            container_name=container_name,
            count=count,
            created_at=created_at,
            description=description,
            destination_ip=destination_ip,
            destination_port=destination_port,
            direction=direction,
            encrypted=encrypted,
            event_type=event_type,
            geoip=geoip,
            headers=headers,
            host_name=host_name,
            http_content_type=http_content_type,
            http_type=http_type,
            http_user_agent=http_user_agent,
            internal=internal,
            ip_reputation=ip_reputation,
            kubernetes_cluster_name=kubernetes_cluster_name,
            length=length,
            local_port=local_port,
            masked=masked,
            matched=matched,
            node_id=node_id,
            node_type=node_type,
            pod_name=pod_name,
            protocol=protocol,
            request_method=request_method,
            request_path=request_path,
            request_payload=request_payload,
            request_printable_payload=request_printable_payload,
            resource_type=resource_type,
            response_payload=response_payload,
            response_printable_payload=response_printable_payload,
            rule_id=rule_id,
            severity=severity,
            severity_score=severity_score,
            signature_id=signature_id,
            source_ip=source_ip,
            source_port=source_port,
            status=status,
            summary=summary,
            tags=tags,
            updated_at=updated_at,
            url=url,
            tactics=tactics,
            techniques=techniques,
        )

        model_network_alert.additional_properties = d
        return model_network_alert

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
