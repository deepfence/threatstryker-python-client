from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_add_scheduled_task_request_action import ModelAddScheduledTaskRequestAction
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_node_identifier import ModelNodeIdentifier
    from ..models.model_scan_filter import ModelScanFilter
    from ..models.model_vulnerability_scan_config_language import ModelVulnerabilityScanConfigLanguage


T = TypeVar("T", bound="ModelAddScheduledTaskRequest")


@_attrs_define
class ModelAddScheduledTaskRequest:
    """
    Example:
        {'benchmark_types': ['benchmark_types', 'benchmark_types'], 'scan_config': [{'language': 'base'}, {'language':
            'base'}], 'cron_expr': 'cron_expr', 'action': 'SecretScan', 'description': 'description', 'filters':
            {'container_scan_filter': {'filter_in': {'key': ['', '']}}, 'cloud_account_scan_filter': {'filter_in': {'key':
            ['', '']}}, 'image_scan_filter': {'filter_in': {'key': ['', '']}}, 'kubernetes_cluster_scan_filter':
            {'filter_in': {'key': ['', '']}}, 'host_scan_filter': {'filter_in': {'key': ['', '']}}}, 'node_ids':
            [{'node_type': 'image', 'node_id': 'node_id'}, {'node_type': 'image', 'node_id': 'node_id'}]}

    Attributes:
        action (ModelAddScheduledTaskRequestAction):
        filters (ModelScanFilter):  Example: {'container_scan_filter': {'filter_in': {'key': ['', '']}},
            'cloud_account_scan_filter': {'filter_in': {'key': ['', '']}}, 'image_scan_filter': {'filter_in': {'key': ['',
            '']}}, 'kubernetes_cluster_scan_filter': {'filter_in': {'key': ['', '']}}, 'host_scan_filter': {'filter_in':
            {'key': ['', '']}}}.
        benchmark_types (Optional[List[str]]):
        cron_expr (Union[Unset, str]):
        description (Union[Unset, str]):
        node_ids (Optional[List['ModelNodeIdentifier']]):
        scan_config (Optional[List['ModelVulnerabilityScanConfigLanguage']]):
    """

    action: ModelAddScheduledTaskRequestAction
    filters: "ModelScanFilter"
    benchmark_types: Optional[List[str]]
    node_ids: Optional[List["ModelNodeIdentifier"]]
    scan_config: Optional[List["ModelVulnerabilityScanConfigLanguage"]]
    cron_expr: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action = self.action.value

        filters = self.filters.to_dict()

        if self.benchmark_types is None:
            benchmark_types = None
        else:
            benchmark_types = self.benchmark_types

        cron_expr = self.cron_expr
        description = self.description
        if self.node_ids is None:
            node_ids = None
        else:
            node_ids = []
            for node_ids_item_data in self.node_ids:
                node_ids_item = node_ids_item_data.to_dict()

                node_ids.append(node_ids_item)

        if self.scan_config is None:
            scan_config = None
        else:
            scan_config = []
            for scan_config_item_data in self.scan_config:
                scan_config_item = scan_config_item_data.to_dict()

                scan_config.append(scan_config_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "filters": filters,
                "benchmark_types": benchmark_types,
                "node_ids": node_ids,
                "scan_config": scan_config,
            }
        )
        if cron_expr is not UNSET:
            field_dict["cron_expr"] = cron_expr
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_node_identifier import ModelNodeIdentifier
        from ..models.model_scan_filter import ModelScanFilter
        from ..models.model_vulnerability_scan_config_language import ModelVulnerabilityScanConfigLanguage

        d = src_dict.copy()
        action = ModelAddScheduledTaskRequestAction(d.pop("action"))

        filters = ModelScanFilter.from_dict(d.pop("filters"))

        benchmark_types = cast(List[str], d.pop("benchmark_types"))

        cron_expr = d.pop("cron_expr", UNSET)

        description = d.pop("description", UNSET)

        node_ids = []
        _node_ids = d.pop("node_ids")
        for node_ids_item_data in _node_ids or []:
            node_ids_item = ModelNodeIdentifier.from_dict(node_ids_item_data)

            node_ids.append(node_ids_item)

        scan_config = []
        _scan_config = d.pop("scan_config")
        for scan_config_item_data in _scan_config or []:
            scan_config_item = ModelVulnerabilityScanConfigLanguage.from_dict(scan_config_item_data)

            scan_config.append(scan_config_item)

        model_add_scheduled_task_request = cls(
            action=action,
            filters=filters,
            benchmark_types=benchmark_types,
            cron_expr=cron_expr,
            description=description,
            node_ids=node_ids,
            scan_config=scan_config,
        )

        model_add_scheduled_task_request.additional_properties = d
        return model_add_scheduled_task_request

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
