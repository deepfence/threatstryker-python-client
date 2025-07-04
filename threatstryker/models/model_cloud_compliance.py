from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_cloud_compliance_compliance_check_type import ModelCloudComplianceComplianceCheckType
from ..models.model_cloud_compliance_status import ModelCloudComplianceStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_basic_node import ModelBasicNode


T = TypeVar("T", bound="ModelCloudCompliance")


@_attrs_define
class ModelCloudCompliance:
    """
    Attributes:
        account_id (str):
        cloud_provider (str):
        compliance_check_type (ModelCloudComplianceComplianceCheckType):
        control_id (str):
        count (int):
        description (str):
        group (str):
        masked (bool):
        node_id (str):
        node_name (str):
        reason (str):
        region (str):
        resource (str):
        service (str):
        severity (str):
        status (ModelCloudComplianceStatus):
        title (str):
        type_ (str):
        updated_at (int):
        resources (Union[None, Unset, list['ModelBasicNode']]):
    """

    account_id: str
    cloud_provider: str
    compliance_check_type: ModelCloudComplianceComplianceCheckType
    control_id: str
    count: int
    description: str
    group: str
    masked: bool
    node_id: str
    node_name: str
    reason: str
    region: str
    resource: str
    service: str
    severity: str
    status: ModelCloudComplianceStatus
    title: str
    type_: str
    updated_at: int
    resources: Union[None, Unset, list["ModelBasicNode"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        cloud_provider = self.cloud_provider

        compliance_check_type = self.compliance_check_type.value

        control_id = self.control_id

        count = self.count

        description = self.description

        group = self.group

        masked = self.masked

        node_id = self.node_id

        node_name = self.node_name

        reason = self.reason

        region = self.region

        resource = self.resource

        service = self.service

        severity = self.severity

        status = self.status.value

        title = self.title

        type_ = self.type_

        updated_at = self.updated_at

        resources: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.resources, Unset):
            resources = UNSET
        elif isinstance(self.resources, list):
            resources = []
            for resources_type_0_item_data in self.resources:
                resources_type_0_item = resources_type_0_item_data.to_dict()
                resources.append(resources_type_0_item)

        else:
            resources = self.resources

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "cloud_provider": cloud_provider,
                "compliance_check_type": compliance_check_type,
                "control_id": control_id,
                "count": count,
                "description": description,
                "group": group,
                "masked": masked,
                "node_id": node_id,
                "node_name": node_name,
                "reason": reason,
                "region": region,
                "resource": resource,
                "service": service,
                "severity": severity,
                "status": status,
                "title": title,
                "type": type_,
                "updated_at": updated_at,
            }
        )
        if resources is not UNSET:
            field_dict["resources"] = resources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_basic_node import ModelBasicNode

        d = dict(src_dict)
        account_id = d.pop("account_id")

        cloud_provider = d.pop("cloud_provider")

        compliance_check_type = ModelCloudComplianceComplianceCheckType(d.pop("compliance_check_type"))

        control_id = d.pop("control_id")

        count = d.pop("count")

        description = d.pop("description")

        group = d.pop("group")

        masked = d.pop("masked")

        node_id = d.pop("node_id")

        node_name = d.pop("node_name")

        reason = d.pop("reason")

        region = d.pop("region")

        resource = d.pop("resource")

        service = d.pop("service")

        severity = d.pop("severity")

        status = ModelCloudComplianceStatus(d.pop("status"))

        title = d.pop("title")

        type_ = d.pop("type")

        updated_at = d.pop("updated_at")

        def _parse_resources(data: object) -> Union[None, Unset, list["ModelBasicNode"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                resources_type_0 = []
                _resources_type_0 = data
                for resources_type_0_item_data in _resources_type_0:
                    resources_type_0_item = ModelBasicNode.from_dict(resources_type_0_item_data)

                    resources_type_0.append(resources_type_0_item)

                return resources_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["ModelBasicNode"]], data)

        resources = _parse_resources(d.pop("resources", UNSET))

        model_cloud_compliance = cls(
            account_id=account_id,
            cloud_provider=cloud_provider,
            compliance_check_type=compliance_check_type,
            control_id=control_id,
            count=count,
            description=description,
            group=group,
            masked=masked,
            node_id=node_id,
            node_name=node_name,
            reason=reason,
            region=region,
            resource=resource,
            service=service,
            severity=severity,
            status=status,
            title=title,
            type_=type_,
            updated_at=updated_at,
            resources=resources,
        )

        model_cloud_compliance.additional_properties = d
        return model_cloud_compliance

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
