import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelDatabaseInfoResponse")


@_attrs_define
class ModelDatabaseInfoResponse:
    """
    Attributes:
        malware_rules_updated_at (Union[Unset, datetime.datetime]):
        network_alert_rules_updated_at (Union[Unset, datetime.datetime]):
        posture_controls_updated_at (Union[Unset, datetime.datetime]):
        secrets_rules_updated_at (Union[Unset, datetime.datetime]):
        vulnerability_db_updated_at (Union[Unset, datetime.datetime]):
    """

    malware_rules_updated_at: Union[Unset, datetime.datetime] = UNSET
    network_alert_rules_updated_at: Union[Unset, datetime.datetime] = UNSET
    posture_controls_updated_at: Union[Unset, datetime.datetime] = UNSET
    secrets_rules_updated_at: Union[Unset, datetime.datetime] = UNSET
    vulnerability_db_updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        malware_rules_updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.malware_rules_updated_at, Unset):
            malware_rules_updated_at = self.malware_rules_updated_at.isoformat()

        network_alert_rules_updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.network_alert_rules_updated_at, Unset):
            network_alert_rules_updated_at = self.network_alert_rules_updated_at.isoformat()

        posture_controls_updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.posture_controls_updated_at, Unset):
            posture_controls_updated_at = self.posture_controls_updated_at.isoformat()

        secrets_rules_updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.secrets_rules_updated_at, Unset):
            secrets_rules_updated_at = self.secrets_rules_updated_at.isoformat()

        vulnerability_db_updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.vulnerability_db_updated_at, Unset):
            vulnerability_db_updated_at = self.vulnerability_db_updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if malware_rules_updated_at is not UNSET:
            field_dict["malware_rules_updated_at"] = malware_rules_updated_at
        if network_alert_rules_updated_at is not UNSET:
            field_dict["network_alert_rules_updated_at"] = network_alert_rules_updated_at
        if posture_controls_updated_at is not UNSET:
            field_dict["posture_controls_updated_at"] = posture_controls_updated_at
        if secrets_rules_updated_at is not UNSET:
            field_dict["secrets_rules_updated_at"] = secrets_rules_updated_at
        if vulnerability_db_updated_at is not UNSET:
            field_dict["vulnerability_db_updated_at"] = vulnerability_db_updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _malware_rules_updated_at = d.pop("malware_rules_updated_at", UNSET)
        malware_rules_updated_at: Union[Unset, datetime.datetime]
        if isinstance(_malware_rules_updated_at, Unset):
            malware_rules_updated_at = UNSET
        else:
            malware_rules_updated_at = isoparse(_malware_rules_updated_at)

        _network_alert_rules_updated_at = d.pop("network_alert_rules_updated_at", UNSET)
        network_alert_rules_updated_at: Union[Unset, datetime.datetime]
        if isinstance(_network_alert_rules_updated_at, Unset):
            network_alert_rules_updated_at = UNSET
        else:
            network_alert_rules_updated_at = isoparse(_network_alert_rules_updated_at)

        _posture_controls_updated_at = d.pop("posture_controls_updated_at", UNSET)
        posture_controls_updated_at: Union[Unset, datetime.datetime]
        if isinstance(_posture_controls_updated_at, Unset):
            posture_controls_updated_at = UNSET
        else:
            posture_controls_updated_at = isoparse(_posture_controls_updated_at)

        _secrets_rules_updated_at = d.pop("secrets_rules_updated_at", UNSET)
        secrets_rules_updated_at: Union[Unset, datetime.datetime]
        if isinstance(_secrets_rules_updated_at, Unset):
            secrets_rules_updated_at = UNSET
        else:
            secrets_rules_updated_at = isoparse(_secrets_rules_updated_at)

        _vulnerability_db_updated_at = d.pop("vulnerability_db_updated_at", UNSET)
        vulnerability_db_updated_at: Union[Unset, datetime.datetime]
        if isinstance(_vulnerability_db_updated_at, Unset):
            vulnerability_db_updated_at = UNSET
        else:
            vulnerability_db_updated_at = isoparse(_vulnerability_db_updated_at)

        model_database_info_response = cls(
            malware_rules_updated_at=malware_rules_updated_at,
            network_alert_rules_updated_at=network_alert_rules_updated_at,
            posture_controls_updated_at=posture_controls_updated_at,
            secrets_rules_updated_at=secrets_rules_updated_at,
            vulnerability_db_updated_at=vulnerability_db_updated_at,
        )

        model_database_info_response.additional_properties = d
        return model_database_info_response

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
