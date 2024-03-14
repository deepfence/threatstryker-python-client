from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

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
    Attributes:
        http_rules (ControlsNetworkRules):
        https_rules (ControlsNetworkRules):
        mode (ControlsNetworkTracerConfigMode):
        node_id (str):
        process_names (Union[List[str], None]):
        tcp_rules (ControlsNetworkRules):
        updated_at (int):
        ignored_rule_ids (Union[List[str], None, Unset]):
    """

    http_rules: "ControlsNetworkRules"
    https_rules: "ControlsNetworkRules"
    mode: ControlsNetworkTracerConfigMode
    node_id: str
    process_names: Union[List[str], None]
    tcp_rules: "ControlsNetworkRules"
    updated_at: int
    ignored_rule_ids: Union[List[str], None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        http_rules = self.http_rules.to_dict()

        https_rules = self.https_rules.to_dict()

        mode = self.mode.value

        node_id = self.node_id

        process_names: Union[List[str], None]
        if isinstance(self.process_names, list):
            process_names = self.process_names

        else:
            process_names = self.process_names

        tcp_rules = self.tcp_rules.to_dict()

        updated_at = self.updated_at

        ignored_rule_ids: Union[List[str], None, Unset]
        if isinstance(self.ignored_rule_ids, Unset):
            ignored_rule_ids = UNSET
        elif isinstance(self.ignored_rule_ids, list):
            ignored_rule_ids = self.ignored_rule_ids

        else:
            ignored_rule_ids = self.ignored_rule_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "http_rules": http_rules,
                "https_rules": https_rules,
                "mode": mode,
                "node_id": node_id,
                "process_names": process_names,
                "tcp_rules": tcp_rules,
                "updated_at": updated_at,
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

        def _parse_process_names(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                process_names_type_0 = cast(List[str], data)

                return process_names_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

        process_names = _parse_process_names(d.pop("process_names"))

        tcp_rules = ControlsNetworkRules.from_dict(d.pop("tcp_rules"))

        updated_at = d.pop("updated_at")

        def _parse_ignored_rule_ids(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ignored_rule_ids_type_0 = cast(List[str], data)

                return ignored_rule_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        ignored_rule_ids = _parse_ignored_rule_ids(d.pop("ignored_rule_ids", UNSET))

        controls_network_tracer_config = cls(
            http_rules=http_rules,
            https_rules=https_rules,
            mode=mode,
            node_id=node_id,
            process_names=process_names,
            tcp_rules=tcp_rules,
            updated_at=updated_at,
            ignored_rule_ids=ignored_rule_ids,
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
