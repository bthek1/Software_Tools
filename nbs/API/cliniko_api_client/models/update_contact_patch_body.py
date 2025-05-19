from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_contact_patch_body_doctor_type import (
    UpdateContactPatchBodyDoctorType,
    check_update_contact_patch_body_doctor_type,
)
from ..models.update_contact_patch_body_type_code import (
    UpdateContactPatchBodyTypeCode,
    check_update_contact_patch_body_type_code,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_contact_patch_body_phone_numbers_item import UpdateContactPatchBodyPhoneNumbersItem


T = TypeVar("T", bound="UpdateContactPatchBody")


@_attrs_define
class UpdateContactPatchBody:
    """
    Attributes:
        address_1 (Union[None, Unset, str]):
        address_2 (Union[None, Unset, str]):
        address_3 (Union[None, Unset, str]):
        city (Union[None, Unset, str]):
        company_name (Union[None, Unset, str]):
        country_code (Union[None, Unset, str]): [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1#Current_codes)
            country code Example: AU.
        doctor_type (Union[Unset, UpdateContactPatchBodyDoctorType]):
        email (Union[None, Unset, str]):
        first_name (Union[None, Unset, str]):
        last_name (Union[None, Unset, str]):
        notes (Union[None, Unset, str]):
        occupation (Union[None, Unset, str]):
        post_code (Union[None, Unset, str]):
        preferred_name (Union[None, Unset, str]):
        provider_number (Union[None, Unset, str]):
        state (Union[None, Unset, str]):
        title (Union[None, Unset, str]):
        type_code (Union[Unset, UpdateContactPatchBodyTypeCode]):
        phone_numbers (Union[Unset, List['UpdateContactPatchBodyPhoneNumbersItem']]):
    """

    address_1: Union[None, Unset, str] = UNSET
    address_2: Union[None, Unset, str] = UNSET
    address_3: Union[None, Unset, str] = UNSET
    city: Union[None, Unset, str] = UNSET
    company_name: Union[None, Unset, str] = UNSET
    country_code: Union[None, Unset, str] = UNSET
    doctor_type: Union[Unset, UpdateContactPatchBodyDoctorType] = UNSET
    email: Union[None, Unset, str] = UNSET
    first_name: Union[None, Unset, str] = UNSET
    last_name: Union[None, Unset, str] = UNSET
    notes: Union[None, Unset, str] = UNSET
    occupation: Union[None, Unset, str] = UNSET
    post_code: Union[None, Unset, str] = UNSET
    preferred_name: Union[None, Unset, str] = UNSET
    provider_number: Union[None, Unset, str] = UNSET
    state: Union[None, Unset, str] = UNSET
    title: Union[None, Unset, str] = UNSET
    type_code: Union[Unset, UpdateContactPatchBodyTypeCode] = UNSET
    phone_numbers: Union[Unset, List["UpdateContactPatchBodyPhoneNumbersItem"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address_1: Union[None, Unset, str]
        if isinstance(self.address_1, Unset):
            address_1 = UNSET
        else:
            address_1 = self.address_1

        address_2: Union[None, Unset, str]
        if isinstance(self.address_2, Unset):
            address_2 = UNSET
        else:
            address_2 = self.address_2

        address_3: Union[None, Unset, str]
        if isinstance(self.address_3, Unset):
            address_3 = UNSET
        else:
            address_3 = self.address_3

        city: Union[None, Unset, str]
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        company_name: Union[None, Unset, str]
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        country_code: Union[None, Unset, str]
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        else:
            country_code = self.country_code

        doctor_type: Union[Unset, str] = UNSET
        if not isinstance(self.doctor_type, Unset):
            doctor_type = self.doctor_type

        email: Union[None, Unset, str]
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        first_name: Union[None, Unset, str]
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        last_name: Union[None, Unset, str]
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        occupation: Union[None, Unset, str]
        if isinstance(self.occupation, Unset):
            occupation = UNSET
        else:
            occupation = self.occupation

        post_code: Union[None, Unset, str]
        if isinstance(self.post_code, Unset):
            post_code = UNSET
        else:
            post_code = self.post_code

        preferred_name: Union[None, Unset, str]
        if isinstance(self.preferred_name, Unset):
            preferred_name = UNSET
        else:
            preferred_name = self.preferred_name

        provider_number: Union[None, Unset, str]
        if isinstance(self.provider_number, Unset):
            provider_number = UNSET
        else:
            provider_number = self.provider_number

        state: Union[None, Unset, str]
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        type_code: Union[Unset, int] = UNSET
        if not isinstance(self.type_code, Unset):
            type_code = self.type_code

        phone_numbers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.phone_numbers, Unset):
            phone_numbers = []
            for phone_numbers_item_data in self.phone_numbers:
                phone_numbers_item = phone_numbers_item_data.to_dict()
                phone_numbers.append(phone_numbers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_1 is not UNSET:
            field_dict["address_1"] = address_1
        if address_2 is not UNSET:
            field_dict["address_2"] = address_2
        if address_3 is not UNSET:
            field_dict["address_3"] = address_3
        if city is not UNSET:
            field_dict["city"] = city
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if doctor_type is not UNSET:
            field_dict["doctor_type"] = doctor_type
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if notes is not UNSET:
            field_dict["notes"] = notes
        if occupation is not UNSET:
            field_dict["occupation"] = occupation
        if post_code is not UNSET:
            field_dict["post_code"] = post_code
        if preferred_name is not UNSET:
            field_dict["preferred_name"] = preferred_name
        if provider_number is not UNSET:
            field_dict["provider_number"] = provider_number
        if state is not UNSET:
            field_dict["state"] = state
        if title is not UNSET:
            field_dict["title"] = title
        if type_code is not UNSET:
            field_dict["type_code"] = type_code
        if phone_numbers is not UNSET:
            field_dict["phone_numbers"] = phone_numbers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.update_contact_patch_body_phone_numbers_item import UpdateContactPatchBodyPhoneNumbersItem

        d = src_dict.copy()

        def _parse_address_1(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        address_1 = _parse_address_1(d.pop("address_1", UNSET))

        def _parse_address_2(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        address_2 = _parse_address_2(d.pop("address_2", UNSET))

        def _parse_address_3(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        address_3 = _parse_address_3(d.pop("address_3", UNSET))

        def _parse_city(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_company_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))

        def _parse_country_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        country_code = _parse_country_code(d.pop("country_code", UNSET))

        _doctor_type = d.pop("doctor_type", UNSET)
        doctor_type: Union[Unset, UpdateContactPatchBodyDoctorType]
        if isinstance(_doctor_type, Unset):
            doctor_type = UNSET
        else:
            doctor_type = check_update_contact_patch_body_doctor_type(_doctor_type)

        def _parse_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_first_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))

        def _parse_last_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_name = _parse_last_name(d.pop("last_name", UNSET))

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_occupation(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        occupation = _parse_occupation(d.pop("occupation", UNSET))

        def _parse_post_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        post_code = _parse_post_code(d.pop("post_code", UNSET))

        def _parse_preferred_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        preferred_name = _parse_preferred_name(d.pop("preferred_name", UNSET))

        def _parse_provider_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        provider_number = _parse_provider_number(d.pop("provider_number", UNSET))

        def _parse_state(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        _type_code = d.pop("type_code", UNSET)
        type_code: Union[Unset, UpdateContactPatchBodyTypeCode]
        if isinstance(_type_code, Unset):
            type_code = UNSET
        else:
            type_code = check_update_contact_patch_body_type_code(_type_code)

        phone_numbers = []
        _phone_numbers = d.pop("phone_numbers", UNSET)
        for phone_numbers_item_data in _phone_numbers or []:
            phone_numbers_item = UpdateContactPatchBodyPhoneNumbersItem.from_dict(phone_numbers_item_data)

            phone_numbers.append(phone_numbers_item)

        update_contact_patch_body = cls(
            address_1=address_1,
            address_2=address_2,
            address_3=address_3,
            city=city,
            company_name=company_name,
            country_code=country_code,
            doctor_type=doctor_type,
            email=email,
            first_name=first_name,
            last_name=last_name,
            notes=notes,
            occupation=occupation,
            post_code=post_code,
            preferred_name=preferred_name,
            provider_number=provider_number,
            state=state,
            title=title,
            type_code=type_code,
            phone_numbers=phone_numbers,
        )

        update_contact_patch_body.additional_properties = d
        return update_contact_patch_body

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
