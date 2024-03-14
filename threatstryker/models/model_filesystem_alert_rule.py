from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelFilesystemAlertRule")


@_attrs_define
class ModelFilesystemAlertRule:
    """
    Attributes:
        anomaly (Union[Unset, str]):
        category (Union[Unset, str]):
        rule_id (Union[Unset, str]):
        severity (Union[Unset, str]):
        summary (Union[Unset, str]):
        tactics (Union[List[str], None, Unset]):
        techniques (Union[List[str], None, Unset]):
    """

    anomaly: Union[Unset, str] = UNSET
    category: Union[Unset, str] = UNSET
    rule_id: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    tactics: Union[List[str], None, Unset] = UNSET
    techniques: Union[List[str], None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        anomaly = self.anomaly

        category = self.category

        rule_id = self.rule_id

        severity = self.severity

        summary = self.summary

        tactics: Union[List[str], None, Unset]
        if isinstance(self.tactics, Unset):
            tactics = UNSET
        elif isinstance(self.tactics, list):
            tactics = self.tactics

        else:
            tactics = self.tactics

        techniques: Union[List[str], None, Unset]
        if isinstance(self.techniques, Unset):
            techniques = UNSET
        elif isinstance(self.techniques, list):
            techniques = self.techniques

        else:
            techniques = self.techniques

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        anomaly = d.pop("anomaly", UNSET)

        category = d.pop("category", UNSET)

        rule_id = d.pop("rule_id", UNSET)

        severity = d.pop("severity", UNSET)

        summary = d.pop("summary", UNSET)

        def _parse_tactics(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tactics_type_0 = cast(List[str], data)

                return tactics_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        tactics = _parse_tactics(d.pop("tactics", UNSET))

        def _parse_techniques(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                techniques_type_0 = cast(List[str], data)

                return techniques_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        techniques = _parse_techniques(d.pop("techniques", UNSET))

        model_filesystem_alert_rule = cls(
            anomaly=anomaly,
            category=category,
            rule_id=rule_id,
            severity=severity,
            summary=summary,
            tactics=tactics,
            techniques=techniques,
        )

        model_filesystem_alert_rule.additional_properties = d
        return model_filesystem_alert_rule

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
