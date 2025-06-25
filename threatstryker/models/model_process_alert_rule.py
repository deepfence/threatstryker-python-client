from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelProcessAlertRule")


@_attrs_define
class ModelProcessAlertRule:
    """
    Attributes:
        anomaly (Union[Unset, str]):
        category (Union[Unset, str]):
        rule_id (Union[Unset, str]):
        severity (Union[Unset, str]):
        summary (Union[Unset, str]):
        tactics (Union[None, Unset, list[str]]):
        techniques (Union[None, Unset, list[str]]):
    """

    anomaly: Union[Unset, str] = UNSET
    category: Union[Unset, str] = UNSET
    rule_id: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    tactics: Union[None, Unset, list[str]] = UNSET
    techniques: Union[None, Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        anomaly = self.anomaly

        category = self.category

        rule_id = self.rule_id

        severity = self.severity

        summary = self.summary

        tactics: Union[None, Unset, list[str]]
        if isinstance(self.tactics, Unset):
            tactics = UNSET
        elif isinstance(self.tactics, list):
            tactics = self.tactics

        else:
            tactics = self.tactics

        techniques: Union[None, Unset, list[str]]
        if isinstance(self.techniques, Unset):
            techniques = UNSET
        elif isinstance(self.techniques, list):
            techniques = self.techniques

        else:
            techniques = self.techniques

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if anomaly is not UNSET:
            field_dict["anomaly"] = anomaly
        if category is not UNSET:
            field_dict["category"] = category
        if rule_id is not UNSET:
            field_dict["rule_id"] = rule_id
        if severity is not UNSET:
            field_dict["severity"] = severity
        if summary is not UNSET:
            field_dict["summary"] = summary
        if tactics is not UNSET:
            field_dict["tactics"] = tactics
        if techniques is not UNSET:
            field_dict["techniques"] = techniques

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        anomaly = d.pop("anomaly", UNSET)

        category = d.pop("category", UNSET)

        rule_id = d.pop("rule_id", UNSET)

        severity = d.pop("severity", UNSET)

        summary = d.pop("summary", UNSET)

        def _parse_tactics(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tactics_type_0 = cast(list[str], data)

                return tactics_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        tactics = _parse_tactics(d.pop("tactics", UNSET))

        def _parse_techniques(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                techniques_type_0 = cast(list[str], data)

                return techniques_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        techniques = _parse_techniques(d.pop("techniques", UNSET))

        model_process_alert_rule = cls(
            anomaly=anomaly,
            category=category,
            rule_id=rule_id,
            severity=severity,
            summary=summary,
            tactics=tactics,
            techniques=techniques,
        )

        model_process_alert_rule.additional_properties = d
        return model_process_alert_rule

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
