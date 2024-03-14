from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.controls_network_policy import ControlsNetworkPolicy


T = TypeVar("T", bound="ControlsPolicyFilterConfig")


@_attrs_define
class ControlsPolicyFilterConfig:
    """
    Attributes:
        ignored_remote_ips (Union[List[str], None]):
        node_id (str):
        policies (Union[List['ControlsNetworkPolicy'], None]):
        updated_at (int):
        use_waf (bool):
        enable_policy_logs (Union[Unset, bool]):
    """

    ignored_remote_ips: Union[List[str], None]
    node_id: str
    policies: Union[List["ControlsNetworkPolicy"], None]
    updated_at: int
    use_waf: bool
    enable_policy_logs: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ignored_remote_ips: Union[List[str], None]
        if isinstance(self.ignored_remote_ips, list):
            ignored_remote_ips = self.ignored_remote_ips

        else:
            ignored_remote_ips = self.ignored_remote_ips

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

        use_waf = self.use_waf

        enable_policy_logs = self.enable_policy_logs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ignored_remote_ips": ignored_remote_ips,
                "node_id": node_id,
                "policies": policies,
                "updated_at": updated_at,
                "use_waf": use_waf,
            }
        )
        if enable_policy_logs is not UNSET:
            field_dict["enable_policy_logs"] = enable_policy_logs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.controls_network_policy import ControlsNetworkPolicy

        d = src_dict.copy()

        def _parse_ignored_remote_ips(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ignored_remote_ips_type_0 = cast(List[str], data)

                return ignored_remote_ips_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

        ignored_remote_ips = _parse_ignored_remote_ips(d.pop("ignored_remote_ips"))

        node_id = d.pop("node_id")

        def _parse_policies(data: object) -> Union[List["ControlsNetworkPolicy"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                policies_type_0 = []
                _policies_type_0 = data
                for policies_type_0_item_data in _policies_type_0:
                    policies_type_0_item = ControlsNetworkPolicy.from_dict(policies_type_0_item_data)

                    policies_type_0.append(policies_type_0_item)

                return policies_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ControlsNetworkPolicy"], None], data)

        policies = _parse_policies(d.pop("policies"))

        updated_at = d.pop("updated_at")

        use_waf = d.pop("use_waf")

        enable_policy_logs = d.pop("enable_policy_logs", UNSET)

        controls_policy_filter_config = cls(
            ignored_remote_ips=ignored_remote_ips,
            node_id=node_id,
            policies=policies,
            updated_at=updated_at,
            use_waf=use_waf,
            enable_policy_logs=enable_policy_logs,
        )

        controls_policy_filter_config.additional_properties = d
        return controls_policy_filter_config

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
