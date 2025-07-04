from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SearchNodeCountResp")


@_attrs_define
class SearchNodeCountResp:
    """
    Attributes:
        cloud_provider (int):
        container (int):
        container_image (int):
        host (int):
        kubernetes_cluster (int):
        namespace (int):
        pod (int):
    """

    cloud_provider: int
    container: int
    container_image: int
    host: int
    kubernetes_cluster: int
    namespace: int
    pod: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cloud_provider = self.cloud_provider

        container = self.container

        container_image = self.container_image

        host = self.host

        kubernetes_cluster = self.kubernetes_cluster

        namespace = self.namespace

        pod = self.pod

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cloud_provider": cloud_provider,
                "container": container,
                "container_image": container_image,
                "host": host,
                "kubernetes_cluster": kubernetes_cluster,
                "namespace": namespace,
                "pod": pod,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cloud_provider = d.pop("cloud_provider")

        container = d.pop("container")

        container_image = d.pop("container_image")

        host = d.pop("host")

        kubernetes_cluster = d.pop("kubernetes_cluster")

        namespace = d.pop("namespace")

        pod = d.pop("pod")

        search_node_count_resp = cls(
            cloud_provider=cloud_provider,
            container=container,
            container_image=container_image,
            host=host,
            kubernetes_cluster=kubernetes_cluster,
            namespace=namespace,
            pod=pod,
        )

        search_node_count_resp.additional_properties = d
        return search_node_count_resp

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
