import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.patient_case_referral_type import PatientCaseReferralType, check_patient_case_referral_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patient_case_attendees import PatientCaseAttendees
    from ..models.patient_case_bookings import PatientCaseBookings
    from ..models.patient_case_contact import PatientCaseContact
    from ..models.patient_case_invoices import PatientCaseInvoices
    from ..models.patient_case_links import PatientCaseLinks
    from ..models.patient_case_patient import PatientCasePatient
    from ..models.patient_case_patient_attachments import PatientCasePatientAttachments


T = TypeVar("T", bound="PatientCase")


@_attrs_define
class PatientCase:
    """
    Attributes:
        archived_at (Union[None, Unset, datetime.datetime]):
        attendee_ids (Union[List[str], None, Unset]):
        attendees (Union[Unset, PatientCaseAttendees]):
        bookings (Union[Unset, PatientCaseBookings]):
        closed (Union[None, Unset, bool]):
        closed_at (Union[None, Unset, datetime.datetime]):
        contact (Union[Unset, PatientCaseContact]):
        created_at (Union[Unset, datetime.datetime]):
        expiry_date (Union[None, Unset, datetime.date]):
        id (Union[Unset, str]):
        include_cancelled_attendees (Union[None, Unset, bool]):
        include_dna_attendees (Union[None, Unset, bool]):
        invoices (Union[Unset, PatientCaseInvoices]):
        issue_date (Union[None, Unset, datetime.date]):
        links (Union[Unset, PatientCaseLinks]):
        max_invoiceable_amount (Union[None, Unset, str]):
        max_sessions (Union[None, Unset, int]):
        name (Union[Unset, str]):
        notes (Union[None, Unset, str]):
        patient (Union[Unset, PatientCasePatient]):
        patient_attachments (Union[Unset, PatientCasePatientAttachments]):
        referral (Union[None, Unset, bool]):
        referral_type (Union[Unset, PatientCaseReferralType]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    archived_at: Union[None, Unset, datetime.datetime] = UNSET
    attendee_ids: Union[List[str], None, Unset] = UNSET
    attendees: Union[Unset, "PatientCaseAttendees"] = UNSET
    bookings: Union[Unset, "PatientCaseBookings"] = UNSET
    closed: Union[None, Unset, bool] = UNSET
    closed_at: Union[None, Unset, datetime.datetime] = UNSET
    contact: Union[Unset, "PatientCaseContact"] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    expiry_date: Union[None, Unset, datetime.date] = UNSET
    id: Union[Unset, str] = UNSET
    include_cancelled_attendees: Union[None, Unset, bool] = UNSET
    include_dna_attendees: Union[None, Unset, bool] = UNSET
    invoices: Union[Unset, "PatientCaseInvoices"] = UNSET
    issue_date: Union[None, Unset, datetime.date] = UNSET
    links: Union[Unset, "PatientCaseLinks"] = UNSET
    max_invoiceable_amount: Union[None, Unset, str] = UNSET
    max_sessions: Union[None, Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    notes: Union[None, Unset, str] = UNSET
    patient: Union[Unset, "PatientCasePatient"] = UNSET
    patient_attachments: Union[Unset, "PatientCasePatientAttachments"] = UNSET
    referral: Union[None, Unset, bool] = UNSET
    referral_type: Union[Unset, PatientCaseReferralType] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        archived_at: Union[None, Unset, str]
        if isinstance(self.archived_at, Unset):
            archived_at = UNSET
        elif isinstance(self.archived_at, datetime.datetime):
            archived_at = self.archived_at.isoformat()
        else:
            archived_at = self.archived_at

        attendee_ids: Union[List[str], None, Unset]
        if isinstance(self.attendee_ids, Unset):
            attendee_ids = UNSET
        elif isinstance(self.attendee_ids, list):
            attendee_ids = self.attendee_ids

        else:
            attendee_ids = self.attendee_ids

        attendees: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attendees, Unset):
            attendees = self.attendees.to_dict()

        bookings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bookings, Unset):
            bookings = self.bookings.to_dict()

        closed: Union[None, Unset, bool]
        if isinstance(self.closed, Unset):
            closed = UNSET
        else:
            closed = self.closed

        closed_at: Union[None, Unset, str]
        if isinstance(self.closed_at, Unset):
            closed_at = UNSET
        elif isinstance(self.closed_at, datetime.datetime):
            closed_at = self.closed_at.isoformat()
        else:
            closed_at = self.closed_at

        contact: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        expiry_date: Union[None, Unset, str]
        if isinstance(self.expiry_date, Unset):
            expiry_date = UNSET
        elif isinstance(self.expiry_date, datetime.date):
            expiry_date = self.expiry_date.isoformat()
        else:
            expiry_date = self.expiry_date

        id = self.id

        include_cancelled_attendees: Union[None, Unset, bool]
        if isinstance(self.include_cancelled_attendees, Unset):
            include_cancelled_attendees = UNSET
        else:
            include_cancelled_attendees = self.include_cancelled_attendees

        include_dna_attendees: Union[None, Unset, bool]
        if isinstance(self.include_dna_attendees, Unset):
            include_dna_attendees = UNSET
        else:
            include_dna_attendees = self.include_dna_attendees

        invoices: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.invoices, Unset):
            invoices = self.invoices.to_dict()

        issue_date: Union[None, Unset, str]
        if isinstance(self.issue_date, Unset):
            issue_date = UNSET
        elif isinstance(self.issue_date, datetime.date):
            issue_date = self.issue_date.isoformat()
        else:
            issue_date = self.issue_date

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        max_invoiceable_amount: Union[None, Unset, str]
        if isinstance(self.max_invoiceable_amount, Unset):
            max_invoiceable_amount = UNSET
        else:
            max_invoiceable_amount = self.max_invoiceable_amount

        max_sessions: Union[None, Unset, int]
        if isinstance(self.max_sessions, Unset):
            max_sessions = UNSET
        else:
            max_sessions = self.max_sessions

        name = self.name

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        patient: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.patient, Unset):
            patient = self.patient.to_dict()

        patient_attachments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.patient_attachments, Unset):
            patient_attachments = self.patient_attachments.to_dict()

        referral: Union[None, Unset, bool]
        if isinstance(self.referral, Unset):
            referral = UNSET
        else:
            referral = self.referral

        referral_type: Union[Unset, str] = UNSET
        if not isinstance(self.referral_type, Unset):
            referral_type = self.referral_type

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if attendee_ids is not UNSET:
            field_dict["attendee_ids"] = attendee_ids
        if attendees is not UNSET:
            field_dict["attendees"] = attendees
        if bookings is not UNSET:
            field_dict["bookings"] = bookings
        if closed is not UNSET:
            field_dict["closed"] = closed
        if closed_at is not UNSET:
            field_dict["closed_at"] = closed_at
        if contact is not UNSET:
            field_dict["contact"] = contact
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if expiry_date is not UNSET:
            field_dict["expiry_date"] = expiry_date
        if id is not UNSET:
            field_dict["id"] = id
        if include_cancelled_attendees is not UNSET:
            field_dict["include_cancelled_attendees"] = include_cancelled_attendees
        if include_dna_attendees is not UNSET:
            field_dict["include_dna_attendees"] = include_dna_attendees
        if invoices is not UNSET:
            field_dict["invoices"] = invoices
        if issue_date is not UNSET:
            field_dict["issue_date"] = issue_date
        if links is not UNSET:
            field_dict["links"] = links
        if max_invoiceable_amount is not UNSET:
            field_dict["max_invoiceable_amount"] = max_invoiceable_amount
        if max_sessions is not UNSET:
            field_dict["max_sessions"] = max_sessions
        if name is not UNSET:
            field_dict["name"] = name
        if notes is not UNSET:
            field_dict["notes"] = notes
        if patient is not UNSET:
            field_dict["patient"] = patient
        if patient_attachments is not UNSET:
            field_dict["patient_attachments"] = patient_attachments
        if referral is not UNSET:
            field_dict["referral"] = referral
        if referral_type is not UNSET:
            field_dict["referral_type"] = referral_type
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.patient_case_attendees import PatientCaseAttendees
        from ..models.patient_case_bookings import PatientCaseBookings
        from ..models.patient_case_contact import PatientCaseContact
        from ..models.patient_case_invoices import PatientCaseInvoices
        from ..models.patient_case_links import PatientCaseLinks
        from ..models.patient_case_patient import PatientCasePatient
        from ..models.patient_case_patient_attachments import PatientCasePatientAttachments

        d = src_dict.copy()

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

        def _parse_attendee_ids(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attendee_ids_type_0 = cast(List[str], data)

                return attendee_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        attendee_ids = _parse_attendee_ids(d.pop("attendee_ids", UNSET))

        _attendees = d.pop("attendees", UNSET)
        attendees: Union[Unset, PatientCaseAttendees]
        if isinstance(_attendees, Unset):
            attendees = UNSET
        else:
            attendees = PatientCaseAttendees.from_dict(_attendees)

        _bookings = d.pop("bookings", UNSET)
        bookings: Union[Unset, PatientCaseBookings]
        if isinstance(_bookings, Unset):
            bookings = UNSET
        else:
            bookings = PatientCaseBookings.from_dict(_bookings)

        def _parse_closed(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        closed = _parse_closed(d.pop("closed", UNSET))

        def _parse_closed_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                closed_at_type_0 = isoparse(data)

                return closed_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        closed_at = _parse_closed_at(d.pop("closed_at", UNSET))

        _contact = d.pop("contact", UNSET)
        contact: Union[Unset, PatientCaseContact]
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = PatientCaseContact.from_dict(_contact)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        def _parse_expiry_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiry_date_type_0 = isoparse(data).date()

                return expiry_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        expiry_date = _parse_expiry_date(d.pop("expiry_date", UNSET))

        id = d.pop("id", UNSET)

        def _parse_include_cancelled_attendees(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        include_cancelled_attendees = _parse_include_cancelled_attendees(d.pop("include_cancelled_attendees", UNSET))

        def _parse_include_dna_attendees(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        include_dna_attendees = _parse_include_dna_attendees(d.pop("include_dna_attendees", UNSET))

        _invoices = d.pop("invoices", UNSET)
        invoices: Union[Unset, PatientCaseInvoices]
        if isinstance(_invoices, Unset):
            invoices = UNSET
        else:
            invoices = PatientCaseInvoices.from_dict(_invoices)

        def _parse_issue_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                issue_date_type_0 = isoparse(data).date()

                return issue_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        issue_date = _parse_issue_date(d.pop("issue_date", UNSET))

        _links = d.pop("links", UNSET)
        links: Union[Unset, PatientCaseLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = PatientCaseLinks.from_dict(_links)

        def _parse_max_invoiceable_amount(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        max_invoiceable_amount = _parse_max_invoiceable_amount(d.pop("max_invoiceable_amount", UNSET))

        def _parse_max_sessions(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_sessions = _parse_max_sessions(d.pop("max_sessions", UNSET))

        name = d.pop("name", UNSET)

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        _patient = d.pop("patient", UNSET)
        patient: Union[Unset, PatientCasePatient]
        if isinstance(_patient, Unset):
            patient = UNSET
        else:
            patient = PatientCasePatient.from_dict(_patient)

        _patient_attachments = d.pop("patient_attachments", UNSET)
        patient_attachments: Union[Unset, PatientCasePatientAttachments]
        if isinstance(_patient_attachments, Unset):
            patient_attachments = UNSET
        else:
            patient_attachments = PatientCasePatientAttachments.from_dict(_patient_attachments)

        def _parse_referral(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        referral = _parse_referral(d.pop("referral", UNSET))

        _referral_type = d.pop("referral_type", UNSET)
        referral_type: Union[Unset, PatientCaseReferralType]
        if isinstance(_referral_type, Unset):
            referral_type = UNSET
        else:
            referral_type = check_patient_case_referral_type(_referral_type)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        patient_case = cls(
            archived_at=archived_at,
            attendee_ids=attendee_ids,
            attendees=attendees,
            bookings=bookings,
            closed=closed,
            closed_at=closed_at,
            contact=contact,
            created_at=created_at,
            expiry_date=expiry_date,
            id=id,
            include_cancelled_attendees=include_cancelled_attendees,
            include_dna_attendees=include_dna_attendees,
            invoices=invoices,
            issue_date=issue_date,
            links=links,
            max_invoiceable_amount=max_invoiceable_amount,
            max_sessions=max_sessions,
            name=name,
            notes=notes,
            patient=patient,
            patient_attachments=patient_attachments,
            referral=referral,
            referral_type=referral_type,
            updated_at=updated_at,
        )

        patient_case.additional_properties = d
        return patient_case

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
