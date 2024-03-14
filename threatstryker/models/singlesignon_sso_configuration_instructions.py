from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.singlesignon_sso_configuration_instruction import SinglesignonSSOConfigurationInstruction


T = TypeVar("T", bound="SinglesignonSSOConfigurationInstructions")


@_attrs_define
class SinglesignonSSOConfigurationInstructions:
    """
    Attributes:
        github (Union[List['SinglesignonSSOConfigurationInstruction'], None, Unset]):
        google (Union[List['SinglesignonSSOConfigurationInstruction'], None, Unset]):
        microsoft (Union[List['SinglesignonSSOConfigurationInstruction'], None, Unset]):
        oidc (Union[List['SinglesignonSSOConfigurationInstruction'], None, Unset]):
    """

    github: Union[List["SinglesignonSSOConfigurationInstruction"], None, Unset] = UNSET
    google: Union[List["SinglesignonSSOConfigurationInstruction"], None, Unset] = UNSET
    microsoft: Union[List["SinglesignonSSOConfigurationInstruction"], None, Unset] = UNSET
    oidc: Union[List["SinglesignonSSOConfigurationInstruction"], None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        github: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.github, Unset):
            github = UNSET
        elif isinstance(self.github, list):
            github = []
            for github_type_0_item_data in self.github:
                github_type_0_item = github_type_0_item_data.to_dict()
                github.append(github_type_0_item)

        else:
            github = self.github

        google: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.google, Unset):
            google = UNSET
        elif isinstance(self.google, list):
            google = []
            for google_type_0_item_data in self.google:
                google_type_0_item = google_type_0_item_data.to_dict()
                google.append(google_type_0_item)

        else:
            google = self.google

        microsoft: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.microsoft, Unset):
            microsoft = UNSET
        elif isinstance(self.microsoft, list):
            microsoft = []
            for microsoft_type_0_item_data in self.microsoft:
                microsoft_type_0_item = microsoft_type_0_item_data.to_dict()
                microsoft.append(microsoft_type_0_item)

        else:
            microsoft = self.microsoft

        oidc: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.oidc, Unset):
            oidc = UNSET
        elif isinstance(self.oidc, list):
            oidc = []
            for oidc_type_0_item_data in self.oidc:
                oidc_type_0_item = oidc_type_0_item_data.to_dict()
                oidc.append(oidc_type_0_item)

        else:
            oidc = self.oidc

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

        def _parse_github(data: object) -> Union[List["SinglesignonSSOConfigurationInstruction"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                github_type_0 = []
                _github_type_0 = data
                for github_type_0_item_data in _github_type_0:
                    github_type_0_item = SinglesignonSSOConfigurationInstruction.from_dict(github_type_0_item_data)

                    github_type_0.append(github_type_0_item)

                return github_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["SinglesignonSSOConfigurationInstruction"], None, Unset], data)

        github = _parse_github(d.pop("github", UNSET))

        def _parse_google(data: object) -> Union[List["SinglesignonSSOConfigurationInstruction"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                google_type_0 = []
                _google_type_0 = data
                for google_type_0_item_data in _google_type_0:
                    google_type_0_item = SinglesignonSSOConfigurationInstruction.from_dict(google_type_0_item_data)

                    google_type_0.append(google_type_0_item)

                return google_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["SinglesignonSSOConfigurationInstruction"], None, Unset], data)

        google = _parse_google(d.pop("google", UNSET))

        def _parse_microsoft(data: object) -> Union[List["SinglesignonSSOConfigurationInstruction"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                microsoft_type_0 = []
                _microsoft_type_0 = data
                for microsoft_type_0_item_data in _microsoft_type_0:
                    microsoft_type_0_item = SinglesignonSSOConfigurationInstruction.from_dict(
                        microsoft_type_0_item_data
                    )

                    microsoft_type_0.append(microsoft_type_0_item)

                return microsoft_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["SinglesignonSSOConfigurationInstruction"], None, Unset], data)

        microsoft = _parse_microsoft(d.pop("microsoft", UNSET))

        def _parse_oidc(data: object) -> Union[List["SinglesignonSSOConfigurationInstruction"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                oidc_type_0 = []
                _oidc_type_0 = data
                for oidc_type_0_item_data in _oidc_type_0:
                    oidc_type_0_item = SinglesignonSSOConfigurationInstruction.from_dict(oidc_type_0_item_data)

                    oidc_type_0.append(oidc_type_0_item)

                return oidc_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["SinglesignonSSOConfigurationInstruction"], None, Unset], data)

        oidc = _parse_oidc(d.pop("oidc", UNSET))

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
