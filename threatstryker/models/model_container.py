from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_container_docker_labels_type_0 import ModelContainerDockerLabelsType0
    from ..models.model_container_image import ModelContainerImage
    from ..models.model_process import ModelProcess


T = TypeVar("T", bound="ModelContainer")


@_attrs_define
class ModelContainer:
    """
    Attributes:
        cpu_max (float):
        cpu_usage (float):
        docker_container_command (str):
        docker_container_created (str):
        docker_container_ips (Union[None, list[Any]]):
        docker_container_name (str):
        docker_container_network_mode (str):
        docker_container_networks (str):
        docker_container_ports (str):
        docker_container_state (str):
        docker_container_state_human (str):
        docker_image_name_with_tag (str):
        docker_labels (Union['ModelContainerDockerLabelsType0', None]):
        host_name (str):
        image (ModelContainerImage):
        is_deepfence_system (bool):
        kubernetes_cluster_id (str):
        kubernetes_cluster_name (str):
        kubernetes_namespace (str):
        malware_latest_scan_id (str):
        malware_scan_status (str):
        malwares_count (int):
        memory_max (int):
        memory_usage (int):
        node_id (str):
        node_name (str):
        processes (Union[None, list['ModelProcess']]):
        secret_latest_scan_id (str):
        secret_scan_status (str):
        secrets_count (int):
        tags (Union[None, list[str]]):
        uptime (int):
        vulnerabilities_count (int):
        vulnerability_latest_scan_id (str):
        vulnerability_scan_status (str):
    """

    cpu_max: float
    cpu_usage: float
    docker_container_command: str
    docker_container_created: str
    docker_container_ips: Union[None, list[Any]]
    docker_container_name: str
    docker_container_network_mode: str
    docker_container_networks: str
    docker_container_ports: str
    docker_container_state: str
    docker_container_state_human: str
    docker_image_name_with_tag: str
    docker_labels: Union["ModelContainerDockerLabelsType0", None]
    host_name: str
    image: "ModelContainerImage"
    is_deepfence_system: bool
    kubernetes_cluster_id: str
    kubernetes_cluster_name: str
    kubernetes_namespace: str
    malware_latest_scan_id: str
    malware_scan_status: str
    malwares_count: int
    memory_max: int
    memory_usage: int
    node_id: str
    node_name: str
    processes: Union[None, list["ModelProcess"]]
    secret_latest_scan_id: str
    secret_scan_status: str
    secrets_count: int
    tags: Union[None, list[str]]
    uptime: int
    vulnerabilities_count: int
    vulnerability_latest_scan_id: str
    vulnerability_scan_status: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.model_container_docker_labels_type_0 import ModelContainerDockerLabelsType0

        cpu_max = self.cpu_max

        cpu_usage = self.cpu_usage

        docker_container_command = self.docker_container_command

        docker_container_created = self.docker_container_created

        docker_container_ips: Union[None, list[Any]]
        if isinstance(self.docker_container_ips, list):
            docker_container_ips = self.docker_container_ips

        else:
            docker_container_ips = self.docker_container_ips

        docker_container_name = self.docker_container_name

        docker_container_network_mode = self.docker_container_network_mode

        docker_container_networks = self.docker_container_networks

        docker_container_ports = self.docker_container_ports

        docker_container_state = self.docker_container_state

        docker_container_state_human = self.docker_container_state_human

        docker_image_name_with_tag = self.docker_image_name_with_tag

        docker_labels: Union[None, dict[str, Any]]
        if isinstance(self.docker_labels, ModelContainerDockerLabelsType0):
            docker_labels = self.docker_labels.to_dict()
        else:
            docker_labels = self.docker_labels

        host_name = self.host_name

        image = self.image.to_dict()

        is_deepfence_system = self.is_deepfence_system

        kubernetes_cluster_id = self.kubernetes_cluster_id

        kubernetes_cluster_name = self.kubernetes_cluster_name

        kubernetes_namespace = self.kubernetes_namespace

        malware_latest_scan_id = self.malware_latest_scan_id

        malware_scan_status = self.malware_scan_status

        malwares_count = self.malwares_count

        memory_max = self.memory_max

        memory_usage = self.memory_usage

        node_id = self.node_id

        node_name = self.node_name

        processes: Union[None, list[dict[str, Any]]]
        if isinstance(self.processes, list):
            processes = []
            for processes_type_0_item_data in self.processes:
                processes_type_0_item = processes_type_0_item_data.to_dict()
                processes.append(processes_type_0_item)

        else:
            processes = self.processes

        secret_latest_scan_id = self.secret_latest_scan_id

        secret_scan_status = self.secret_scan_status

        secrets_count = self.secrets_count

        tags: Union[None, list[str]]
        if isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        uptime = self.uptime

        vulnerabilities_count = self.vulnerabilities_count

        vulnerability_latest_scan_id = self.vulnerability_latest_scan_id

        vulnerability_scan_status = self.vulnerability_scan_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cpu_max": cpu_max,
                "cpu_usage": cpu_usage,
                "docker_container_command": docker_container_command,
                "docker_container_created": docker_container_created,
                "docker_container_ips": docker_container_ips,
                "docker_container_name": docker_container_name,
                "docker_container_network_mode": docker_container_network_mode,
                "docker_container_networks": docker_container_networks,
                "docker_container_ports": docker_container_ports,
                "docker_container_state": docker_container_state,
                "docker_container_state_human": docker_container_state_human,
                "docker_image_name_with_tag": docker_image_name_with_tag,
                "docker_labels": docker_labels,
                "host_name": host_name,
                "image": image,
                "is_deepfence_system": is_deepfence_system,
                "kubernetes_cluster_id": kubernetes_cluster_id,
                "kubernetes_cluster_name": kubernetes_cluster_name,
                "kubernetes_namespace": kubernetes_namespace,
                "malware_latest_scan_id": malware_latest_scan_id,
                "malware_scan_status": malware_scan_status,
                "malwares_count": malwares_count,
                "memory_max": memory_max,
                "memory_usage": memory_usage,
                "node_id": node_id,
                "node_name": node_name,
                "processes": processes,
                "secret_latest_scan_id": secret_latest_scan_id,
                "secret_scan_status": secret_scan_status,
                "secrets_count": secrets_count,
                "tags": tags,
                "uptime": uptime,
                "vulnerabilities_count": vulnerabilities_count,
                "vulnerability_latest_scan_id": vulnerability_latest_scan_id,
                "vulnerability_scan_status": vulnerability_scan_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_container_docker_labels_type_0 import ModelContainerDockerLabelsType0
        from ..models.model_container_image import ModelContainerImage
        from ..models.model_process import ModelProcess

        d = dict(src_dict)
        cpu_max = d.pop("cpu_max")

        cpu_usage = d.pop("cpu_usage")

        docker_container_command = d.pop("docker_container_command")

        docker_container_created = d.pop("docker_container_created")

        def _parse_docker_container_ips(data: object) -> Union[None, list[Any]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                docker_container_ips_type_0 = cast(list[Any], data)

                return docker_container_ips_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[Any]], data)

        docker_container_ips = _parse_docker_container_ips(d.pop("docker_container_ips"))

        docker_container_name = d.pop("docker_container_name")

        docker_container_network_mode = d.pop("docker_container_network_mode")

        docker_container_networks = d.pop("docker_container_networks")

        docker_container_ports = d.pop("docker_container_ports")

        docker_container_state = d.pop("docker_container_state")

        docker_container_state_human = d.pop("docker_container_state_human")

        docker_image_name_with_tag = d.pop("docker_image_name_with_tag")

        def _parse_docker_labels(data: object) -> Union["ModelContainerDockerLabelsType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                docker_labels_type_0 = ModelContainerDockerLabelsType0.from_dict(data)

                return docker_labels_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ModelContainerDockerLabelsType0", None], data)

        docker_labels = _parse_docker_labels(d.pop("docker_labels"))

        host_name = d.pop("host_name")

        image = ModelContainerImage.from_dict(d.pop("image"))

        is_deepfence_system = d.pop("is_deepfence_system")

        kubernetes_cluster_id = d.pop("kubernetes_cluster_id")

        kubernetes_cluster_name = d.pop("kubernetes_cluster_name")

        kubernetes_namespace = d.pop("kubernetes_namespace")

        malware_latest_scan_id = d.pop("malware_latest_scan_id")

        malware_scan_status = d.pop("malware_scan_status")

        malwares_count = d.pop("malwares_count")

        memory_max = d.pop("memory_max")

        memory_usage = d.pop("memory_usage")

        node_id = d.pop("node_id")

        node_name = d.pop("node_name")

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

        vulnerabilities_count = d.pop("vulnerabilities_count")

        vulnerability_latest_scan_id = d.pop("vulnerability_latest_scan_id")

        vulnerability_scan_status = d.pop("vulnerability_scan_status")

        model_container = cls(
            cpu_max=cpu_max,
            cpu_usage=cpu_usage,
            docker_container_command=docker_container_command,
            docker_container_created=docker_container_created,
            docker_container_ips=docker_container_ips,
            docker_container_name=docker_container_name,
            docker_container_network_mode=docker_container_network_mode,
            docker_container_networks=docker_container_networks,
            docker_container_ports=docker_container_ports,
            docker_container_state=docker_container_state,
            docker_container_state_human=docker_container_state_human,
            docker_image_name_with_tag=docker_image_name_with_tag,
            docker_labels=docker_labels,
            host_name=host_name,
            image=image,
            is_deepfence_system=is_deepfence_system,
            kubernetes_cluster_id=kubernetes_cluster_id,
            kubernetes_cluster_name=kubernetes_cluster_name,
            kubernetes_namespace=kubernetes_namespace,
            malware_latest_scan_id=malware_latest_scan_id,
            malware_scan_status=malware_scan_status,
            malwares_count=malwares_count,
            memory_max=memory_max,
            memory_usage=memory_usage,
            node_id=node_id,
            node_name=node_name,
            processes=processes,
            secret_latest_scan_id=secret_latest_scan_id,
            secret_scan_status=secret_scan_status,
            secrets_count=secrets_count,
            tags=tags,
            uptime=uptime,
            vulnerabilities_count=vulnerabilities_count,
            vulnerability_latest_scan_id=vulnerability_latest_scan_id,
            vulnerability_scan_status=vulnerability_scan_status,
        )

        model_container.additional_properties = d
        return model_container

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
