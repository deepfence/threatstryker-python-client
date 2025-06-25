import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostgresqlDbGetAuditLogsRow")


@_attrs_define
class PostgresqlDbGetAuditLogsRow:
    """
    Attributes:
        action (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        email (Union[Unset, str]):
        event (Union[Unset, str]):
        resources (Union[Unset, str]):
        role (Union[Unset, str]):
        success (Union[Unset, bool]):
    """

    action: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    email: Union[Unset, str] = UNSET
    event: Union[Unset, str] = UNSET
    resources: Union[Unset, str] = UNSET
    role: Union[Unset, str] = UNSET
    success: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        email = self.email

        event = self.event

        resources = self.resources

        role = self.role

        success = self.success

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if email is not UNSET:
            field_dict["email"] = email
        if event is not UNSET:
            field_dict["event"] = event
        if resources is not UNSET:
            field_dict["resources"] = resources
        if role is not UNSET:
            field_dict["role"] = role
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = d.pop("action", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        email = d.pop("email", UNSET)

        event = d.pop("event", UNSET)

        resources = d.pop("resources", UNSET)

        role = d.pop("role", UNSET)

        success = d.pop("success", UNSET)

        postgresql_db_get_audit_logs_row = cls(
            action=action,
            created_at=created_at,
            email=email,
            event=event,
            resources=resources,
            role=role,
            success=success,
        )

        postgresql_db_get_audit_logs_row.additional_properties = d
        return postgresql_db_get_audit_logs_row

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
