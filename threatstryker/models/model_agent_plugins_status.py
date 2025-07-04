from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_plugin_status import ModelPluginStatus


T = TypeVar("T", bound="ModelAgentPluginsStatus")


@_attrs_define
class ModelAgentPluginsStatus:
    """
    Attributes:
        agent_installer_tracer_status (ModelPluginStatus):
        cloud_network_tracer_status (ModelPluginStatus):
        filesystem_tracer_status (ModelPluginStatus):
        network_filter_status (ModelPluginStatus):
        network_tracer_status (ModelPluginStatus):
        process_tracer_status (ModelPluginStatus):
    """

    agent_installer_tracer_status: "ModelPluginStatus"
    cloud_network_tracer_status: "ModelPluginStatus"
    filesystem_tracer_status: "ModelPluginStatus"
    network_filter_status: "ModelPluginStatus"
    network_tracer_status: "ModelPluginStatus"
    process_tracer_status: "ModelPluginStatus"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_installer_tracer_status = self.agent_installer_tracer_status.to_dict()

        cloud_network_tracer_status = self.cloud_network_tracer_status.to_dict()

        filesystem_tracer_status = self.filesystem_tracer_status.to_dict()

        network_filter_status = self.network_filter_status.to_dict()

        network_tracer_status = self.network_tracer_status.to_dict()

        process_tracer_status = self.process_tracer_status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_installer_tracer_status": agent_installer_tracer_status,
                "cloud_network_tracer_status": cloud_network_tracer_status,
                "filesystem_tracer_status": filesystem_tracer_status,
                "network_filter_status": network_filter_status,
                "network_tracer_status": network_tracer_status,
                "process_tracer_status": process_tracer_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_plugin_status import ModelPluginStatus

        d = dict(src_dict)
        agent_installer_tracer_status = ModelPluginStatus.from_dict(d.pop("agent_installer_tracer_status"))

        cloud_network_tracer_status = ModelPluginStatus.from_dict(d.pop("cloud_network_tracer_status"))

        filesystem_tracer_status = ModelPluginStatus.from_dict(d.pop("filesystem_tracer_status"))

        network_filter_status = ModelPluginStatus.from_dict(d.pop("network_filter_status"))

        network_tracer_status = ModelPluginStatus.from_dict(d.pop("network_tracer_status"))

        process_tracer_status = ModelPluginStatus.from_dict(d.pop("process_tracer_status"))

        model_agent_plugins_status = cls(
            agent_installer_tracer_status=agent_installer_tracer_status,
            cloud_network_tracer_status=cloud_network_tracer_status,
            filesystem_tracer_status=filesystem_tracer_status,
            network_filter_status=network_filter_status,
            network_tracer_status=network_tracer_status,
            process_tracer_status=process_tracer_status,
        )

        model_agent_plugins_status.additional_properties = d
        return model_agent_plugins_status

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
