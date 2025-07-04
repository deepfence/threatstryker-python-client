from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_fetch_window import ModelFetchWindow
    from ..models.model_node_identifier import ModelNodeIdentifier
    from ..models.reporters_fields_filters import ReportersFieldsFilters


T = TypeVar("T", bound="ModelScanListReq")


@_attrs_define
class ModelScanListReq:
    """
    Attributes:
        fields_filter (ReportersFieldsFilters):
        node_ids (Union[None, list['ModelNodeIdentifier']]):
        window (ModelFetchWindow):
    """

    fields_filter: "ReportersFieldsFilters"
    node_ids: Union[None, list["ModelNodeIdentifier"]]
    window: "ModelFetchWindow"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fields_filter = self.fields_filter.to_dict()

        node_ids: Union[None, list[dict[str, Any]]]
        if isinstance(self.node_ids, list):
            node_ids = []
            for node_ids_type_0_item_data in self.node_ids:
                node_ids_type_0_item = node_ids_type_0_item_data.to_dict()
                node_ids.append(node_ids_type_0_item)

        else:
            node_ids = self.node_ids

        window = self.window.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fields_filter": fields_filter,
                "node_ids": node_ids,
                "window": window,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_fetch_window import ModelFetchWindow
        from ..models.model_node_identifier import ModelNodeIdentifier
        from ..models.reporters_fields_filters import ReportersFieldsFilters

        d = dict(src_dict)
        fields_filter = ReportersFieldsFilters.from_dict(d.pop("fields_filter"))

        def _parse_node_ids(data: object) -> Union[None, list["ModelNodeIdentifier"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                node_ids_type_0 = []
                _node_ids_type_0 = data
                for node_ids_type_0_item_data in _node_ids_type_0:
                    node_ids_type_0_item = ModelNodeIdentifier.from_dict(node_ids_type_0_item_data)

                    node_ids_type_0.append(node_ids_type_0_item)

                return node_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["ModelNodeIdentifier"]], data)

        node_ids = _parse_node_ids(d.pop("node_ids"))

        window = ModelFetchWindow.from_dict(d.pop("window"))

        model_scan_list_req = cls(
            fields_filter=fields_filter,
            node_ids=node_ids,
            window=window,
        )

        model_scan_list_req.additional_properties = d
        return model_scan_list_req

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
