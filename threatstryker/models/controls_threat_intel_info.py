from typing import Any, Dict, List, Optional, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ControlsThreatIntelInfo")


@_attrs_define
class ControlsThreatIntelInfo:
    """
    Example:
        {'updated_at': 0, 'network_alert_rules_url': 'network_alert_rules_url', 'ignored_alert_rule_ids':
            ['ignored_alert_rule_ids', 'ignored_alert_rule_ids'], 'internal_ips': ['internal_ips', 'internal_ips'],
            'rules_hash': 'rules_hash'}

    Attributes:
        network_alert_rules_url (str):
        rules_hash (str):
        updated_at (int):
        ignored_alert_rule_ids (Optional[List[str]]):
        internal_ips (Optional[List[str]]):
    """

    network_alert_rules_url: str
    rules_hash: str
    updated_at: int
    ignored_alert_rule_ids: Optional[List[str]]
    internal_ips: Optional[List[str]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        network_alert_rules_url = self.network_alert_rules_url
        rules_hash = self.rules_hash
        updated_at = self.updated_at
        if self.ignored_alert_rule_ids is None:
            ignored_alert_rule_ids = None
        else:
            ignored_alert_rule_ids = self.ignored_alert_rule_ids

        if self.internal_ips is None:
            internal_ips = None
        else:
            internal_ips = self.internal_ips

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "network_alert_rules_url": network_alert_rules_url,
                "rules_hash": rules_hash,
                "updated_at": updated_at,
                "ignored_alert_rule_ids": ignored_alert_rule_ids,
                "internal_ips": internal_ips,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        network_alert_rules_url = d.pop("network_alert_rules_url")

        rules_hash = d.pop("rules_hash")

        updated_at = d.pop("updated_at")

        ignored_alert_rule_ids = cast(List[str], d.pop("ignored_alert_rule_ids"))

        internal_ips = cast(List[str], d.pop("internal_ips"))

        controls_threat_intel_info = cls(
            network_alert_rules_url=network_alert_rules_url,
            rules_hash=rules_hash,
            updated_at=updated_at,
            ignored_alert_rule_ids=ignored_alert_rule_ids,
            internal_ips=internal_ips,
        )

        controls_threat_intel_info.additional_properties = d
        return controls_threat_intel_info

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
