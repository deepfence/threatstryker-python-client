from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiagnosisDiagnosticLogsLink")


@_attrs_define
class DiagnosisDiagnosticLogsLink:
    """
    Attributes:
        created_at (Union[Unset, str]):
        label (Union[Unset, str]):
        message (Union[Unset, str]):
        type_ (Union[Unset, str]):
        url_link (Union[Unset, str]):
    """

    created_at: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    url_link: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        label = self.label

        message = self.message

        type_ = self.type_

        url_link = self.url_link

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if label is not UNSET:
            field_dict["label"] = label
        if message is not UNSET:
            field_dict["message"] = message
        if type_ is not UNSET:
            field_dict["type"] = type_
        if url_link is not UNSET:
            field_dict["url_link"] = url_link

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        label = d.pop("label", UNSET)

        message = d.pop("message", UNSET)

        type_ = d.pop("type", UNSET)

        url_link = d.pop("url_link", UNSET)

        diagnosis_diagnostic_logs_link = cls(
            created_at=created_at,
            label=label,
            message=message,
            type_=type_,
            url_link=url_link,
        )

        diagnosis_diagnostic_logs_link.additional_properties = d
        return diagnosis_diagnostic_logs_link

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
