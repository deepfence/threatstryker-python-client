from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ingesters_waf_rule_action import IngestersWAFRuleAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="IngestersWAFRule")


@_attrs_define
class IngestersWAFRule:
    """
    Example:
        {'remote_ip': 'remote_ip', 'executed_at': 0, 'remote_port': 6, 'action': 'block', 'host_name': 'host_name'}

    Attributes:
        action (IngestersWAFRuleAction):
        remote_ip (str):
        executed_at (Union[Unset, int]):
        host_name (Union[Unset, str]):
        remote_port (Union[Unset, int]):
    """

    action: IngestersWAFRuleAction
    remote_ip: str
    executed_at: Union[Unset, int] = UNSET
    host_name: Union[Unset, str] = UNSET
    remote_port: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action = self.action.value

        remote_ip = self.remote_ip

        executed_at = self.executed_at

        host_name = self.host_name

        remote_port = self.remote_port

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "remote_ip": remote_ip,
            }
        )
        if executed_at is not UNSET:
            field_dict["executed_at"] = executed_at
        if host_name is not UNSET:
            field_dict["host_name"] = host_name
        if remote_port is not UNSET:
            field_dict["remote_port"] = remote_port

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        action = IngestersWAFRuleAction(d.pop("action"))

        remote_ip = d.pop("remote_ip")

        executed_at = d.pop("executed_at", UNSET)

        host_name = d.pop("host_name", UNSET)

        remote_port = d.pop("remote_port", UNSET)

        ingesters_waf_rule = cls(
            action=action,
            remote_ip=remote_ip,
            executed_at=executed_at,
            host_name=host_name,
            remote_port=remote_port,
        )

        ingesters_waf_rule.additional_properties = d
        return ingesters_waf_rule

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
