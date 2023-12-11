from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelProcessAlertRule")


@_attrs_define
class ModelProcessAlertRule:
    """
    Example:
        {'rule_id': 'rule_id', 'severity': 'severity', 'summary': 'summary', 'anomaly': 'anomaly', 'event_type':
            'event_type', 'techniques': ['techniques', 'techniques'], 'resource_type': 'resource_type', 'tactics':
            ['tactics', 'tactics'], 'category': 'category', 'type': 'type'}

    Attributes:
        anomaly (Union[Unset, str]):
        category (Union[Unset, str]):
        event_type (Union[Unset, str]):
        resource_type (Union[Unset, str]):
        rule_id (Union[Unset, str]):
        severity (Union[Unset, str]):
        summary (Union[Unset, str]):
        tactics (Union[Unset, None, List[str]]):
        techniques (Union[Unset, None, List[str]]):
        type (Union[Unset, str]):
    """

    anomaly: Union[Unset, str] = UNSET
    category: Union[Unset, str] = UNSET
    event_type: Union[Unset, str] = UNSET
    resource_type: Union[Unset, str] = UNSET
    rule_id: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    tactics: Union[Unset, None, List[str]] = UNSET
    techniques: Union[Unset, None, List[str]] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        anomaly = self.anomaly
        category = self.category
        event_type = self.event_type
        resource_type = self.resource_type
        rule_id = self.rule_id
        severity = self.severity
        summary = self.summary
        tactics: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.tactics, Unset):
            if self.tactics is None:
                tactics = None
            else:
                tactics = self.tactics

        techniques: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.techniques, Unset):
            if self.techniques is None:
                techniques = None
            else:
                techniques = self.techniques

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if anomaly is not UNSET:
            field_dict["anomaly"] = anomaly
        if category is not UNSET:
            field_dict["category"] = category
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if resource_type is not UNSET:
            field_dict["resource_type"] = resource_type
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
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        anomaly = d.pop("anomaly", UNSET)

        category = d.pop("category", UNSET)

        event_type = d.pop("event_type", UNSET)

        resource_type = d.pop("resource_type", UNSET)

        rule_id = d.pop("rule_id", UNSET)

        severity = d.pop("severity", UNSET)

        summary = d.pop("summary", UNSET)

        tactics = cast(List[str], d.pop("tactics", UNSET))

        techniques = cast(List[str], d.pop("techniques", UNSET))

        type = d.pop("type", UNSET)

        model_process_alert_rule = cls(
            anomaly=anomaly,
            category=category,
            event_type=event_type,
            resource_type=resource_type,
            rule_id=rule_id,
            severity=severity,
            summary=summary,
            tactics=tactics,
            techniques=techniques,
            type=type,
        )

        model_process_alert_rule.additional_properties = d
        return model_process_alert_rule

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
