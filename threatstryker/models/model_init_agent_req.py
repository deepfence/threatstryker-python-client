from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelInitAgentReq")


@_attrs_define
class ModelInitAgentReq:
    """
    Attributes:
        available_workload (int):
        node_id (str):
        node_type (str):
        version (str):
    """

    available_workload: int
    node_id: str
    node_type: str
    version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available_workload = self.available_workload

        node_id = self.node_id

        node_type = self.node_type

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "available_workload": available_workload,
                "node_id": node_id,
                "node_type": node_type,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        available_workload = d.pop("available_workload")

        node_id = d.pop("node_id")

        node_type = d.pop("node_type")

        version = d.pop("version")

        model_init_agent_req = cls(
            available_workload=available_workload,
            node_id=node_id,
            node_type=node_type,
            version=version,
        )

        model_init_agent_req.additional_properties = d
        return model_init_agent_req

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
