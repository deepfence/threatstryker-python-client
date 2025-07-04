from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IngestersSecretScanStatus")


@_attrs_define
class IngestersSecretScanStatus:
    """
    Attributes:
        scan_id (Union[Unset, str]):
        scan_message (Union[Unset, str]):
        scan_status (Union[Unset, str]):
    """

    scan_id: Union[Unset, str] = UNSET
    scan_message: Union[Unset, str] = UNSET
    scan_status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scan_id = self.scan_id

        scan_message = self.scan_message

        scan_status = self.scan_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scan_id is not UNSET:
            field_dict["scan_id"] = scan_id
        if scan_message is not UNSET:
            field_dict["scan_message"] = scan_message
        if scan_status is not UNSET:
            field_dict["scan_status"] = scan_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scan_id = d.pop("scan_id", UNSET)

        scan_message = d.pop("scan_message", UNSET)

        scan_status = d.pop("scan_status", UNSET)

        ingesters_secret_scan_status = cls(
            scan_id=scan_id,
            scan_message=scan_message,
            scan_status=scan_status,
        )

        ingesters_secret_scan_status.additional_properties = d
        return ingesters_secret_scan_status

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
