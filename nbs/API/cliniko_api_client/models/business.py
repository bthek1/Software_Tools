import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.business_appointments import BusinessAppointments
    from ..models.business_links import BusinessLinks
    from ..models.business_practitioners import BusinessPractitioners


T = TypeVar("T", bound="Business")


@_attrs_define
class Business:
    """
    Attributes:
        additional_information (Union[None, Unset, str]):
        additional_invoice_information (Union[None, Unset, str]):
        address_1 (Union[None, Unset, str]):
        address_2 (Union[None, Unset, str]):
        appointment_reminders_enabled (Union[None, Unset, bool]):
        appointment_type_ids (Union[List[str], None, Unset]):
        appointments (Union[Unset, BusinessAppointments]):
        archived_at (Union[None, Unset, datetime.datetime]):
        business_name (Union[None, Unset, str]):
        business_registration_name (Union[None, Unset, str]):
        business_registration_value (Union[None, Unset, str]):
        city (Union[None, Unset, str]):
        contact_information (Union[None, Unset, str]):
        country (Union[None, Unset, str]):
        country_code (Union[None, Unset, str]): [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1#Current_codes)
            country code Example: AU.
        created_at (Union[Unset, datetime.datetime]):
        deleted_at (Union[None, Unset, datetime.datetime]):
        display_name (Union[None, Unset, str]):
        email_reply_to (Union[None, Unset, str]):
        id (Union[Unset, str]):
        label (Union[None, Unset, str]):
        links (Union[Unset, BusinessLinks]):
        post_code (Union[None, Unset, str]):
        practitioners (Union[Unset, BusinessPractitioners]):
        show_in_online_bookings (Union[None, Unset, bool]):
        state (Union[None, Unset, str]):
        time_zone (Union[None, Unset, str]): Human-readable label for a time zone. See link below for supported values.
            Example: Melbourne.
        time_zone_identifier (Union[None, Unset, str]): IANA identifier for a time zone. See link below for supported
            values. Example: Australia/Melbourne.
        updated_at (Union[Unset, datetime.datetime]):
        website_address (Union[None, Unset, str]):
    """

    additional_information: Union[None, Unset, str] = UNSET
    additional_invoice_information: Union[None, Unset, str] = UNSET
    address_1: Union[None, Unset, str] = UNSET
    address_2: Union[None, Unset, str] = UNSET
    appointment_reminders_enabled: Union[None, Unset, bool] = UNSET
    appointment_type_ids: Union[List[str], None, Unset] = UNSET
    appointments: Union[Unset, "BusinessAppointments"] = UNSET
    archived_at: Union[None, Unset, datetime.datetime] = UNSET
    business_name: Union[None, Unset, str] = UNSET
    business_registration_name: Union[None, Unset, str] = UNSET
    business_registration_value: Union[None, Unset, str] = UNSET
    city: Union[None, Unset, str] = UNSET
    contact_information: Union[None, Unset, str] = UNSET
    country: Union[None, Unset, str] = UNSET
    country_code: Union[None, Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    deleted_at: Union[None, Unset, datetime.datetime] = UNSET
    display_name: Union[None, Unset, str] = UNSET
    email_reply_to: Union[None, Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    label: Union[None, Unset, str] = UNSET
    links: Union[Unset, "BusinessLinks"] = UNSET
    post_code: Union[None, Unset, str] = UNSET
    practitioners: Union[Unset, "BusinessPractitioners"] = UNSET
    show_in_online_bookings: Union[None, Unset, bool] = UNSET
    state: Union[None, Unset, str] = UNSET
    time_zone: Union[None, Unset, str] = UNSET
    time_zone_identifier: Union[None, Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    website_address: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        additional_information: Union[None, Unset, str]
        if isinstance(self.additional_information, Unset):
            additional_information = UNSET
        else:
            additional_information = self.additional_information

        additional_invoice_information: Union[None, Unset, str]
        if isinstance(self.additional_invoice_information, Unset):
            additional_invoice_information = UNSET
        else:
            additional_invoice_information = self.additional_invoice_information

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

        appointment_reminders_enabled: Union[None, Unset, bool]
        if isinstance(self.appointment_reminders_enabled, Unset):
            appointment_reminders_enabled = UNSET
        else:
            appointment_reminders_enabled = self.appointment_reminders_enabled

        appointment_type_ids: Union[List[str], None, Unset]
        if isinstance(self.appointment_type_ids, Unset):
            appointment_type_ids = UNSET
        elif isinstance(self.appointment_type_ids, list):
            appointment_type_ids = self.appointment_type_ids

        else:
            appointment_type_ids = self.appointment_type_ids

        appointments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.appointments, Unset):
            appointments = self.appointments.to_dict()

        archived_at: Union[None, Unset, str]
        if isinstance(self.archived_at, Unset):
            archived_at = UNSET
        elif isinstance(self.archived_at, datetime.datetime):
            archived_at = self.archived_at.isoformat()
        else:
            archived_at = self.archived_at

        business_name: Union[None, Unset, str]
        if isinstance(self.business_name, Unset):
            business_name = UNSET
        else:
            business_name = self.business_name

        business_registration_name: Union[None, Unset, str]
        if isinstance(self.business_registration_name, Unset):
            business_registration_name = UNSET
        else:
            business_registration_name = self.business_registration_name

        business_registration_value: Union[None, Unset, str]
        if isinstance(self.business_registration_value, Unset):
            business_registration_value = UNSET
        else:
            business_registration_value = self.business_registration_value

        city: Union[None, Unset, str]
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        contact_information: Union[None, Unset, str]
        if isinstance(self.contact_information, Unset):
            contact_information = UNSET
        else:
            contact_information = self.contact_information

        country: Union[None, Unset, str]
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        country_code: Union[None, Unset, str]
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        else:
            country_code = self.country_code

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        elif isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        display_name: Union[None, Unset, str]
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        email_reply_to: Union[None, Unset, str]
        if isinstance(self.email_reply_to, Unset):
            email_reply_to = UNSET
        else:
            email_reply_to = self.email_reply_to

        id = self.id

        label: Union[None, Unset, str]
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        post_code: Union[None, Unset, str]
        if isinstance(self.post_code, Unset):
            post_code = UNSET
        else:
            post_code = self.post_code

        practitioners: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.practitioners, Unset):
            practitioners = self.practitioners.to_dict()

        show_in_online_bookings: Union[None, Unset, bool]
        if isinstance(self.show_in_online_bookings, Unset):
            show_in_online_bookings = UNSET
        else:
            show_in_online_bookings = self.show_in_online_bookings

        state: Union[None, Unset, str]
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        time_zone: Union[None, Unset, str]
        if isinstance(self.time_zone, Unset):
            time_zone = UNSET
        else:
            time_zone = self.time_zone

        time_zone_identifier: Union[None, Unset, str]
        if isinstance(self.time_zone_identifier, Unset):
            time_zone_identifier = UNSET
        else:
            time_zone_identifier = self.time_zone_identifier

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        website_address: Union[None, Unset, str]
        if isinstance(self.website_address, Unset):
            website_address = UNSET
        else:
            website_address = self.website_address

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_information is not UNSET:
            field_dict["additional_information"] = additional_information
        if additional_invoice_information is not UNSET:
            field_dict["additional_invoice_information"] = additional_invoice_information
        if address_1 is not UNSET:
            field_dict["address_1"] = address_1
        if address_2 is not UNSET:
            field_dict["address_2"] = address_2
        if appointment_reminders_enabled is not UNSET:
            field_dict["appointment_reminders_enabled"] = appointment_reminders_enabled
        if appointment_type_ids is not UNSET:
            field_dict["appointment_type_ids"] = appointment_type_ids
        if appointments is not UNSET:
            field_dict["appointments"] = appointments
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if business_name is not UNSET:
            field_dict["business_name"] = business_name
        if business_registration_name is not UNSET:
            field_dict["business_registration_name"] = business_registration_name
        if business_registration_value is not UNSET:
            field_dict["business_registration_value"] = business_registration_value
        if city is not UNSET:
            field_dict["city"] = city
        if contact_information is not UNSET:
            field_dict["contact_information"] = contact_information
        if country is not UNSET:
            field_dict["country"] = country
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if email_reply_to is not UNSET:
            field_dict["email_reply_to"] = email_reply_to
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label
        if links is not UNSET:
            field_dict["links"] = links
        if post_code is not UNSET:
            field_dict["post_code"] = post_code
        if practitioners is not UNSET:
            field_dict["practitioners"] = practitioners
        if show_in_online_bookings is not UNSET:
            field_dict["show_in_online_bookings"] = show_in_online_bookings
        if state is not UNSET:
            field_dict["state"] = state
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone
        if time_zone_identifier is not UNSET:
            field_dict["time_zone_identifier"] = time_zone_identifier
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if website_address is not UNSET:
            field_dict["website_address"] = website_address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.business_appointments import BusinessAppointments
        from ..models.business_links import BusinessLinks
        from ..models.business_practitioners import BusinessPractitioners

        d = src_dict.copy()

        def _parse_additional_information(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        additional_information = _parse_additional_information(d.pop("additional_information", UNSET))

        def _parse_additional_invoice_information(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        additional_invoice_information = _parse_additional_invoice_information(
            d.pop("additional_invoice_information", UNSET)
        )

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

        def _parse_appointment_reminders_enabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        appointment_reminders_enabled = _parse_appointment_reminders_enabled(
            d.pop("appointment_reminders_enabled", UNSET)
        )

        def _parse_appointment_type_ids(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                appointment_type_ids_type_0 = cast(List[str], data)

                return appointment_type_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        appointment_type_ids = _parse_appointment_type_ids(d.pop("appointment_type_ids", UNSET))

        _appointments = d.pop("appointments", UNSET)
        appointments: Union[Unset, BusinessAppointments]
        if isinstance(_appointments, Unset):
            appointments = UNSET
        else:
            appointments = BusinessAppointments.from_dict(_appointments)

        def _parse_archived_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                archived_at_type_0 = isoparse(data)

                return archived_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        archived_at = _parse_archived_at(d.pop("archived_at", UNSET))

        def _parse_business_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        business_name = _parse_business_name(d.pop("business_name", UNSET))

        def _parse_business_registration_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        business_registration_name = _parse_business_registration_name(d.pop("business_registration_name", UNSET))

        def _parse_business_registration_value(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        business_registration_value = _parse_business_registration_value(d.pop("business_registration_value", UNSET))

        def _parse_city(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_contact_information(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        contact_information = _parse_contact_information(d.pop("contact_information", UNSET))

        def _parse_country(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_country_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        country_code = _parse_country_code(d.pop("country_code", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        def _parse_deleted_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_at_type_0 = isoparse(data)

                return deleted_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at", UNSET))

        def _parse_display_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        def _parse_email_reply_to(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email_reply_to = _parse_email_reply_to(d.pop("email_reply_to", UNSET))

        id = d.pop("id", UNSET)

        def _parse_label(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        label = _parse_label(d.pop("label", UNSET))

        _links = d.pop("links", UNSET)
        links: Union[Unset, BusinessLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = BusinessLinks.from_dict(_links)

        def _parse_post_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        post_code = _parse_post_code(d.pop("post_code", UNSET))

        _practitioners = d.pop("practitioners", UNSET)
        practitioners: Union[Unset, BusinessPractitioners]
        if isinstance(_practitioners, Unset):
            practitioners = UNSET
        else:
            practitioners = BusinessPractitioners.from_dict(_practitioners)

        def _parse_show_in_online_bookings(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        show_in_online_bookings = _parse_show_in_online_bookings(d.pop("show_in_online_bookings", UNSET))

        def _parse_state(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_time_zone(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        time_zone = _parse_time_zone(d.pop("time_zone", UNSET))

        def _parse_time_zone_identifier(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        time_zone_identifier = _parse_time_zone_identifier(d.pop("time_zone_identifier", UNSET))

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        def _parse_website_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        website_address = _parse_website_address(d.pop("website_address", UNSET))

        business = cls(
            additional_information=additional_information,
            additional_invoice_information=additional_invoice_information,
            address_1=address_1,
            address_2=address_2,
            appointment_reminders_enabled=appointment_reminders_enabled,
            appointment_type_ids=appointment_type_ids,
            appointments=appointments,
            archived_at=archived_at,
            business_name=business_name,
            business_registration_name=business_registration_name,
            business_registration_value=business_registration_value,
            city=city,
            contact_information=contact_information,
            country=country,
            country_code=country_code,
            created_at=created_at,
            deleted_at=deleted_at,
            display_name=display_name,
            email_reply_to=email_reply_to,
            id=id,
            label=label,
            links=links,
            post_code=post_code,
            practitioners=practitioners,
            show_in_online_bookings=show_in_online_bookings,
            state=state,
            time_zone=time_zone,
            time_zone_identifier=time_zone_identifier,
            updated_at=updated_at,
            website_address=website_address,
        )

        business.additional_properties = d
        return business

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
