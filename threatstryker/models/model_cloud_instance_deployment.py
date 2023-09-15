from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelCloudInstanceDeployment")


@_attrs_define
class ModelCloudInstanceDeployment:
    """
    Example:
        {'hostname': 'hostname', 'account_id': 'account_id', 'instance_id': 'instance_id', 'region': 'region'}

    Attributes:
        account_id (Union[Unset, str]):
        hostname (Union[Unset, str]):
        instance_id (Union[Unset, str]):
        region (Union[Unset, str]):
    """

    account_id: Union[Unset, str] = UNSET
    hostname: Union[Unset, str] = UNSET
    instance_id: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id
        hostname = self.hostname
        instance_id = self.instance_id
        region = self.region

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if instance_id is not UNSET:
            field_dict["instance_id"] = instance_id
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("account_id", UNSET)

        hostname = d.pop("hostname", UNSET)

        instance_id = d.pop("instance_id", UNSET)

        region = d.pop("region", UNSET)

        model_cloud_instance_deployment = cls(
            account_id=account_id,
            hostname=hostname,
            instance_id=instance_id,
            region=region,
        )

        model_cloud_instance_deployment.additional_properties = d
        return model_cloud_instance_deployment

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
