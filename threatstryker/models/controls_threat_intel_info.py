from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ControlsThreatIntelInfo")


@_attrs_define
class ControlsThreatIntelInfo:
    """
    Example:
        {'cloud_posture_controls_hash': 'cloud_posture_controls_hash', 'cloud_posture_controls_url':
            'cloud_posture_controls_url', 'updated_at': 0, 'network_alert_rules_url': 'network_alert_rules_url',
            'ignored_alert_rule_ids': ['ignored_alert_rule_ids', 'ignored_alert_rule_ids'], 'internal_ips': ['internal_ips',
            'internal_ips'], 'secret_scanner_rules_hash': 'secret_scanner_rules_hash', 'secret_scanner_rules_url':
            'secret_scanner_rules_url', 'malware_scanner_rules_hash': 'malware_scanner_rules_hash',
            'malware_scanner_rules_url': 'malware_scanner_rules_url', 'rules_hash': 'rules_hash'}

    Attributes:
        cloud_posture_controls_hash (str):
        cloud_posture_controls_url (str):
        ignored_alert_rule_ids (Union[List[str], None]):
        internal_ips (Union[List[str], None]):
        malware_scanner_rules_hash (str):
        malware_scanner_rules_url (str):
        network_alert_rules_url (str):
        rules_hash (str):
        secret_scanner_rules_hash (str):
        secret_scanner_rules_url (str):
        updated_at (int):
    """

    cloud_posture_controls_hash: str
    cloud_posture_controls_url: str
    ignored_alert_rule_ids: Union[List[str], None]
    internal_ips: Union[List[str], None]
    malware_scanner_rules_hash: str
    malware_scanner_rules_url: str
    network_alert_rules_url: str
    rules_hash: str
    secret_scanner_rules_hash: str
    secret_scanner_rules_url: str
    updated_at: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cloud_posture_controls_hash = self.cloud_posture_controls_hash

        cloud_posture_controls_url = self.cloud_posture_controls_url

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

        malware_scanner_rules_hash = self.malware_scanner_rules_hash

        malware_scanner_rules_url = self.malware_scanner_rules_url

        network_alert_rules_url = self.network_alert_rules_url

        rules_hash = self.rules_hash

        secret_scanner_rules_hash = self.secret_scanner_rules_hash

        secret_scanner_rules_url = self.secret_scanner_rules_url

        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cloud_posture_controls_hash": cloud_posture_controls_hash,
                "cloud_posture_controls_url": cloud_posture_controls_url,
                "ignored_alert_rule_ids": ignored_alert_rule_ids,
                "internal_ips": internal_ips,
                "malware_scanner_rules_hash": malware_scanner_rules_hash,
                "malware_scanner_rules_url": malware_scanner_rules_url,
                "network_alert_rules_url": network_alert_rules_url,
                "rules_hash": rules_hash,
                "secret_scanner_rules_hash": secret_scanner_rules_hash,
                "secret_scanner_rules_url": secret_scanner_rules_url,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cloud_posture_controls_hash = d.pop("cloud_posture_controls_hash")

        cloud_posture_controls_url = d.pop("cloud_posture_controls_url")

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

        malware_scanner_rules_hash = d.pop("malware_scanner_rules_hash")

        malware_scanner_rules_url = d.pop("malware_scanner_rules_url")

        network_alert_rules_url = d.pop("network_alert_rules_url")

        rules_hash = d.pop("rules_hash")

        secret_scanner_rules_hash = d.pop("secret_scanner_rules_hash")

        secret_scanner_rules_url = d.pop("secret_scanner_rules_url")

        updated_at = d.pop("updated_at")

        controls_threat_intel_info = cls(
            cloud_posture_controls_hash=cloud_posture_controls_hash,
            cloud_posture_controls_url=cloud_posture_controls_url,
            ignored_alert_rule_ids=ignored_alert_rule_ids,
            internal_ips=internal_ips,
            malware_scanner_rules_hash=malware_scanner_rules_hash,
            malware_scanner_rules_url=malware_scanner_rules_url,
            network_alert_rules_url=network_alert_rules_url,
            rules_hash=rules_hash,
            secret_scanner_rules_hash=secret_scanner_rules_hash,
            secret_scanner_rules_url=secret_scanner_rules_url,
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
