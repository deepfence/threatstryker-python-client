from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ControlsThreatIntelInfo")


@_attrs_define
class ControlsThreatIntelInfo:
    """
    Attributes:
        ignored_alert_rule_ids (Union[List[str], None]):
        internal_ips (Union[List[str], None]):
        network_alert_rules_url (str):
        rules_hash (str):
        updated_at (int):
    """

    ignored_alert_rule_ids: Union[List[str], None]
    internal_ips: Union[List[str], None]
    network_alert_rules_url: str
    rules_hash: str
    updated_at: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ignored_alert_rule_ids: Union[List[str], None]
        if isinstance(self.ignored_alert_rule_ids, list):
            ignored_alert_rule_ids = self.ignored_alert_rule_ids

        else:
            ignored_alert_rule_ids = self.ignored_alert_rule_ids

        internal_ips: Union[List[str], None]
        if isinstance(self.internal_ips, list):
            internal_ips = self.internal_ips

        else:
            internal_ips = self.internal_ips

        network_alert_rules_url = self.network_alert_rules_url

        rules_hash = self.rules_hash

        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ignored_alert_rule_ids": ignored_alert_rule_ids,
                "internal_ips": internal_ips,
                "network_alert_rules_url": network_alert_rules_url,
                "rules_hash": rules_hash,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_ignored_alert_rule_ids(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ignored_alert_rule_ids_type_0 = cast(List[str], data)

                return ignored_alert_rule_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

        ignored_alert_rule_ids = _parse_ignored_alert_rule_ids(d.pop("ignored_alert_rule_ids"))

        def _parse_internal_ips(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                internal_ips_type_0 = cast(List[str], data)

                return internal_ips_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

        internal_ips = _parse_internal_ips(d.pop("internal_ips"))

        network_alert_rules_url = d.pop("network_alert_rules_url")

        rules_hash = d.pop("rules_hash")

        updated_at = d.pop("updated_at")

        controls_threat_intel_info = cls(
            ignored_alert_rule_ids=ignored_alert_rule_ids,
            internal_ips=internal_ips,
            network_alert_rules_url=network_alert_rules_url,
            rules_hash=rules_hash,
            updated_at=updated_at,
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
