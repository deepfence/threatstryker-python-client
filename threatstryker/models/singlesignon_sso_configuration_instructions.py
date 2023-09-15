from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.singlesignon_sso_configuration_instruction import SinglesignonSSOConfigurationInstruction


T = TypeVar("T", bound="SinglesignonSSOConfigurationInstructions")


@_attrs_define
class SinglesignonSSOConfigurationInstructions:
    """
    Example:
        {'github': [{'value': 'value', 'key': 'key'}, {'value': 'value', 'key': 'key'}], 'google': [{'value': 'value',
            'key': 'key'}, {'value': 'value', 'key': 'key'}], 'microsoft': [{'value': 'value', 'key': 'key'}, {'value':
            'value', 'key': 'key'}], 'oidc': [{'value': 'value', 'key': 'key'}, {'value': 'value', 'key': 'key'}]}

    Attributes:
        github (Union[Unset, None, List['SinglesignonSSOConfigurationInstruction']]):
        google (Union[Unset, None, List['SinglesignonSSOConfigurationInstruction']]):
        microsoft (Union[Unset, None, List['SinglesignonSSOConfigurationInstruction']]):
        oidc (Union[Unset, None, List['SinglesignonSSOConfigurationInstruction']]):
    """

    github: Union[Unset, None, List["SinglesignonSSOConfigurationInstruction"]] = UNSET
    google: Union[Unset, None, List["SinglesignonSSOConfigurationInstruction"]] = UNSET
    microsoft: Union[Unset, None, List["SinglesignonSSOConfigurationInstruction"]] = UNSET
    oidc: Union[Unset, None, List["SinglesignonSSOConfigurationInstruction"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        github: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.github, Unset):
            if self.github is None:
                github = None
            else:
                github = []
                for github_item_data in self.github:
                    github_item = github_item_data.to_dict()

                    github.append(github_item)

        google: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.google, Unset):
            if self.google is None:
                google = None
            else:
                google = []
                for google_item_data in self.google:
                    google_item = google_item_data.to_dict()

                    google.append(google_item)

        microsoft: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.microsoft, Unset):
            if self.microsoft is None:
                microsoft = None
            else:
                microsoft = []
                for microsoft_item_data in self.microsoft:
                    microsoft_item = microsoft_item_data.to_dict()

                    microsoft.append(microsoft_item)

        oidc: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.oidc, Unset):
            if self.oidc is None:
                oidc = None
            else:
                oidc = []
                for oidc_item_data in self.oidc:
                    oidc_item = oidc_item_data.to_dict()

                    oidc.append(oidc_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if github is not UNSET:
            field_dict["github"] = github
        if google is not UNSET:
            field_dict["google"] = google
        if microsoft is not UNSET:
            field_dict["microsoft"] = microsoft
        if oidc is not UNSET:
            field_dict["oidc"] = oidc

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.singlesignon_sso_configuration_instruction import SinglesignonSSOConfigurationInstruction

        d = src_dict.copy()
        github = []
        _github = d.pop("github", UNSET)
        for github_item_data in _github or []:
            github_item = SinglesignonSSOConfigurationInstruction.from_dict(github_item_data)

            github.append(github_item)

        google = []
        _google = d.pop("google", UNSET)
        for google_item_data in _google or []:
            google_item = SinglesignonSSOConfigurationInstruction.from_dict(google_item_data)

            google.append(google_item)

        microsoft = []
        _microsoft = d.pop("microsoft", UNSET)
        for microsoft_item_data in _microsoft or []:
            microsoft_item = SinglesignonSSOConfigurationInstruction.from_dict(microsoft_item_data)

            microsoft.append(microsoft_item)

        oidc = []
        _oidc = d.pop("oidc", UNSET)
        for oidc_item_data in _oidc or []:
            oidc_item = SinglesignonSSOConfigurationInstruction.from_dict(oidc_item_data)

            oidc.append(oidc_item)

        singlesignon_sso_configuration_instructions = cls(
            github=github,
            google=google,
            microsoft=microsoft,
            oidc=oidc,
        )

        singlesignon_sso_configuration_instructions.additional_properties = d
        return singlesignon_sso_configuration_instructions

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
