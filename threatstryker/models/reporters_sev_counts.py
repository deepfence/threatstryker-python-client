from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.reporters_sev_counts_counts import ReportersSevCountsCounts


T = TypeVar("T", bound="ReportersSevCounts")


@_attrs_define
class ReportersSevCounts:
    """
    Example:
        {'counts': {'key': 0}}

    Attributes:
        counts (Optional[ReportersSevCountsCounts]):
    """

    counts: Optional["ReportersSevCountsCounts"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        counts = self.counts.to_dict() if self.counts else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "counts": counts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reporters_sev_counts_counts import ReportersSevCountsCounts

        d = src_dict.copy()
        _counts = d.pop("counts")
        counts: Optional[ReportersSevCountsCounts]
        if _counts is None:
            counts = None
        else:
            counts = ReportersSevCountsCounts.from_dict(_counts)

        reporters_sev_counts = cls(
            counts=counts,
        )

        reporters_sev_counts.additional_properties = d
        return reporters_sev_counts

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
