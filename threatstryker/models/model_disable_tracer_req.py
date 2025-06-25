from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_agent_id import ModelAgentID


T = TypeVar("T", bound="ModelDisableTracerReq")


@_attrs_define
class ModelDisableTracerReq:
    """
    Attributes:
        agent_ids (Union[None, list['ModelAgentID']]):
    """

    agent_ids: Union[None, list["ModelAgentID"]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent_ids: Union[None, list[dict[str, Any]]]
        if isinstance(self.agent_ids, list):
            agent_ids = []
            for agent_ids_type_0_item_data in self.agent_ids:
                agent_ids_type_0_item = agent_ids_type_0_item_data.to_dict()
                agent_ids.append(agent_ids_type_0_item)

        else:
            agent_ids = self.agent_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_ids": agent_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_agent_id import ModelAgentID

        d = dict(src_dict)

        def _parse_agent_ids(data: object) -> Union[None, list["ModelAgentID"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                agent_ids_type_0 = []
                _agent_ids_type_0 = data
                for agent_ids_type_0_item_data in _agent_ids_type_0:
                    agent_ids_type_0_item = ModelAgentID.from_dict(agent_ids_type_0_item_data)

                    agent_ids_type_0.append(agent_ids_type_0_item)

                return agent_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["ModelAgentID"]], data)

        agent_ids = _parse_agent_ids(d.pop("agent_ids"))

        model_disable_tracer_req = cls(
            agent_ids=agent_ids,
        )

        model_disable_tracer_req.additional_properties = d
        return model_disable_tracer_req

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
