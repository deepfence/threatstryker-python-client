from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_agent_plugin_config_names import ModelAgentPluginConfigNames
    from ..models.model_agent_plugins_status import ModelAgentPluginsStatus
    from ..models.model_api_endpoint import ModelAPIEndpoint
    from ..models.model_connection import ModelConnection
    from ..models.model_container import ModelContainer
    from ..models.model_container_image import ModelContainerImage
    from ..models.model_host_alerts_counts_type_0 import ModelHostAlertsCountsType0
    from ..models.model_pod import ModelPod
    from ..models.model_process import ModelProcess


T = TypeVar("T", bound="ModelHost")


@_attrs_define
class ModelHost:
    """
    Attributes:
        agent_installer_tracer_status (str):
        agent_installer_tracer_status_updated_at (int):
        agent_running (bool):
        alerts_counts (Union['ModelHostAlertsCountsType0', None]):
        api_endpoints (Union[None, list['ModelAPIEndpoint']]):
        availability_zone (str):
        cloud_account_id (str):
        cloud_compliance_latest_scan_id (str):
        cloud_compliance_scan_status (str):
        cloud_compliances_count (int):
        cloud_provider (str):
        cloud_region (str):
        cloud_warn_alarm_count (int):
        compliance_latest_scan_id (str):
        compliance_scan_status (str):
        compliances_count (int):
        config_names (ModelAgentPluginConfigNames):
        container_images (Union[None, list['ModelContainerImage']]):
        containers (Union[None, list['ModelContainer']]):
        cpu_max (float):
        cpu_usage (float):
        cr_id (str):
        exploitable_malwares_count (int):
        exploitable_secrets_count (int):
        exploitable_vulnerabilities_count (int):
        filesystem_tracer_status (str):
        filesystem_tracer_status_updated_at (int):
        host_name (str):
        inbound_connections (Union[None, list['ModelConnection']]):
        instance_id (str):
        instance_type (str):
        is_console_vm (bool):
        kernel_id (str):
        kernel_version (str):
        local_cidr (Union[None, list[Any]]):
        local_networks (Union[None, list[Any]]):
        malware_latest_scan_id (str):
        malware_scan_status (str):
        malwares_count (int):
        memory_max (int):
        memory_usage (int):
        network_filter_status (str):
        network_tracer_status (str):
        network_tracer_status_updated_at (int):
        node_id (str):
        node_name (str):
        os (str):
        outbound_connections (Union[None, list['ModelConnection']]):
        plugin_status (ModelAgentPluginsStatus):
        pods (Union[None, list['ModelPod']]):
        private_ip (Union[None, list[Any]]):
        process_tracer_status (str):
        process_tracer_status_updated_at (int):
        processes (Union[None, list['ModelProcess']]):
        public_ip (Union[None, list[Any]]):
        resource_group (str):
        secret_latest_scan_id (str):
        secret_scan_status (str):
        secrets_count (int):
        tags (Union[None, list[str]]):
        uptime (int):
        version (str):
        vulnerabilities_count (int):
        vulnerability_latest_scan_id (str):
        vulnerability_scan_status (str):
        warn_alarm_count (int):
        account_id (Union[Unset, str]):
    """

    agent_installer_tracer_status: str
    agent_installer_tracer_status_updated_at: int
    agent_running: bool
    alerts_counts: Union["ModelHostAlertsCountsType0", None]
    api_endpoints: Union[None, list["ModelAPIEndpoint"]]
    availability_zone: str
    cloud_account_id: str
    cloud_compliance_latest_scan_id: str
    cloud_compliance_scan_status: str
    cloud_compliances_count: int
    cloud_provider: str
    cloud_region: str
    cloud_warn_alarm_count: int
    compliance_latest_scan_id: str
    compliance_scan_status: str
    compliances_count: int
    config_names: "ModelAgentPluginConfigNames"
    container_images: Union[None, list["ModelContainerImage"]]
    containers: Union[None, list["ModelContainer"]]
    cpu_max: float
    cpu_usage: float
    cr_id: str
    exploitable_malwares_count: int
    exploitable_secrets_count: int
    exploitable_vulnerabilities_count: int
    filesystem_tracer_status: str
    filesystem_tracer_status_updated_at: int
    host_name: str
    inbound_connections: Union[None, list["ModelConnection"]]
    instance_id: str
    instance_type: str
    is_console_vm: bool
    kernel_id: str
    kernel_version: str
    local_cidr: Union[None, list[Any]]
    local_networks: Union[None, list[Any]]
    malware_latest_scan_id: str
    malware_scan_status: str
    malwares_count: int
    memory_max: int
    memory_usage: int
    network_filter_status: str
    network_tracer_status: str
    network_tracer_status_updated_at: int
    node_id: str
    node_name: str
    os: str
    outbound_connections: Union[None, list["ModelConnection"]]
    plugin_status: "ModelAgentPluginsStatus"
    pods: Union[None, list["ModelPod"]]
    private_ip: Union[None, list[Any]]
    process_tracer_status: str
    process_tracer_status_updated_at: int
    processes: Union[None, list["ModelProcess"]]
    public_ip: Union[None, list[Any]]
    resource_group: str
    secret_latest_scan_id: str
    secret_scan_status: str
    secrets_count: int
    tags: Union[None, list[str]]
    uptime: int
    version: str
    vulnerabilities_count: int
    vulnerability_latest_scan_id: str
    vulnerability_scan_status: str
    warn_alarm_count: int
    account_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.model_host_alerts_counts_type_0 import ModelHostAlertsCountsType0

        agent_installer_tracer_status = self.agent_installer_tracer_status

        agent_installer_tracer_status_updated_at = self.agent_installer_tracer_status_updated_at

        agent_running = self.agent_running

        alerts_counts: Union[None, dict[str, Any]]
        if isinstance(self.alerts_counts, ModelHostAlertsCountsType0):
            alerts_counts = self.alerts_counts.to_dict()
        else:
            alerts_counts = self.alerts_counts

        api_endpoints: Union[None, list[dict[str, Any]]]
        if isinstance(self.api_endpoints, list):
            api_endpoints = []
            for api_endpoints_type_0_item_data in self.api_endpoints:
                api_endpoints_type_0_item = api_endpoints_type_0_item_data.to_dict()
                api_endpoints.append(api_endpoints_type_0_item)

        else:
            api_endpoints = self.api_endpoints

        availability_zone = self.availability_zone

        cloud_account_id = self.cloud_account_id

        cloud_compliance_latest_scan_id = self.cloud_compliance_latest_scan_id

        cloud_compliance_scan_status = self.cloud_compliance_scan_status

        cloud_compliances_count = self.cloud_compliances_count

        cloud_provider = self.cloud_provider

        cloud_region = self.cloud_region

        cloud_warn_alarm_count = self.cloud_warn_alarm_count

        compliance_latest_scan_id = self.compliance_latest_scan_id

        compliance_scan_status = self.compliance_scan_status

        compliances_count = self.compliances_count

        config_names = self.config_names.to_dict()

        container_images: Union[None, list[dict[str, Any]]]
        if isinstance(self.container_images, list):
            container_images = []
            for container_images_type_0_item_data in self.container_images:
                container_images_type_0_item = container_images_type_0_item_data.to_dict()
                container_images.append(container_images_type_0_item)

        else:
            container_images = self.container_images

        containers: Union[None, list[dict[str, Any]]]
        if isinstance(self.containers, list):
            containers = []
            for containers_type_0_item_data in self.containers:
                containers_type_0_item = containers_type_0_item_data.to_dict()
                containers.append(containers_type_0_item)

        else:
            containers = self.containers

        cpu_max = self.cpu_max

        cpu_usage = self.cpu_usage

        cr_id = self.cr_id

        exploitable_malwares_count = self.exploitable_malwares_count

        exploitable_secrets_count = self.exploitable_secrets_count

        exploitable_vulnerabilities_count = self.exploitable_vulnerabilities_count

        filesystem_tracer_status = self.filesystem_tracer_status

        filesystem_tracer_status_updated_at = self.filesystem_tracer_status_updated_at

        host_name = self.host_name

        inbound_connections: Union[None, list[dict[str, Any]]]
        if isinstance(self.inbound_connections, list):
            inbound_connections = []
            for inbound_connections_type_0_item_data in self.inbound_connections:
                inbound_connections_type_0_item = inbound_connections_type_0_item_data.to_dict()
                inbound_connections.append(inbound_connections_type_0_item)

        else:
            inbound_connections = self.inbound_connections

        instance_id = self.instance_id

        instance_type = self.instance_type

        is_console_vm = self.is_console_vm

        kernel_id = self.kernel_id

        kernel_version = self.kernel_version

        local_cidr: Union[None, list[Any]]
        if isinstance(self.local_cidr, list):
            local_cidr = self.local_cidr

        else:
            local_cidr = self.local_cidr

        local_networks: Union[None, list[Any]]
        if isinstance(self.local_networks, list):
            local_networks = self.local_networks

        else:
            local_networks = self.local_networks

        malware_latest_scan_id = self.malware_latest_scan_id

        malware_scan_status = self.malware_scan_status

        malwares_count = self.malwares_count

        memory_max = self.memory_max

        memory_usage = self.memory_usage

        network_filter_status = self.network_filter_status

        network_tracer_status = self.network_tracer_status

        network_tracer_status_updated_at = self.network_tracer_status_updated_at

        node_id = self.node_id

        node_name = self.node_name

        os = self.os

        outbound_connections: Union[None, list[dict[str, Any]]]
        if isinstance(self.outbound_connections, list):
            outbound_connections = []
            for outbound_connections_type_0_item_data in self.outbound_connections:
                outbound_connections_type_0_item = outbound_connections_type_0_item_data.to_dict()
                outbound_connections.append(outbound_connections_type_0_item)

        else:
            outbound_connections = self.outbound_connections

        plugin_status = self.plugin_status.to_dict()

        pods: Union[None, list[dict[str, Any]]]
        if isinstance(self.pods, list):
            pods = []
            for pods_type_0_item_data in self.pods:
                pods_type_0_item = pods_type_0_item_data.to_dict()
                pods.append(pods_type_0_item)

        else:
            pods = self.pods

        private_ip: Union[None, list[Any]]
        if isinstance(self.private_ip, list):
            private_ip = self.private_ip

        else:
            private_ip = self.private_ip

        process_tracer_status = self.process_tracer_status

        process_tracer_status_updated_at = self.process_tracer_status_updated_at

        processes: Union[None, list[dict[str, Any]]]
        if isinstance(self.processes, list):
            processes = []
            for processes_type_0_item_data in self.processes:
                processes_type_0_item = processes_type_0_item_data.to_dict()
                processes.append(processes_type_0_item)

        else:
            processes = self.processes

        public_ip: Union[None, list[Any]]
        if isinstance(self.public_ip, list):
            public_ip = self.public_ip

        else:
            public_ip = self.public_ip

        resource_group = self.resource_group

        secret_latest_scan_id = self.secret_latest_scan_id

        secret_scan_status = self.secret_scan_status

        secrets_count = self.secrets_count

        tags: Union[None, list[str]]
        if isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        uptime = self.uptime

        version = self.version

        vulnerabilities_count = self.vulnerabilities_count

        vulnerability_latest_scan_id = self.vulnerability_latest_scan_id

        vulnerability_scan_status = self.vulnerability_scan_status

        warn_alarm_count = self.warn_alarm_count

        account_id = self.account_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_installer_tracer_status": agent_installer_tracer_status,
                "agent_installer_tracer_status_updated_at": agent_installer_tracer_status_updated_at,
                "agent_running": agent_running,
                "alerts_counts": alerts_counts,
                "api_endpoints": api_endpoints,
                "availability_zone": availability_zone,
                "cloud_account_id": cloud_account_id,
                "cloud_compliance_latest_scan_id": cloud_compliance_latest_scan_id,
                "cloud_compliance_scan_status": cloud_compliance_scan_status,
                "cloud_compliances_count": cloud_compliances_count,
                "cloud_provider": cloud_provider,
                "cloud_region": cloud_region,
                "cloud_warn_alarm_count": cloud_warn_alarm_count,
                "compliance_latest_scan_id": compliance_latest_scan_id,
                "compliance_scan_status": compliance_scan_status,
                "compliances_count": compliances_count,
                "config_names": config_names,
                "container_images": container_images,
                "containers": containers,
                "cpu_max": cpu_max,
                "cpu_usage": cpu_usage,
                "cr_id": cr_id,
                "exploitable_malwares_count": exploitable_malwares_count,
                "exploitable_secrets_count": exploitable_secrets_count,
                "exploitable_vulnerabilities_count": exploitable_vulnerabilities_count,
                "filesystem_tracer_status": filesystem_tracer_status,
                "filesystem_tracer_status_updated_at": filesystem_tracer_status_updated_at,
                "host_name": host_name,
                "inbound_connections": inbound_connections,
                "instance_id": instance_id,
                "instance_type": instance_type,
                "is_console_vm": is_console_vm,
                "kernel_id": kernel_id,
                "kernel_version": kernel_version,
                "local_cidr": local_cidr,
                "local_networks": local_networks,
                "malware_latest_scan_id": malware_latest_scan_id,
                "malware_scan_status": malware_scan_status,
                "malwares_count": malwares_count,
                "memory_max": memory_max,
                "memory_usage": memory_usage,
                "network_filter_status": network_filter_status,
                "network_tracer_status": network_tracer_status,
                "network_tracer_status_updated_at": network_tracer_status_updated_at,
                "node_id": node_id,
                "node_name": node_name,
                "os": os,
                "outbound_connections": outbound_connections,
                "plugin_status": plugin_status,
                "pods": pods,
                "private_ip": private_ip,
                "process_tracer_status": process_tracer_status,
                "process_tracer_status_updated_at": process_tracer_status_updated_at,
                "processes": processes,
                "public_ip": public_ip,
                "resource_group": resource_group,
                "secret_latest_scan_id": secret_latest_scan_id,
                "secret_scan_status": secret_scan_status,
                "secrets_count": secrets_count,
                "tags": tags,
                "uptime": uptime,
                "version": version,
                "vulnerabilities_count": vulnerabilities_count,
                "vulnerability_latest_scan_id": vulnerability_latest_scan_id,
                "vulnerability_scan_status": vulnerability_scan_status,
                "warn_alarm_count": warn_alarm_count,
            }
        )
        if account_id is not UNSET:
            field_dict["account_id"] = account_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_agent_plugin_config_names import ModelAgentPluginConfigNames
        from ..models.model_agent_plugins_status import ModelAgentPluginsStatus
        from ..models.model_api_endpoint import ModelAPIEndpoint
        from ..models.model_connection import ModelConnection
        from ..models.model_container import ModelContainer
        from ..models.model_container_image import ModelContainerImage
        from ..models.model_host_alerts_counts_type_0 import ModelHostAlertsCountsType0
        from ..models.model_pod import ModelPod
        from ..models.model_process import ModelProcess

        d = dict(src_dict)
        agent_installer_tracer_status = d.pop("agent_installer_tracer_status")

        agent_installer_tracer_status_updated_at = d.pop("agent_installer_tracer_status_updated_at")

        agent_running = d.pop("agent_running")

        def _parse_alerts_counts(data: object) -> Union["ModelHostAlertsCountsType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                alerts_counts_type_0 = ModelHostAlertsCountsType0.from_dict(data)

                return alerts_counts_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ModelHostAlertsCountsType0", None], data)

        alerts_counts = _parse_alerts_counts(d.pop("alerts_counts"))

        def _parse_api_endpoints(data: object) -> Union[None, list["ModelAPIEndpoint"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                api_endpoints_type_0 = []
                _api_endpoints_type_0 = data
                for api_endpoints_type_0_item_data in _api_endpoints_type_0:
                    api_endpoints_type_0_item = ModelAPIEndpoint.from_dict(api_endpoints_type_0_item_data)

                    api_endpoints_type_0.append(api_endpoints_type_0_item)

                return api_endpoints_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["ModelAPIEndpoint"]], data)

        api_endpoints = _parse_api_endpoints(d.pop("api_endpoints"))

        availability_zone = d.pop("availability_zone")

        cloud_account_id = d.pop("cloud_account_id")

        cloud_compliance_latest_scan_id = d.pop("cloud_compliance_latest_scan_id")

        cloud_compliance_scan_status = d.pop("cloud_compliance_scan_status")

        cloud_compliances_count = d.pop("cloud_compliances_count")

        cloud_provider = d.pop("cloud_provider")

        cloud_region = d.pop("cloud_region")

        cloud_warn_alarm_count = d.pop("cloud_warn_alarm_count")

        compliance_latest_scan_id = d.pop("compliance_latest_scan_id")

        compliance_scan_status = d.pop("compliance_scan_status")

        compliances_count = d.pop("compliances_count")

        config_names = ModelAgentPluginConfigNames.from_dict(d.pop("config_names"))

        def _parse_container_images(data: object) -> Union[None, list["ModelContainerImage"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                container_images_type_0 = []
                _container_images_type_0 = data
                for container_images_type_0_item_data in _container_images_type_0:
                    container_images_type_0_item = ModelContainerImage.from_dict(container_images_type_0_item_data)

                    container_images_type_0.append(container_images_type_0_item)

                return container_images_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["ModelContainerImage"]], data)

        container_images = _parse_container_images(d.pop("container_images"))

        def _parse_containers(data: object) -> Union[None, list["ModelContainer"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                containers_type_0 = []
                _containers_type_0 = data
                for containers_type_0_item_data in _containers_type_0:
                    containers_type_0_item = ModelContainer.from_dict(containers_type_0_item_data)

                    containers_type_0.append(containers_type_0_item)

                return containers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["ModelContainer"]], data)

        containers = _parse_containers(d.pop("containers"))

        cpu_max = d.pop("cpu_max")

        cpu_usage = d.pop("cpu_usage")

        cr_id = d.pop("cr_id")

        exploitable_malwares_count = d.pop("exploitable_malwares_count")

        exploitable_secrets_count = d.pop("exploitable_secrets_count")

        exploitable_vulnerabilities_count = d.pop("exploitable_vulnerabilities_count")

        filesystem_tracer_status = d.pop("filesystem_tracer_status")

        filesystem_tracer_status_updated_at = d.pop("filesystem_tracer_status_updated_at")

        host_name = d.pop("host_name")

        def _parse_inbound_connections(data: object) -> Union[None, list["ModelConnection"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                inbound_connections_type_0 = []
                _inbound_connections_type_0 = data
                for inbound_connections_type_0_item_data in _inbound_connections_type_0:
                    inbound_connections_type_0_item = ModelConnection.from_dict(inbound_connections_type_0_item_data)

                    inbound_connections_type_0.append(inbound_connections_type_0_item)

                return inbound_connections_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["ModelConnection"]], data)

        inbound_connections = _parse_inbound_connections(d.pop("inbound_connections"))

        instance_id = d.pop("instance_id")

        instance_type = d.pop("instance_type")

        is_console_vm = d.pop("is_console_vm")

        kernel_id = d.pop("kernel_id")

        kernel_version = d.pop("kernel_version")

        def _parse_local_cidr(data: object) -> Union[None, list[Any]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                local_cidr_type_0 = cast(list[Any], data)

                return local_cidr_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[Any]], data)

        local_cidr = _parse_local_cidr(d.pop("local_cidr"))

        def _parse_local_networks(data: object) -> Union[None, list[Any]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                local_networks_type_0 = cast(list[Any], data)

                return local_networks_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[Any]], data)

        local_networks = _parse_local_networks(d.pop("local_networks"))

        malware_latest_scan_id = d.pop("malware_latest_scan_id")

        malware_scan_status = d.pop("malware_scan_status")

        malwares_count = d.pop("malwares_count")

        memory_max = d.pop("memory_max")

        memory_usage = d.pop("memory_usage")

        network_filter_status = d.pop("network_filter_status")

        network_tracer_status = d.pop("network_tracer_status")

        network_tracer_status_updated_at = d.pop("network_tracer_status_updated_at")

        node_id = d.pop("node_id")

        node_name = d.pop("node_name")

        os = d.pop("os")

        def _parse_outbound_connections(data: object) -> Union[None, list["ModelConnection"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                outbound_connections_type_0 = []
                _outbound_connections_type_0 = data
                for outbound_connections_type_0_item_data in _outbound_connections_type_0:
                    outbound_connections_type_0_item = ModelConnection.from_dict(outbound_connections_type_0_item_data)

                    outbound_connections_type_0.append(outbound_connections_type_0_item)

                return outbound_connections_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["ModelConnection"]], data)

        outbound_connections = _parse_outbound_connections(d.pop("outbound_connections"))

        plugin_status = ModelAgentPluginsStatus.from_dict(d.pop("plugin_status"))

        def _parse_pods(data: object) -> Union[None, list["ModelPod"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                pods_type_0 = []
                _pods_type_0 = data
                for pods_type_0_item_data in _pods_type_0:
                    pods_type_0_item = ModelPod.from_dict(pods_type_0_item_data)

                    pods_type_0.append(pods_type_0_item)

                return pods_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["ModelPod"]], data)

        pods = _parse_pods(d.pop("pods"))

        def _parse_private_ip(data: object) -> Union[None, list[Any]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                private_ip_type_0 = cast(list[Any], data)

                return private_ip_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[Any]], data)

        private_ip = _parse_private_ip(d.pop("private_ip"))

        process_tracer_status = d.pop("process_tracer_status")

        process_tracer_status_updated_at = d.pop("process_tracer_status_updated_at")

        def _parse_processes(data: object) -> Union[None, list["ModelProcess"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                processes_type_0 = []
                _processes_type_0 = data
                for processes_type_0_item_data in _processes_type_0:
                    processes_type_0_item = ModelProcess.from_dict(processes_type_0_item_data)

                    processes_type_0.append(processes_type_0_item)

                return processes_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["ModelProcess"]], data)

        processes = _parse_processes(d.pop("processes"))

        def _parse_public_ip(data: object) -> Union[None, list[Any]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                public_ip_type_0 = cast(list[Any], data)

                return public_ip_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[Any]], data)

        public_ip = _parse_public_ip(d.pop("public_ip"))

        resource_group = d.pop("resource_group")

        secret_latest_scan_id = d.pop("secret_latest_scan_id")

        secret_scan_status = d.pop("secret_scan_status")

        secrets_count = d.pop("secrets_count")

        def _parse_tags(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tags_type_0 = cast(list[str], data)

                return tags_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        tags = _parse_tags(d.pop("tags"))

        uptime = d.pop("uptime")

        version = d.pop("version")

        vulnerabilities_count = d.pop("vulnerabilities_count")

        vulnerability_latest_scan_id = d.pop("vulnerability_latest_scan_id")

        vulnerability_scan_status = d.pop("vulnerability_scan_status")

        warn_alarm_count = d.pop("warn_alarm_count")

        account_id = d.pop("account_id", UNSET)

        model_host = cls(
            agent_installer_tracer_status=agent_installer_tracer_status,
            agent_installer_tracer_status_updated_at=agent_installer_tracer_status_updated_at,
            agent_running=agent_running,
            alerts_counts=alerts_counts,
            api_endpoints=api_endpoints,
            availability_zone=availability_zone,
            cloud_account_id=cloud_account_id,
            cloud_compliance_latest_scan_id=cloud_compliance_latest_scan_id,
            cloud_compliance_scan_status=cloud_compliance_scan_status,
            cloud_compliances_count=cloud_compliances_count,
            cloud_provider=cloud_provider,
            cloud_region=cloud_region,
            cloud_warn_alarm_count=cloud_warn_alarm_count,
            compliance_latest_scan_id=compliance_latest_scan_id,
            compliance_scan_status=compliance_scan_status,
            compliances_count=compliances_count,
            config_names=config_names,
            container_images=container_images,
            containers=containers,
            cpu_max=cpu_max,
            cpu_usage=cpu_usage,
            cr_id=cr_id,
            exploitable_malwares_count=exploitable_malwares_count,
            exploitable_secrets_count=exploitable_secrets_count,
            exploitable_vulnerabilities_count=exploitable_vulnerabilities_count,
            filesystem_tracer_status=filesystem_tracer_status,
            filesystem_tracer_status_updated_at=filesystem_tracer_status_updated_at,
            host_name=host_name,
            inbound_connections=inbound_connections,
            instance_id=instance_id,
            instance_type=instance_type,
            is_console_vm=is_console_vm,
            kernel_id=kernel_id,
            kernel_version=kernel_version,
            local_cidr=local_cidr,
            local_networks=local_networks,
            malware_latest_scan_id=malware_latest_scan_id,
            malware_scan_status=malware_scan_status,
            malwares_count=malwares_count,
            memory_max=memory_max,
            memory_usage=memory_usage,
            network_filter_status=network_filter_status,
            network_tracer_status=network_tracer_status,
            network_tracer_status_updated_at=network_tracer_status_updated_at,
            node_id=node_id,
            node_name=node_name,
            os=os,
            outbound_connections=outbound_connections,
            plugin_status=plugin_status,
            pods=pods,
            private_ip=private_ip,
            process_tracer_status=process_tracer_status,
            process_tracer_status_updated_at=process_tracer_status_updated_at,
            processes=processes,
            public_ip=public_ip,
            resource_group=resource_group,
            secret_latest_scan_id=secret_latest_scan_id,
            secret_scan_status=secret_scan_status,
            secrets_count=secrets_count,
            tags=tags,
            uptime=uptime,
            version=version,
            vulnerabilities_count=vulnerabilities_count,
            vulnerability_latest_scan_id=vulnerability_latest_scan_id,
            vulnerability_scan_status=vulnerability_scan_status,
            warn_alarm_count=warn_alarm_count,
            account_id=account_id,
        )

        model_host.additional_properties = d
        return model_host

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
