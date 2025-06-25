from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_filters_req_having_type_0 import ModelFiltersReqHavingType0


T = TypeVar("T", bound="ModelFiltersReq")


@_attrs_define
class ModelFiltersReq:
    """
    Attributes:
        filters (Union[None, list[str]]):
        having (Union['ModelFiltersReqHavingType0', None, Unset]):
    """

    filters: Union[None, list[str]]
    having: Union["ModelFiltersReqHavingType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.model_filters_req_having_type_0 import ModelFiltersReqHavingType0

        filters: Union[None, list[str]]
        if isinstance(self.filters, list):
            filters = self.filters

        else:
            filters = self.filters

        having: Union[None, Unset, dict[str, Any]]
        if isinstance(self.having, Unset):
            having = UNSET
        elif isinstance(self.having, ModelFiltersReqHavingType0):
            having = self.having.to_dict()
        else:
            having = self.having

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filters": filters,
            }
        )
        if having is not UNSET:
            field_dict["having"] = having

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_filters_req_having_type_0 import ModelFiltersReqHavingType0

        d = dict(src_dict)

        def _parse_filters(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                filters_type_0 = cast(list[str], data)

                return filters_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        filters = _parse_filters(d.pop("filters"))

        def _parse_having(data: object) -> Union["ModelFiltersReqHavingType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                having_type_0 = ModelFiltersReqHavingType0.from_dict(data)

                return having_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ModelFiltersReqHavingType0", None, Unset], data)

        having = _parse_having(d.pop("having", UNSET))

        model_filters_req = cls(
            filters=filters,
            having=having,
        )

        model_filters_req.additional_properties = d
        return model_filters_req

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
