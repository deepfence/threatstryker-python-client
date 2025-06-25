from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_search_filter import SearchSearchFilter


T = TypeVar("T", bound="SearchChainedSearchFilter")


@_attrs_define
class SearchChainedSearchFilter:
    """
    Attributes:
        node_filter (SearchSearchFilter):
        relation_ship (str):
        next_filter (Union[Unset, SearchChainedSearchFilter]):
    """

    node_filter: "SearchSearchFilter"
    relation_ship: str
    next_filter: Union[Unset, "SearchChainedSearchFilter"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_filter = self.node_filter.to_dict()

        relation_ship = self.relation_ship

        next_filter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.next_filter, Unset):
            next_filter = self.next_filter.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node_filter": node_filter,
                "relation_ship": relation_ship,
            }
        )
        if next_filter is not UNSET:
            field_dict["next_filter"] = next_filter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_search_filter import SearchSearchFilter

        d = dict(src_dict)
        node_filter = SearchSearchFilter.from_dict(d.pop("node_filter"))

        relation_ship = d.pop("relation_ship")

        _next_filter = d.pop("next_filter", UNSET)
        next_filter: Union[Unset, SearchChainedSearchFilter]
        if isinstance(_next_filter, Unset):
            next_filter = UNSET
        else:
            next_filter = SearchChainedSearchFilter.from_dict(_next_filter)

        search_chained_search_filter = cls(
            node_filter=node_filter,
            relation_ship=relation_ship,
            next_filter=next_filter,
        )

        search_chained_search_filter.additional_properties = d
        return search_chained_search_filter

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
