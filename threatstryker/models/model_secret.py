from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_secret_level import ModelSecretLevel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_basic_node import ModelBasicNode


T = TypeVar("T", bound="ModelSecret")


@_attrs_define
class ModelSecret:
    """
    Attributes:
        full_filename (str):
        level (ModelSecretLevel):
        masked (bool):
        matched_content (str):
        node_id (str):
        rule_id (str):
        score (float):
        starting_index (int):
        updated_at (int):
        exploitability_score (Union[Unset, int]):
        max_exploitability_score (Union[Unset, int]):
        resources (Union[None, Unset, list['ModelBasicNode']]):
    """

    full_filename: str
    level: ModelSecretLevel
    masked: bool
    matched_content: str
    node_id: str
    rule_id: str
    score: float
    starting_index: int
    updated_at: int
    exploitability_score: Union[Unset, int] = UNSET
    max_exploitability_score: Union[Unset, int] = UNSET
    resources: Union[None, Unset, list["ModelBasicNode"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        full_filename = self.full_filename

        level = self.level.value

        masked = self.masked

        matched_content = self.matched_content

        node_id = self.node_id

        rule_id = self.rule_id

        score = self.score

        starting_index = self.starting_index

        updated_at = self.updated_at

        exploitability_score = self.exploitability_score

        max_exploitability_score = self.max_exploitability_score

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
                "full_filename": full_filename,
                "level": level,
                "masked": masked,
                "matched_content": matched_content,
                "node_id": node_id,
                "rule_id": rule_id,
                "score": score,
                "starting_index": starting_index,
                "updated_at": updated_at,
            }
        )
        if exploitability_score is not UNSET:
            field_dict["exploitability_score"] = exploitability_score
        if max_exploitability_score is not UNSET:
            field_dict["max_exploitability_score"] = max_exploitability_score
        if resources is not UNSET:
            field_dict["resources"] = resources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_basic_node import ModelBasicNode

        d = dict(src_dict)
        full_filename = d.pop("full_filename")

        level = ModelSecretLevel(d.pop("level"))

        masked = d.pop("masked")

        matched_content = d.pop("matched_content")

        node_id = d.pop("node_id")

        rule_id = d.pop("rule_id")

        score = d.pop("score")

        starting_index = d.pop("starting_index")

        updated_at = d.pop("updated_at")

        exploitability_score = d.pop("exploitability_score", UNSET)

        max_exploitability_score = d.pop("max_exploitability_score", UNSET)

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

        model_secret = cls(
            full_filename=full_filename,
            level=level,
            masked=masked,
            matched_content=matched_content,
            node_id=node_id,
            rule_id=rule_id,
            score=score,
            starting_index=starting_index,
            updated_at=updated_at,
            exploitability_score=exploitability_score,
            max_exploitability_score=max_exploitability_score,
            resources=resources,
        )

        model_secret.additional_properties = d
        return model_secret

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
