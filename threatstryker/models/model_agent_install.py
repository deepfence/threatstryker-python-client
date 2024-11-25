from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_agent_install_cloud_provider import ModelAgentInstallCloudProvider

if TYPE_CHECKING:
    from ..models.model_agent_id import ModelAgentID
    from ..models.model_region_i_ds import ModelRegionIDs


T = TypeVar("T", bound="ModelAgentInstall")


@_attrs_define
class ModelAgentInstall:
    """
    Example:
        {'cloud_scanner_id': {'node_type': 'node_type', 'available_workload': 0, 'node_id': 'node_id'},
            'cloud_provider': 'aws', 'region_ids': [{'ids': ['ids', 'ids'], 'region': 'region'}, {'ids': ['ids', 'ids'],
            'region': 'region'}]}

    Attributes:
        cloud_provider (ModelAgentInstallCloudProvider):
        cloud_scanner_id (ModelAgentID):  Example: {'node_type': 'node_type', 'available_workload': 0, 'node_id':
            'node_id'}.
        region_ids (Union[List['ModelRegionIDs'], None]):
    """

    cloud_provider: ModelAgentInstallCloudProvider
    cloud_scanner_id: "ModelAgentID"
    region_ids: Union[List["ModelRegionIDs"], None]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cloud_provider = self.cloud_provider.value

        cloud_scanner_id = self.cloud_scanner_id.to_dict()

        region_ids: Union[List[Dict[str, Any]], None]
        if isinstance(self.region_ids, list):
            region_ids = []
            for region_ids_type_0_item_data in self.region_ids:
                region_ids_type_0_item = region_ids_type_0_item_data.to_dict()
                region_ids.append(region_ids_type_0_item)

        else:
            region_ids = self.region_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cloud_provider": cloud_provider,
                "cloud_scanner_id": cloud_scanner_id,
                "region_ids": region_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_agent_id import ModelAgentID
        from ..models.model_region_i_ds import ModelRegionIDs

        d = src_dict.copy()
        cloud_provider = ModelAgentInstallCloudProvider(d.pop("cloud_provider"))

        cloud_scanner_id = ModelAgentID.from_dict(d.pop("cloud_scanner_id"))

        def _parse_region_ids(data: object) -> Union[List["ModelRegionIDs"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                region_ids_type_0 = []
                _region_ids_type_0 = data
                for region_ids_type_0_item_data in _region_ids_type_0:
                    region_ids_type_0_item = ModelRegionIDs.from_dict(region_ids_type_0_item_data)

                    region_ids_type_0.append(region_ids_type_0_item)

                return region_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelRegionIDs"], None], data)

        region_ids = _parse_region_ids(d.pop("region_ids"))

        model_agent_install = cls(
            cloud_provider=cloud_provider,
            cloud_scanner_id=cloud_scanner_id,
            region_ids=region_ids,
        )

        model_agent_install.additional_properties = d
        return model_agent_install

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
