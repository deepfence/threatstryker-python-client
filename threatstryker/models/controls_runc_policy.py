from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.controls_runc_policy_action import ControlsRuncPolicyAction
from ..models.controls_runc_policy_node_type import ControlsRuncPolicyNodeType

if TYPE_CHECKING:
    from ..models.controls_policy_alert_matcher import ControlsPolicyAlertMatcher


T = TypeVar("T", bound="ControlsRuncPolicy")


@_attrs_define
class ControlsRuncPolicy:
    """
    Attributes:
        action (ControlsRuncPolicyAction):
        count_limit (int):
        duration_count_limit_sec (int):
        matcher (ControlsPolicyAlertMatcher):
        node_type (ControlsRuncPolicyNodeType):
        policy_id (str):
        updated_at (int):
    """

    action: ControlsRuncPolicyAction
    count_limit: int
    duration_count_limit_sec: int
    matcher: "ControlsPolicyAlertMatcher"
    node_type: ControlsRuncPolicyNodeType
    policy_id: str
    updated_at: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        count_limit = self.count_limit

        duration_count_limit_sec = self.duration_count_limit_sec

        matcher = self.matcher.to_dict()

        node_type = self.node_type.value

        policy_id = self.policy_id

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "count_limit": count_limit,
                "duration_count_limit_sec": duration_count_limit_sec,
                "matcher": matcher,
                "node_type": node_type,
                "policy_id": policy_id,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.controls_policy_alert_matcher import ControlsPolicyAlertMatcher

        d = dict(src_dict)
        action = ControlsRuncPolicyAction(d.pop("action"))

        count_limit = d.pop("count_limit")

        duration_count_limit_sec = d.pop("duration_count_limit_sec")

        matcher = ControlsPolicyAlertMatcher.from_dict(d.pop("matcher"))

        node_type = ControlsRuncPolicyNodeType(d.pop("node_type"))

        policy_id = d.pop("policy_id")

        updated_at = d.pop("updated_at")

        controls_runc_policy = cls(
            action=action,
            count_limit=count_limit,
            duration_count_limit_sec=duration_count_limit_sec,
            matcher=matcher,
            node_type=node_type,
            policy_id=policy_id,
            updated_at=updated_at,
        )

        controls_runc_policy.additional_properties = d
        return controls_runc_policy

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
