from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_benchmark_type import ModelBenchmarkType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_node_identifier import ModelNodeIdentifier
    from ..models.model_scan_filter import ModelScanFilter


T = TypeVar("T", bound="ModelComplianceScanTriggerReq")


@_attrs_define
class ModelComplianceScanTriggerReq:
    """
    Attributes:
        benchmark_types (Union[None, list[ModelBenchmarkType]]):
        filters (ModelScanFilter):
        node_ids (Union[None, list['ModelNodeIdentifier']]):
        deepfence_system_scan (Union[Unset, bool]):
        is_priority (Union[Unset, bool]):
    """

    benchmark_types: Union[None, list[ModelBenchmarkType]]
    filters: "ModelScanFilter"
    node_ids: Union[None, list["ModelNodeIdentifier"]]
    deepfence_system_scan: Union[Unset, bool] = UNSET
    is_priority: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        benchmark_types: Union[None, list[str]]
        if isinstance(self.benchmark_types, list):
            benchmark_types = []
            for benchmark_types_type_0_item_data in self.benchmark_types:
                benchmark_types_type_0_item = benchmark_types_type_0_item_data.value
                benchmark_types.append(benchmark_types_type_0_item)

        else:
            benchmark_types = self.benchmark_types

        filters = self.filters.to_dict()

        node_ids: Union[None, list[dict[str, Any]]]
        if isinstance(self.node_ids, list):
            node_ids = []
            for node_ids_type_0_item_data in self.node_ids:
                node_ids_type_0_item = node_ids_type_0_item_data.to_dict()
                node_ids.append(node_ids_type_0_item)

        else:
            node_ids = self.node_ids

        deepfence_system_scan = self.deepfence_system_scan

        is_priority = self.is_priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "benchmark_types": benchmark_types,
                "filters": filters,
                "node_ids": node_ids,
            }
        )
        if deepfence_system_scan is not UNSET:
            field_dict["deepfence_system_scan"] = deepfence_system_scan
        if is_priority is not UNSET:
            field_dict["is_priority"] = is_priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_node_identifier import ModelNodeIdentifier
        from ..models.model_scan_filter import ModelScanFilter

        d = dict(src_dict)

        def _parse_benchmark_types(data: object) -> Union[None, list[ModelBenchmarkType]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                benchmark_types_type_0 = []
                _benchmark_types_type_0 = data
                for benchmark_types_type_0_item_data in _benchmark_types_type_0:
                    benchmark_types_type_0_item = ModelBenchmarkType(benchmark_types_type_0_item_data)

                    benchmark_types_type_0.append(benchmark_types_type_0_item)

                return benchmark_types_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[ModelBenchmarkType]], data)

        benchmark_types = _parse_benchmark_types(d.pop("benchmark_types"))

        filters = ModelScanFilter.from_dict(d.pop("filters"))

        def _parse_node_ids(data: object) -> Union[None, list["ModelNodeIdentifier"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                node_ids_type_0 = []
                _node_ids_type_0 = data
                for node_ids_type_0_item_data in _node_ids_type_0:
                    node_ids_type_0_item = ModelNodeIdentifier.from_dict(node_ids_type_0_item_data)

                    node_ids_type_0.append(node_ids_type_0_item)

                return node_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["ModelNodeIdentifier"]], data)

        node_ids = _parse_node_ids(d.pop("node_ids"))

        deepfence_system_scan = d.pop("deepfence_system_scan", UNSET)

        is_priority = d.pop("is_priority", UNSET)

        model_compliance_scan_trigger_req = cls(
            benchmark_types=benchmark_types,
            filters=filters,
            node_ids=node_ids,
            deepfence_system_scan=deepfence_system_scan,
            is_priority=is_priority,
        )

        model_compliance_scan_trigger_req.additional_properties = d
        return model_compliance_scan_trigger_req

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
