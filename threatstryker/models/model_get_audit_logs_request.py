from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_fetch_window import ModelFetchWindow


T = TypeVar("T", bound="ModelGetAuditLogsRequest")


@_attrs_define
class ModelGetAuditLogsRequest:
    """
    Attributes:
        window (ModelFetchWindow):
    """

    window: "ModelFetchWindow"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        window = self.window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "window": window,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_fetch_window import ModelFetchWindow

        d = dict(src_dict)
        window = ModelFetchWindow.from_dict(d.pop("window"))

        model_get_audit_logs_request = cls(
            window=window,
        )

        model_get_audit_logs_request.additional_properties = d
        return model_get_audit_logs_request

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
