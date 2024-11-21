from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.controls_policy_alert_matcher_fields_matcher_type_0 import (
        ControlsPolicyAlertMatcherFieldsMatcherType0,
    )


T = TypeVar("T", bound="ControlsPolicyAlertMatcher")


@_attrs_define
class ControlsPolicyAlertMatcher:
    """
    Example:
        {'fields_matcher': {'key': ['fields_matcher', 'fields_matcher']}}

    Attributes:
        fields_matcher (Union['ControlsPolicyAlertMatcherFieldsMatcherType0', None]):
    """

    fields_matcher: Union["ControlsPolicyAlertMatcherFieldsMatcherType0", None]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.controls_policy_alert_matcher_fields_matcher_type_0 import (
            ControlsPolicyAlertMatcherFieldsMatcherType0,
        )

        fields_matcher: Union[Dict[str, Any], None]
        if isinstance(self.fields_matcher, ControlsPolicyAlertMatcherFieldsMatcherType0):
            fields_matcher = self.fields_matcher.to_dict()
        else:
            fields_matcher = self.fields_matcher

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
        from ..models.controls_policy_alert_matcher_fields_matcher_type_0 import (
            ControlsPolicyAlertMatcherFieldsMatcherType0,
        )

        d = src_dict.copy()

        def _parse_fields_matcher(data: object) -> Union["ControlsPolicyAlertMatcherFieldsMatcherType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                fields_matcher_type_0 = ControlsPolicyAlertMatcherFieldsMatcherType0.from_dict(data)

                return fields_matcher_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ControlsPolicyAlertMatcherFieldsMatcherType0", None], data)

        fields_matcher = _parse_fields_matcher(d.pop("fields_matcher"))

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
