from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ingesters_cloud_waf_config_cloud_provider import IngestersCloudWafConfigCloudProvider

if TYPE_CHECKING:
    from ..models.ingesters_aws_waf_arn import IngestersAWSWafARN


T = TypeVar("T", bound="IngestersCloudWafConfig")


@_attrs_define
class IngestersCloudWafConfig:
    """
    Example:
        {'aws_waf_arn': [{'arn': 'arn', 'region': 'CLOUDFRONT'}, {'arn': 'arn', 'region': 'CLOUDFRONT'}],
            'cloud_provider': 'aws'}

    Attributes:
        cloud_provider (IngestersCloudWafConfigCloudProvider):
        aws_waf_arn (Optional[List['IngestersAWSWafARN']]):
    """

    cloud_provider: IngestersCloudWafConfigCloudProvider
    aws_waf_arn: Optional[List["IngestersAWSWafARN"]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cloud_provider = self.cloud_provider.value

        if self.aws_waf_arn is None:
            aws_waf_arn = None
        else:
            aws_waf_arn = []
            for aws_waf_arn_item_data in self.aws_waf_arn:
                aws_waf_arn_item = aws_waf_arn_item_data.to_dict()

                aws_waf_arn.append(aws_waf_arn_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cloud_provider": cloud_provider,
                "aws_waf_arn": aws_waf_arn,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ingesters_aws_waf_arn import IngestersAWSWafARN

        d = src_dict.copy()
        cloud_provider = IngestersCloudWafConfigCloudProvider(d.pop("cloud_provider"))

        aws_waf_arn = []
        _aws_waf_arn = d.pop("aws_waf_arn")
        for aws_waf_arn_item_data in _aws_waf_arn or []:
            aws_waf_arn_item = IngestersAWSWafARN.from_dict(aws_waf_arn_item_data)

            aws_waf_arn.append(aws_waf_arn_item)

        ingesters_cloud_waf_config = cls(
            cloud_provider=cloud_provider,
            aws_waf_arn=aws_waf_arn,
        )

        ingesters_cloud_waf_config.additional_properties = d
        return ingesters_cloud_waf_config

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
