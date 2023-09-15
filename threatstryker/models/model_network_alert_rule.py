from typing import Any, Dict, List, Optional, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelNetworkAlertRule")


@_attrs_define
class ModelNetworkAlertRule:
    """
    Example:
        {'rule_id': 'rule_id', 'severity': 'severity', 'summary': 'summary', 'signature_id': 6, 'updated_at': 1,
            'masked': True, 'techniques': ['techniques', 'techniques'], 'description': 'description', 'tactics': ['tactics',
            'tactics'], 'category': 'category', 'node_id': 'node_id', 'severity_score': 0.8008281904610115}

    Attributes:
        category (str):
        description (str):
        masked (bool):
        node_id (str):
        rule_id (str):
        severity (str):
        severity_score (float):
        signature_id (int):
        summary (str):
        updated_at (int):
        tactics (Optional[List[str]]):
        techniques (Optional[List[str]]):
    """

    category: str
    description: str
    masked: bool
    node_id: str
    rule_id: str
    severity: str
    severity_score: float
    signature_id: int
    summary: str
    updated_at: int
    tactics: Optional[List[str]]
    techniques: Optional[List[str]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category = self.category
        description = self.description
        masked = self.masked
        node_id = self.node_id
        rule_id = self.rule_id
        severity = self.severity
        severity_score = self.severity_score
        signature_id = self.signature_id
        summary = self.summary
        updated_at = self.updated_at
        if self.tactics is None:
            tactics = None
        else:
            tactics = self.tactics

        if self.techniques is None:
            techniques = None
        else:
            techniques = self.techniques

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "description": description,
                "masked": masked,
                "node_id": node_id,
                "rule_id": rule_id,
                "severity": severity,
                "severity_score": severity_score,
                "signature_id": signature_id,
                "summary": summary,
                "updated_at": updated_at,
                "tactics": tactics,
                "techniques": techniques,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        category = d.pop("category")

        description = d.pop("description")

        masked = d.pop("masked")

        node_id = d.pop("node_id")

        rule_id = d.pop("rule_id")

        severity = d.pop("severity")

        severity_score = d.pop("severity_score")

        signature_id = d.pop("signature_id")

        summary = d.pop("summary")

        updated_at = d.pop("updated_at")

        tactics = cast(List[str], d.pop("tactics"))

        techniques = cast(List[str], d.pop("techniques"))

        model_network_alert_rule = cls(
            category=category,
            description=description,
            masked=masked,
            node_id=node_id,
            rule_id=rule_id,
            severity=severity,
            severity_score=severity_score,
            signature_id=signature_id,
            summary=summary,
            updated_at=updated_at,
            tactics=tactics,
            techniques=techniques,
        )

        model_network_alert_rule.additional_properties = d
        return model_network_alert_rule

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
