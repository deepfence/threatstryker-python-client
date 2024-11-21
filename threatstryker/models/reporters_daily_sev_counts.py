from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.reporters_daily_sev_counts_days_to_sev_counts_type_0 import (
        ReportersDailySevCountsDaysToSevCountsType0,
    )


T = TypeVar("T", bound="ReportersDailySevCounts")


@_attrs_define
class ReportersDailySevCounts:
    """
    Example:
        {'days_to_sev_counts': {'key': {'counts': {'key': 0}}}}

    Attributes:
        days_to_sev_counts (Union['ReportersDailySevCountsDaysToSevCountsType0', None]):
    """

    days_to_sev_counts: Union["ReportersDailySevCountsDaysToSevCountsType0", None]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.reporters_daily_sev_counts_days_to_sev_counts_type_0 import (
            ReportersDailySevCountsDaysToSevCountsType0,
        )

        days_to_sev_counts: Union[Dict[str, Any], None]
        if isinstance(self.days_to_sev_counts, ReportersDailySevCountsDaysToSevCountsType0):
            days_to_sev_counts = self.days_to_sev_counts.to_dict()
        else:
            days_to_sev_counts = self.days_to_sev_counts

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
        from ..models.reporters_daily_sev_counts_days_to_sev_counts_type_0 import (
            ReportersDailySevCountsDaysToSevCountsType0,
        )

        d = src_dict.copy()

        def _parse_days_to_sev_counts(data: object) -> Union["ReportersDailySevCountsDaysToSevCountsType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                days_to_sev_counts_type_0 = ReportersDailySevCountsDaysToSevCountsType0.from_dict(data)

                return days_to_sev_counts_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ReportersDailySevCountsDaysToSevCountsType0", None], data)

        days_to_sev_counts = _parse_days_to_sev_counts(d.pop("days_to_sev_counts"))

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
