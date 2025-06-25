from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_compliance_scan_result_control_group_counts import ModelComplianceScanResultControlGroupCounts


T = TypeVar("T", bound="ModelComplianceScanResultControlGroup")


@_attrs_define
class ModelComplianceScanResultControlGroup:
    """
    Attributes:
        benchmark_types (Union[Unset, list[str]]):
        counts (Union[Unset, ModelComplianceScanResultControlGroupCounts]):
        problem_title (Union[Unset, str]):
    """

    benchmark_types: Union[Unset, list[str]] = UNSET
    counts: Union[Unset, "ModelComplianceScanResultControlGroupCounts"] = UNSET
    problem_title: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        benchmark_types: Union[Unset, list[str]] = UNSET
        if not isinstance(self.benchmark_types, Unset):
            benchmark_types = self.benchmark_types

        counts: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.counts, Unset):
            counts = self.counts.to_dict()

        problem_title = self.problem_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if benchmark_types is not UNSET:
            field_dict["benchmark_types"] = benchmark_types
        if counts is not UNSET:
            field_dict["counts"] = counts
        if problem_title is not UNSET:
            field_dict["problem_title"] = problem_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_compliance_scan_result_control_group_counts import (
            ModelComplianceScanResultControlGroupCounts,
        )

        d = dict(src_dict)
        benchmark_types = cast(list[str], d.pop("benchmark_types", UNSET))

        _counts = d.pop("counts", UNSET)
        counts: Union[Unset, ModelComplianceScanResultControlGroupCounts]
        if isinstance(_counts, Unset):
            counts = UNSET
        else:
            counts = ModelComplianceScanResultControlGroupCounts.from_dict(_counts)

        problem_title = d.pop("problem_title", UNSET)

        model_compliance_scan_result_control_group = cls(
            benchmark_types=benchmark_types,
            counts=counts,
            problem_title=problem_title,
        )

        model_compliance_scan_result_control_group.additional_properties = d
        return model_compliance_scan_result_control_group

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
