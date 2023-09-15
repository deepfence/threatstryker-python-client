from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.reporters_daily_sev_counts_days_to_sev_counts import ReportersDailySevCountsDaysToSevCounts


T = TypeVar("T", bound="ReportersDailySevCounts")


@_attrs_define
class ReportersDailySevCounts:
    """
    Example:
        {'days_to_sev_counts': {'key': {'counts': {'key': 0}}}}

    Attributes:
        days_to_sev_counts (Optional[ReportersDailySevCountsDaysToSevCounts]):
    """

    days_to_sev_counts: Optional["ReportersDailySevCountsDaysToSevCounts"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        days_to_sev_counts = self.days_to_sev_counts.to_dict() if self.days_to_sev_counts else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "days_to_sev_counts": days_to_sev_counts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reporters_daily_sev_counts_days_to_sev_counts import ReportersDailySevCountsDaysToSevCounts

        d = src_dict.copy()
        _days_to_sev_counts = d.pop("days_to_sev_counts")
        days_to_sev_counts: Optional[ReportersDailySevCountsDaysToSevCounts]
        if _days_to_sev_counts is None:
            days_to_sev_counts = None
        else:
            days_to_sev_counts = ReportersDailySevCountsDaysToSevCounts.from_dict(_days_to_sev_counts)

        reporters_daily_sev_counts = cls(
            days_to_sev_counts=days_to_sev_counts,
        )

        reporters_daily_sev_counts.additional_properties = d
        return reporters_daily_sev_counts

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
