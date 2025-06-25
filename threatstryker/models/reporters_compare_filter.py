from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReportersCompareFilter")


@_attrs_define
class ReportersCompareFilter:
    """
    Attributes:
        field_name (str):
        field_value (Any):
        greater_than (bool):
    """

    field_name: str
    field_value: Any
    greater_than: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_name = self.field_name

        field_value = self.field_value

        greater_than = self.greater_than

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field_name": field_name,
                "field_value": field_value,
                "greater_than": greater_than,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_name = d.pop("field_name")

        field_value = d.pop("field_value")

        greater_than = d.pop("greater_than")

        reporters_compare_filter = cls(
            field_name=field_name,
            field_value=field_value,
            greater_than=greater_than,
        )

        reporters_compare_filter.additional_properties = d
        return reporters_compare_filter

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
