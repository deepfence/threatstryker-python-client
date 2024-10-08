from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.setting_setting_update_request_key import SettingSettingUpdateRequestKey

T = TypeVar("T", bound="SettingSettingUpdateRequest")


@_attrs_define
class SettingSettingUpdateRequest:
    """
    Attributes:
        key (SettingSettingUpdateRequestKey):
        value (str):
    """

    key: SettingSettingUpdateRequestKey
    value: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key.value

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = SettingSettingUpdateRequestKey(d.pop("key"))

        value = d.pop("value")

        setting_setting_update_request = cls(
            key=key,
            value=value,
        )

        setting_setting_update_request.additional_properties = d
        return setting_setting_update_request

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
