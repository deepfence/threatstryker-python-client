from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelCloudNodeComplianceControl")


@_attrs_define
class ModelCloudNodeComplianceControl:
    """
    Attributes:
        category_hierarchy (Union[None, Unset, list[str]]):
        category_hierarchy_short (Union[Unset, str]):
        compliance_type (Union[Unset, str]):
        control_id (Union[Unset, str]):
        description (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        node_id (Union[Unset, str]):
        problem_title (Union[Unset, str]):
        service (Union[Unset, str]):
        title (Union[Unset, str]):
    """

    category_hierarchy: Union[None, Unset, list[str]] = UNSET
    category_hierarchy_short: Union[Unset, str] = UNSET
    compliance_type: Union[Unset, str] = UNSET
    control_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    node_id: Union[Unset, str] = UNSET
    problem_title: Union[Unset, str] = UNSET
    service: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category_hierarchy: Union[None, Unset, list[str]]
        if isinstance(self.category_hierarchy, Unset):
            category_hierarchy = UNSET
        elif isinstance(self.category_hierarchy, list):
            category_hierarchy = self.category_hierarchy

        else:
            category_hierarchy = self.category_hierarchy

        category_hierarchy_short = self.category_hierarchy_short

        compliance_type = self.compliance_type

        control_id = self.control_id

        description = self.description

        enabled = self.enabled

        node_id = self.node_id

        problem_title = self.problem_title

        service = self.service

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category_hierarchy is not UNSET:
            field_dict["category_hierarchy"] = category_hierarchy
        if category_hierarchy_short is not UNSET:
            field_dict["category_hierarchy_short"] = category_hierarchy_short
        if compliance_type is not UNSET:
            field_dict["compliance_type"] = compliance_type
        if control_id is not UNSET:
            field_dict["control_id"] = control_id
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if problem_title is not UNSET:
            field_dict["problem_title"] = problem_title
        if service is not UNSET:
            field_dict["service"] = service
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_category_hierarchy(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                category_hierarchy_type_0 = cast(list[str], data)

                return category_hierarchy_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        category_hierarchy = _parse_category_hierarchy(d.pop("category_hierarchy", UNSET))

        category_hierarchy_short = d.pop("category_hierarchy_short", UNSET)

        compliance_type = d.pop("compliance_type", UNSET)

        control_id = d.pop("control_id", UNSET)

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        node_id = d.pop("node_id", UNSET)

        problem_title = d.pop("problem_title", UNSET)

        service = d.pop("service", UNSET)

        title = d.pop("title", UNSET)

        model_cloud_node_compliance_control = cls(
            category_hierarchy=category_hierarchy,
            category_hierarchy_short=category_hierarchy_short,
            compliance_type=compliance_type,
            control_id=control_id,
            description=description,
            enabled=enabled,
            node_id=node_id,
            problem_title=problem_title,
            service=service,
            title=title,
        )

        model_cloud_node_compliance_control.additional_properties = d
        return model_cloud_node_compliance_control

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
