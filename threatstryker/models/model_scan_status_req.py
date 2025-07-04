from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelScanStatusReq")


@_attrs_define
class ModelScanStatusReq:
    """
    Attributes:
        bulk_scan_id (str):
        scan_ids (Union[None, list[str]]):
    """

    bulk_scan_id: str
    scan_ids: Union[None, list[str]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bulk_scan_id = self.bulk_scan_id

        scan_ids: Union[None, list[str]]
        if isinstance(self.scan_ids, list):
            scan_ids = self.scan_ids

        else:
            scan_ids = self.scan_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bulk_scan_id": bulk_scan_id,
                "scan_ids": scan_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bulk_scan_id = d.pop("bulk_scan_id")

        def _parse_scan_ids(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scan_ids_type_0 = cast(list[str], data)

                return scan_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        scan_ids = _parse_scan_ids(d.pop("scan_ids"))

        model_scan_status_req = cls(
            bulk_scan_id=bulk_scan_id,
            scan_ids=scan_ids,
        )

        model_scan_status_req.additional_properties = d
        return model_scan_status_req

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
