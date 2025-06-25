from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelNetworkAlertRule")


@_attrs_define
class ModelNetworkAlertRule:
    """
    Attributes:
        category (str):
        description (str):
        masked (bool):
        node_id (str):
        payload (str):
        rule_id (str):
        severity (str):
        summary (str):
        tactics (Union[None, list[str]]):
        techniques (Union[None, list[str]]):
        updated_at (int):
    """

    category: str
    description: str
    masked: bool
    node_id: str
    payload: str
    rule_id: str
    severity: str
    summary: str
    tactics: Union[None, list[str]]
    techniques: Union[None, list[str]]
    updated_at: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        description = self.description

        masked = self.masked

        node_id = self.node_id

        payload = self.payload

        rule_id = self.rule_id

        severity = self.severity

        summary = self.summary

        tactics: Union[None, list[str]]
        if isinstance(self.tactics, list):
            tactics = self.tactics

        else:
            tactics = self.tactics

        techniques: Union[None, list[str]]
        if isinstance(self.techniques, list):
            techniques = self.techniques

        else:
            techniques = self.techniques

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "description": description,
                "masked": masked,
                "node_id": node_id,
                "payload": payload,
                "rule_id": rule_id,
                "severity": severity,
                "summary": summary,
                "tactics": tactics,
                "techniques": techniques,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category")

        description = d.pop("description")

        masked = d.pop("masked")

        node_id = d.pop("node_id")

        payload = d.pop("payload")

        rule_id = d.pop("rule_id")

        severity = d.pop("severity")

        summary = d.pop("summary")

        def _parse_tactics(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tactics_type_0 = cast(list[str], data)

                return tactics_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        tactics = _parse_tactics(d.pop("tactics"))

        def _parse_techniques(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                techniques_type_0 = cast(list[str], data)

                return techniques_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        techniques = _parse_techniques(d.pop("techniques"))

        updated_at = d.pop("updated_at")

        model_network_alert_rule = cls(
            category=category,
            description=description,
            masked=masked,
            node_id=node_id,
            payload=payload,
            rule_id=rule_id,
            severity=severity,
            summary=summary,
            tactics=tactics,
            techniques=techniques,
            updated_at=updated_at,
        )

        model_network_alert_rule.additional_properties = d
        return model_network_alert_rule

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
