from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ingesters_secret_match import IngestersSecretMatch
    from ..models.ingesters_secret_rule import IngestersSecretRule
    from ..models.ingesters_secret_severity import IngestersSecretSeverity


T = TypeVar("T", bound="IngestersSecret")


@_attrs_define
class IngestersSecret:
    """
    Attributes:
        match (Union[Unset, IngestersSecretMatch]):
        rule (Union[Unset, IngestersSecretRule]):
        scan_id (Union[Unset, str]):
        severity (Union[Unset, IngestersSecretSeverity]):
    """

    match: Union[Unset, "IngestersSecretMatch"] = UNSET
    rule: Union[Unset, "IngestersSecretRule"] = UNSET
    scan_id: Union[Unset, str] = UNSET
    severity: Union[Unset, "IngestersSecretSeverity"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        match: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.match, Unset):
            match = self.match.to_dict()

        rule: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.rule, Unset):
            rule = self.rule.to_dict()

        scan_id = self.scan_id

        severity: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if match is not UNSET:
            field_dict["match"] = match
        if rule is not UNSET:
            field_dict["rule"] = rule
        if scan_id is not UNSET:
            field_dict["scan_id"] = scan_id
        if severity is not UNSET:
            field_dict["severity"] = severity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ingesters_secret_match import IngestersSecretMatch
        from ..models.ingesters_secret_rule import IngestersSecretRule
        from ..models.ingesters_secret_severity import IngestersSecretSeverity

        d = dict(src_dict)
        _match = d.pop("match", UNSET)
        match: Union[Unset, IngestersSecretMatch]
        if isinstance(_match, Unset):
            match = UNSET
        else:
            match = IngestersSecretMatch.from_dict(_match)

        _rule = d.pop("rule", UNSET)
        rule: Union[Unset, IngestersSecretRule]
        if isinstance(_rule, Unset):
            rule = UNSET
        else:
            rule = IngestersSecretRule.from_dict(_rule)

        scan_id = d.pop("scan_id", UNSET)

        _severity = d.pop("severity", UNSET)
        severity: Union[Unset, IngestersSecretSeverity]
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = IngestersSecretSeverity.from_dict(_severity)

        ingesters_secret = cls(
            match=match,
            rule=rule,
            scan_id=scan_id,
            severity=severity,
        )

        ingesters_secret.additional_properties = d
        return ingesters_secret

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
