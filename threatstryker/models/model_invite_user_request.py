from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_invite_user_request_action import ModelInviteUserRequestAction
from ..models.model_invite_user_request_role import ModelInviteUserRequestRole

T = TypeVar("T", bound="ModelInviteUserRequest")


@_attrs_define
class ModelInviteUserRequest:
    """
    Attributes:
        action (ModelInviteUserRequestAction):
        email (str):
        role (ModelInviteUserRequestRole):
    """

    action: ModelInviteUserRequestAction
    email: str
    role: ModelInviteUserRequestRole
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action = self.action.value

        email = self.email

        role = self.role.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "email": email,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action = ModelInviteUserRequestAction(d.pop("action"))

        email = d.pop("email")

        role = ModelInviteUserRequestRole(d.pop("role"))

        model_invite_user_request = cls(
            action=action,
            email=email,
            role=role,
        )

        model_invite_user_request.additional_properties = d
        return model_invite_user_request

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
