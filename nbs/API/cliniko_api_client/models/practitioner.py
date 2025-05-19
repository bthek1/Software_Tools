import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.practitioner_appointment_types import PractitionerAppointmentTypes
    from ..models.practitioner_appointments import PractitionerAppointments
    from ..models.practitioner_default_appointment_type import PractitionerDefaultAppointmentType
    from ..models.practitioner_invoices import PractitionerInvoices
    from ..models.practitioner_links import PractitionerLinks
    from ..models.practitioner_practitioner_reference_numbers import PractitionerPractitionerReferenceNumbers
    from ..models.practitioner_user import PractitionerUser


T = TypeVar("T", bound="Practitioner")


@_attrs_define
class Practitioner:
    """
    Attributes:
        active (Union[None, Unset, bool]):
        appointment_types (Union[Unset, PractitionerAppointmentTypes]):
        appointments (Union[Unset, PractitionerAppointments]):
        created_at (Union[Unset, datetime.datetime]):
        default_appointment_type (Union[Unset, PractitionerDefaultAppointmentType]):
        description (Union[None, Unset, str]):
        designation (Union[None, Unset, str]):
        display_name (Union[None, Unset, str]):
        first_name (Union[None, Unset, str]):
        id (Union[Unset, str]):
        invoices (Union[Unset, PractitionerInvoices]):
        label (Union[None, Unset, str]):
        last_name (Union[None, Unset, str]):
        links (Union[Unset, PractitionerLinks]):
        practitioner_reference_numbers (Union[Unset, PractitionerPractitionerReferenceNumbers]):
        show_in_online_bookings (Union[None, Unset, bool]):
        title (Union[None, Unset, str]):
        updated_at (Union[Unset, datetime.datetime]):
        user (Union[Unset, PractitionerUser]):
    """

    active: Union[None, Unset, bool] = UNSET
    appointment_types: Union[Unset, "PractitionerAppointmentTypes"] = UNSET
    appointments: Union[Unset, "PractitionerAppointments"] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    default_appointment_type: Union[Unset, "PractitionerDefaultAppointmentType"] = UNSET
    description: Union[None, Unset, str] = UNSET
    designation: Union[None, Unset, str] = UNSET
    display_name: Union[None, Unset, str] = UNSET
    first_name: Union[None, Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    invoices: Union[Unset, "PractitionerInvoices"] = UNSET
    label: Union[None, Unset, str] = UNSET
    last_name: Union[None, Unset, str] = UNSET
    links: Union[Unset, "PractitionerLinks"] = UNSET
    practitioner_reference_numbers: Union[Unset, "PractitionerPractitionerReferenceNumbers"] = UNSET
    show_in_online_bookings: Union[None, Unset, bool] = UNSET
    title: Union[None, Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    user: Union[Unset, "PractitionerUser"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active: Union[None, Unset, bool]
        if isinstance(self.active, Unset):
            active = UNSET
        else:
            active = self.active

        appointment_types: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.appointment_types, Unset):
            appointment_types = self.appointment_types.to_dict()

        appointments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.appointments, Unset):
            appointments = self.appointments.to_dict()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        default_appointment_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.default_appointment_type, Unset):
            default_appointment_type = self.default_appointment_type.to_dict()

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        designation: Union[None, Unset, str]
        if isinstance(self.designation, Unset):
            designation = UNSET
        else:
            designation = self.designation

        display_name: Union[None, Unset, str]
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        first_name: Union[None, Unset, str]
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        id = self.id

        invoices: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.invoices, Unset):
            invoices = self.invoices.to_dict()

        label: Union[None, Unset, str]
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        last_name: Union[None, Unset, str]
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        practitioner_reference_numbers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.practitioner_reference_numbers, Unset):
            practitioner_reference_numbers = self.practitioner_reference_numbers.to_dict()

        show_in_online_bookings: Union[None, Unset, bool]
        if isinstance(self.show_in_online_bookings, Unset):
            show_in_online_bookings = UNSET
        else:
            show_in_online_bookings = self.show_in_online_bookings

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if appointment_types is not UNSET:
            field_dict["appointment_types"] = appointment_types
        if appointments is not UNSET:
            field_dict["appointments"] = appointments
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if default_appointment_type is not UNSET:
            field_dict["default_appointment_type"] = default_appointment_type
        if description is not UNSET:
            field_dict["description"] = description
        if designation is not UNSET:
            field_dict["designation"] = designation
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if id is not UNSET:
            field_dict["id"] = id
        if invoices is not UNSET:
            field_dict["invoices"] = invoices
        if label is not UNSET:
            field_dict["label"] = label
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if links is not UNSET:
            field_dict["links"] = links
        if practitioner_reference_numbers is not UNSET:
            field_dict["practitioner_reference_numbers"] = practitioner_reference_numbers
        if show_in_online_bookings is not UNSET:
            field_dict["show_in_online_bookings"] = show_in_online_bookings
        if title is not UNSET:
            field_dict["title"] = title
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.practitioner_appointment_types import PractitionerAppointmentTypes
        from ..models.practitioner_appointments import PractitionerAppointments
        from ..models.practitioner_default_appointment_type import PractitionerDefaultAppointmentType
        from ..models.practitioner_invoices import PractitionerInvoices
        from ..models.practitioner_links import PractitionerLinks
        from ..models.practitioner_practitioner_reference_numbers import PractitionerPractitionerReferenceNumbers
        from ..models.practitioner_user import PractitionerUser

        d = src_dict.copy()

        def _parse_active(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        active = _parse_active(d.pop("active", UNSET))

        _appointment_types = d.pop("appointment_types", UNSET)
        appointment_types: Union[Unset, PractitionerAppointmentTypes]
        if isinstance(_appointment_types, Unset):
            appointment_types = UNSET
        else:
            appointment_types = PractitionerAppointmentTypes.from_dict(_appointment_types)

        _appointments = d.pop("appointments", UNSET)
        appointments: Union[Unset, PractitionerAppointments]
        if isinstance(_appointments, Unset):
            appointments = UNSET
        else:
            appointments = PractitionerAppointments.from_dict(_appointments)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _default_appointment_type = d.pop("default_appointment_type", UNSET)
        default_appointment_type: Union[Unset, PractitionerDefaultAppointmentType]
        if isinstance(_default_appointment_type, Unset):
            default_appointment_type = UNSET
        else:
            default_appointment_type = PractitionerDefaultAppointmentType.from_dict(_default_appointment_type)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_designation(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        designation = _parse_designation(d.pop("designation", UNSET))

        def _parse_display_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        def _parse_first_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))

        id = d.pop("id", UNSET)

        _invoices = d.pop("invoices", UNSET)
        invoices: Union[Unset, PractitionerInvoices]
        if isinstance(_invoices, Unset):
            invoices = UNSET
        else:
            invoices = PractitionerInvoices.from_dict(_invoices)

        def _parse_label(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        label = _parse_label(d.pop("label", UNSET))

        def _parse_last_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_name = _parse_last_name(d.pop("last_name", UNSET))

        _links = d.pop("links", UNSET)
        links: Union[Unset, PractitionerLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = PractitionerLinks.from_dict(_links)

        _practitioner_reference_numbers = d.pop("practitioner_reference_numbers", UNSET)
        practitioner_reference_numbers: Union[Unset, PractitionerPractitionerReferenceNumbers]
        if isinstance(_practitioner_reference_numbers, Unset):
            practitioner_reference_numbers = UNSET
        else:
            practitioner_reference_numbers = PractitionerPractitionerReferenceNumbers.from_dict(
                _practitioner_reference_numbers
            )

        def _parse_show_in_online_bookings(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        show_in_online_bookings = _parse_show_in_online_bookings(d.pop("show_in_online_bookings", UNSET))

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

        _user = d.pop("user", UNSET)
        user: Union[Unset, PractitionerUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = PractitionerUser.from_dict(_user)

        practitioner = cls(
            active=active,
            appointment_types=appointment_types,
            appointments=appointments,
            created_at=created_at,
            default_appointment_type=default_appointment_type,
            description=description,
            designation=designation,
            display_name=display_name,
            first_name=first_name,
            id=id,
            invoices=invoices,
            label=label,
            last_name=last_name,
            links=links,
            practitioner_reference_numbers=practitioner_reference_numbers,
            show_in_online_bookings=show_in_online_bookings,
            title=title,
            updated_at=updated_at,
            user=user,
        )

        practitioner.additional_properties = d
        return practitioner

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
