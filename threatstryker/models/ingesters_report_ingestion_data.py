from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ingesters_report_ingestion_data_api_endpoints_batch_type_0_item import (
        IngestersReportIngestionDataApiEndpointsBatchType0Item,
    )
    from ..models.ingesters_report_ingestion_data_api_endpoints_edge_batch_type_0_item import (
        IngestersReportIngestionDataApiEndpointsEdgeBatchType0Item,
    )
    from ..models.ingesters_report_ingestion_data_container_batch_type_0_item import (
        IngestersReportIngestionDataContainerBatchType0Item,
    )
    from ..models.ingesters_report_ingestion_data_container_edges_batch_type_0_item import (
        IngestersReportIngestionDataContainerEdgesBatchType0Item,
    )
    from ..models.ingesters_report_ingestion_data_container_image_batch_type_0_item import (
        IngestersReportIngestionDataContainerImageBatchType0Item,
    )
    from ..models.ingesters_report_ingestion_data_container_image_edge_batch_type_0_item import (
        IngestersReportIngestionDataContainerImageEdgeBatchType0Item,
    )
    from ..models.ingesters_report_ingestion_data_container_process_edge_batch_type_0_item import (
        IngestersReportIngestionDataContainerProcessEdgeBatchType0Item,
    )
    from ..models.ingesters_report_ingestion_data_endpoint_edges_batch_type_0_item import (
        IngestersReportIngestionDataEndpointEdgesBatchType0Item,
    )
    from ..models.ingesters_report_ingestion_data_host_batch_type_0_item import (
        IngestersReportIngestionDataHostBatchType0Item,
    )
    from ..models.ingesters_report_ingestion_data_hosts_type_0_item import IngestersReportIngestionDataHostsType0Item
    from ..models.ingesters_report_ingestion_data_kubernetes_cluster_batch_type_0_item import (
        IngestersReportIngestionDataKubernetesClusterBatchType0Item,
    )
    from ..models.ingesters_report_ingestion_data_kubernetes_cluster_edge_batch_type_0_item import (
        IngestersReportIngestionDataKubernetesClusterEdgeBatchType0Item,
    )
    from ..models.ingesters_report_ingestion_data_pod_batch_type_0_item import (
        IngestersReportIngestionDataPodBatchType0Item,
    )
    from ..models.ingesters_report_ingestion_data_pod_edges_batch_type_0_item import (
        IngestersReportIngestionDataPodEdgesBatchType0Item,
    )
    from ..models.ingesters_report_ingestion_data_pod_host_edges_batch_type_0_item import (
        IngestersReportIngestionDataPodHostEdgesBatchType0Item,
    )
    from ..models.ingesters_report_ingestion_data_process_batch_type_0_item import (
        IngestersReportIngestionDataProcessBatchType0Item,
    )
    from ..models.ingesters_report_ingestion_data_process_edges_batch_type_0_item import (
        IngestersReportIngestionDataProcessEdgesBatchType0Item,
    )


T = TypeVar("T", bound="IngestersReportIngestionData")


@_attrs_define
class IngestersReportIngestionData:
    """
    Attributes:
        api_endpoints_batch (Union[None, list['IngestersReportIngestionDataApiEndpointsBatchType0Item']]):
        api_endpoints_edge_batch (Union[None, list['IngestersReportIngestionDataApiEndpointsEdgeBatchType0Item']]):
        container_batch (Union[None, list['IngestersReportIngestionDataContainerBatchType0Item']]):
        container_edges_batch (Union[None, list['IngestersReportIngestionDataContainerEdgesBatchType0Item']]):
        container_image_batch (Union[None, list['IngestersReportIngestionDataContainerImageBatchType0Item']]):
        container_image_edge_batch (Union[None, list['IngestersReportIngestionDataContainerImageEdgeBatchType0Item']]):
        container_process_edge_batch (Union[None,
            list['IngestersReportIngestionDataContainerProcessEdgeBatchType0Item']]):
        endpoint_edges_batch (Union[None, list['IngestersReportIngestionDataEndpointEdgesBatchType0Item']]):
        host_batch (Union[None, list['IngestersReportIngestionDataHostBatchType0Item']]):
        hosts (Union[None, list['IngestersReportIngestionDataHostsType0Item']]):
        kubernetes_cluster_batch (Union[None, list['IngestersReportIngestionDataKubernetesClusterBatchType0Item']]):
        kubernetes_cluster_edge_batch (Union[None,
            list['IngestersReportIngestionDataKubernetesClusterEdgeBatchType0Item']]):
        num_merged (int):
        pod_batch (Union[None, list['IngestersReportIngestionDataPodBatchType0Item']]):
        pod_edges_batch (Union[None, list['IngestersReportIngestionDataPodEdgesBatchType0Item']]):
        pod_host_edges_batch (Union[None, list['IngestersReportIngestionDataPodHostEdgesBatchType0Item']]):
        process_batch (Union[None, list['IngestersReportIngestionDataProcessBatchType0Item']]):
        process_edges_batch (Union[None, list['IngestersReportIngestionDataProcessEdgesBatchType0Item']]):
    """

    api_endpoints_batch: Union[None, list["IngestersReportIngestionDataApiEndpointsBatchType0Item"]]
    api_endpoints_edge_batch: Union[None, list["IngestersReportIngestionDataApiEndpointsEdgeBatchType0Item"]]
    container_batch: Union[None, list["IngestersReportIngestionDataContainerBatchType0Item"]]
    container_edges_batch: Union[None, list["IngestersReportIngestionDataContainerEdgesBatchType0Item"]]
    container_image_batch: Union[None, list["IngestersReportIngestionDataContainerImageBatchType0Item"]]
    container_image_edge_batch: Union[None, list["IngestersReportIngestionDataContainerImageEdgeBatchType0Item"]]
    container_process_edge_batch: Union[None, list["IngestersReportIngestionDataContainerProcessEdgeBatchType0Item"]]
    endpoint_edges_batch: Union[None, list["IngestersReportIngestionDataEndpointEdgesBatchType0Item"]]
    host_batch: Union[None, list["IngestersReportIngestionDataHostBatchType0Item"]]
    hosts: Union[None, list["IngestersReportIngestionDataHostsType0Item"]]
    kubernetes_cluster_batch: Union[None, list["IngestersReportIngestionDataKubernetesClusterBatchType0Item"]]
    kubernetes_cluster_edge_batch: Union[None, list["IngestersReportIngestionDataKubernetesClusterEdgeBatchType0Item"]]
    num_merged: int
    pod_batch: Union[None, list["IngestersReportIngestionDataPodBatchType0Item"]]
    pod_edges_batch: Union[None, list["IngestersReportIngestionDataPodEdgesBatchType0Item"]]
    pod_host_edges_batch: Union[None, list["IngestersReportIngestionDataPodHostEdgesBatchType0Item"]]
    process_batch: Union[None, list["IngestersReportIngestionDataProcessBatchType0Item"]]
    process_edges_batch: Union[None, list["IngestersReportIngestionDataProcessEdgesBatchType0Item"]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_endpoints_batch: Union[None, list[dict[str, Any]]]
        if isinstance(self.api_endpoints_batch, list):
            api_endpoints_batch = []
            for api_endpoints_batch_type_0_item_data in self.api_endpoints_batch:
                api_endpoints_batch_type_0_item = api_endpoints_batch_type_0_item_data.to_dict()
                api_endpoints_batch.append(api_endpoints_batch_type_0_item)

        else:
            api_endpoints_batch = self.api_endpoints_batch

        api_endpoints_edge_batch: Union[None, list[dict[str, Any]]]
        if isinstance(self.api_endpoints_edge_batch, list):
            api_endpoints_edge_batch = []
            for api_endpoints_edge_batch_type_0_item_data in self.api_endpoints_edge_batch:
                api_endpoints_edge_batch_type_0_item = api_endpoints_edge_batch_type_0_item_data.to_dict()
                api_endpoints_edge_batch.append(api_endpoints_edge_batch_type_0_item)

        else:
            api_endpoints_edge_batch = self.api_endpoints_edge_batch

        container_batch: Union[None, list[dict[str, Any]]]
        if isinstance(self.container_batch, list):
            container_batch = []
            for container_batch_type_0_item_data in self.container_batch:
                container_batch_type_0_item = container_batch_type_0_item_data.to_dict()
                container_batch.append(container_batch_type_0_item)

        else:
            container_batch = self.container_batch

        container_edges_batch: Union[None, list[dict[str, Any]]]
        if isinstance(self.container_edges_batch, list):
            container_edges_batch = []
            for container_edges_batch_type_0_item_data in self.container_edges_batch:
                container_edges_batch_type_0_item = container_edges_batch_type_0_item_data.to_dict()
                container_edges_batch.append(container_edges_batch_type_0_item)

        else:
            container_edges_batch = self.container_edges_batch

        container_image_batch: Union[None, list[dict[str, Any]]]
        if isinstance(self.container_image_batch, list):
            container_image_batch = []
            for container_image_batch_type_0_item_data in self.container_image_batch:
                container_image_batch_type_0_item = container_image_batch_type_0_item_data.to_dict()
                container_image_batch.append(container_image_batch_type_0_item)

        else:
            container_image_batch = self.container_image_batch

        container_image_edge_batch: Union[None, list[dict[str, Any]]]
        if isinstance(self.container_image_edge_batch, list):
            container_image_edge_batch = []
            for container_image_edge_batch_type_0_item_data in self.container_image_edge_batch:
                container_image_edge_batch_type_0_item = container_image_edge_batch_type_0_item_data.to_dict()
                container_image_edge_batch.append(container_image_edge_batch_type_0_item)

        else:
            container_image_edge_batch = self.container_image_edge_batch

        container_process_edge_batch: Union[None, list[dict[str, Any]]]
        if isinstance(self.container_process_edge_batch, list):
            container_process_edge_batch = []
            for container_process_edge_batch_type_0_item_data in self.container_process_edge_batch:
                container_process_edge_batch_type_0_item = container_process_edge_batch_type_0_item_data.to_dict()
                container_process_edge_batch.append(container_process_edge_batch_type_0_item)

        else:
            container_process_edge_batch = self.container_process_edge_batch

        endpoint_edges_batch: Union[None, list[dict[str, Any]]]
        if isinstance(self.endpoint_edges_batch, list):
            endpoint_edges_batch = []
            for endpoint_edges_batch_type_0_item_data in self.endpoint_edges_batch:
                endpoint_edges_batch_type_0_item = endpoint_edges_batch_type_0_item_data.to_dict()
                endpoint_edges_batch.append(endpoint_edges_batch_type_0_item)

        else:
            endpoint_edges_batch = self.endpoint_edges_batch

        host_batch: Union[None, list[dict[str, Any]]]
        if isinstance(self.host_batch, list):
            host_batch = []
            for host_batch_type_0_item_data in self.host_batch:
                host_batch_type_0_item = host_batch_type_0_item_data.to_dict()
                host_batch.append(host_batch_type_0_item)

        else:
            host_batch = self.host_batch

        hosts: Union[None, list[dict[str, Any]]]
        if isinstance(self.hosts, list):
            hosts = []
            for hosts_type_0_item_data in self.hosts:
                hosts_type_0_item = hosts_type_0_item_data.to_dict()
                hosts.append(hosts_type_0_item)

        else:
            hosts = self.hosts

        kubernetes_cluster_batch: Union[None, list[dict[str, Any]]]
        if isinstance(self.kubernetes_cluster_batch, list):
            kubernetes_cluster_batch = []
            for kubernetes_cluster_batch_type_0_item_data in self.kubernetes_cluster_batch:
                kubernetes_cluster_batch_type_0_item = kubernetes_cluster_batch_type_0_item_data.to_dict()
                kubernetes_cluster_batch.append(kubernetes_cluster_batch_type_0_item)

        else:
            kubernetes_cluster_batch = self.kubernetes_cluster_batch

        kubernetes_cluster_edge_batch: Union[None, list[dict[str, Any]]]
        if isinstance(self.kubernetes_cluster_edge_batch, list):
            kubernetes_cluster_edge_batch = []
            for kubernetes_cluster_edge_batch_type_0_item_data in self.kubernetes_cluster_edge_batch:
                kubernetes_cluster_edge_batch_type_0_item = kubernetes_cluster_edge_batch_type_0_item_data.to_dict()
                kubernetes_cluster_edge_batch.append(kubernetes_cluster_edge_batch_type_0_item)

        else:
            kubernetes_cluster_edge_batch = self.kubernetes_cluster_edge_batch

        num_merged = self.num_merged

        pod_batch: Union[None, list[dict[str, Any]]]
        if isinstance(self.pod_batch, list):
            pod_batch = []
            for pod_batch_type_0_item_data in self.pod_batch:
                pod_batch_type_0_item = pod_batch_type_0_item_data.to_dict()
                pod_batch.append(pod_batch_type_0_item)

        else:
            pod_batch = self.pod_batch

        pod_edges_batch: Union[None, list[dict[str, Any]]]
        if isinstance(self.pod_edges_batch, list):
            pod_edges_batch = []
            for pod_edges_batch_type_0_item_data in self.pod_edges_batch:
                pod_edges_batch_type_0_item = pod_edges_batch_type_0_item_data.to_dict()
                pod_edges_batch.append(pod_edges_batch_type_0_item)

        else:
            pod_edges_batch = self.pod_edges_batch

        pod_host_edges_batch: Union[None, list[dict[str, Any]]]
        if isinstance(self.pod_host_edges_batch, list):
            pod_host_edges_batch = []
            for pod_host_edges_batch_type_0_item_data in self.pod_host_edges_batch:
                pod_host_edges_batch_type_0_item = pod_host_edges_batch_type_0_item_data.to_dict()
                pod_host_edges_batch.append(pod_host_edges_batch_type_0_item)

        else:
            pod_host_edges_batch = self.pod_host_edges_batch

        process_batch: Union[None, list[dict[str, Any]]]
        if isinstance(self.process_batch, list):
            process_batch = []
            for process_batch_type_0_item_data in self.process_batch:
                process_batch_type_0_item = process_batch_type_0_item_data.to_dict()
                process_batch.append(process_batch_type_0_item)

        else:
            process_batch = self.process_batch

        process_edges_batch: Union[None, list[dict[str, Any]]]
        if isinstance(self.process_edges_batch, list):
            process_edges_batch = []
            for process_edges_batch_type_0_item_data in self.process_edges_batch:
                process_edges_batch_type_0_item = process_edges_batch_type_0_item_data.to_dict()
                process_edges_batch.append(process_edges_batch_type_0_item)

        else:
            process_edges_batch = self.process_edges_batch

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "api_endpoints_batch": api_endpoints_batch,
                "api_endpoints_edge_batch": api_endpoints_edge_batch,
                "container_batch": container_batch,
                "container_edges_batch": container_edges_batch,
                "container_image_batch": container_image_batch,
                "container_image_edge_batch": container_image_edge_batch,
                "container_process_edge_batch": container_process_edge_batch,
                "endpoint_edges_batch": endpoint_edges_batch,
                "host_batch": host_batch,
                "hosts": hosts,
                "kubernetes_cluster_batch": kubernetes_cluster_batch,
                "kubernetes_cluster_edge_batch": kubernetes_cluster_edge_batch,
                "num_merged": num_merged,
                "pod_batch": pod_batch,
                "pod_edges_batch": pod_edges_batch,
                "pod_host_edges_batch": pod_host_edges_batch,
                "process_batch": process_batch,
                "process_edges_batch": process_edges_batch,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ingesters_report_ingestion_data_api_endpoints_batch_type_0_item import (
            IngestersReportIngestionDataApiEndpointsBatchType0Item,
        )
        from ..models.ingesters_report_ingestion_data_api_endpoints_edge_batch_type_0_item import (
            IngestersReportIngestionDataApiEndpointsEdgeBatchType0Item,
        )
        from ..models.ingesters_report_ingestion_data_container_batch_type_0_item import (
            IngestersReportIngestionDataContainerBatchType0Item,
        )
        from ..models.ingesters_report_ingestion_data_container_edges_batch_type_0_item import (
            IngestersReportIngestionDataContainerEdgesBatchType0Item,
        )
        from ..models.ingesters_report_ingestion_data_container_image_batch_type_0_item import (
            IngestersReportIngestionDataContainerImageBatchType0Item,
        )
        from ..models.ingesters_report_ingestion_data_container_image_edge_batch_type_0_item import (
            IngestersReportIngestionDataContainerImageEdgeBatchType0Item,
        )
        from ..models.ingesters_report_ingestion_data_container_process_edge_batch_type_0_item import (
            IngestersReportIngestionDataContainerProcessEdgeBatchType0Item,
        )
        from ..models.ingesters_report_ingestion_data_endpoint_edges_batch_type_0_item import (
            IngestersReportIngestionDataEndpointEdgesBatchType0Item,
        )
        from ..models.ingesters_report_ingestion_data_host_batch_type_0_item import (
            IngestersReportIngestionDataHostBatchType0Item,
        )
        from ..models.ingesters_report_ingestion_data_hosts_type_0_item import (
            IngestersReportIngestionDataHostsType0Item,
        )
        from ..models.ingesters_report_ingestion_data_kubernetes_cluster_batch_type_0_item import (
            IngestersReportIngestionDataKubernetesClusterBatchType0Item,
        )
        from ..models.ingesters_report_ingestion_data_kubernetes_cluster_edge_batch_type_0_item import (
            IngestersReportIngestionDataKubernetesClusterEdgeBatchType0Item,
        )
        from ..models.ingesters_report_ingestion_data_pod_batch_type_0_item import (
            IngestersReportIngestionDataPodBatchType0Item,
        )
        from ..models.ingesters_report_ingestion_data_pod_edges_batch_type_0_item import (
            IngestersReportIngestionDataPodEdgesBatchType0Item,
        )
        from ..models.ingesters_report_ingestion_data_pod_host_edges_batch_type_0_item import (
            IngestersReportIngestionDataPodHostEdgesBatchType0Item,
        )
        from ..models.ingesters_report_ingestion_data_process_batch_type_0_item import (
            IngestersReportIngestionDataProcessBatchType0Item,
        )
        from ..models.ingesters_report_ingestion_data_process_edges_batch_type_0_item import (
            IngestersReportIngestionDataProcessEdgesBatchType0Item,
        )

        d = dict(src_dict)

        def _parse_api_endpoints_batch(
            data: object,
        ) -> Union[None, list["IngestersReportIngestionDataApiEndpointsBatchType0Item"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                api_endpoints_batch_type_0 = []
                _api_endpoints_batch_type_0 = data
                for api_endpoints_batch_type_0_item_data in _api_endpoints_batch_type_0:
                    api_endpoints_batch_type_0_item = IngestersReportIngestionDataApiEndpointsBatchType0Item.from_dict(
                        api_endpoints_batch_type_0_item_data
                    )

                    api_endpoints_batch_type_0.append(api_endpoints_batch_type_0_item)

                return api_endpoints_batch_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["IngestersReportIngestionDataApiEndpointsBatchType0Item"]], data)

        api_endpoints_batch = _parse_api_endpoints_batch(d.pop("api_endpoints_batch"))

        def _parse_api_endpoints_edge_batch(
            data: object,
        ) -> Union[None, list["IngestersReportIngestionDataApiEndpointsEdgeBatchType0Item"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                api_endpoints_edge_batch_type_0 = []
                _api_endpoints_edge_batch_type_0 = data
                for api_endpoints_edge_batch_type_0_item_data in _api_endpoints_edge_batch_type_0:
                    api_endpoints_edge_batch_type_0_item = (
                        IngestersReportIngestionDataApiEndpointsEdgeBatchType0Item.from_dict(
                            api_endpoints_edge_batch_type_0_item_data
                        )
                    )

                    api_endpoints_edge_batch_type_0.append(api_endpoints_edge_batch_type_0_item)

                return api_endpoints_edge_batch_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["IngestersReportIngestionDataApiEndpointsEdgeBatchType0Item"]], data)

        api_endpoints_edge_batch = _parse_api_endpoints_edge_batch(d.pop("api_endpoints_edge_batch"))

        def _parse_container_batch(
            data: object,
        ) -> Union[None, list["IngestersReportIngestionDataContainerBatchType0Item"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                container_batch_type_0 = []
                _container_batch_type_0 = data
                for container_batch_type_0_item_data in _container_batch_type_0:
                    container_batch_type_0_item = IngestersReportIngestionDataContainerBatchType0Item.from_dict(
                        container_batch_type_0_item_data
                    )

                    container_batch_type_0.append(container_batch_type_0_item)

                return container_batch_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["IngestersReportIngestionDataContainerBatchType0Item"]], data)

        container_batch = _parse_container_batch(d.pop("container_batch"))

        def _parse_container_edges_batch(
            data: object,
        ) -> Union[None, list["IngestersReportIngestionDataContainerEdgesBatchType0Item"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                container_edges_batch_type_0 = []
                _container_edges_batch_type_0 = data
                for container_edges_batch_type_0_item_data in _container_edges_batch_type_0:
                    container_edges_batch_type_0_item = (
                        IngestersReportIngestionDataContainerEdgesBatchType0Item.from_dict(
                            container_edges_batch_type_0_item_data
                        )
                    )

                    container_edges_batch_type_0.append(container_edges_batch_type_0_item)

                return container_edges_batch_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["IngestersReportIngestionDataContainerEdgesBatchType0Item"]], data)

        container_edges_batch = _parse_container_edges_batch(d.pop("container_edges_batch"))

        def _parse_container_image_batch(
            data: object,
        ) -> Union[None, list["IngestersReportIngestionDataContainerImageBatchType0Item"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                container_image_batch_type_0 = []
                _container_image_batch_type_0 = data
                for container_image_batch_type_0_item_data in _container_image_batch_type_0:
                    container_image_batch_type_0_item = (
                        IngestersReportIngestionDataContainerImageBatchType0Item.from_dict(
                            container_image_batch_type_0_item_data
                        )
                    )

                    container_image_batch_type_0.append(container_image_batch_type_0_item)

                return container_image_batch_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["IngestersReportIngestionDataContainerImageBatchType0Item"]], data)

        container_image_batch = _parse_container_image_batch(d.pop("container_image_batch"))

        def _parse_container_image_edge_batch(
            data: object,
        ) -> Union[None, list["IngestersReportIngestionDataContainerImageEdgeBatchType0Item"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                container_image_edge_batch_type_0 = []
                _container_image_edge_batch_type_0 = data
                for container_image_edge_batch_type_0_item_data in _container_image_edge_batch_type_0:
                    container_image_edge_batch_type_0_item = (
                        IngestersReportIngestionDataContainerImageEdgeBatchType0Item.from_dict(
                            container_image_edge_batch_type_0_item_data
                        )
                    )

                    container_image_edge_batch_type_0.append(container_image_edge_batch_type_0_item)

                return container_image_edge_batch_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["IngestersReportIngestionDataContainerImageEdgeBatchType0Item"]], data)

        container_image_edge_batch = _parse_container_image_edge_batch(d.pop("container_image_edge_batch"))

        def _parse_container_process_edge_batch(
            data: object,
        ) -> Union[None, list["IngestersReportIngestionDataContainerProcessEdgeBatchType0Item"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                container_process_edge_batch_type_0 = []
                _container_process_edge_batch_type_0 = data
                for container_process_edge_batch_type_0_item_data in _container_process_edge_batch_type_0:
                    container_process_edge_batch_type_0_item = (
                        IngestersReportIngestionDataContainerProcessEdgeBatchType0Item.from_dict(
                            container_process_edge_batch_type_0_item_data
                        )
                    )

                    container_process_edge_batch_type_0.append(container_process_edge_batch_type_0_item)

                return container_process_edge_batch_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["IngestersReportIngestionDataContainerProcessEdgeBatchType0Item"]], data)

        container_process_edge_batch = _parse_container_process_edge_batch(d.pop("container_process_edge_batch"))

        def _parse_endpoint_edges_batch(
            data: object,
        ) -> Union[None, list["IngestersReportIngestionDataEndpointEdgesBatchType0Item"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                endpoint_edges_batch_type_0 = []
                _endpoint_edges_batch_type_0 = data
                for endpoint_edges_batch_type_0_item_data in _endpoint_edges_batch_type_0:
                    endpoint_edges_batch_type_0_item = (
                        IngestersReportIngestionDataEndpointEdgesBatchType0Item.from_dict(
                            endpoint_edges_batch_type_0_item_data
                        )
                    )

                    endpoint_edges_batch_type_0.append(endpoint_edges_batch_type_0_item)

                return endpoint_edges_batch_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["IngestersReportIngestionDataEndpointEdgesBatchType0Item"]], data)

        endpoint_edges_batch = _parse_endpoint_edges_batch(d.pop("endpoint_edges_batch"))

        def _parse_host_batch(data: object) -> Union[None, list["IngestersReportIngestionDataHostBatchType0Item"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                host_batch_type_0 = []
                _host_batch_type_0 = data
                for host_batch_type_0_item_data in _host_batch_type_0:
                    host_batch_type_0_item = IngestersReportIngestionDataHostBatchType0Item.from_dict(
                        host_batch_type_0_item_data
                    )

                    host_batch_type_0.append(host_batch_type_0_item)

                return host_batch_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["IngestersReportIngestionDataHostBatchType0Item"]], data)

        host_batch = _parse_host_batch(d.pop("host_batch"))

        def _parse_hosts(data: object) -> Union[None, list["IngestersReportIngestionDataHostsType0Item"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                hosts_type_0 = []
                _hosts_type_0 = data
                for hosts_type_0_item_data in _hosts_type_0:
                    hosts_type_0_item = IngestersReportIngestionDataHostsType0Item.from_dict(hosts_type_0_item_data)

                    hosts_type_0.append(hosts_type_0_item)

                return hosts_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["IngestersReportIngestionDataHostsType0Item"]], data)

        hosts = _parse_hosts(d.pop("hosts"))

        def _parse_kubernetes_cluster_batch(
            data: object,
        ) -> Union[None, list["IngestersReportIngestionDataKubernetesClusterBatchType0Item"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                kubernetes_cluster_batch_type_0 = []
                _kubernetes_cluster_batch_type_0 = data
                for kubernetes_cluster_batch_type_0_item_data in _kubernetes_cluster_batch_type_0:
                    kubernetes_cluster_batch_type_0_item = (
                        IngestersReportIngestionDataKubernetesClusterBatchType0Item.from_dict(
                            kubernetes_cluster_batch_type_0_item_data
                        )
                    )

                    kubernetes_cluster_batch_type_0.append(kubernetes_cluster_batch_type_0_item)

                return kubernetes_cluster_batch_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["IngestersReportIngestionDataKubernetesClusterBatchType0Item"]], data)

        kubernetes_cluster_batch = _parse_kubernetes_cluster_batch(d.pop("kubernetes_cluster_batch"))

        def _parse_kubernetes_cluster_edge_batch(
            data: object,
        ) -> Union[None, list["IngestersReportIngestionDataKubernetesClusterEdgeBatchType0Item"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                kubernetes_cluster_edge_batch_type_0 = []
                _kubernetes_cluster_edge_batch_type_0 = data
                for kubernetes_cluster_edge_batch_type_0_item_data in _kubernetes_cluster_edge_batch_type_0:
                    kubernetes_cluster_edge_batch_type_0_item = (
                        IngestersReportIngestionDataKubernetesClusterEdgeBatchType0Item.from_dict(
                            kubernetes_cluster_edge_batch_type_0_item_data
                        )
                    )

                    kubernetes_cluster_edge_batch_type_0.append(kubernetes_cluster_edge_batch_type_0_item)

                return kubernetes_cluster_edge_batch_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["IngestersReportIngestionDataKubernetesClusterEdgeBatchType0Item"]], data)

        kubernetes_cluster_edge_batch = _parse_kubernetes_cluster_edge_batch(d.pop("kubernetes_cluster_edge_batch"))

        num_merged = d.pop("num_merged")

        def _parse_pod_batch(data: object) -> Union[None, list["IngestersReportIngestionDataPodBatchType0Item"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                pod_batch_type_0 = []
                _pod_batch_type_0 = data
                for pod_batch_type_0_item_data in _pod_batch_type_0:
                    pod_batch_type_0_item = IngestersReportIngestionDataPodBatchType0Item.from_dict(
                        pod_batch_type_0_item_data
                    )

                    pod_batch_type_0.append(pod_batch_type_0_item)

                return pod_batch_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["IngestersReportIngestionDataPodBatchType0Item"]], data)

        pod_batch = _parse_pod_batch(d.pop("pod_batch"))

        def _parse_pod_edges_batch(
            data: object,
        ) -> Union[None, list["IngestersReportIngestionDataPodEdgesBatchType0Item"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                pod_edges_batch_type_0 = []
                _pod_edges_batch_type_0 = data
                for pod_edges_batch_type_0_item_data in _pod_edges_batch_type_0:
                    pod_edges_batch_type_0_item = IngestersReportIngestionDataPodEdgesBatchType0Item.from_dict(
                        pod_edges_batch_type_0_item_data
                    )

                    pod_edges_batch_type_0.append(pod_edges_batch_type_0_item)

                return pod_edges_batch_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["IngestersReportIngestionDataPodEdgesBatchType0Item"]], data)

        pod_edges_batch = _parse_pod_edges_batch(d.pop("pod_edges_batch"))

        def _parse_pod_host_edges_batch(
            data: object,
        ) -> Union[None, list["IngestersReportIngestionDataPodHostEdgesBatchType0Item"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                pod_host_edges_batch_type_0 = []
                _pod_host_edges_batch_type_0 = data
                for pod_host_edges_batch_type_0_item_data in _pod_host_edges_batch_type_0:
                    pod_host_edges_batch_type_0_item = IngestersReportIngestionDataPodHostEdgesBatchType0Item.from_dict(
                        pod_host_edges_batch_type_0_item_data
                    )

                    pod_host_edges_batch_type_0.append(pod_host_edges_batch_type_0_item)

                return pod_host_edges_batch_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["IngestersReportIngestionDataPodHostEdgesBatchType0Item"]], data)

        pod_host_edges_batch = _parse_pod_host_edges_batch(d.pop("pod_host_edges_batch"))

        def _parse_process_batch(
            data: object,
        ) -> Union[None, list["IngestersReportIngestionDataProcessBatchType0Item"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                process_batch_type_0 = []
                _process_batch_type_0 = data
                for process_batch_type_0_item_data in _process_batch_type_0:
                    process_batch_type_0_item = IngestersReportIngestionDataProcessBatchType0Item.from_dict(
                        process_batch_type_0_item_data
                    )

                    process_batch_type_0.append(process_batch_type_0_item)

                return process_batch_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["IngestersReportIngestionDataProcessBatchType0Item"]], data)

        process_batch = _parse_process_batch(d.pop("process_batch"))

        def _parse_process_edges_batch(
            data: object,
        ) -> Union[None, list["IngestersReportIngestionDataProcessEdgesBatchType0Item"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                process_edges_batch_type_0 = []
                _process_edges_batch_type_0 = data
                for process_edges_batch_type_0_item_data in _process_edges_batch_type_0:
                    process_edges_batch_type_0_item = IngestersReportIngestionDataProcessEdgesBatchType0Item.from_dict(
                        process_edges_batch_type_0_item_data
                    )

                    process_edges_batch_type_0.append(process_edges_batch_type_0_item)

                return process_edges_batch_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["IngestersReportIngestionDataProcessEdgesBatchType0Item"]], data)

        process_edges_batch = _parse_process_edges_batch(d.pop("process_edges_batch"))

        ingesters_report_ingestion_data = cls(
            api_endpoints_batch=api_endpoints_batch,
            api_endpoints_edge_batch=api_endpoints_edge_batch,
            container_batch=container_batch,
            container_edges_batch=container_edges_batch,
            container_image_batch=container_image_batch,
            container_image_edge_batch=container_image_edge_batch,
            container_process_edge_batch=container_process_edge_batch,
            endpoint_edges_batch=endpoint_edges_batch,
            host_batch=host_batch,
            hosts=hosts,
            kubernetes_cluster_batch=kubernetes_cluster_batch,
            kubernetes_cluster_edge_batch=kubernetes_cluster_edge_batch,
            num_merged=num_merged,
            pod_batch=pod_batch,
            pod_edges_batch=pod_edges_batch,
            pod_host_edges_batch=pod_host_edges_batch,
            process_batch=process_batch,
            process_edges_batch=process_edges_batch,
        )

        ingesters_report_ingestion_data.additional_properties = d
        return ingesters_report_ingestion_data

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
