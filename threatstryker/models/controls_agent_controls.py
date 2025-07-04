from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.controls_action import ControlsAction


T = TypeVar("T", bound="ControlsAgentControls")


@_attrs_define
class ControlsAgentControls:
    """
    Attributes:
        beatrate (int):
        commands (Union[None, list['ControlsAction']]):
    """

    beatrate: int
    commands: Union[None, list["ControlsAction"]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        beatrate = self.beatrate

        commands: Union[None, list[dict[str, Any]]]
        if isinstance(self.commands, list):
            commands = []
            for commands_type_0_item_data in self.commands:
                commands_type_0_item = commands_type_0_item_data.to_dict()
                commands.append(commands_type_0_item)

        else:
            commands = self.commands

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "beatrate": beatrate,
                "commands": commands,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.controls_action import ControlsAction

        d = dict(src_dict)
        beatrate = d.pop("beatrate")

        def _parse_commands(data: object) -> Union[None, list["ControlsAction"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                commands_type_0 = []
                _commands_type_0 = data
                for commands_type_0_item_data in _commands_type_0:
                    commands_type_0_item = ControlsAction.from_dict(commands_type_0_item_data)

                    commands_type_0.append(commands_type_0_item)

                return commands_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["ControlsAction"]], data)

        commands = _parse_commands(d.pop("commands"))

        controls_agent_controls = cls(
            beatrate=beatrate,
            commands=commands,
        )

        controls_agent_controls.additional_properties = d
        return controls_agent_controls

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
