from typing import Any, Dict, List, Optional, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelSecretScanResultRules")


@_attrs_define
class ModelSecretScanResultRules:
    """
    Example:
        {'rules': ['rules', 'rules']}

    Attributes:
        rules (Optional[List[str]]):
    """

    rules: Optional[List[str]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if self.rules is None:
            rules = None
        else:
            rules = self.rules

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rules": rules,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rules = cast(List[str], d.pop("rules"))

        model_secret_scan_result_rules = cls(
            rules=rules,
        )

        model_secret_scan_result_rules.additional_properties = d
        return model_secret_scan_result_rules

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
