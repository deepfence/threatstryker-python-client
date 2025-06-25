from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.controls_runc_policy import ControlsRuncPolicy


T = TypeVar("T", bound="ControlsQuarantineConfig")


@_attrs_define
class ControlsQuarantineConfig:
    """
    Attributes:
        node_id (str):
        policies (Union[None, list['ControlsRuncPolicy']]):
        updated_at (int):
    """

    node_id: str
    policies: Union[None, list["ControlsRuncPolicy"]]
    updated_at: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_id = self.node_id

        policies: Union[None, list[dict[str, Any]]]
        if isinstance(self.policies, list):
            policies = []
            for policies_type_0_item_data in self.policies:
                policies_type_0_item = policies_type_0_item_data.to_dict()
                policies.append(policies_type_0_item)

        else:
            policies = self.policies

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.controls_runc_policy import ControlsRuncPolicy

        d = dict(src_dict)
        node_id = d.pop("node_id")

        def _parse_policies(data: object) -> Union[None, list["ControlsRuncPolicy"]]:
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
            return cast(Union[None, list["ControlsRuncPolicy"]], data)

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
