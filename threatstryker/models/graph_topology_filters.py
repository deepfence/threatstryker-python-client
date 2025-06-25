from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.reporters_fields_filters import ReportersFieldsFilters


T = TypeVar("T", bound="GraphTopologyFilters")


@_attrs_define
class GraphTopologyFilters:
    """
    Attributes:
        cloud_filter (Union[None, list[str]]):
        container_filter (Union[None, list[str]]):
        field_filters (ReportersFieldsFilters):
        host_filter (Union[None, list[str]]):
        kubernetes_filter (Union[None, list[str]]):
        pod_filter (Union[None, list[str]]):
        region_filter (Union[None, list[str]]):
        skip_connections (bool):
    """

    cloud_filter: Union[None, list[str]]
    container_filter: Union[None, list[str]]
    field_filters: "ReportersFieldsFilters"
    host_filter: Union[None, list[str]]
    kubernetes_filter: Union[None, list[str]]
    pod_filter: Union[None, list[str]]
    region_filter: Union[None, list[str]]
    skip_connections: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cloud_filter: Union[None, list[str]]
        if isinstance(self.cloud_filter, list):
            cloud_filter = self.cloud_filter

        else:
            cloud_filter = self.cloud_filter

        container_filter: Union[None, list[str]]
        if isinstance(self.container_filter, list):
            container_filter = self.container_filter

        else:
            container_filter = self.container_filter

        field_filters = self.field_filters.to_dict()

        host_filter: Union[None, list[str]]
        if isinstance(self.host_filter, list):
            host_filter = self.host_filter

        else:
            host_filter = self.host_filter

        kubernetes_filter: Union[None, list[str]]
        if isinstance(self.kubernetes_filter, list):
            kubernetes_filter = self.kubernetes_filter

        else:
            kubernetes_filter = self.kubernetes_filter

        pod_filter: Union[None, list[str]]
        if isinstance(self.pod_filter, list):
            pod_filter = self.pod_filter

        else:
            pod_filter = self.pod_filter

        region_filter: Union[None, list[str]]
        if isinstance(self.region_filter, list):
            region_filter = self.region_filter

        else:
            region_filter = self.region_filter

        skip_connections = self.skip_connections

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cloud_filter": cloud_filter,
                "container_filter": container_filter,
                "field_filters": field_filters,
                "host_filter": host_filter,
                "kubernetes_filter": kubernetes_filter,
                "pod_filter": pod_filter,
                "region_filter": region_filter,
                "skip_connections": skip_connections,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reporters_fields_filters import ReportersFieldsFilters

        d = dict(src_dict)

        def _parse_cloud_filter(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cloud_filter_type_0 = cast(list[str], data)

                return cloud_filter_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        cloud_filter = _parse_cloud_filter(d.pop("cloud_filter"))

        def _parse_container_filter(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                container_filter_type_0 = cast(list[str], data)

                return container_filter_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        container_filter = _parse_container_filter(d.pop("container_filter"))

        field_filters = ReportersFieldsFilters.from_dict(d.pop("field_filters"))

        def _parse_host_filter(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                host_filter_type_0 = cast(list[str], data)

                return host_filter_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        host_filter = _parse_host_filter(d.pop("host_filter"))

        def _parse_kubernetes_filter(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                kubernetes_filter_type_0 = cast(list[str], data)

                return kubernetes_filter_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        kubernetes_filter = _parse_kubernetes_filter(d.pop("kubernetes_filter"))

        def _parse_pod_filter(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                pod_filter_type_0 = cast(list[str], data)

                return pod_filter_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        pod_filter = _parse_pod_filter(d.pop("pod_filter"))

        def _parse_region_filter(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                region_filter_type_0 = cast(list[str], data)

                return region_filter_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        region_filter = _parse_region_filter(d.pop("region_filter"))

        skip_connections = d.pop("skip_connections")

        graph_topology_filters = cls(
            cloud_filter=cloud_filter,
            container_filter=container_filter,
            field_filters=field_filters,
            host_filter=host_filter,
            kubernetes_filter=kubernetes_filter,
            pod_filter=pod_filter,
            region_filter=region_filter,
            skip_connections=skip_connections,
        )

        graph_topology_filters.additional_properties = d
        return graph_topology_filters

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
