from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelGetAgentConfigReq")


@_attrs_define
class ModelGetAgentConfigReq:
    """
    Attributes:
        config_ids (Union[None, list[str]]):
    """

    config_ids: Union[None, list[str]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config_ids: Union[None, list[str]]
        if isinstance(self.config_ids, list):
            config_ids = self.config_ids

        else:
            config_ids = self.config_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config_ids": config_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_config_ids(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                config_ids_type_0 = cast(list[str], data)

                return config_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        config_ids = _parse_config_ids(d.pop("config_ids"))

        model_get_agent_config_req = cls(
            config_ids=config_ids,
        )

        model_get_agent_config_req.additional_properties = d
        return model_get_agent_config_req

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
