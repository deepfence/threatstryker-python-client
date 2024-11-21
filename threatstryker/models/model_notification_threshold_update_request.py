from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelNotificationThresholdUpdateRequest")


@_attrs_define
class ModelNotificationThresholdUpdateRequest:
    """
    Example:
        {'notification_threshold_percentage': 0}

    Attributes:
        notification_threshold_percentage (int):
    """

    notification_threshold_percentage: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        notification_threshold_percentage = self.notification_threshold_percentage

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "notification_threshold_percentage": notification_threshold_percentage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        notification_threshold_percentage = d.pop("notification_threshold_percentage")

        model_notification_threshold_update_request = cls(
            notification_threshold_percentage=notification_threshold_percentage,
        )

        model_notification_threshold_update_request.additional_properties = d
        return model_notification_threshold_update_request

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
