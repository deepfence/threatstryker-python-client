from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.controls_policy_alert_matcher_fields_matcher import ControlsPolicyAlertMatcherFieldsMatcher


T = TypeVar("T", bound="ControlsPolicyAlertMatcher")


@_attrs_define
class ControlsPolicyAlertMatcher:
    """
    Example:
        {'fields_matcher': {'key': ['fields_matcher', 'fields_matcher']}}

    Attributes:
        fields_matcher (Optional[ControlsPolicyAlertMatcherFieldsMatcher]):
    """

    fields_matcher: Optional["ControlsPolicyAlertMatcherFieldsMatcher"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fields_matcher = self.fields_matcher.to_dict() if self.fields_matcher else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fields_matcher": fields_matcher,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.controls_policy_alert_matcher_fields_matcher import ControlsPolicyAlertMatcherFieldsMatcher

        d = src_dict.copy()
        _fields_matcher = d.pop("fields_matcher")
        fields_matcher: Optional[ControlsPolicyAlertMatcherFieldsMatcher]
        if _fields_matcher is None:
            fields_matcher = None
        else:
            fields_matcher = ControlsPolicyAlertMatcherFieldsMatcher.from_dict(_fields_matcher)

        controls_policy_alert_matcher = cls(
            fields_matcher=fields_matcher,
        )

        controls_policy_alert_matcher.additional_properties = d
        return controls_policy_alert_matcher

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
