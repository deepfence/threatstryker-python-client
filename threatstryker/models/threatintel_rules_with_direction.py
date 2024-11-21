from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.threatintel_rules_with_direction_inbound_type_0 import ThreatintelRulesWithDirectionInboundType0
    from ..models.threatintel_rules_with_direction_outbound_type_0 import ThreatintelRulesWithDirectionOutboundType0


T = TypeVar("T", bound="ThreatintelRulesWithDirection")


@_attrs_define
class ThreatintelRulesWithDirection:
    """
    Example:
        {'inbound': {'key': 'inbound'}, 'outbound': {'key': 'outbound'}}

    Attributes:
        inbound (Union['ThreatintelRulesWithDirectionInboundType0', None, Unset]):
        outbound (Union['ThreatintelRulesWithDirectionOutboundType0', None, Unset]):
    """

    inbound: Union["ThreatintelRulesWithDirectionInboundType0", None, Unset] = UNSET
    outbound: Union["ThreatintelRulesWithDirectionOutboundType0", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.threatintel_rules_with_direction_inbound_type_0 import ThreatintelRulesWithDirectionInboundType0
        from ..models.threatintel_rules_with_direction_outbound_type_0 import ThreatintelRulesWithDirectionOutboundType0

        inbound: Union[Dict[str, Any], None, Unset]
        if isinstance(self.inbound, Unset):
            inbound = UNSET
        elif isinstance(self.inbound, ThreatintelRulesWithDirectionInboundType0):
            inbound = self.inbound.to_dict()
        else:
            inbound = self.inbound

        outbound: Union[Dict[str, Any], None, Unset]
        if isinstance(self.outbound, Unset):
            outbound = UNSET
        elif isinstance(self.outbound, ThreatintelRulesWithDirectionOutboundType0):
            outbound = self.outbound.to_dict()
        else:
            outbound = self.outbound

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inbound is not UNSET:
            field_dict["inbound"] = inbound
        if outbound is not UNSET:
            field_dict["outbound"] = outbound

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.threatintel_rules_with_direction_inbound_type_0 import ThreatintelRulesWithDirectionInboundType0
        from ..models.threatintel_rules_with_direction_outbound_type_0 import ThreatintelRulesWithDirectionOutboundType0

        d = src_dict.copy()

        def _parse_inbound(data: object) -> Union["ThreatintelRulesWithDirectionInboundType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                inbound_type_0 = ThreatintelRulesWithDirectionInboundType0.from_dict(data)

                return inbound_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ThreatintelRulesWithDirectionInboundType0", None, Unset], data)

        inbound = _parse_inbound(d.pop("inbound", UNSET))

        def _parse_outbound(data: object) -> Union["ThreatintelRulesWithDirectionOutboundType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                outbound_type_0 = ThreatintelRulesWithDirectionOutboundType0.from_dict(data)

                return outbound_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ThreatintelRulesWithDirectionOutboundType0", None, Unset], data)

        outbound = _parse_outbound(d.pop("outbound", UNSET))

        threatintel_rules_with_direction = cls(
            inbound=inbound,
            outbound=outbound,
        )

        threatintel_rules_with_direction.additional_properties = d
        return threatintel_rules_with_direction

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
