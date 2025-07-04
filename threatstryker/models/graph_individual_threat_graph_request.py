from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.graph_individual_threat_graph_request_graph_type import GraphIndividualThreatGraphRequestGraphType
from ..models.graph_individual_threat_graph_request_issue_type import GraphIndividualThreatGraphRequestIssueType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GraphIndividualThreatGraphRequest")


@_attrs_define
class GraphIndividualThreatGraphRequest:
    """
    Attributes:
        graph_type (GraphIndividualThreatGraphRequestGraphType):
        issue_type (GraphIndividualThreatGraphRequestIssueType):
        node_ids (Union[None, Unset, list[str]]):
    """

    graph_type: GraphIndividualThreatGraphRequestGraphType
    issue_type: GraphIndividualThreatGraphRequestIssueType
    node_ids: Union[None, Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        graph_type = self.graph_type.value

        issue_type = self.issue_type.value

        node_ids: Union[None, Unset, list[str]]
        if isinstance(self.node_ids, Unset):
            node_ids = UNSET
        elif isinstance(self.node_ids, list):
            node_ids = self.node_ids

        else:
            node_ids = self.node_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "graph_type": graph_type,
                "issue_type": issue_type,
            }
        )
        if node_ids is not UNSET:
            field_dict["node_ids"] = node_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        graph_type = GraphIndividualThreatGraphRequestGraphType(d.pop("graph_type"))

        issue_type = GraphIndividualThreatGraphRequestIssueType(d.pop("issue_type"))

        def _parse_node_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                node_ids_type_0 = cast(list[str], data)

                return node_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        node_ids = _parse_node_ids(d.pop("node_ids", UNSET))

        graph_individual_threat_graph_request = cls(
            graph_type=graph_type,
            issue_type=issue_type,
            node_ids=node_ids,
        )

        graph_individual_threat_graph_request.additional_properties = d
        return graph_individual_threat_graph_request

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
