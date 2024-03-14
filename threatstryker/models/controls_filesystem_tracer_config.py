from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.controls_monitored_files_config import ControlsMonitoredFilesConfig


T = TypeVar("T", bound="ControlsFilesystemTracerConfig")


@_attrs_define
class ControlsFilesystemTracerConfig:
    """
    Attributes:
        node_id (str):
        updated_at (int):
        watchedentries (Union[List['ControlsMonitoredFilesConfig'], None]):
    """

    node_id: str
    updated_at: int
    watchedentries: Union[List["ControlsMonitoredFilesConfig"], None]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        node_id = self.node_id

        updated_at = self.updated_at

        watchedentries: Union[List[Dict[str, Any]], None]
        if isinstance(self.watchedentries, list):
            watchedentries = []
            for watchedentries_type_0_item_data in self.watchedentries:
                watchedentries_type_0_item = watchedentries_type_0_item_data.to_dict()
                watchedentries.append(watchedentries_type_0_item)

        else:
            watchedentries = self.watchedentries

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

        def _parse_watchedentries(data: object) -> Union[List["ControlsMonitoredFilesConfig"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                watchedentries_type_0 = []
                _watchedentries_type_0 = data
                for watchedentries_type_0_item_data in _watchedentries_type_0:
                    watchedentries_type_0_item = ControlsMonitoredFilesConfig.from_dict(watchedentries_type_0_item_data)

                    watchedentries_type_0.append(watchedentries_type_0_item)

                return watchedentries_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ControlsMonitoredFilesConfig"], None], data)

        watchedentries = _parse_watchedentries(d.pop("watchedentries"))

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
