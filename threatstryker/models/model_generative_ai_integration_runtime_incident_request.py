from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_generative_ai_integration_runtime_incident_request_query_type import (
    ModelGenerativeAiIntegrationRuntimeIncidentRequestQueryType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelGenerativeAiIntegrationRuntimeIncidentRequest")


@_attrs_define
class ModelGenerativeAiIntegrationRuntimeIncidentRequest:
    """
    Attributes:
        category (str):
        event_type (str):
        query_type (ModelGenerativeAiIntegrationRuntimeIncidentRequestQueryType):
        summary (str):
        integration_id (Union[Unset, int]):
    """

    category: str
    event_type: str
    query_type: ModelGenerativeAiIntegrationRuntimeIncidentRequestQueryType
    summary: str
    integration_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category = self.category

        event_type = self.event_type

        query_type = self.query_type.value

        summary = self.summary

        integration_id = self.integration_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "event_type": event_type,
                "query_type": query_type,
                "summary": summary,
            }
        )
        if integration_id is not UNSET:
            field_dict["integration_id"] = integration_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        category = d.pop("category")

        event_type = d.pop("event_type")

        query_type = ModelGenerativeAiIntegrationRuntimeIncidentRequestQueryType(d.pop("query_type"))

        summary = d.pop("summary")

        integration_id = d.pop("integration_id", UNSET)

        model_generative_ai_integration_runtime_incident_request = cls(
            category=category,
            event_type=event_type,
            query_type=query_type,
            summary=summary,
            integration_id=integration_id,
        )

        model_generative_ai_integration_runtime_incident_request.additional_properties = d
        return model_generative_ai_integration_runtime_incident_request

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
