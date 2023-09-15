from typing import Any, Dict, List, Optional, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelGetAgentConfigReq")


@_attrs_define
class ModelGetAgentConfigReq:
    """
    Example:
        {'config_ids': ['config_ids', 'config_ids']}

    Attributes:
        config_ids (Optional[List[str]]):
    """

    config_ids: Optional[List[str]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if self.config_ids is None:
            config_ids = None
        else:
            config_ids = self.config_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config_ids": config_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        config_ids = cast(List[str], d.pop("config_ids"))

        model_get_agent_config_req = cls(
            config_ids=config_ids,
        )

        model_get_agent_config_req.additional_properties = d
        return model_get_agent_config_req

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
