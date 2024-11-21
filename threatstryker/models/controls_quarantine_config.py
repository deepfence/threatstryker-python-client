from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

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
        policies (Union[List['ControlsRuncPolicy'], None]):
        updated_at (int):
    """

    node_id: str
    policies: Union[List["ControlsRuncPolicy"], None]
    updated_at: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        node_id = self.node_id

        policies: Union[List[Dict[str, Any]], None]
        if isinstance(self.policies, list):
            policies = []
            for policies_type_0_item_data in self.policies:
                policies_type_0_item = policies_type_0_item_data.to_dict()
                policies.append(policies_type_0_item)

        else:
            policies = self.policies

        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node_id": node_id,
                "policies": policies,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.controls_runc_policy import ControlsRuncPolicy

        d = src_dict.copy()
        node_id = d.pop("node_id")

        def _parse_policies(data: object) -> Union[List["ControlsRuncPolicy"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                policies_type_0 = []
                _policies_type_0 = data
                for policies_type_0_item_data in _policies_type_0:
                    policies_type_0_item = ControlsRuncPolicy.from_dict(policies_type_0_item_data)

                    policies_type_0.append(policies_type_0_item)

                return policies_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ControlsRuncPolicy"], None], data)

        policies = _parse_policies(d.pop("policies"))

        updated_at = d.pop("updated_at")

        controls_quarantine_config = cls(
            node_id=node_id,
            policies=policies,
            updated_at=updated_at,
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
