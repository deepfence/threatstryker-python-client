from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_scan_results_common import ModelScanResultsCommon


T = TypeVar("T", bound="ModelDownloadScanResultsResponse")


@_attrs_define
class ModelDownloadScanResultsResponse:
    """
    Attributes:
        scan_info (Union[Unset, ModelScanResultsCommon]):
        scan_results (Union[None, Unset, list[Any]]):
    """

    scan_info: Union[Unset, "ModelScanResultsCommon"] = UNSET
    scan_results: Union[None, Unset, list[Any]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scan_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.scan_info, Unset):
            scan_info = self.scan_info.to_dict()

        scan_results: Union[None, Unset, list[Any]]
        if isinstance(self.scan_results, Unset):
            scan_results = UNSET
        elif isinstance(self.scan_results, list):
            scan_results = self.scan_results

        else:
            scan_results = self.scan_results

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scan_info is not UNSET:
            field_dict["scan_info"] = scan_info
        if scan_results is not UNSET:
            field_dict["scan_results"] = scan_results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_scan_results_common import ModelScanResultsCommon

        d = dict(src_dict)
        _scan_info = d.pop("scan_info", UNSET)
        scan_info: Union[Unset, ModelScanResultsCommon]
        if isinstance(_scan_info, Unset):
            scan_info = UNSET
        else:
            scan_info = ModelScanResultsCommon.from_dict(_scan_info)

        def _parse_scan_results(data: object) -> Union[None, Unset, list[Any]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scan_results_type_0 = cast(list[Any], data)

                return scan_results_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[Any]], data)

        scan_results = _parse_scan_results(d.pop("scan_results", UNSET))

        model_download_scan_results_response = cls(
            scan_info=scan_info,
            scan_results=scan_results,
        )

        model_download_scan_results_response.additional_properties = d
        return model_download_scan_results_response

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
