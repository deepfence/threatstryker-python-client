from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_node_identifier_node_type import ModelNodeIdentifierNodeType

T = TypeVar("T", bound="ModelNodeIdentifier")


@_attrs_define
class ModelNodeIdentifier:
    """
    Attributes:
        node_id (str):
        node_type (ModelNodeIdentifierNodeType):
    """

    node_id: str
    node_type: ModelNodeIdentifierNodeType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_id = self.node_id

        node_type = self.node_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node_id": node_id,
                "node_type": node_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        node_id = d.pop("node_id")

        node_type = ModelNodeIdentifierNodeType(d.pop("node_type"))

        model_node_identifier = cls(
            node_id=node_id,
            node_type=node_type,
        )

        model_node_identifier.additional_properties = d
        return model_node_identifier

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
