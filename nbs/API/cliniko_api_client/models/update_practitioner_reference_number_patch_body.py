from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdatePractitionerReferenceNumberPatchBody")


@_attrs_define
class UpdatePractitionerReferenceNumberPatchBody:
    """
    Attributes:
        name (Union[None, Unset, str]):
        reference_number (Union[None, Unset, str]):
        business_id (Union[Unset, str]): business id Example: 1.
        practitioner_id (Union[Unset, str]): practitioner id Example: 1.
    """

    name: Union[None, Unset, str] = UNSET
    reference_number: Union[None, Unset, str] = UNSET
    business_id: Union[Unset, str] = UNSET
    practitioner_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        reference_number: Union[None, Unset, str]
        if isinstance(self.reference_number, Unset):
            reference_number = UNSET
        else:
            reference_number = self.reference_number

        business_id = self.business_id

        practitioner_id = self.practitioner_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if reference_number is not UNSET:
            field_dict["reference_number"] = reference_number
        if business_id is not UNSET:
            field_dict["business_id"] = business_id
        if practitioner_id is not UNSET:
            field_dict["practitioner_id"] = practitioner_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_reference_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reference_number = _parse_reference_number(d.pop("reference_number", UNSET))

        business_id = d.pop("business_id", UNSET)

        practitioner_id = d.pop("practitioner_id", UNSET)

        update_practitioner_reference_number_patch_body = cls(
            name=name,
            reference_number=reference_number,
            business_id=business_id,
            practitioner_id=practitioner_id,
        )

        update_practitioner_reference_number_patch_body.additional_properties = d
        return update_practitioner_reference_number_patch_body

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
