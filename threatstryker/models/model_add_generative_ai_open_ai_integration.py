from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_add_generative_ai_open_ai_integration_model_id import ModelAddGenerativeAiOpenAIIntegrationModelId

T = TypeVar("T", bound="ModelAddGenerativeAiOpenAIIntegration")


@_attrs_define
class ModelAddGenerativeAiOpenAIIntegration:
    """
    Attributes:
        api_key (str):
        model_id (ModelAddGenerativeAiOpenAIIntegrationModelId):
    """

    api_key: str
    model_id: ModelAddGenerativeAiOpenAIIntegrationModelId
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        model_id = self.model_id.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "api_key": api_key,
                "model_id": model_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("api_key")

        model_id = ModelAddGenerativeAiOpenAIIntegrationModelId(d.pop("model_id"))

        model_add_generative_ai_open_ai_integration = cls(
            api_key=api_key,
            model_id=model_id,
        )

        model_add_generative_ai_open_ai_integration.additional_properties = d
        return model_add_generative_ai_open_ai_integration

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
