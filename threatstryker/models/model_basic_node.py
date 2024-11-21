from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelBasicNode")


@_attrs_define
class ModelBasicNode:
    """
    Example:
        {'node_type': 'node_type', 'live_secrets': ['live_secrets', 'live_secrets'], 'live_cves': ['live_cves',
            'live_cves'], 'name': 'name', 'host_name': 'host_name', 'live_malwares': ['live_malwares', 'live_malwares'],
            'node_id': 'node_id'}

    Attributes:
        host_name (str):
        live_cves (Union[List[str], None]):
        live_malwares (Union[List[str], None]):
        live_secrets (Union[List[str], None]):
        name (str):
        node_id (str):
        node_type (str):
    """

    host_name: str
    live_cves: Union[List[str], None]
    live_malwares: Union[List[str], None]
    live_secrets: Union[List[str], None]
    name: str
    node_id: str
    node_type: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        host_name = self.host_name

        live_cves: Union[List[str], None]
        if isinstance(self.live_cves, list):
            live_cves = self.live_cves

        else:
            live_cves = self.live_cves

        live_malwares: Union[List[str], None]
        if isinstance(self.live_malwares, list):
            live_malwares = self.live_malwares

        else:
            live_malwares = self.live_malwares

        live_secrets: Union[List[str], None]
        if isinstance(self.live_secrets, list):
            live_secrets = self.live_secrets

        else:
            live_secrets = self.live_secrets

        name = self.name

        node_id = self.node_id

        node_type = self.node_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        host_name = d.pop("host_name")

        def _parse_live_cves(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                live_cves_type_0 = cast(List[str], data)

                return live_cves_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

        live_cves = _parse_live_cves(d.pop("live_cves"))

        def _parse_live_malwares(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                live_malwares_type_0 = cast(List[str], data)

                return live_malwares_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

        live_malwares = _parse_live_malwares(d.pop("live_malwares"))

        def _parse_live_secrets(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                live_secrets_type_0 = cast(List[str], data)

                return live_secrets_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

        live_secrets = _parse_live_secrets(d.pop("live_secrets"))

        name = d.pop("name")

        node_id = d.pop("node_id")

        node_type = d.pop("node_type")

        model_basic_node = cls(
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
