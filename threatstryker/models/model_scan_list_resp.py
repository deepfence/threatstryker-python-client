from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_scan_info import ModelScanInfo


T = TypeVar("T", bound="ModelScanListResp")


@_attrs_define
class ModelScanListResp:
    """
    Example:
        {'scans_info': [{'severity_counts': {'key': 6}, 'status_message': 'status_message', 'node_type': 'node_type',
            'updated_at': 1, 'node_name': 'node_name', 'created_at': 0, 'scan_id': 'scan_id', 'node_id': 'node_id',
            'status': 'status'}, {'severity_counts': {'key': 6}, 'status_message': 'status_message', 'node_type':
            'node_type', 'updated_at': 1, 'node_name': 'node_name', 'created_at': 0, 'scan_id': 'scan_id', 'node_id':
            'node_id', 'status': 'status'}]}

    Attributes:
        scans_info (Optional[List['ModelScanInfo']]):
    """

    scans_info: Optional[List["ModelScanInfo"]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if self.scans_info is None:
            scans_info = None
        else:
            scans_info = []
            for scans_info_item_data in self.scans_info:
                scans_info_item = scans_info_item_data.to_dict()

                scans_info.append(scans_info_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scans_info": scans_info,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_scan_info import ModelScanInfo

        d = src_dict.copy()
        scans_info = []
        _scans_info = d.pop("scans_info")
        for scans_info_item_data in _scans_info or []:
            scans_info_item = ModelScanInfo.from_dict(scans_info_item_data)

            scans_info.append(scans_info_item)

        model_scan_list_resp = cls(
            scans_info=scans_info,
        )

        model_scan_list_resp.additional_properties = d
        return model_scan_list_resp

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties