from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelCloudNodeComplianceControl")


@_attrs_define
class ModelCloudNodeComplianceControl:
    """
    Attributes:
        category_hierarchy (Union[List[str], None, Unset]):
        control_id (Union[Unset, str]):
        description (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        service (Union[Unset, str]):
        title (Union[Unset, str]):
    """

    category_hierarchy: Union[List[str], None, Unset] = UNSET
    control_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    service: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category_hierarchy: Union[List[str], None, Unset]
        if isinstance(self.category_hierarchy, Unset):
            category_hierarchy = UNSET
        elif isinstance(self.category_hierarchy, list):
            category_hierarchy = self.category_hierarchy

        else:
            category_hierarchy = self.category_hierarchy

        control_id = self.control_id

        description = self.description

        enabled = self.enabled

        service = self.service

        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category_hierarchy is not UNSET:
            field_dict["category_hierarchy"] = category_hierarchy
        if control_id is not UNSET:
            field_dict["control_id"] = control_id
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if service is not UNSET:
            field_dict["service"] = service
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_category_hierarchy(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                category_hierarchy_type_0 = cast(List[str], data)

                return category_hierarchy_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        category_hierarchy = _parse_category_hierarchy(d.pop("category_hierarchy", UNSET))

        control_id = d.pop("control_id", UNSET)

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        service = d.pop("service", UNSET)

        title = d.pop("title", UNSET)

        model_cloud_node_compliance_control = cls(
            category_hierarchy=category_hierarchy,
            control_id=control_id,
            description=description,
            enabled=enabled,
            service=service,
            title=title,
        )

        model_cloud_node_compliance_control.additional_properties = d
        return model_cloud_node_compliance_control

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
