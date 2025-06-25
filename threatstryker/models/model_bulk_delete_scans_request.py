from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_bulk_delete_scans_request_scan_type import ModelBulkDeleteScansRequestScanType

if TYPE_CHECKING:
    from ..models.reporters_fields_filters import ReportersFieldsFilters


T = TypeVar("T", bound="ModelBulkDeleteScansRequest")


@_attrs_define
class ModelBulkDeleteScansRequest:
    """
    Attributes:
        filters (ReportersFieldsFilters):
        scan_type (ModelBulkDeleteScansRequestScanType):
    """

    filters: "ReportersFieldsFilters"
    scan_type: ModelBulkDeleteScansRequestScanType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filters = self.filters.to_dict()

        scan_type = self.scan_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filters": filters,
                "scan_type": scan_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reporters_fields_filters import ReportersFieldsFilters

        d = dict(src_dict)
        filters = ReportersFieldsFilters.from_dict(d.pop("filters"))

        scan_type = ModelBulkDeleteScansRequestScanType(d.pop("scan_type"))

        model_bulk_delete_scans_request = cls(
            filters=filters,
            scan_type=scan_type,
        )

        model_bulk_delete_scans_request.additional_properties = d
        return model_bulk_delete_scans_request

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
