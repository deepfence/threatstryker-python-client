from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_nodes_in_scan_result_request_scan_type import ModelNodesInScanResultRequestScanType

T = TypeVar("T", bound="ModelNodesInScanResultRequest")


@_attrs_define
class ModelNodesInScanResultRequest:
    """
    Attributes:
        result_ids (Union[None, list[str]]):
        scan_type (ModelNodesInScanResultRequestScanType):
    """

    result_ids: Union[None, list[str]]
    scan_type: ModelNodesInScanResultRequestScanType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        result_ids: Union[None, list[str]]
        if isinstance(self.result_ids, list):
            result_ids = self.result_ids

        else:
            result_ids = self.result_ids

        scan_type = self.scan_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "result_ids": result_ids,
                "scan_type": scan_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_result_ids(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                result_ids_type_0 = cast(list[str], data)

                return result_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        result_ids = _parse_result_ids(d.pop("result_ids"))

        scan_type = ModelNodesInScanResultRequestScanType(d.pop("scan_type"))

        model_nodes_in_scan_result_request = cls(
            result_ids=result_ids,
            scan_type=scan_type,
        )

        model_nodes_in_scan_result_request.additional_properties = d
        return model_nodes_in_scan_result_request

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
