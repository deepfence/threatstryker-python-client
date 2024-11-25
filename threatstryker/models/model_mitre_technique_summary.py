from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelMitreTechniqueSummary")


@_attrs_define
class ModelMitreTechniqueSummary:
    """
    Example:
        {'severity': 'severity', 'count': 6}

    Attributes:
        count (int):
        severity (str):
    """

    count: int
    severity: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count

        severity = self.severity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "severity": severity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        count = d.pop("count")

        severity = d.pop("severity")

        model_mitre_technique_summary = cls(
            count=count,
            severity=severity,
        )

        model_mitre_technique_summary.additional_properties = d
        return model_mitre_technique_summary

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
