from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ControlsNetworkRules")


@_attrs_define
class ControlsNetworkRules:
    """
    Example:
        {'inbound': ['inbound', 'inbound'], 'outbound': ['outbound', 'outbound']}

    Attributes:
        inbound (Union[List[str], None]):
        outbound (Union[List[str], None]):
    """

    inbound: Union[List[str], None]
    outbound: Union[List[str], None]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        inbound: Union[List[str], None]
        if isinstance(self.inbound, list):
            inbound = self.inbound

        else:
            inbound = self.inbound

        outbound: Union[List[str], None]
        if isinstance(self.outbound, list):
            outbound = self.outbound

        else:
            outbound = self.outbound

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inbound": inbound,
                "outbound": outbound,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_inbound(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                inbound_type_0 = cast(List[str], data)

                return inbound_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

        inbound = _parse_inbound(d.pop("inbound"))

        def _parse_outbound(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                outbound_type_0 = cast(List[str], data)

                return outbound_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

        outbound = _parse_outbound(d.pop("outbound"))

        controls_network_rules = cls(
            inbound=inbound,
            outbound=outbound,
        )

        controls_network_rules.additional_properties = d
        return controls_network_rules

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
