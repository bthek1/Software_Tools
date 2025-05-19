from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.phone_number_phone_type import PhoneNumberPhoneType, check_phone_number_phone_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="PhoneNumber")


@_attrs_define
class PhoneNumber:
    """
    Attributes:
        normalized_number (Union[Unset, str]):  Example: 39012345678.
        number (Union[Unset, str]):  Example: 0-123-456-78.
        phone_type (Union[Unset, PhoneNumberPhoneType]):
    """

    normalized_number: Union[Unset, str] = UNSET
    number: Union[Unset, str] = UNSET
    phone_type: Union[Unset, PhoneNumberPhoneType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        normalized_number = self.normalized_number

        number = self.number

        phone_type: Union[Unset, str] = UNSET
        if not isinstance(self.phone_type, Unset):
            phone_type = self.phone_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if normalized_number is not UNSET:
            field_dict["normalized_number"] = normalized_number
        if number is not UNSET:
            field_dict["number"] = number
        if phone_type is not UNSET:
            field_dict["phone_type"] = phone_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        normalized_number = d.pop("normalized_number", UNSET)

        number = d.pop("number", UNSET)

        _phone_type = d.pop("phone_type", UNSET)
        phone_type: Union[Unset, PhoneNumberPhoneType]
        if isinstance(_phone_type, Unset):
            phone_type = UNSET
        else:
            phone_type = check_phone_number_phone_type(_phone_type)

        phone_number = cls(
            normalized_number=normalized_number,
            number=number,
            phone_type=phone_type,
        )

        phone_number.additional_properties = d
        return phone_number

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
