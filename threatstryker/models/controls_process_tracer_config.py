from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.controls_process_event_entry import ControlsProcessEventEntry


T = TypeVar("T", bound="ControlsProcessTracerConfig")


@_attrs_define
class ControlsProcessTracerConfig:
    """
    Example:
        {'updated_at': 0, 'monitoredprocessevents': [{'skip_path_list': ['skip_path_list', 'skip_path_list'],
            'failure_severity': 'failure_severity', 'skip_user_list': ['skip_user_list', 'skip_user_list'],
            'success_severity': 'success_severity', 'event': 'bin-execution', 'skip_comm_list': ['skip_comm_list',
            'skip_comm_list']}, {'skip_path_list': ['skip_path_list', 'skip_path_list'], 'failure_severity':
            'failure_severity', 'skip_user_list': ['skip_user_list', 'skip_user_list'], 'success_severity':
            'success_severity', 'event': 'bin-execution', 'skip_comm_list': ['skip_comm_list', 'skip_comm_list']}],
            'node_id': 'node_id'}

    Attributes:
        node_id (str):
        updated_at (int):
        monitoredprocessevents (Union[List['ControlsProcessEventEntry'], None, Unset]):
    """

    node_id: str
    updated_at: int
    monitoredprocessevents: Union[List["ControlsProcessEventEntry"], None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        node_id = self.node_id

        updated_at = self.updated_at

        monitoredprocessevents: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.monitoredprocessevents, Unset):
            monitoredprocessevents = UNSET
        elif isinstance(self.monitoredprocessevents, list):
            monitoredprocessevents = []
            for monitoredprocessevents_type_0_item_data in self.monitoredprocessevents:
                monitoredprocessevents_type_0_item = monitoredprocessevents_type_0_item_data.to_dict()
                monitoredprocessevents.append(monitoredprocessevents_type_0_item)

        else:
            monitoredprocessevents = self.monitoredprocessevents

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node_id": node_id,
                "updated_at": updated_at,
            }
        )
        if monitoredprocessevents is not UNSET:
            field_dict["monitoredprocessevents"] = monitoredprocessevents

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.controls_process_event_entry import ControlsProcessEventEntry

        d = src_dict.copy()
        node_id = d.pop("node_id")

        updated_at = d.pop("updated_at")

        def _parse_monitoredprocessevents(data: object) -> Union[List["ControlsProcessEventEntry"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                monitoredprocessevents_type_0 = []
                _monitoredprocessevents_type_0 = data
                for monitoredprocessevents_type_0_item_data in _monitoredprocessevents_type_0:
                    monitoredprocessevents_type_0_item = ControlsProcessEventEntry.from_dict(
                        monitoredprocessevents_type_0_item_data
                    )

                    monitoredprocessevents_type_0.append(monitoredprocessevents_type_0_item)

                return monitoredprocessevents_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ControlsProcessEventEntry"], None, Unset], data)

        monitoredprocessevents = _parse_monitoredprocessevents(d.pop("monitoredprocessevents", UNSET))

        controls_process_tracer_config = cls(
            node_id=node_id,
            updated_at=updated_at,
            monitoredprocessevents=monitoredprocessevents,
        )

        controls_process_tracer_config.additional_properties = d
        return controls_process_tracer_config

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
