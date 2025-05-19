from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_contact_patch_body_phone_numbers_item_phone_type import (
    UpdateContactPatchBodyPhoneNumbersItemPhoneType,
    check_update_contact_patch_body_phone_numbers_item_phone_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateContactPatchBodyPhoneNumbersItem")


@_attrs_define
class UpdateContactPatchBodyPhoneNumbersItem:
    """
    Attributes:
        phone_type (Union[Unset, UpdateContactPatchBodyPhoneNumbersItemPhoneType]):
        number (Union[Unset, str]):  Example: 0-123-456-78.
    """

    phone_type: Union[Unset, UpdateContactPatchBodyPhoneNumbersItemPhoneType] = UNSET
    number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        phone_type: Union[Unset, str] = UNSET
        if not isinstance(self.phone_type, Unset):
            phone_type = self.phone_type

        number = self.number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if phone_type is not UNSET:
            field_dict["phone_type"] = phone_type
        if number is not UNSET:
            field_dict["number"] = number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _phone_type = d.pop("phone_type", UNSET)
        phone_type: Union[Unset, UpdateContactPatchBodyPhoneNumbersItemPhoneType]
        if isinstance(_phone_type, Unset):
            phone_type = UNSET
        else:
            phone_type = check_update_contact_patch_body_phone_numbers_item_phone_type(_phone_type)

        number = d.pop("number", UNSET)

        update_contact_patch_body_phone_numbers_item = cls(
            phone_type=phone_type,
            number=number,
        )

        update_contact_patch_body_phone_numbers_item.additional_properties = d
        return update_contact_patch_body_phone_numbers_item

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
