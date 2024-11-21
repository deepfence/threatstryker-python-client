from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.reporters_sev_counts_counts_type_0 import ReportersSevCountsCountsType0


T = TypeVar("T", bound="ReportersSevCounts")


@_attrs_define
class ReportersSevCounts:
    """
    Example:
        {'counts': {'key': 0}}

    Attributes:
        counts (Union['ReportersSevCountsCountsType0', None]):
    """

    counts: Union["ReportersSevCountsCountsType0", None]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.reporters_sev_counts_counts_type_0 import ReportersSevCountsCountsType0

        counts: Union[Dict[str, Any], None]
        if isinstance(self.counts, ReportersSevCountsCountsType0):
            counts = self.counts.to_dict()
        else:
            counts = self.counts

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
        from ..models.reporters_sev_counts_counts_type_0 import ReportersSevCountsCountsType0

        d = src_dict.copy()

        def _parse_counts(data: object) -> Union["ReportersSevCountsCountsType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                counts_type_0 = ReportersSevCountsCountsType0.from_dict(data)

                return counts_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ReportersSevCountsCountsType0", None], data)

        counts = _parse_counts(d.pop("counts"))

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
