import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelDeepfenceCommunication")


@_attrs_define
class ModelDeepfenceCommunication:
    """
    Attributes:
        button_content (Union[Unset, str]):
        content (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        id (Union[Unset, int]):
        link (Union[Unset, str]):
        link_title (Union[Unset, str]):
        read (Union[Unset, bool]):
        title (Union[Unset, str]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    button_content: Union[Unset, str] = UNSET
    content: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, int] = UNSET
    link: Union[Unset, str] = UNSET
    link_title: Union[Unset, str] = UNSET
    read: Union[Unset, bool] = UNSET
    title: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        button_content = self.button_content

        content = self.content

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        id = self.id

        link = self.link

        link_title = self.link_title

        read = self.read

        title = self.title

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if button_content is not UNSET:
            field_dict["button_content"] = button_content
        if content is not UNSET:
            field_dict["content"] = content
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if link is not UNSET:
            field_dict["link"] = link
        if link_title is not UNSET:
            field_dict["link_title"] = link_title
        if read is not UNSET:
            field_dict["read"] = read
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        button_content = d.pop("button_content", UNSET)

        content = d.pop("content", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        id = d.pop("id", UNSET)

        link = d.pop("link", UNSET)

        link_title = d.pop("link_title", UNSET)

        read = d.pop("read", UNSET)

        title = d.pop("title", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        model_deepfence_communication = cls(
            button_content=button_content,
            content=content,
            created_at=created_at,
            id=id,
            link=link,
            link_title=link_title,
            read=read,
            title=title,
            updated_at=updated_at,
        )

        model_deepfence_communication.additional_properties = d
        return model_deepfence_communication

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
