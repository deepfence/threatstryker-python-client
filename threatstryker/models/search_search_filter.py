from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_fetch_window import ModelFetchWindow
    from ..models.reporters_fields_filters import ReportersFieldsFilters


T = TypeVar("T", bound="SearchSearchFilter")


@_attrs_define
class SearchSearchFilter:
    """
    Attributes:
        filters (ReportersFieldsFilters):
        in_field_filter (Union[None, list[str]]):
        window (ModelFetchWindow):
    """

    filters: "ReportersFieldsFilters"
    in_field_filter: Union[None, list[str]]
    window: "ModelFetchWindow"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filters = self.filters.to_dict()

        in_field_filter: Union[None, list[str]]
        if isinstance(self.in_field_filter, list):
            in_field_filter = self.in_field_filter

        else:
            in_field_filter = self.in_field_filter

        window = self.window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filters": filters,
                "in_field_filter": in_field_filter,
                "window": window,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_fetch_window import ModelFetchWindow
        from ..models.reporters_fields_filters import ReportersFieldsFilters

        d = dict(src_dict)
        filters = ReportersFieldsFilters.from_dict(d.pop("filters"))

        def _parse_in_field_filter(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                in_field_filter_type_0 = cast(list[str], data)

                return in_field_filter_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        in_field_filter = _parse_in_field_filter(d.pop("in_field_filter"))

        window = ModelFetchWindow.from_dict(d.pop("window"))

        search_search_filter = cls(
            filters=filters,
            in_field_filter=in_field_filter,
            window=window,
        )

        search_search_filter.additional_properties = d
        return search_search_filter

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
