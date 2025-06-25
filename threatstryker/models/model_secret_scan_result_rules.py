from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelSecretScanResultRules")


@_attrs_define
class ModelSecretScanResultRules:
    """
    Attributes:
        rules (Union[None, list[str]]):
    """

    rules: Union[None, list[str]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rules: Union[None, list[str]]
        if isinstance(self.rules, list):
            rules = self.rules

        else:
            rules = self.rules

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rules": rules,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_rules(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rules_type_0 = cast(list[str], data)

                return rules_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        rules = _parse_rules(d.pop("rules"))

        model_secret_scan_result_rules = cls(
            rules=rules,
        )

        model_secret_scan_result_rules.additional_properties = d
        return model_secret_scan_result_rules

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
