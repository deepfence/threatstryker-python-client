from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_host import ModelHost


T = TypeVar("T", bound="ModelKubernetesCluster")


@_attrs_define
class ModelKubernetesCluster:
    """
    Attributes:
        agent_running (bool):
        hosts (Union[None, list['ModelHost']]):
        node_id (str):
        node_name (str):
        tags (Union[None, list[str]]):
    """

    agent_running: bool
    hosts: Union[None, list["ModelHost"]]
    node_id: str
    node_name: str
    tags: Union[None, list[str]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_running = self.agent_running

        hosts: Union[None, list[dict[str, Any]]]
        if isinstance(self.hosts, list):
            hosts = []
            for hosts_type_0_item_data in self.hosts:
                hosts_type_0_item = hosts_type_0_item_data.to_dict()
                hosts.append(hosts_type_0_item)

        else:
            hosts = self.hosts

        node_id = self.node_id

        node_name = self.node_name

        tags: Union[None, list[str]]
        if isinstance(self.tags, list):
            tags = self.tags

        else:
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_running": agent_running,
                "hosts": hosts,
                "node_id": node_id,
                "node_name": node_name,
                "tags": tags,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_host import ModelHost

        d = dict(src_dict)
        agent_running = d.pop("agent_running")

        def _parse_hosts(data: object) -> Union[None, list["ModelHost"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                hosts_type_0 = []
                _hosts_type_0 = data
                for hosts_type_0_item_data in _hosts_type_0:
                    hosts_type_0_item = ModelHost.from_dict(hosts_type_0_item_data)

                    hosts_type_0.append(hosts_type_0_item)

                return hosts_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["ModelHost"]], data)

        hosts = _parse_hosts(d.pop("hosts"))

        node_id = d.pop("node_id")

        node_name = d.pop("node_name")

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

        model_kubernetes_cluster = cls(
            agent_running=agent_running,
            hosts=hosts,
            node_id=node_id,
            node_name=node_name,
            tags=tags,
        )

        model_kubernetes_cluster.additional_properties = d
        return model_kubernetes_cluster

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
