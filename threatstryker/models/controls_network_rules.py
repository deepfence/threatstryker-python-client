from typing import Any, Dict, List, Optional, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ControlsNetworkRules")


@_attrs_define
class ControlsNetworkRules:
    """
    Example:
        {'inbound': ['inbound', 'inbound'], 'outbound': ['outbound', 'outbound']}

    Attributes:
        inbound (Optional[List[str]]):
        outbound (Optional[List[str]]):
    """

    inbound: Optional[List[str]]
    outbound: Optional[List[str]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if self.inbound is None:
            inbound = None
        else:
            inbound = self.inbound

        if self.outbound is None:
            outbound = None
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
        inbound = cast(List[str], d.pop("inbound"))

        outbound = cast(List[str], d.pop("outbound"))

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
