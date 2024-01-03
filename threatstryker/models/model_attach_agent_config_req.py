from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_agent_id import ModelAgentID


T = TypeVar("T", bound="ModelAttachAgentConfigReq")


@_attrs_define
class ModelAttachAgentConfigReq:
    """
    Example:
        {'config_id': 'config_id', 'agent_ids': [{'available_workload': 0, 'node_id': 'node_id'}, {'available_workload':
            0, 'node_id': 'node_id'}]}

    Attributes:
        config_id (str):
        agent_ids (Optional[List['ModelAgentID']]):
    """

    config_id: str
    agent_ids: Optional[List["ModelAgentID"]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        config_id = self.config_id
        if self.agent_ids is None:
            agent_ids = None
        else:
            agent_ids = []
            for agent_ids_item_data in self.agent_ids:
                agent_ids_item = agent_ids_item_data.to_dict()

                agent_ids.append(agent_ids_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config_id": config_id,
                "agent_ids": agent_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_agent_id import ModelAgentID

        d = src_dict.copy()
        config_id = d.pop("config_id")

        agent_ids = []
        _agent_ids = d.pop("agent_ids")
        for agent_ids_item_data in _agent_ids or []:
            agent_ids_item = ModelAgentID.from_dict(agent_ids_item_data)

            agent_ids.append(agent_ids_item)

        model_attach_agent_config_req = cls(
            config_id=config_id,
            agent_ids=agent_ids,
        )

        model_attach_agent_config_req.additional_properties = d
        return model_attach_agent_config_req

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
