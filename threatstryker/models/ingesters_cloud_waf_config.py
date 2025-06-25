from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ingesters_cloud_waf_config_cloud_provider import IngestersCloudWafConfigCloudProvider

if TYPE_CHECKING:
    from ..models.ingesters_aws_waf_arn import IngestersAWSWafARN


T = TypeVar("T", bound="IngestersCloudWafConfig")


@_attrs_define
class IngestersCloudWafConfig:
    """
    Attributes:
        aws_waf_arn (Union[None, list['IngestersAWSWafARN']]):
        cloud_provider (IngestersCloudWafConfigCloudProvider):
    """

    aws_waf_arn: Union[None, list["IngestersAWSWafARN"]]
    cloud_provider: IngestersCloudWafConfigCloudProvider
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aws_waf_arn: Union[None, list[dict[str, Any]]]
        if isinstance(self.aws_waf_arn, list):
            aws_waf_arn = []
            for aws_waf_arn_type_0_item_data in self.aws_waf_arn:
                aws_waf_arn_type_0_item = aws_waf_arn_type_0_item_data.to_dict()
                aws_waf_arn.append(aws_waf_arn_type_0_item)

        else:
            aws_waf_arn = self.aws_waf_arn

        cloud_provider = self.cloud_provider.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aws_waf_arn": aws_waf_arn,
                "cloud_provider": cloud_provider,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ingesters_aws_waf_arn import IngestersAWSWafARN

        d = dict(src_dict)

        def _parse_aws_waf_arn(data: object) -> Union[None, list["IngestersAWSWafARN"]]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                aws_waf_arn_type_0 = []
                _aws_waf_arn_type_0 = data
                for aws_waf_arn_type_0_item_data in _aws_waf_arn_type_0:
                    aws_waf_arn_type_0_item = IngestersAWSWafARN.from_dict(aws_waf_arn_type_0_item_data)

                    aws_waf_arn_type_0.append(aws_waf_arn_type_0_item)

                return aws_waf_arn_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, list["IngestersAWSWafARN"]], data)

        aws_waf_arn = _parse_aws_waf_arn(d.pop("aws_waf_arn"))

        cloud_provider = IngestersCloudWafConfigCloudProvider(d.pop("cloud_provider"))

        ingesters_cloud_waf_config = cls(
            aws_waf_arn=aws_waf_arn,
            cloud_provider=cloud_provider,
        )

        ingesters_cloud_waf_config.additional_properties = d
        return ingesters_cloud_waf_config

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
