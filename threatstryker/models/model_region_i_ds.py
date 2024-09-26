from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelRegionIDs")


@_attrs_define
class ModelRegionIDs:
    """
    Attributes:
        ids (Union[List[str], None]):
        region (str):
    """

    ids: Union[List[str], None]
    region: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ids: Union[List[str], None]
        if isinstance(self.ids, list):
            ids = self.ids

        else:
            ids = self.ids

        region = self.region

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ids": ids,
                "region": region,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_ids(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ids_type_0 = cast(List[str], data)

                return ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

        ids = _parse_ids(d.pop("ids"))

        region = d.pop("region")

        model_region_i_ds = cls(
            ids=ids,
            region=region,
        )

        model_region_i_ds.additional_properties = d
        return model_region_i_ds

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
