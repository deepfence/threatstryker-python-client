from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_integration_add_req_config_type_0 import ModelIntegrationAddReqConfigType0
    from ..models.model_integration_filters import ModelIntegrationFilters


T = TypeVar("T", bound="ModelIntegrationAddReq")


@_attrs_define
class ModelIntegrationAddReq:
    """
    Attributes:
        integration_type (str):
        notification_type (str):
        config (Union['ModelIntegrationAddReqConfigType0', None, Unset]):
        filters (Union[Unset, ModelIntegrationFilters]):
        send_summary (Union[Unset, bool]):
    """

    integration_type: str
    notification_type: str
    config: Union["ModelIntegrationAddReqConfigType0", None, Unset] = UNSET
    filters: Union[Unset, "ModelIntegrationFilters"] = UNSET
    send_summary: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.model_integration_add_req_config_type_0 import ModelIntegrationAddReqConfigType0

        integration_type = self.integration_type

        notification_type = self.notification_type

        config: Union[None, Unset, dict[str, Any]]
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, ModelIntegrationAddReqConfigType0):
            config = self.config.to_dict()
        else:
            config = self.config

        filters: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        send_summary = self.send_summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "integration_type": integration_type,
                "notification_type": notification_type,
            }
        )
        if config is not UNSET:
            field_dict["config"] = config
        if filters is not UNSET:
            field_dict["filters"] = filters
        if send_summary is not UNSET:
            field_dict["send_summary"] = send_summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_integration_add_req_config_type_0 import ModelIntegrationAddReqConfigType0
        from ..models.model_integration_filters import ModelIntegrationFilters

        d = dict(src_dict)
        integration_type = d.pop("integration_type")

        notification_type = d.pop("notification_type")

        def _parse_config(data: object) -> Union["ModelIntegrationAddReqConfigType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0 = ModelIntegrationAddReqConfigType0.from_dict(data)

                return config_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ModelIntegrationAddReqConfigType0", None, Unset], data)

        config = _parse_config(d.pop("config", UNSET))

        _filters = d.pop("filters", UNSET)
        filters: Union[Unset, ModelIntegrationFilters]
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = ModelIntegrationFilters.from_dict(_filters)

        send_summary = d.pop("send_summary", UNSET)

        model_integration_add_req = cls(
            integration_type=integration_type,
            notification_type=notification_type,
            config=config,
            filters=filters,
            send_summary=send_summary,
        )

        model_integration_add_req.additional_properties = d
        return model_integration_add_req

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
