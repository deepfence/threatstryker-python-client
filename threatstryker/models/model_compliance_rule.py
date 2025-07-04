from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelComplianceRule")


@_attrs_define
class ModelComplianceRule:
    """
    Attributes:
        description (str):
        masked (bool):
        test_category (str):
        test_desc (str):
        test_number (str):
        test_rationale (str):
        test_severity (str):
        updated_at (int):
    """

    description: str
    masked: bool
    test_category: str
    test_desc: str
    test_number: str
    test_rationale: str
    test_severity: str
    updated_at: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        masked = self.masked

        test_category = self.test_category

        test_desc = self.test_desc

        test_number = self.test_number

        test_rationale = self.test_rationale

        test_severity = self.test_severity

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "masked": masked,
                "test_category": test_category,
                "test_desc": test_desc,
                "test_number": test_number,
                "test_rationale": test_rationale,
                "test_severity": test_severity,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        masked = d.pop("masked")

        test_category = d.pop("test_category")

        test_desc = d.pop("test_desc")

        test_number = d.pop("test_number")

        test_rationale = d.pop("test_rationale")

        test_severity = d.pop("test_severity")

        updated_at = d.pop("updated_at")

        model_compliance_rule = cls(
            description=description,
            masked=masked,
            test_category=test_category,
            test_desc=test_desc,
            test_number=test_number,
            test_rationale=test_rationale,
            test_severity=test_severity,
            updated_at=updated_at,
        )

        model_compliance_rule.additional_properties = d
        return model_compliance_rule

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
