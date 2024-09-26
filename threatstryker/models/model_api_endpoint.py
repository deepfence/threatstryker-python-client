from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_api_endpoint_direction import ModelAPIEndpointDirection
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelAPIEndpoint")


@_attrs_define
class ModelAPIEndpoint:
    """
    Attributes:
        cloud_provider (Union[Unset, str]):
        cloud_region (Union[Unset, str]):
        cloud_type (Union[Unset, str]):
        created_at (Union[Unset, int]):
        direction (Union[Unset, ModelAPIEndpointDirection]):
        host (Union[Unset, str]):
        host_ip (Union[Unset, str]):
        method (Union[Unset, str]):
        path (Union[Unset, str]):
        port (Union[Unset, int]):
        schema_info (Union[Unset, str]):
        source_hosts (Union[List[str], None, Unset]):
        updated_at (Union[Unset, int]):
    """

    cloud_provider: Union[Unset, str] = UNSET
    cloud_region: Union[Unset, str] = UNSET
    cloud_type: Union[Unset, str] = UNSET
    created_at: Union[Unset, int] = UNSET
    direction: Union[Unset, ModelAPIEndpointDirection] = UNSET
    host: Union[Unset, str] = UNSET
    host_ip: Union[Unset, str] = UNSET
    method: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    schema_info: Union[Unset, str] = UNSET
    source_hosts: Union[List[str], None, Unset] = UNSET
    updated_at: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cloud_provider = self.cloud_provider

        cloud_region = self.cloud_region

        cloud_type = self.cloud_type

        created_at = self.created_at

        direction: Union[Unset, str] = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value

        host = self.host

        host_ip = self.host_ip

        method = self.method

        path = self.path

        port = self.port

        schema_info = self.schema_info

        source_hosts: Union[List[str], None, Unset]
        if isinstance(self.source_hosts, Unset):
            source_hosts = UNSET
        elif isinstance(self.source_hosts, list):
            source_hosts = self.source_hosts

        else:
            source_hosts = self.source_hosts

        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cloud_provider is not UNSET:
            field_dict["cloud_provider"] = cloud_provider
        if cloud_region is not UNSET:
            field_dict["cloud_region"] = cloud_region
        if cloud_type is not UNSET:
            field_dict["cloud_type"] = cloud_type
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if direction is not UNSET:
            field_dict["direction"] = direction
        if host is not UNSET:
            field_dict["host"] = host
        if host_ip is not UNSET:
            field_dict["host_ip"] = host_ip
        if method is not UNSET:
            field_dict["method"] = method
        if path is not UNSET:
            field_dict["path"] = path
        if port is not UNSET:
            field_dict["port"] = port
        if schema_info is not UNSET:
            field_dict["schema_info"] = schema_info
        if source_hosts is not UNSET:
            field_dict["source_hosts"] = source_hosts
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cloud_provider = d.pop("cloud_provider", UNSET)

        cloud_region = d.pop("cloud_region", UNSET)

        cloud_type = d.pop("cloud_type", UNSET)

        created_at = d.pop("created_at", UNSET)

        _direction = d.pop("direction", UNSET)
        direction: Union[Unset, ModelAPIEndpointDirection]
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = ModelAPIEndpointDirection(_direction)

        host = d.pop("host", UNSET)

        host_ip = d.pop("host_ip", UNSET)

        method = d.pop("method", UNSET)

        path = d.pop("path", UNSET)

        port = d.pop("port", UNSET)

        schema_info = d.pop("schema_info", UNSET)

        def _parse_source_hosts(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                source_hosts_type_0 = cast(List[str], data)

                return source_hosts_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        source_hosts = _parse_source_hosts(d.pop("source_hosts", UNSET))

        updated_at = d.pop("updated_at", UNSET)

        model_api_endpoint = cls(
            cloud_provider=cloud_provider,
            cloud_region=cloud_region,
            cloud_type=cloud_type,
            created_at=created_at,
            direction=direction,
            host=host,
            host_ip=host_ip,
            method=method,
            path=path,
            port=port,
            schema_info=schema_info,
            source_hosts=source_hosts,
            updated_at=updated_at,
        )

        model_api_endpoint.additional_properties = d
        return model_api_endpoint

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
