from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_plugin_status import ModelPluginStatus


T = TypeVar("T", bound="ModelAgentPluginsStatus")


@_attrs_define
class ModelAgentPluginsStatus:
    """
    Example:
        {'network_tracer_status': {'description': 'description', 'status': 'status'}, 'network_filter_status':
            {'description': 'description', 'status': 'status'}, 'filesystem_tracer_status': {'description': 'description',
            'status': 'status'}}

    Attributes:
        filesystem_tracer_status (ModelPluginStatus):  Example: {'description': 'description', 'status': 'status'}.
        network_filter_status (ModelPluginStatus):  Example: {'description': 'description', 'status': 'status'}.
        network_tracer_status (ModelPluginStatus):  Example: {'description': 'description', 'status': 'status'}.
    """

    filesystem_tracer_status: "ModelPluginStatus"
    network_filter_status: "ModelPluginStatus"
    network_tracer_status: "ModelPluginStatus"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filesystem_tracer_status = self.filesystem_tracer_status.to_dict()

        network_filter_status = self.network_filter_status.to_dict()

        network_tracer_status = self.network_tracer_status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filesystem_tracer_status": filesystem_tracer_status,
                "network_filter_status": network_filter_status,
                "network_tracer_status": network_tracer_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_plugin_status import ModelPluginStatus

        d = src_dict.copy()
        filesystem_tracer_status = ModelPluginStatus.from_dict(d.pop("filesystem_tracer_status"))

        network_filter_status = ModelPluginStatus.from_dict(d.pop("network_filter_status"))

        network_tracer_status = ModelPluginStatus.from_dict(d.pop("network_tracer_status"))

        model_agent_plugins_status = cls(
            filesystem_tracer_status=filesystem_tracer_status,
            network_filter_status=network_filter_status,
            network_tracer_status=network_tracer_status,
        )

        model_agent_plugins_status.additional_properties = d
        return model_agent_plugins_status

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
