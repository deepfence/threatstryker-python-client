from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_cloud_instance_deployment import ModelCloudInstanceDeployment
    from ..models.model_cloud_node_account_register_resp_data_scans import ModelCloudNodeAccountRegisterRespDataScans
    from ..models.model_cloud_node_cloudtrail_trail import ModelCloudNodeCloudtrailTrail


T = TypeVar("T", bound="ModelCloudNodeAccountRegisterRespData")


@_attrs_define
class ModelCloudNodeAccountRegisterRespData:
    """
    Example:
        {'deploy_instances': [{'hostname': 'hostname', 'account_id': 'account_id', 'instance_id': 'instance_id',
            'region': 'region'}, {'hostname': 'hostname', 'account_id': 'account_id', 'instance_id': 'instance_id',
            'region': 'region'}], 'cloudtrail_trails': [{'account_id': 'account_id', 'trail_name': 'trail_name'},
            {'account_id': 'account_id', 'trail_name': 'trail_name'}], 'scans': {'key': {'account_id': 'account_id',
            'benchmarks': [{'controls': ['controls', 'controls'], 'compliance_type': 'compliance_type', 'id': 'id'},
            {'controls': ['controls', 'controls'], 'compliance_type': 'compliance_type', 'id': 'id'}], 'scan_id': 'scan_id',
            'scan_types': ['scan_types', 'scan_types']}}, 'refresh': 'refresh'}

    Attributes:
        cloudtrail_trails (Union[Unset, None, List['ModelCloudNodeCloudtrailTrail']]):
        deploy_instances (Union[Unset, None, List['ModelCloudInstanceDeployment']]):
        refresh (Union[Unset, str]):
        scans (Union[Unset, None, ModelCloudNodeAccountRegisterRespDataScans]):
    """

    cloudtrail_trails: Union[Unset, None, List["ModelCloudNodeCloudtrailTrail"]] = UNSET
    deploy_instances: Union[Unset, None, List["ModelCloudInstanceDeployment"]] = UNSET
    refresh: Union[Unset, str] = UNSET
    scans: Union[Unset, None, "ModelCloudNodeAccountRegisterRespDataScans"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cloudtrail_trails: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.cloudtrail_trails, Unset):
            if self.cloudtrail_trails is None:
                cloudtrail_trails = None
            else:
                cloudtrail_trails = []
                for cloudtrail_trails_item_data in self.cloudtrail_trails:
                    cloudtrail_trails_item = cloudtrail_trails_item_data.to_dict()

                    cloudtrail_trails.append(cloudtrail_trails_item)

        deploy_instances: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.deploy_instances, Unset):
            if self.deploy_instances is None:
                deploy_instances = None
            else:
                deploy_instances = []
                for deploy_instances_item_data in self.deploy_instances:
                    deploy_instances_item = deploy_instances_item_data.to_dict()

                    deploy_instances.append(deploy_instances_item)

        refresh = self.refresh
        scans: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.scans, Unset):
            scans = self.scans.to_dict() if self.scans else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cloudtrail_trails is not UNSET:
            field_dict["cloudtrail_trails"] = cloudtrail_trails
        if deploy_instances is not UNSET:
            field_dict["deploy_instances"] = deploy_instances
        if refresh is not UNSET:
            field_dict["refresh"] = refresh
        if scans is not UNSET:
            field_dict["scans"] = scans

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_cloud_instance_deployment import ModelCloudInstanceDeployment
        from ..models.model_cloud_node_account_register_resp_data_scans import (
            ModelCloudNodeAccountRegisterRespDataScans,
        )
        from ..models.model_cloud_node_cloudtrail_trail import ModelCloudNodeCloudtrailTrail

        d = src_dict.copy()
        cloudtrail_trails = []
        _cloudtrail_trails = d.pop("cloudtrail_trails", UNSET)
        for cloudtrail_trails_item_data in _cloudtrail_trails or []:
            cloudtrail_trails_item = ModelCloudNodeCloudtrailTrail.from_dict(cloudtrail_trails_item_data)

            cloudtrail_trails.append(cloudtrail_trails_item)

        deploy_instances = []
        _deploy_instances = d.pop("deploy_instances", UNSET)
        for deploy_instances_item_data in _deploy_instances or []:
            deploy_instances_item = ModelCloudInstanceDeployment.from_dict(deploy_instances_item_data)

            deploy_instances.append(deploy_instances_item)

        refresh = d.pop("refresh", UNSET)

        _scans = d.pop("scans", UNSET)
        scans: Union[Unset, None, ModelCloudNodeAccountRegisterRespDataScans]
        if _scans is None:
            scans = None
        elif isinstance(_scans, Unset):
            scans = UNSET
        else:
            scans = ModelCloudNodeAccountRegisterRespDataScans.from_dict(_scans)

        model_cloud_node_account_register_resp_data = cls(
            cloudtrail_trails=cloudtrail_trails,
            deploy_instances=deploy_instances,
            refresh=refresh,
            scans=scans,
        )

        model_cloud_node_account_register_resp_data.additional_properties = d
        return model_cloud_node_account_register_resp_data

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
