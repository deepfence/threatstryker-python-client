from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_fetch_window import ModelFetchWindow
    from ..models.reporters_fields_filters import ReportersFieldsFilters


T = TypeVar("T", bound="ModelScanResultsReq")


@_attrs_define
class ModelScanResultsReq:
    """
    Attributes:
        fields_filter (ReportersFieldsFilters):
        scan_id (str):
        window (ModelFetchWindow):
    """

    fields_filter: "ReportersFieldsFilters"
    scan_id: str
    window: "ModelFetchWindow"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fields_filter = self.fields_filter.to_dict()

        scan_id = self.scan_id

        window = self.window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fields_filter": fields_filter,
                "scan_id": scan_id,
                "window": window,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_fetch_window import ModelFetchWindow
        from ..models.reporters_fields_filters import ReportersFieldsFilters

        d = dict(src_dict)
        fields_filter = ReportersFieldsFilters.from_dict(d.pop("fields_filter"))

        scan_id = d.pop("scan_id")

        window = ModelFetchWindow.from_dict(d.pop("window"))

        model_scan_results_req = cls(
            fields_filter=fields_filter,
            scan_id=scan_id,
            window=window,
        )

        model_scan_results_req.additional_properties = d
        return model_scan_results_req

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
