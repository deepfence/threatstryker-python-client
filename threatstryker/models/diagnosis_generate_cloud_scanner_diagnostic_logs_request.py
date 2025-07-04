from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.diagnosis_node_identifier import DiagnosisNodeIdentifier


T = TypeVar("T", bound="DiagnosisGenerateCloudScannerDiagnosticLogsRequest")


@_attrs_define
class DiagnosisGenerateCloudScannerDiagnosticLogsRequest:
    """
    Attributes:
        node_ids (Union[None, list['DiagnosisNodeIdentifier']]):
        tail (int):
    """

    node_ids: Union[None, list["DiagnosisNodeIdentifier"]]
    tail: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_ids: Union[None, list[dict[str, Any]]]
        if isinstance(self.node_ids, list):
            node_ids = []
            for node_ids_type_0_item_data in self.node_ids:
                node_ids_type_0_item = node_ids_type_0_item_data.to_dict()
                node_ids.append(node_ids_type_0_item)

        else:
            node_ids = self.node_ids

        tail = self.tail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node_ids": node_ids,
                "tail": tail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.diagnosis_node_identifier import DiagnosisNodeIdentifier

        d = dict(src_dict)

        def _parse_node_ids(data: object) -> Union[None, list["DiagnosisNodeIdentifier"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                node_ids_type_0 = []
                _node_ids_type_0 = data
                for node_ids_type_0_item_data in _node_ids_type_0:
                    node_ids_type_0_item = DiagnosisNodeIdentifier.from_dict(node_ids_type_0_item_data)

                    node_ids_type_0.append(node_ids_type_0_item)

                return node_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["DiagnosisNodeIdentifier"]], data)

        node_ids = _parse_node_ids(d.pop("node_ids"))

        tail = d.pop("tail")

        diagnosis_generate_cloud_scanner_diagnostic_logs_request = cls(
            node_ids=node_ids,
            tail=tail,
        )

        diagnosis_generate_cloud_scanner_diagnostic_logs_request.additional_properties = d
        return diagnosis_generate_cloud_scanner_diagnostic_logs_request

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
