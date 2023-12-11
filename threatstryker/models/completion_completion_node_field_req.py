from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_fetch_window import ModelFetchWindow


T = TypeVar("T", bound="CompletionCompletionNodeFieldReq")


@_attrs_define
class CompletionCompletionNodeFieldReq:
    """
    Example:
        {'completion': 'completion', 'scan_id': 'scan_id', 'window': {'offset': 0, 'size': 6}, 'field_name':
            'field_name'}

    Attributes:
        completion (str):
        field_name (str):
        window (ModelFetchWindow):  Example: {'offset': 0, 'size': 6}.
        scan_id (Union[Unset, str]):
    """

    completion: str
    field_name: str
    window: "ModelFetchWindow"
    scan_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        completion = self.completion
        field_name = self.field_name
        window = self.window.to_dict()

        scan_id = self.scan_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "completion": completion,
                "field_name": field_name,
                "window": window,
            }
        )
        if scan_id is not UNSET:
            field_dict["scan_id"] = scan_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_fetch_window import ModelFetchWindow

        d = src_dict.copy()
        completion = d.pop("completion")

        field_name = d.pop("field_name")

        window = ModelFetchWindow.from_dict(d.pop("window"))

        scan_id = d.pop("scan_id", UNSET)

        completion_completion_node_field_req = cls(
            completion=completion,
            field_name=field_name,
            window=window,
            scan_id=scan_id,
        )

        completion_completion_node_field_req.additional_properties = d
        return completion_completion_node_field_req

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
