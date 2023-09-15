from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.singlesignon_sso_configuration_instructions import SinglesignonSSOConfigurationInstructions
    from ..models.singlesignon_sso_response import SinglesignonSSOResponse


T = TypeVar("T", bound="SinglesignonGetSingleSignOnResponse")


@_attrs_define
class SinglesignonGetSingleSignOnResponse:
    """
    Example:
        {'instructions': {'github': [{'value': 'value', 'key': 'key'}, {'value': 'value', 'key': 'key'}], 'google':
            [{'value': 'value', 'key': 'key'}, {'value': 'value', 'key': 'key'}], 'microsoft': [{'value': 'value', 'key':
            'key'}, {'value': 'value', 'key': 'key'}], 'oidc': [{'value': 'value', 'key': 'key'}, {'value': 'value', 'key':
            'key'}]}, 'config': [{'issuer_url': 'issuer_url', 'updated_at': datetime.datetime(2000, 1, 23, 4, 56, 7,
            tzinfo=datetime.timezone.utc), 'sso_provider_type': 'sso_provider_type', 'created_at': datetime.datetime(2000,
            1, 23, 4, 56, 7, tzinfo=datetime.timezone.utc), 'disable_password_login': True, 'id': 0, 'label': 'label',
            'client_id': 'client_id'}, {'issuer_url': 'issuer_url', 'updated_at': datetime.datetime(2000, 1, 23, 4, 56, 7,
            tzinfo=datetime.timezone.utc), 'sso_provider_type': 'sso_provider_type', 'created_at': datetime.datetime(2000,
            1, 23, 4, 56, 7, tzinfo=datetime.timezone.utc), 'disable_password_login': True, 'id': 0, 'label': 'label',
            'client_id': 'client_id'}]}

    Attributes:
        instructions (SinglesignonSSOConfigurationInstructions):  Example: {'github': [{'value': 'value', 'key': 'key'},
            {'value': 'value', 'key': 'key'}], 'google': [{'value': 'value', 'key': 'key'}, {'value': 'value', 'key':
            'key'}], 'microsoft': [{'value': 'value', 'key': 'key'}, {'value': 'value', 'key': 'key'}], 'oidc': [{'value':
            'value', 'key': 'key'}, {'value': 'value', 'key': 'key'}]}.
        config (Optional[List['SinglesignonSSOResponse']]):
    """

    instructions: "SinglesignonSSOConfigurationInstructions"
    config: Optional[List["SinglesignonSSOResponse"]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        instructions = self.instructions.to_dict()

        if self.config is None:
            config = None
        else:
            config = []
            for config_item_data in self.config:
                config_item = config_item_data.to_dict()

                config.append(config_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instructions": instructions,
                "config": config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.singlesignon_sso_configuration_instructions import SinglesignonSSOConfigurationInstructions
        from ..models.singlesignon_sso_response import SinglesignonSSOResponse

        d = src_dict.copy()
        instructions = SinglesignonSSOConfigurationInstructions.from_dict(d.pop("instructions"))

        config = []
        _config = d.pop("config")
        for config_item_data in _config or []:
            config_item = SinglesignonSSOResponse.from_dict(config_item_data)

            config.append(config_item)

        singlesignon_get_single_sign_on_response = cls(
            instructions=instructions,
            config=config,
        )

        singlesignon_get_single_sign_on_response.additional_properties = d
        return singlesignon_get_single_sign_on_response

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
