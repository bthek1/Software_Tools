import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.user_role import UserRole, check_user_role
from ..models.user_time_zone import UserTimeZone, check_user_time_zone
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.phone_number import PhoneNumber
    from ..models.user_links import UserLinks


T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        active (Union[None, Unset, bool]):
        created_at (Union[Unset, datetime.datetime]):
        email (Union[Unset, str]):
        first_name (Union[Unset, str]):
        id (Union[Unset, str]):
        last_name (Union[Unset, str]):
        links (Union[Unset, UserLinks]):
        phone_numbers (Union[List['PhoneNumber'], None, Unset]):
        role (Union[Unset, UserRole]):
        time_zone (Union[Unset, UserTimeZone]): See: [supported time zones](/developer-
            portal/guides/time_zone_support/#accepted-values-for-time_zone) Example: Melbourne.
        time_zone_identifier (Union[None, Unset, str]): See: [supported time zone identifiers](/developer-
            portal/guides/time_zone_support/#accepted-values-for-time_zone_identifier) Example: Australia/Melbourne.
        title (Union[None, Unset, str]):
        updated_at (Union[Unset, datetime.datetime]):
        user_active (Union[None, Unset, bool]):
    """

    active: Union[None, Unset, bool] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    email: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    links: Union[Unset, "UserLinks"] = UNSET
    phone_numbers: Union[List["PhoneNumber"], None, Unset] = UNSET
    role: Union[Unset, UserRole] = UNSET
    time_zone: Union[Unset, UserTimeZone] = UNSET
    time_zone_identifier: Union[None, Unset, str] = UNSET
    title: Union[None, Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    user_active: Union[None, Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active: Union[None, Unset, bool]
        if isinstance(self.active, Unset):
            active = UNSET
        else:
            active = self.active

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        email = self.email

        first_name = self.first_name

        id = self.id

        last_name = self.last_name

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        phone_numbers: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.phone_numbers, Unset):
            phone_numbers = UNSET
        elif isinstance(self.phone_numbers, list):
            phone_numbers = []
            for phone_numbers_type_0_item_data in self.phone_numbers:
                phone_numbers_type_0_item = phone_numbers_type_0_item_data.to_dict()
                phone_numbers.append(phone_numbers_type_0_item)

        else:
            phone_numbers = self.phone_numbers

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role

        time_zone: Union[Unset, str] = UNSET
        if not isinstance(self.time_zone, Unset):
            time_zone = self.time_zone

        time_zone_identifier: Union[None, Unset, str]
        if isinstance(self.time_zone_identifier, Unset):
            time_zone_identifier = UNSET
        else:
            time_zone_identifier = self.time_zone_identifier

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        user_active: Union[None, Unset, bool]
        if isinstance(self.user_active, Unset):
            user_active = UNSET
        else:
            user_active = self.user_active

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if id is not UNSET:
            field_dict["id"] = id
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if links is not UNSET:
            field_dict["links"] = links
        if phone_numbers is not UNSET:
            field_dict["phone_numbers"] = phone_numbers
        if role is not UNSET:
            field_dict["role"] = role
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone
        if time_zone_identifier is not UNSET:
            field_dict["time_zone_identifier"] = time_zone_identifier
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user_active is not UNSET:
            field_dict["user_active"] = user_active

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.phone_number import PhoneNumber
        from ..models.user_links import UserLinks

        d = src_dict.copy()

        def _parse_active(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        active = _parse_active(d.pop("active", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        email = d.pop("email", UNSET)

        first_name = d.pop("first_name", UNSET)

        id = d.pop("id", UNSET)

        last_name = d.pop("last_name", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, UserLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = UserLinks.from_dict(_links)

        def _parse_phone_numbers(data: object) -> Union[List["PhoneNumber"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                phone_numbers_type_0 = []
                _phone_numbers_type_0 = data
                for phone_numbers_type_0_item_data in _phone_numbers_type_0:
                    phone_numbers_type_0_item = PhoneNumber.from_dict(phone_numbers_type_0_item_data)

                    phone_numbers_type_0.append(phone_numbers_type_0_item)

                return phone_numbers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["PhoneNumber"], None, Unset], data)

        phone_numbers = _parse_phone_numbers(d.pop("phone_numbers", UNSET))

        _role = d.pop("role", UNSET)
        role: Union[Unset, UserRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = check_user_role(_role)

        _time_zone = d.pop("time_zone", UNSET)
        time_zone: Union[Unset, UserTimeZone]
        if isinstance(_time_zone, Unset):
            time_zone = UNSET
        else:
            time_zone = check_user_time_zone(_time_zone)

        def _parse_time_zone_identifier(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        time_zone_identifier = _parse_time_zone_identifier(d.pop("time_zone_identifier", UNSET))

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        def _parse_user_active(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        user_active = _parse_user_active(d.pop("user_active", UNSET))

        user = cls(
            active=active,
            created_at=created_at,
            email=email,
            first_name=first_name,
            id=id,
            last_name=last_name,
            links=links,
            phone_numbers=phone_numbers,
            role=role,
            time_zone=time_zone,
            time_zone_identifier=time_zone_identifier,
            title=title,
            updated_at=updated_at,
            user_active=user_active,
        )

        user.additional_properties = d
        return user

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
