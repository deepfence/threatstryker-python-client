from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SinglesignonVerifySSOAuthRequest")


@_attrs_define
class SinglesignonVerifySSOAuthRequest:
    """
    Example:
        {'code': 'code', 'user_id': 0, 'namespace': 'namespace'}

    Attributes:
        code (str):
        namespace (str):
        user_id (int):
    """

    code: str
    namespace: str
    user_id: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code = self.code

        namespace = self.namespace

        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "namespace": namespace,
                "user_id": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code = d.pop("code")

        namespace = d.pop("namespace")

        user_id = d.pop("user_id")

        singlesignon_verify_sso_auth_request = cls(
            code=code,
            namespace=namespace,
            user_id=user_id,
        )

        singlesignon_verify_sso_auth_request.additional_properties = d
        return singlesignon_verify_sso_auth_request

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
