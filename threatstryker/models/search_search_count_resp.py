from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.search_search_count_resp_categories_type_0 import SearchSearchCountRespCategoriesType0


T = TypeVar("T", bound="SearchSearchCountResp")


@_attrs_define
class SearchSearchCountResp:
    """
    Attributes:
        categories (Union['SearchSearchCountRespCategoriesType0', None]):
        count (int):
    """

    categories: Union["SearchSearchCountRespCategoriesType0", None]
    count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.search_search_count_resp_categories_type_0 import SearchSearchCountRespCategoriesType0

        categories: Union[None, dict[str, Any]]
        if isinstance(self.categories, SearchSearchCountRespCategoriesType0):
            categories = self.categories.to_dict()
        else:
            categories = self.categories

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "categories": categories,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_search_count_resp_categories_type_0 import SearchSearchCountRespCategoriesType0

        d = dict(src_dict)

        def _parse_categories(data: object) -> Union["SearchSearchCountRespCategoriesType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                categories_type_0 = SearchSearchCountRespCategoriesType0.from_dict(data)

                return categories_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SearchSearchCountRespCategoriesType0", None], data)

        categories = _parse_categories(d.pop("categories"))

        count = d.pop("count")

        search_search_count_resp = cls(
            categories=categories,
            count=count,
        )

        search_search_count_resp.additional_properties = d
        return search_search_count_resp

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
