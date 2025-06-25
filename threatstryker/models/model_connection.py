from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelConnection")


@_attrs_define
class ModelConnection:
    """
    Attributes:
        count (Union[Unset, int]):
        ips (Union[None, Unset, list[Any]]):
        malicious_ip (Union[None, Unset, list[bool]]):
        node_id (Union[Unset, str]):
        node_name (Union[Unset, str]):
    """

    count: Union[Unset, int] = UNSET
    ips: Union[None, Unset, list[Any]] = UNSET
    malicious_ip: Union[None, Unset, list[bool]] = UNSET
    node_id: Union[Unset, str] = UNSET
    node_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        ips: Union[None, Unset, list[Any]]
        if isinstance(self.ips, Unset):
            ips = UNSET
        elif isinstance(self.ips, list):
            ips = self.ips

        else:
            ips = self.ips

        malicious_ip: Union[None, Unset, list[bool]]
        if isinstance(self.malicious_ip, Unset):
            malicious_ip = UNSET
        elif isinstance(self.malicious_ip, list):
            malicious_ip = self.malicious_ip

        else:
            malicious_ip = self.malicious_ip

        node_id = self.node_id

        node_name = self.node_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if ips is not UNSET:
            field_dict["ips"] = ips
        if malicious_ip is not UNSET:
            field_dict["malicious_ip"] = malicious_ip
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if node_name is not UNSET:
            field_dict["node_name"] = node_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        def _parse_ips(data: object) -> Union[None, Unset, list[Any]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ips_type_0 = cast(list[Any], data)

                return ips_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[Any]], data)

        ips = _parse_ips(d.pop("ips", UNSET))

        def _parse_malicious_ip(data: object) -> Union[None, Unset, list[bool]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                malicious_ip_type_0 = cast(list[bool], data)

                return malicious_ip_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[bool]], data)

        malicious_ip = _parse_malicious_ip(d.pop("malicious_ip", UNSET))

        node_id = d.pop("node_id", UNSET)

        node_name = d.pop("node_name", UNSET)

        model_connection = cls(
            count=count,
            ips=ips,
            malicious_ip=malicious_ip,
            node_id=node_id,
            node_name=node_name,
        )

        model_connection.additional_properties = d
        return model_connection

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
