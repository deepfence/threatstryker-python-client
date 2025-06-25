from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UtilsAdvancedReportFilters")


@_attrs_define
class UtilsAdvancedReportFilters:
    """
    Attributes:
        container_name (Union[Unset, list[str]]):
        host_name (Union[Unset, list[str]]):
        image_name (Union[Unset, list[str]]):
        kubernetes_cluster_name (Union[Unset, list[str]]):
        masked (Union[Unset, list[bool]]):
        most_exploitable_scores (Union[Unset, list[int]]):
        node_id (Union[Unset, list[str]]):
        pod_name (Union[Unset, list[str]]):
        scan_status (Union[Unset, list[str]]):
    """

    container_name: Union[Unset, list[str]] = UNSET
    host_name: Union[Unset, list[str]] = UNSET
    image_name: Union[Unset, list[str]] = UNSET
    kubernetes_cluster_name: Union[Unset, list[str]] = UNSET
    masked: Union[Unset, list[bool]] = UNSET
    most_exploitable_scores: Union[Unset, list[int]] = UNSET
    node_id: Union[Unset, list[str]] = UNSET
    pod_name: Union[Unset, list[str]] = UNSET
    scan_status: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        container_name: Union[Unset, list[str]] = UNSET
        if not isinstance(self.container_name, Unset):
            container_name = self.container_name

        host_name: Union[Unset, list[str]] = UNSET
        if not isinstance(self.host_name, Unset):
            host_name = self.host_name

        image_name: Union[Unset, list[str]] = UNSET
        if not isinstance(self.image_name, Unset):
            image_name = self.image_name

        kubernetes_cluster_name: Union[Unset, list[str]] = UNSET
        if not isinstance(self.kubernetes_cluster_name, Unset):
            kubernetes_cluster_name = self.kubernetes_cluster_name

        masked: Union[Unset, list[bool]] = UNSET
        if not isinstance(self.masked, Unset):
            masked = self.masked

        most_exploitable_scores: Union[Unset, list[int]] = UNSET
        if not isinstance(self.most_exploitable_scores, Unset):
            most_exploitable_scores = self.most_exploitable_scores

        node_id: Union[Unset, list[str]] = UNSET
        if not isinstance(self.node_id, Unset):
            node_id = self.node_id

        pod_name: Union[Unset, list[str]] = UNSET
        if not isinstance(self.pod_name, Unset):
            pod_name = self.pod_name

        scan_status: Union[Unset, list[str]] = UNSET
        if not isinstance(self.scan_status, Unset):
            scan_status = self.scan_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if container_name is not UNSET:
            field_dict["container_name"] = container_name
        if host_name is not UNSET:
            field_dict["host_name"] = host_name
        if image_name is not UNSET:
            field_dict["image_name"] = image_name
        if kubernetes_cluster_name is not UNSET:
            field_dict["kubernetes_cluster_name"] = kubernetes_cluster_name
        if masked is not UNSET:
            field_dict["masked"] = masked
        if most_exploitable_scores is not UNSET:
            field_dict["most_exploitable_scores"] = most_exploitable_scores
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if pod_name is not UNSET:
            field_dict["pod_name"] = pod_name
        if scan_status is not UNSET:
            field_dict["scan_status"] = scan_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        container_name = cast(list[str], d.pop("container_name", UNSET))

        host_name = cast(list[str], d.pop("host_name", UNSET))

        image_name = cast(list[str], d.pop("image_name", UNSET))

        kubernetes_cluster_name = cast(list[str], d.pop("kubernetes_cluster_name", UNSET))

        masked = cast(list[bool], d.pop("masked", UNSET))

        most_exploitable_scores = cast(list[int], d.pop("most_exploitable_scores", UNSET))

        node_id = cast(list[str], d.pop("node_id", UNSET))

        pod_name = cast(list[str], d.pop("pod_name", UNSET))

        scan_status = cast(list[str], d.pop("scan_status", UNSET))

        utils_advanced_report_filters = cls(
            container_name=container_name,
            host_name=host_name,
            image_name=image_name,
            kubernetes_cluster_name=kubernetes_cluster_name,
            masked=masked,
            most_exploitable_scores=most_exploitable_scores,
            node_id=node_id,
            pod_name=pod_name,
            scan_status=scan_status,
        )

        utils_advanced_report_filters.additional_properties = d
        return utils_advanced_report_filters

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
