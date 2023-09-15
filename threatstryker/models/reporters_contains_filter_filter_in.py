from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReportersContainsFilterFilterIn")


@_attrs_define
class ReportersContainsFilterFilterIn:
    """ """

    additional_properties: Dict[str, List[Any]] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reporters_contains_filter_filter_in = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = cast(List[Any], prop_dict)

            additional_properties[prop_name] = additional_property

        reporters_contains_filter_filter_in.additional_properties = additional_properties
        return reporters_contains_filter_filter_in

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> List[Any]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: List[Any]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
