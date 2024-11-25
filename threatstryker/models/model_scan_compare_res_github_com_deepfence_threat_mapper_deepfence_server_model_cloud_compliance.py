from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_cloud_compliance import ModelCloudCompliance


T = TypeVar("T", bound="ModelScanCompareResGithubComDeepfenceThreatMapperDeepfenceServerModelCloudCompliance")


@_attrs_define
class ModelScanCompareResGithubComDeepfenceThreatMapperDeepfenceServerModelCloudCompliance:
    """
    Example:
        {'new': [{'severity': 'severity', 'reason': 'reason', 'control_id': 'control_id', 'resource': 'resource',
            'masked': True, 'count': 0, 'node_name': 'node_name', 'description': 'description', 'resources': [{'node_type':
            'node_type', 'live_secrets': ['live_secrets', 'live_secrets'], 'live_cves': ['live_cves', 'live_cves'], 'name':
            'name', 'host_name': 'host_name', 'live_malwares': ['live_malwares', 'live_malwares'], 'node_id': 'node_id'},
            {'node_type': 'node_type', 'live_secrets': ['live_secrets', 'live_secrets'], 'live_cves': ['live_cves',
            'live_cves'], 'name': 'name', 'host_name': 'host_name', 'live_malwares': ['live_malwares', 'live_malwares'],
            'node_id': 'node_id'}], 'cloud_provider': 'cloud_provider', 'title': 'title', 'type': 'type',
            'compliance_check_type': 'hipaa', 'account_id': 'account_id', 'updated_at': 6, 'service': 'service', 'region':
            'region', 'group': 'group', 'node_id': 'node_id', 'status': 'alarm'}, {'severity': 'severity', 'reason':
            'reason', 'control_id': 'control_id', 'resource': 'resource', 'masked': True, 'count': 0, 'node_name':
            'node_name', 'description': 'description', 'resources': [{'node_type': 'node_type', 'live_secrets':
            ['live_secrets', 'live_secrets'], 'live_cves': ['live_cves', 'live_cves'], 'name': 'name', 'host_name':
            'host_name', 'live_malwares': ['live_malwares', 'live_malwares'], 'node_id': 'node_id'}, {'node_type':
            'node_type', 'live_secrets': ['live_secrets', 'live_secrets'], 'live_cves': ['live_cves', 'live_cves'], 'name':
            'name', 'host_name': 'host_name', 'live_malwares': ['live_malwares', 'live_malwares'], 'node_id': 'node_id'}],
            'cloud_provider': 'cloud_provider', 'title': 'title', 'type': 'type', 'compliance_check_type': 'hipaa',
            'account_id': 'account_id', 'updated_at': 6, 'service': 'service', 'region': 'region', 'group': 'group',
            'node_id': 'node_id', 'status': 'alarm'}]}

    Attributes:
        new (Union[List['ModelCloudCompliance'], None]):
    """

    new: Union[List["ModelCloudCompliance"], None]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        new: Union[List[Dict[str, Any]], None]
        if isinstance(self.new, list):
            new = []
            for new_type_0_item_data in self.new:
                new_type_0_item = new_type_0_item_data.to_dict()
                new.append(new_type_0_item)

        else:
            new = self.new

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "new": new,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_cloud_compliance import ModelCloudCompliance

        d = src_dict.copy()

        def _parse_new(data: object) -> Union[List["ModelCloudCompliance"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                new_type_0 = []
                _new_type_0 = data
                for new_type_0_item_data in _new_type_0:
                    new_type_0_item = ModelCloudCompliance.from_dict(new_type_0_item_data)

                    new_type_0.append(new_type_0_item)

                return new_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelCloudCompliance"], None], data)

        new = _parse_new(d.pop("new"))

        model_scan_compare_res_github_com_deepfence_threat_mapper_deepfence_server_model_cloud_compliance = cls(
            new=new,
        )

        model_scan_compare_res_github_com_deepfence_threat_mapper_deepfence_server_model_cloud_compliance.additional_properties = d
        return model_scan_compare_res_github_com_deepfence_threat_mapper_deepfence_server_model_cloud_compliance

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
