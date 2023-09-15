from typing import Any, Dict, List, Optional, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelCloudResourceDeployAgentReq")


@_attrs_define
class ModelCloudResourceDeployAgentReq:
    """
    Example:
        {'node_ids': ['node_ids', 'node_ids']}

    Attributes:
        node_ids (Optional[List[str]]):
    """

    node_ids: Optional[List[str]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if self.node_ids is None:
            node_ids = None
        else:
            node_ids = self.node_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node_ids": node_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        node_ids = cast(List[str], d.pop("node_ids"))

        model_cloud_resource_deploy_agent_req = cls(
            node_ids=node_ids,
        )

        model_cloud_resource_deploy_agent_req.additional_properties = d
        return model_cloud_resource_deploy_agent_req

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
