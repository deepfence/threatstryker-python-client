from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CompletionCompletionNodeFieldRes")


@_attrs_define
class CompletionCompletionNodeFieldRes:
    """
    Attributes:
        possible_values (Union[None, list[str]]):
    """

    possible_values: Union[None, list[str]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        possible_values: Union[None, list[str]]
        if isinstance(self.possible_values, list):
            possible_values = self.possible_values

        else:
            possible_values = self.possible_values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "possible_values": possible_values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_possible_values(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                possible_values_type_0 = cast(list[str], data)

                return possible_values_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        possible_values = _parse_possible_values(d.pop("possible_values"))

        completion_completion_node_field_res = cls(
            possible_values=possible_values,
        )

        completion_completion_node_field_res.additional_properties = d
        return completion_completion_node_field_res

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
