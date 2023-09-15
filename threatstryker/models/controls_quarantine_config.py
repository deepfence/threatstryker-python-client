from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.controls_runc_policy import ControlsRuncPolicy


T = TypeVar("T", bound="ControlsQuarantineConfig")


@_attrs_define
class ControlsQuarantineConfig:
    """
    Example:
        {'updated_at': 5, 'policies': [{'node_type': 'container', 'policy_id': 'policy_id', 'updated_at': 1,
            'count_limit': 0, 'action': 'restart', 'duration_count_limit_sec': 6, 'matcher': {'fields_matcher': {'key':
            ['fields_matcher', 'fields_matcher']}}}, {'node_type': 'container', 'policy_id': 'policy_id', 'updated_at': 1,
            'count_limit': 0, 'action': 'restart', 'duration_count_limit_sec': 6, 'matcher': {'fields_matcher': {'key':
            ['fields_matcher', 'fields_matcher']}}}], 'node_id': 'node_id'}

    Attributes:
        node_id (str):
        updated_at (int):
        policies (Optional[List['ControlsRuncPolicy']]):
    """

    node_id: str
    updated_at: int
    policies: Optional[List["ControlsRuncPolicy"]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        node_id = self.node_id
        updated_at = self.updated_at
        if self.policies is None:
            policies = None
        else:
            policies = []
            for policies_item_data in self.policies:
                policies_item = policies_item_data.to_dict()

                policies.append(policies_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node_id": node_id,
                "updated_at": updated_at,
                "policies": policies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.controls_runc_policy import ControlsRuncPolicy

        d = src_dict.copy()
        node_id = d.pop("node_id")

        updated_at = d.pop("updated_at")

        policies = []
        _policies = d.pop("policies")
        for policies_item_data in _policies or []:
            policies_item = ControlsRuncPolicy.from_dict(policies_item_data)

            policies.append(policies_item)

        controls_quarantine_config = cls(
            node_id=node_id,
            updated_at=updated_at,
            policies=policies,
        )

        controls_quarantine_config.additional_properties = d
        return controls_quarantine_config

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
