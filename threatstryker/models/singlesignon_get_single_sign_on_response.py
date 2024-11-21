from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

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
            'key'}]}, 'config': [{'issuer_alias_url': 'issuer_alias_url', 'issuer_url': 'issuer_url', 'updated_at':
            datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')),
            'sso_provider_type': 'sso_provider_type', 'created_at': datetime.datetime(2000, 1, 23, 4, 56, 7,
            tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'disable_password_login': True, 'id': 0, 'label':
            'label', 'client_id': 'client_id'}, {'issuer_alias_url': 'issuer_alias_url', 'issuer_url': 'issuer_url',
            'updated_at': datetime.datetime(2000, 1, 23, 4, 56, 7, tzinfo=datetime.timezone(datetime.timedelta(0),
            '+00:00')), 'sso_provider_type': 'sso_provider_type', 'created_at': datetime.datetime(2000, 1, 23, 4, 56, 7,
            tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'disable_password_login': True, 'id': 0, 'label':
            'label', 'client_id': 'client_id'}]}

    Attributes:
        config (Union[List['SinglesignonSSOResponse'], None]):
        instructions (SinglesignonSSOConfigurationInstructions):  Example: {'github': [{'value': 'value', 'key': 'key'},
            {'value': 'value', 'key': 'key'}], 'google': [{'value': 'value', 'key': 'key'}, {'value': 'value', 'key':
            'key'}], 'microsoft': [{'value': 'value', 'key': 'key'}, {'value': 'value', 'key': 'key'}], 'oidc': [{'value':
            'value', 'key': 'key'}, {'value': 'value', 'key': 'key'}]}.
    """

    config: Union[List["SinglesignonSSOResponse"], None]
    instructions: "SinglesignonSSOConfigurationInstructions"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        config: Union[List[Dict[str, Any]], None]
        if isinstance(self.config, list):
            config = []
            for config_type_0_item_data in self.config:
                config_type_0_item = config_type_0_item_data.to_dict()
                config.append(config_type_0_item)

        else:
            config = self.config

        instructions = self.instructions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config": config,
                "instructions": instructions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.singlesignon_sso_configuration_instructions import SinglesignonSSOConfigurationInstructions
        from ..models.singlesignon_sso_response import SinglesignonSSOResponse

        d = src_dict.copy()

        def _parse_config(data: object) -> Union[List["SinglesignonSSOResponse"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                config_type_0 = []
                _config_type_0 = data
                for config_type_0_item_data in _config_type_0:
                    config_type_0_item = SinglesignonSSOResponse.from_dict(config_type_0_item_data)

                    config_type_0.append(config_type_0_item)

                return config_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["SinglesignonSSOResponse"], None], data)

        config = _parse_config(d.pop("config"))

        instructions = SinglesignonSSOConfigurationInstructions.from_dict(d.pop("instructions"))

        singlesignon_get_single_sign_on_response = cls(
            config=config,
            instructions=instructions,
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
