from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelSecretRule")


@_attrs_define
class ModelSecretRule:
    """
    Attributes:
        level (str):
        masked (bool):
        payload (str):
        severity (str):
        summary (str):
        updated_at (int):
        part (Union[Unset, str]):
        rule_id (Union[Unset, str]):
        signature_to_match (Union[Unset, str]):
    """

    level: str
    masked: bool
    payload: str
    severity: str
    summary: str
    updated_at: int
    part: Union[Unset, str] = UNSET
    rule_id: Union[Unset, str] = UNSET
    signature_to_match: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        level = self.level

        masked = self.masked

        payload = self.payload

        severity = self.severity

        summary = self.summary

        updated_at = self.updated_at

        part = self.part

        rule_id = self.rule_id

        signature_to_match = self.signature_to_match

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "level": level,
                "masked": masked,
                "payload": payload,
                "severity": severity,
                "summary": summary,
                "updated_at": updated_at,
            }
        )
        if part is not UNSET:
            field_dict["part"] = part
        if rule_id is not UNSET:
            field_dict["rule_id"] = rule_id
        if signature_to_match is not UNSET:
            field_dict["signature_to_match"] = signature_to_match

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        level = d.pop("level")

        masked = d.pop("masked")

        payload = d.pop("payload")

        severity = d.pop("severity")

        summary = d.pop("summary")

        updated_at = d.pop("updated_at")

        part = d.pop("part", UNSET)

        rule_id = d.pop("rule_id", UNSET)

        signature_to_match = d.pop("signature_to_match", UNSET)

        model_secret_rule = cls(
            level=level,
            masked=masked,
            payload=payload,
            severity=severity,
            summary=summary,
            updated_at=updated_at,
            part=part,
            rule_id=rule_id,
            signature_to_match=signature_to_match,
        )

        model_secret_rule.additional_properties = d
        return model_secret_rule

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
