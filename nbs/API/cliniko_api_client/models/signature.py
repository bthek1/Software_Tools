from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.signature_type import SignatureType, check_signature_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="Signature")


@_attrs_define
class Signature:
    """
    Attributes:
        name (str):
        type (SignatureType):
        signature_id (Union[Unset, str]):  Example: 1.
        required (Union[Unset, bool]):
    """

    name: str
    type: SignatureType
    signature_id: Union[Unset, str] = UNSET
    required: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        type: str = self.type

        signature_id = self.signature_id

        required = self.required

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type,
            }
        )
        if signature_id is not UNSET:
            field_dict["signature_id"] = signature_id
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        type = check_signature_type(d.pop("type"))

        signature_id = d.pop("signature_id", UNSET)

        required = d.pop("required", UNSET)

        signature = cls(
            name=name,
            type=type,
            signature_id=signature_id,
            required=required,
        )

        signature.additional_properties = d
        return signature

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
