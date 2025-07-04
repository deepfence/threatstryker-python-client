from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_fetch_window import ModelFetchWindow


T = TypeVar("T", bound="LookupLookupFilter")


@_attrs_define
class LookupLookupFilter:
    """
    Attributes:
        in_field_filter (Union[None, list[str]]):
        node_ids (Union[None, list[str]]):
        window (ModelFetchWindow):
    """

    in_field_filter: Union[None, list[str]]
    node_ids: Union[None, list[str]]
    window: "ModelFetchWindow"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        in_field_filter: Union[None, list[str]]
        if isinstance(self.in_field_filter, list):
            in_field_filter = self.in_field_filter

        else:
            in_field_filter = self.in_field_filter

        node_ids: Union[None, list[str]]
        if isinstance(self.node_ids, list):
            node_ids = self.node_ids

        else:
            node_ids = self.node_ids

        window = self.window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "in_field_filter": in_field_filter,
                "node_ids": node_ids,
                "window": window,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_fetch_window import ModelFetchWindow

        d = dict(src_dict)

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

        def _parse_node_ids(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                node_ids_type_0 = cast(list[str], data)

                return node_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        node_ids = _parse_node_ids(d.pop("node_ids"))

        window = ModelFetchWindow.from_dict(d.pop("window"))

        lookup_lookup_filter = cls(
            in_field_filter=in_field_filter,
            node_ids=node_ids,
            window=window,
        )

        lookup_lookup_filter.additional_properties = d
        return lookup_lookup_filter

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
