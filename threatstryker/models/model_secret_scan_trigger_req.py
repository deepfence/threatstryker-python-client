from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_node_identifier import ModelNodeIdentifier
    from ..models.model_scan_filter import ModelScanFilter


T = TypeVar("T", bound="ModelSecretScanTriggerReq")


@_attrs_define
class ModelSecretScanTriggerReq:
    """
    Example:
        {'is_priority': True, 'filters': {'container_scan_filter': {'filter_in': {'key': ['', '']}},
            'cloud_account_scan_filter': {'filter_in': {'key': ['', '']}}, 'image_scan_filter': {'filter_in': {'key': ['',
            '']}}, 'kubernetes_cluster_scan_filter': {'filter_in': {'key': ['', '']}}, 'host_scan_filter': {'filter_in':
            {'key': ['', '']}}}, 'node_ids': [{'node_type': 'image', 'node_id': 'node_id'}, {'node_type': 'image',
            'node_id': 'node_id'}]}

    Attributes:
        filters (ModelScanFilter):  Example: {'container_scan_filter': {'filter_in': {'key': ['', '']}},
            'cloud_account_scan_filter': {'filter_in': {'key': ['', '']}}, 'image_scan_filter': {'filter_in': {'key': ['',
            '']}}, 'kubernetes_cluster_scan_filter': {'filter_in': {'key': ['', '']}}, 'host_scan_filter': {'filter_in':
            {'key': ['', '']}}}.
        is_priority (Union[Unset, bool]):
        node_ids (Optional[List['ModelNodeIdentifier']]):
    """

    filters: "ModelScanFilter"
    node_ids: Optional[List["ModelNodeIdentifier"]]
    is_priority: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filters = self.filters.to_dict()

        is_priority = self.is_priority
        if self.node_ids is None:
            node_ids = None
        else:
            node_ids = []
            for node_ids_item_data in self.node_ids:
                node_ids_item = node_ids_item_data.to_dict()

                node_ids.append(node_ids_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filters": filters,
                "node_ids": node_ids,
            }
        )
        if is_priority is not UNSET:
            field_dict["is_priority"] = is_priority

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_node_identifier import ModelNodeIdentifier
        from ..models.model_scan_filter import ModelScanFilter

        d = src_dict.copy()
        filters = ModelScanFilter.from_dict(d.pop("filters"))

        is_priority = d.pop("is_priority", UNSET)

        node_ids = []
        _node_ids = d.pop("node_ids")
        for node_ids_item_data in _node_ids or []:
            node_ids_item = ModelNodeIdentifier.from_dict(node_ids_item_data)

            node_ids.append(node_ids_item)

        model_secret_scan_trigger_req = cls(
            filters=filters,
            is_priority=is_priority,
            node_ids=node_ids,
        )

        model_secret_scan_trigger_req.additional_properties = d
        return model_secret_scan_trigger_req

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
