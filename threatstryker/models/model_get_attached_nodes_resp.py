from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelGetAttachedNodesResp")


@_attrs_define
class ModelGetAttachedNodesResp:
    """
    Example:
        {'node_ids': ['node_ids', 'node_ids']}

    Attributes:
        node_ids (Union[Unset, None, List[str]]):
    """

    node_ids: Union[Unset, None, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        node_ids: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.node_ids, Unset):
            if self.node_ids is None:
                node_ids = None
            else:
                node_ids = self.node_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if node_ids is not UNSET:
            field_dict["node_ids"] = node_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        node_ids = cast(List[str], d.pop("node_ids", UNSET))

        model_get_attached_nodes_resp = cls(
            node_ids=node_ids,
        )

        model_get_attached_nodes_resp.additional_properties = d
        return model_get_attached_nodes_resp

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
