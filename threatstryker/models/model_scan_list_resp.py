from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_scan_info import ModelScanInfo


T = TypeVar("T", bound="ModelScanListResp")


@_attrs_define
class ModelScanListResp:
    """
    Attributes:
        scans_info (Union[None, list['ModelScanInfo']]):
    """

    scans_info: Union[None, list["ModelScanInfo"]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scans_info: Union[None, list[dict[str, Any]]]
        if isinstance(self.scans_info, list):
            scans_info = []
            for scans_info_type_0_item_data in self.scans_info:
                scans_info_type_0_item = scans_info_type_0_item_data.to_dict()
                scans_info.append(scans_info_type_0_item)

        else:
            scans_info = self.scans_info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scans_info": scans_info,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_scan_info import ModelScanInfo

        d = dict(src_dict)

        def _parse_scans_info(data: object) -> Union[None, list["ModelScanInfo"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scans_info_type_0 = []
                _scans_info_type_0 = data
                for scans_info_type_0_item_data in _scans_info_type_0:
                    scans_info_type_0_item = ModelScanInfo.from_dict(scans_info_type_0_item_data)

                    scans_info_type_0.append(scans_info_type_0_item)

                return scans_info_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["ModelScanInfo"]], data)

        scans_info = _parse_scans_info(d.pop("scans_info"))

        model_scan_list_resp = cls(
            scans_info=scans_info,
        )

        model_scan_list_resp.additional_properties = d
        return model_scan_list_resp

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
