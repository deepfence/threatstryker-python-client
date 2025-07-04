from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_compliance_scan_results_group_resp_groups_type_0 import (
        ModelComplianceScanResultsGroupRespGroupsType0,
    )


T = TypeVar("T", bound="ModelComplianceScanResultsGroupResp")


@_attrs_define
class ModelComplianceScanResultsGroupResp:
    """
    Attributes:
        groups (Union['ModelComplianceScanResultsGroupRespGroupsType0', None, Unset]):
    """

    groups: Union["ModelComplianceScanResultsGroupRespGroupsType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.model_compliance_scan_results_group_resp_groups_type_0 import (
            ModelComplianceScanResultsGroupRespGroupsType0,
        )

        groups: Union[None, Unset, dict[str, Any]]
        if isinstance(self.groups, Unset):
            groups = UNSET
        elif isinstance(self.groups, ModelComplianceScanResultsGroupRespGroupsType0):
            groups = self.groups.to_dict()
        else:
            groups = self.groups

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_compliance_scan_results_group_resp_groups_type_0 import (
            ModelComplianceScanResultsGroupRespGroupsType0,
        )

        d = dict(src_dict)

        def _parse_groups(data: object) -> Union["ModelComplianceScanResultsGroupRespGroupsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                groups_type_0 = ModelComplianceScanResultsGroupRespGroupsType0.from_dict(data)

                return groups_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ModelComplianceScanResultsGroupRespGroupsType0", None, Unset], data)

        groups = _parse_groups(d.pop("groups", UNSET))

        model_compliance_scan_results_group_resp = cls(
            groups=groups,
        )

        model_compliance_scan_results_group_resp.additional_properties = d
        return model_compliance_scan_results_group_resp

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
