from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.controls_network_tracer_config_mode import ControlsNetworkTracerConfigMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.controls_network_rules import ControlsNetworkRules


T = TypeVar("T", bound="ControlsNetworkTracerConfig")


@_attrs_define
class ControlsNetworkTracerConfig:
    """
    Example:
        {'mode': 'all', 'process_names': ['process_names', 'process_names'], 'tcp_rules': {'inbound': ['inbound',
            'inbound'], 'outbound': ['outbound', 'outbound']}, 'http_rules': {'inbound': ['inbound', 'inbound'], 'outbound':
            ['outbound', 'outbound']}, 'updated_at': 0, 'ignored_rule_ids': ['ignored_rule_ids', 'ignored_rule_ids'],
            'https_rules': {'inbound': ['inbound', 'inbound'], 'outbound': ['outbound', 'outbound']}, 'node_id': 'node_id'}

    Attributes:
        http_rules (ControlsNetworkRules):  Example: {'inbound': ['inbound', 'inbound'], 'outbound': ['outbound',
            'outbound']}.
        https_rules (ControlsNetworkRules):  Example: {'inbound': ['inbound', 'inbound'], 'outbound': ['outbound',
            'outbound']}.
        mode (ControlsNetworkTracerConfigMode):
        node_id (str):
        tcp_rules (ControlsNetworkRules):  Example: {'inbound': ['inbound', 'inbound'], 'outbound': ['outbound',
            'outbound']}.
        updated_at (int):
        ignored_rule_ids (Union[Unset, None, List[str]]):
        process_names (Optional[List[str]]):
    """

    http_rules: "ControlsNetworkRules"
    https_rules: "ControlsNetworkRules"
    mode: ControlsNetworkTracerConfigMode
    node_id: str
    tcp_rules: "ControlsNetworkRules"
    updated_at: int
    process_names: Optional[List[str]]
    ignored_rule_ids: Union[Unset, None, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        http_rules = self.http_rules.to_dict()

        https_rules = self.https_rules.to_dict()

        mode = self.mode.value

        node_id = self.node_id
        tcp_rules = self.tcp_rules.to_dict()

        updated_at = self.updated_at
        ignored_rule_ids: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.ignored_rule_ids, Unset):
            if self.ignored_rule_ids is None:
                ignored_rule_ids = None
            else:
                ignored_rule_ids = self.ignored_rule_ids

        if self.process_names is None:
            process_names = None
        else:
            process_names = self.process_names

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "http_rules": http_rules,
                "https_rules": https_rules,
                "mode": mode,
                "node_id": node_id,
                "tcp_rules": tcp_rules,
                "updated_at": updated_at,
                "process_names": process_names,
            }
        )
        if ignored_rule_ids is not UNSET:
            field_dict["ignored_rule_ids"] = ignored_rule_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.controls_network_rules import ControlsNetworkRules

        d = src_dict.copy()
        http_rules = ControlsNetworkRules.from_dict(d.pop("http_rules"))

        https_rules = ControlsNetworkRules.from_dict(d.pop("https_rules"))

        mode = ControlsNetworkTracerConfigMode(d.pop("mode"))

        node_id = d.pop("node_id")

        tcp_rules = ControlsNetworkRules.from_dict(d.pop("tcp_rules"))

        updated_at = d.pop("updated_at")

        ignored_rule_ids = cast(List[str], d.pop("ignored_rule_ids", UNSET))

        process_names = cast(List[str], d.pop("process_names"))

        controls_network_tracer_config = cls(
            http_rules=http_rules,
            https_rules=https_rules,
            mode=mode,
            node_id=node_id,
            tcp_rules=tcp_rules,
            updated_at=updated_at,
            ignored_rule_ids=ignored_rule_ids,
            process_names=process_names,
        )

        controls_network_tracer_config.additional_properties = d
        return controls_network_tracer_config

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
