from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelAgentPluginEnable")


@_attrs_define
class ModelAgentPluginEnable:
    """
    Attributes:
        node_id (str):
        plugin_name (str):
        version (str):
    """

    node_id: str
    plugin_name: str
    version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_id = self.node_id

        plugin_name = self.plugin_name

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node_id": node_id,
                "plugin_name": plugin_name,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        node_id = d.pop("node_id")

        plugin_name = d.pop("plugin_name")

        version = d.pop("version")

        model_agent_plugin_enable = cls(
            node_id=node_id,
            plugin_name=plugin_name,
            version=version,
        )

        model_agent_plugin_enable.additional_properties = d
        return model_agent_plugin_enable

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
