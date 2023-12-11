from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.controls_monitored_files_config import ControlsMonitoredFilesConfig


T = TypeVar("T", bound="ControlsFilesystemTracerConfig")


@_attrs_define
class ControlsFilesystemTracerConfig:
    """
    Example:
        {'updated_at': 0, 'watchedentries': [{'severity': 'severity', 'accesstypes': ['accesstypes', 'accesstypes'],
            'root': 'root', 'recursive': True}, {'severity': 'severity', 'accesstypes': ['accesstypes', 'accesstypes'],
            'root': 'root', 'recursive': True}], 'node_id': 'node_id'}

    Attributes:
        node_id (str):
        updated_at (int):
        watchedentries (Optional[List['ControlsMonitoredFilesConfig']]):
    """

    node_id: str
    updated_at: int
    watchedentries: Optional[List["ControlsMonitoredFilesConfig"]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        node_id = self.node_id
        updated_at = self.updated_at
        if self.watchedentries is None:
            watchedentries = None
        else:
            watchedentries = []
            for watchedentries_item_data in self.watchedentries:
                watchedentries_item = watchedentries_item_data.to_dict()

                watchedentries.append(watchedentries_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node_id": node_id,
                "updated_at": updated_at,
                "watchedentries": watchedentries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.controls_monitored_files_config import ControlsMonitoredFilesConfig

        d = src_dict.copy()
        node_id = d.pop("node_id")

        updated_at = d.pop("updated_at")

        watchedentries = []
        _watchedentries = d.pop("watchedentries")
        for watchedentries_item_data in _watchedentries or []:
            watchedentries_item = ControlsMonitoredFilesConfig.from_dict(watchedentries_item_data)

            watchedentries.append(watchedentries_item)

        controls_filesystem_tracer_config = cls(
            node_id=node_id,
            updated_at=updated_at,
            watchedentries=watchedentries,
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
