from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_agent_id import ModelAgentID


T = TypeVar("T", bound="ModelEnableCloudTracerReq")


@_attrs_define
class ModelEnableCloudTracerReq:
    """
    Attributes:
        agent_ids (Union[List['ModelAgentID'], None]):
        aws_s3_bucket (Union[List[str], None]):
    """

    agent_ids: Union[List["ModelAgentID"], None]
    aws_s3_bucket: Union[List[str], None]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        agent_ids: Union[List[Dict[str, Any]], None]
        if isinstance(self.agent_ids, list):
            agent_ids = []
            for agent_ids_type_0_item_data in self.agent_ids:
                agent_ids_type_0_item = agent_ids_type_0_item_data.to_dict()
                agent_ids.append(agent_ids_type_0_item)

        else:
            agent_ids = self.agent_ids

        aws_s3_bucket: Union[List[str], None]
        if isinstance(self.aws_s3_bucket, list):
            aws_s3_bucket = self.aws_s3_bucket

        else:
            aws_s3_bucket = self.aws_s3_bucket

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_ids": agent_ids,
                "aws_s3_bucket": aws_s3_bucket,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_agent_id import ModelAgentID

        d = src_dict.copy()

        def _parse_agent_ids(data: object) -> Union[List["ModelAgentID"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                agent_ids_type_0 = []
                _agent_ids_type_0 = data
                for agent_ids_type_0_item_data in _agent_ids_type_0:
                    agent_ids_type_0_item = ModelAgentID.from_dict(agent_ids_type_0_item_data)

                    agent_ids_type_0.append(agent_ids_type_0_item)

                return agent_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelAgentID"], None], data)

        agent_ids = _parse_agent_ids(d.pop("agent_ids"))

        def _parse_aws_s3_bucket(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                aws_s3_bucket_type_0 = cast(List[str], data)

                return aws_s3_bucket_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

        aws_s3_bucket = _parse_aws_s3_bucket(d.pop("aws_s3_bucket"))

        model_enable_cloud_tracer_req = cls(
            agent_ids=agent_ids,
            aws_s3_bucket=aws_s3_bucket,
        )

        model_enable_cloud_tracer_req.additional_properties = d
        return model_enable_cloud_tracer_req

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
