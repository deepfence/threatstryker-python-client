from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_fetch_window import ModelFetchWindow
    from ..models.reporters_fields_filters import ReportersFieldsFilters


T = TypeVar("T", bound="CompletionCompletionNodeFieldReq")


@_attrs_define
class CompletionCompletionNodeFieldReq:
    """
    Attributes:
        completion (str):
        field_name (str):
        window (ModelFetchWindow):
        filters (Union[Unset, ReportersFieldsFilters]):
        is_array_field (Union[Unset, bool]):
        scan_id (Union[Unset, str]):
    """

    completion: str
    field_name: str
    window: "ModelFetchWindow"
    filters: Union[Unset, "ReportersFieldsFilters"] = UNSET
    is_array_field: Union[Unset, bool] = UNSET
    scan_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        completion = self.completion

        field_name = self.field_name

        window = self.window.to_dict()

        filters: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        is_array_field = self.is_array_field

        scan_id = self.scan_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "completion": completion,
                "field_name": field_name,
                "window": window,
            }
        )
        if filters is not UNSET:
            field_dict["filters"] = filters
        if is_array_field is not UNSET:
            field_dict["is_array_field"] = is_array_field
        if scan_id is not UNSET:
            field_dict["scan_id"] = scan_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_fetch_window import ModelFetchWindow
        from ..models.reporters_fields_filters import ReportersFieldsFilters

        d = dict(src_dict)
        completion = d.pop("completion")

        field_name = d.pop("field_name")

        window = ModelFetchWindow.from_dict(d.pop("window"))

        _filters = d.pop("filters", UNSET)
        filters: Union[Unset, ReportersFieldsFilters]
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = ReportersFieldsFilters.from_dict(_filters)

        is_array_field = d.pop("is_array_field", UNSET)

        scan_id = d.pop("scan_id", UNSET)

        completion_completion_node_field_req = cls(
            completion=completion,
            field_name=field_name,
            window=window,
            filters=filters,
            is_array_field=is_array_field,
            scan_id=scan_id,
        )

        completion_completion_node_field_req.additional_properties = d
        return completion_completion_node_field_req

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
