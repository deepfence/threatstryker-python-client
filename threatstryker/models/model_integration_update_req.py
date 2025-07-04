from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_integration_filters import ModelIntegrationFilters
    from ..models.model_integration_update_req_config_type_0 import ModelIntegrationUpdateReqConfigType0


T = TypeVar("T", bound="ModelIntegrationUpdateReq")


@_attrs_define
class ModelIntegrationUpdateReq:
    """
    Attributes:
        config (Union['ModelIntegrationUpdateReqConfigType0', None, Unset]):
        filters (Union[Unset, ModelIntegrationFilters]):
        id (Union[Unset, int]):
        integration_type (Union[Unset, str]):
        notification_type (Union[Unset, str]):
        send_summary (Union[Unset, bool]):
    """

    config: Union["ModelIntegrationUpdateReqConfigType0", None, Unset] = UNSET
    filters: Union[Unset, "ModelIntegrationFilters"] = UNSET
    id: Union[Unset, int] = UNSET
    integration_type: Union[Unset, str] = UNSET
    notification_type: Union[Unset, str] = UNSET
    send_summary: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.model_integration_update_req_config_type_0 import ModelIntegrationUpdateReqConfigType0

        config: Union[None, Unset, dict[str, Any]]
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, ModelIntegrationUpdateReqConfigType0):
            config = self.config.to_dict()
        else:
            config = self.config

        filters: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        id = self.id

        integration_type = self.integration_type

        notification_type = self.notification_type

        send_summary = self.send_summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if filters is not UNSET:
            field_dict["filters"] = filters
        if id is not UNSET:
            field_dict["id"] = id
        if integration_type is not UNSET:
            field_dict["integration_type"] = integration_type
        if notification_type is not UNSET:
            field_dict["notification_type"] = notification_type
        if send_summary is not UNSET:
            field_dict["send_summary"] = send_summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_integration_filters import ModelIntegrationFilters
        from ..models.model_integration_update_req_config_type_0 import ModelIntegrationUpdateReqConfigType0

        d = dict(src_dict)

        def _parse_config(data: object) -> Union["ModelIntegrationUpdateReqConfigType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0 = ModelIntegrationUpdateReqConfigType0.from_dict(data)

                return config_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ModelIntegrationUpdateReqConfigType0", None, Unset], data)

        config = _parse_config(d.pop("config", UNSET))

        _filters = d.pop("filters", UNSET)
        filters: Union[Unset, ModelIntegrationFilters]
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = ModelIntegrationFilters.from_dict(_filters)

        id = d.pop("id", UNSET)

        integration_type = d.pop("integration_type", UNSET)

        notification_type = d.pop("notification_type", UNSET)

        send_summary = d.pop("send_summary", UNSET)

        model_integration_update_req = cls(
            config=config,
            filters=filters,
            id=id,
            integration_type=integration_type,
            notification_type=notification_type,
            send_summary=send_summary,
        )

        model_integration_update_req.additional_properties = d
        return model_integration_update_req

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
