from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelBasicNode")


@_attrs_define
class ModelBasicNode:
    """
    Attributes:
        active (bool):
        host_name (str):
        live_cves (Union[None, list[str]]):
        live_malwares (Union[None, list[str]]):
        live_secrets (Union[None, list[str]]):
        name (str):
        node_id (str):
        node_type (str):
    """

    active: bool
    host_name: str
    live_cves: Union[None, list[str]]
    live_malwares: Union[None, list[str]]
    live_secrets: Union[None, list[str]]
    name: str
    node_id: str
    node_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active = self.active

        host_name = self.host_name

        live_cves: Union[None, list[str]]
        if isinstance(self.live_cves, list):
            live_cves = self.live_cves

        else:
            live_cves = self.live_cves

        live_malwares: Union[None, list[str]]
        if isinstance(self.live_malwares, list):
            live_malwares = self.live_malwares

        else:
            live_malwares = self.live_malwares

        live_secrets: Union[None, list[str]]
        if isinstance(self.live_secrets, list):
            live_secrets = self.live_secrets

        else:
            live_secrets = self.live_secrets

        name = self.name

        node_id = self.node_id

        node_type = self.node_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active": active,
                "host_name": host_name,
                "live_cves": live_cves,
                "live_malwares": live_malwares,
                "live_secrets": live_secrets,
                "name": name,
                "node_id": node_id,
                "node_type": node_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active = d.pop("active")

        host_name = d.pop("host_name")

        def _parse_live_cves(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                live_cves_type_0 = cast(list[str], data)

                return live_cves_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        live_cves = _parse_live_cves(d.pop("live_cves"))

        def _parse_live_malwares(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                live_malwares_type_0 = cast(list[str], data)

                return live_malwares_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        live_malwares = _parse_live_malwares(d.pop("live_malwares"))

        def _parse_live_secrets(data: object) -> Union[None, list[str]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                live_secrets_type_0 = cast(list[str], data)

                return live_secrets_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str]], data)

        live_secrets = _parse_live_secrets(d.pop("live_secrets"))

        name = d.pop("name")

        node_id = d.pop("node_id")

        node_type = d.pop("node_type")

        model_basic_node = cls(
            active=active,
            host_name=host_name,
            live_cves=live_cves,
            live_malwares=live_malwares,
            live_secrets=live_secrets,
            name=name,
            node_id=node_id,
            node_type=node_type,
        )

        model_basic_node.additional_properties = d
        return model_basic_node

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
