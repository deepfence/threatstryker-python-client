from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelAgentPluginConfigNames")


@_attrs_define
class ModelAgentPluginConfigNames:
    """
    Attributes:
        filesystem_config_name (str):
        network_config_name (str):
        policy_config_name (str):
        process_config_name (str):
    """

    filesystem_config_name: str
    network_config_name: str
    policy_config_name: str
    process_config_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filesystem_config_name = self.filesystem_config_name

        network_config_name = self.network_config_name

        policy_config_name = self.policy_config_name

        process_config_name = self.process_config_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filesystem_config_name": filesystem_config_name,
                "network_config_name": network_config_name,
                "policy_config_name": policy_config_name,
                "process_config_name": process_config_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filesystem_config_name = d.pop("filesystem_config_name")

        network_config_name = d.pop("network_config_name")

        policy_config_name = d.pop("policy_config_name")

        process_config_name = d.pop("process_config_name")

        model_agent_plugin_config_names = cls(
            filesystem_config_name=filesystem_config_name,
            network_config_name=network_config_name,
            policy_config_name=policy_config_name,
            process_config_name=process_config_name,
        )

        model_agent_plugin_config_names.additional_properties = d
        return model_agent_plugin_config_names

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
