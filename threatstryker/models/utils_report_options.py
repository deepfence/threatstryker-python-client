from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.utils_report_options_sbom_format import UtilsReportOptionsSbomFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="UtilsReportOptions")


@_attrs_define
class UtilsReportOptions:
    """
    Attributes:
        sbom_format (Union[Unset, UtilsReportOptionsSbomFormat]):
    """

    sbom_format: Union[Unset, UtilsReportOptionsSbomFormat] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sbom_format: Union[Unset, str] = UNSET
        if not isinstance(self.sbom_format, Unset):
            sbom_format = self.sbom_format.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sbom_format is not UNSET:
            field_dict["sbom_format"] = sbom_format

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _sbom_format = d.pop("sbom_format", UNSET)
        sbom_format: Union[Unset, UtilsReportOptionsSbomFormat]
        if isinstance(_sbom_format, Unset):
            sbom_format = UNSET
        else:
            sbom_format = UtilsReportOptionsSbomFormat(_sbom_format)

        utils_report_options = cls(
            sbom_format=sbom_format,
        )

        utils_report_options.additional_properties = d
        return utils_report_options

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
