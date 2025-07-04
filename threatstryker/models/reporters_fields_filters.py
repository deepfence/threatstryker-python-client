from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reporters_compare_filter import ReportersCompareFilter
    from ..models.reporters_contains_filter import ReportersContainsFilter
    from ..models.reporters_match_filter import ReportersMatchFilter
    from ..models.reporters_order_filter import ReportersOrderFilter


T = TypeVar("T", bound="ReportersFieldsFilters")


@_attrs_define
class ReportersFieldsFilters:
    """
    Attributes:
        compare_filter (Union[None, list['ReportersCompareFilter']]):
        contains_filter (ReportersContainsFilter):
        match_filter (ReportersMatchFilter):
        order_filter (ReportersOrderFilter):
        contains_in_array_filter (Union[Unset, ReportersContainsFilter]):
        match_in_array_filter (Union[Unset, ReportersMatchFilter]):
        not_contains_filter (Union[Unset, ReportersContainsFilter]):
    """

    compare_filter: Union[None, list["ReportersCompareFilter"]]
    contains_filter: "ReportersContainsFilter"
    match_filter: "ReportersMatchFilter"
    order_filter: "ReportersOrderFilter"
    contains_in_array_filter: Union[Unset, "ReportersContainsFilter"] = UNSET
    match_in_array_filter: Union[Unset, "ReportersMatchFilter"] = UNSET
    not_contains_filter: Union[Unset, "ReportersContainsFilter"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        compare_filter: Union[None, list[dict[str, Any]]]
        if isinstance(self.compare_filter, list):
            compare_filter = []
            for compare_filter_type_0_item_data in self.compare_filter:
                compare_filter_type_0_item = compare_filter_type_0_item_data.to_dict()
                compare_filter.append(compare_filter_type_0_item)

        else:
            compare_filter = self.compare_filter

        contains_filter = self.contains_filter.to_dict()

        match_filter = self.match_filter.to_dict()

        order_filter = self.order_filter.to_dict()

        contains_in_array_filter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.contains_in_array_filter, Unset):
            contains_in_array_filter = self.contains_in_array_filter.to_dict()

        match_in_array_filter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.match_in_array_filter, Unset):
            match_in_array_filter = self.match_in_array_filter.to_dict()

        not_contains_filter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.not_contains_filter, Unset):
            not_contains_filter = self.not_contains_filter.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "compare_filter": compare_filter,
                "contains_filter": contains_filter,
                "match_filter": match_filter,
                "order_filter": order_filter,
            }
        )
        if contains_in_array_filter is not UNSET:
            field_dict["contains_in_array_filter"] = contains_in_array_filter
        if match_in_array_filter is not UNSET:
            field_dict["match_in_array_filter"] = match_in_array_filter
        if not_contains_filter is not UNSET:
            field_dict["not_contains_filter"] = not_contains_filter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reporters_compare_filter import ReportersCompareFilter
        from ..models.reporters_contains_filter import ReportersContainsFilter
        from ..models.reporters_match_filter import ReportersMatchFilter
        from ..models.reporters_order_filter import ReportersOrderFilter

        d = dict(src_dict)

        def _parse_compare_filter(data: object) -> Union[None, list["ReportersCompareFilter"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                compare_filter_type_0 = []
                _compare_filter_type_0 = data
                for compare_filter_type_0_item_data in _compare_filter_type_0:
                    compare_filter_type_0_item = ReportersCompareFilter.from_dict(compare_filter_type_0_item_data)

                    compare_filter_type_0.append(compare_filter_type_0_item)

                return compare_filter_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["ReportersCompareFilter"]], data)

        compare_filter = _parse_compare_filter(d.pop("compare_filter"))

        contains_filter = ReportersContainsFilter.from_dict(d.pop("contains_filter"))

        match_filter = ReportersMatchFilter.from_dict(d.pop("match_filter"))

        order_filter = ReportersOrderFilter.from_dict(d.pop("order_filter"))

        _contains_in_array_filter = d.pop("contains_in_array_filter", UNSET)
        contains_in_array_filter: Union[Unset, ReportersContainsFilter]
        if isinstance(_contains_in_array_filter, Unset):
            contains_in_array_filter = UNSET
        else:
            contains_in_array_filter = ReportersContainsFilter.from_dict(_contains_in_array_filter)

        _match_in_array_filter = d.pop("match_in_array_filter", UNSET)
        match_in_array_filter: Union[Unset, ReportersMatchFilter]
        if isinstance(_match_in_array_filter, Unset):
            match_in_array_filter = UNSET
        else:
            match_in_array_filter = ReportersMatchFilter.from_dict(_match_in_array_filter)

        _not_contains_filter = d.pop("not_contains_filter", UNSET)
        not_contains_filter: Union[Unset, ReportersContainsFilter]
        if isinstance(_not_contains_filter, Unset):
            not_contains_filter = UNSET
        else:
            not_contains_filter = ReportersContainsFilter.from_dict(_not_contains_filter)

        reporters_fields_filters = cls(
            compare_filter=compare_filter,
            contains_filter=contains_filter,
            match_filter=match_filter,
            order_filter=order_filter,
            contains_in_array_filter=contains_in_array_filter,
            match_in_array_filter=match_in_array_filter,
            not_contains_filter=not_contains_filter,
        )

        reporters_fields_filters.additional_properties = d
        return reporters_fields_filters

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
