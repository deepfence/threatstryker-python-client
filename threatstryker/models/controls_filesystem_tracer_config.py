from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.controls_monitored_files_config import ControlsMonitoredFilesConfig
    from ..models.controls_process_event_config import ControlsProcessEventConfig


T = TypeVar("T", bound="ControlsFilesystemTracerConfig")


@_attrs_define
class ControlsFilesystemTracerConfig:
    """
    Example:
        {'monitored_files': [{'path': 'path', 'weight': 'weight', 'access_types': ['access_types', 'access_types']},
            {'path': 'path', 'weight': 'weight', 'access_types': ['access_types', 'access_types']}], 'updated_at': 0,
            'process_events': [{'event_name': 'event_name', 'weight': 'weight'}, {'event_name': 'event_name', 'weight':
            'weight'}], 'node_id': 'node_id'}

    Attributes:
        node_id (str):
        updated_at (int):
        monitored_files (Optional[List['ControlsMonitoredFilesConfig']]):
        process_events (Optional[List['ControlsProcessEventConfig']]):
    """

    node_id: str
    updated_at: int
    monitored_files: Optional[List["ControlsMonitoredFilesConfig"]]
    process_events: Optional[List["ControlsProcessEventConfig"]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        node_id = self.node_id
        updated_at = self.updated_at
        if self.monitored_files is None:
            monitored_files = None
        else:
            monitored_files = []
            for monitored_files_item_data in self.monitored_files:
                monitored_files_item = monitored_files_item_data.to_dict()

                monitored_files.append(monitored_files_item)

        if self.process_events is None:
            process_events = None
        else:
            process_events = []
            for process_events_item_data in self.process_events:
                process_events_item = process_events_item_data.to_dict()

                process_events.append(process_events_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node_id": node_id,
                "updated_at": updated_at,
                "monitored_files": monitored_files,
                "process_events": process_events,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.controls_monitored_files_config import ControlsMonitoredFilesConfig
        from ..models.controls_process_event_config import ControlsProcessEventConfig

        d = src_dict.copy()
        node_id = d.pop("node_id")

        updated_at = d.pop("updated_at")

        monitored_files = []
        _monitored_files = d.pop("monitored_files")
        for monitored_files_item_data in _monitored_files or []:
            monitored_files_item = ControlsMonitoredFilesConfig.from_dict(monitored_files_item_data)

            monitored_files.append(monitored_files_item)

        process_events = []
        _process_events = d.pop("process_events")
        for process_events_item_data in _process_events or []:
            process_events_item = ControlsProcessEventConfig.from_dict(process_events_item_data)

            process_events.append(process_events_item)

        controls_filesystem_tracer_config = cls(
            node_id=node_id,
            updated_at=updated_at,
            monitored_files=monitored_files,
            process_events=process_events,
        )

        controls_filesystem_tracer_config.additional_properties = d
        return controls_filesystem_tracer_config

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
