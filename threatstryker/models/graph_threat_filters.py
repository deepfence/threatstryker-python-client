from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.graph_threat_filters_type import GraphThreatFiltersType

if TYPE_CHECKING:
    from ..models.graph_cloud_provider_filter import GraphCloudProviderFilter


T = TypeVar("T", bound="GraphThreatFilters")


@_attrs_define
class GraphThreatFilters:
    """
    Attributes:
        aws_filter (GraphCloudProviderFilter):
        azure_filter (GraphCloudProviderFilter):
        cloud_resource_only (bool):
        gcp_filter (GraphCloudProviderFilter):
        type_ (GraphThreatFiltersType):
    """

    aws_filter: "GraphCloudProviderFilter"
    azure_filter: "GraphCloudProviderFilter"
    cloud_resource_only: bool
    gcp_filter: "GraphCloudProviderFilter"
    type_: GraphThreatFiltersType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aws_filter = self.aws_filter.to_dict()

        azure_filter = self.azure_filter.to_dict()

        cloud_resource_only = self.cloud_resource_only

        gcp_filter = self.gcp_filter.to_dict()

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aws_filter": aws_filter,
                "azure_filter": azure_filter,
                "cloud_resource_only": cloud_resource_only,
                "gcp_filter": gcp_filter,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.graph_cloud_provider_filter import GraphCloudProviderFilter

        d = dict(src_dict)
        aws_filter = GraphCloudProviderFilter.from_dict(d.pop("aws_filter"))

        azure_filter = GraphCloudProviderFilter.from_dict(d.pop("azure_filter"))

        cloud_resource_only = d.pop("cloud_resource_only")

        gcp_filter = GraphCloudProviderFilter.from_dict(d.pop("gcp_filter"))

        type_ = GraphThreatFiltersType(d.pop("type"))

        graph_threat_filters = cls(
            aws_filter=aws_filter,
            azure_filter=azure_filter,
            cloud_resource_only=cloud_resource_only,
            gcp_filter=gcp_filter,
            type_=type_,
        )

        graph_threat_filters.additional_properties = d
        return graph_threat_filters

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
