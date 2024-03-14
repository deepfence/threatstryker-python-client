from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.controls_network_policy_action import ControlsNetworkPolicyAction
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.controls_policy_alert_matcher import ControlsPolicyAlertMatcher


T = TypeVar("T", bound="ControlsNetworkPolicy")


@_attrs_define
class ControlsNetworkPolicy:
    """
    Attributes:
        action (ControlsNetworkPolicyAction):
        count_limit (int):
        duration_count_limit_sec (int):
        duration_sec (int):
        matcher (ControlsPolicyAlertMatcher):
        policy_id (str):
        updated_at (int):
        uuid (Union[Unset, str]):
    """

    action: ControlsNetworkPolicyAction
    count_limit: int
    duration_count_limit_sec: int
    duration_sec: int
    matcher: "ControlsPolicyAlertMatcher"
    policy_id: str
    updated_at: int
    uuid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action = self.action.value

        count_limit = self.count_limit

        duration_count_limit_sec = self.duration_count_limit_sec

        duration_sec = self.duration_sec

        matcher = self.matcher.to_dict()

        policy_id = self.policy_id

        updated_at = self.updated_at

        uuid = self.uuid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "count_limit": count_limit,
                "duration_count_limit_sec": duration_count_limit_sec,
                "duration_sec": duration_sec,
                "matcher": matcher,
                "policy_id": policy_id,
                "updated_at": updated_at,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.controls_policy_alert_matcher import ControlsPolicyAlertMatcher

        d = src_dict.copy()
        action = ControlsNetworkPolicyAction(d.pop("action"))

        count_limit = d.pop("count_limit")

        duration_count_limit_sec = d.pop("duration_count_limit_sec")

        duration_sec = d.pop("duration_sec")

        matcher = ControlsPolicyAlertMatcher.from_dict(d.pop("matcher"))

        policy_id = d.pop("policy_id")

        updated_at = d.pop("updated_at")

        uuid = d.pop("uuid", UNSET)

        controls_network_policy = cls(
            action=action,
            count_limit=count_limit,
            duration_count_limit_sec=duration_count_limit_sec,
            duration_sec=duration_sec,
            matcher=matcher,
            policy_id=policy_id,
            updated_at=updated_at,
            uuid=uuid,
        )

        controls_network_policy.additional_properties = d
        return controls_network_policy

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
