from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_mitre_attack_matrix_technique_summary_type_0 import ModelMitreAttackMatrixTechniqueSummaryType0


T = TypeVar("T", bound="ModelMitreAttackMatrix")


@_attrs_define
class ModelMitreAttackMatrix:
    """
    Attributes:
        count (int):
        tactic (str):
        technique_summary (Union['ModelMitreAttackMatrixTechniqueSummaryType0', None]):
    """

    count: int
    tactic: str
    technique_summary: Union["ModelMitreAttackMatrixTechniqueSummaryType0", None]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.model_mitre_attack_matrix_technique_summary_type_0 import (
            ModelMitreAttackMatrixTechniqueSummaryType0,
        )

        count = self.count

        tactic = self.tactic

        technique_summary: Union[Dict[str, Any], None]
        if isinstance(self.technique_summary, ModelMitreAttackMatrixTechniqueSummaryType0):
            technique_summary = self.technique_summary.to_dict()
        else:
            technique_summary = self.technique_summary

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
        from ..models.model_mitre_attack_matrix_technique_summary_type_0 import (
            ModelMitreAttackMatrixTechniqueSummaryType0,
        )

        d = src_dict.copy()
        count = d.pop("count")

        tactic = d.pop("tactic")

        def _parse_technique_summary(data: object) -> Union["ModelMitreAttackMatrixTechniqueSummaryType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                technique_summary_type_0 = ModelMitreAttackMatrixTechniqueSummaryType0.from_dict(data)

                return technique_summary_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ModelMitreAttackMatrixTechniqueSummaryType0", None], data)

        technique_summary = _parse_technique_summary(d.pop("technique_summary"))

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
