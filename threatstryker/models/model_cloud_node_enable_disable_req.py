from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelCloudNodeEnableDisableReq")


@_attrs_define
class ModelCloudNodeEnableDisableReq:
    """
    Attributes:
        control_ids (Union[None, Unset, list[str]]):
        node_id (Union[Unset, str]):
    """

    control_ids: Union[None, Unset, list[str]] = UNSET
    node_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        control_ids: Union[None, Unset, list[str]]
        if isinstance(self.control_ids, Unset):
            control_ids = UNSET
        elif isinstance(self.control_ids, list):
            control_ids = self.control_ids

        else:
            control_ids = self.control_ids

        node_id = self.node_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if control_ids is not UNSET:
            field_dict["control_ids"] = control_ids
        if node_id is not UNSET:
            field_dict["node_id"] = node_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_control_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                control_ids_type_0 = cast(list[str], data)

                return control_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        control_ids = _parse_control_ids(d.pop("control_ids", UNSET))

        node_id = d.pop("node_id", UNSET)

        model_cloud_node_enable_disable_req = cls(
            control_ids=control_ids,
            node_id=node_id,
        )

        model_cloud_node_enable_disable_req.additional_properties = d
        return model_cloud_node_enable_disable_req

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
