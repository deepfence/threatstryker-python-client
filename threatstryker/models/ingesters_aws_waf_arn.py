from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ingesters_aws_waf_arn_region import IngestersAWSWafARNRegion

T = TypeVar("T", bound="IngestersAWSWafARN")


@_attrs_define
class IngestersAWSWafARN:
    """
    Attributes:
        arn (str):
        region (IngestersAWSWafARNRegion):
    """

    arn: str
    region: IngestersAWSWafARNRegion
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        arn = self.arn

        region = self.region.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "arn": arn,
                "region": region,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        arn = d.pop("arn")

        region = IngestersAWSWafARNRegion(d.pop("region"))

        ingesters_aws_waf_arn = cls(
            arn=arn,
            region=region,
        )

        ingesters_aws_waf_arn.additional_properties = d
        return ingesters_aws_waf_arn

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
