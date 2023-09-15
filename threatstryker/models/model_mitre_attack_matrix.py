from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_mitre_attack_matrix_technique_summary import ModelMitreAttackMatrixTechniqueSummary


T = TypeVar("T", bound="ModelMitreAttackMatrix")


@_attrs_define
class ModelMitreAttackMatrix:
    """
    Example:
        {'count': 0, 'technique_summary': {'key': {'severity': 'severity', 'count': 6}}, 'tactic': 'tactic'}

    Attributes:
        count (int):
        tactic (str):
        technique_summary (Optional[ModelMitreAttackMatrixTechniqueSummary]):
    """

    count: int
    tactic: str
    technique_summary: Optional["ModelMitreAttackMatrixTechniqueSummary"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count
        tactic = self.tactic
        technique_summary = self.technique_summary.to_dict() if self.technique_summary else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "tactic": tactic,
                "technique_summary": technique_summary,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_mitre_attack_matrix_technique_summary import ModelMitreAttackMatrixTechniqueSummary

        d = src_dict.copy()
        count = d.pop("count")

        tactic = d.pop("tactic")

        _technique_summary = d.pop("technique_summary")
        technique_summary: Optional[ModelMitreAttackMatrixTechniqueSummary]
        if _technique_summary is None:
            technique_summary = None
        else:
            technique_summary = ModelMitreAttackMatrixTechniqueSummary.from_dict(_technique_summary)

        model_mitre_attack_matrix = cls(
            count=count,
            tactic=tactic,
            technique_summary=technique_summary,
        )

        model_mitre_attack_matrix.additional_properties = d
        return model_mitre_attack_matrix

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
