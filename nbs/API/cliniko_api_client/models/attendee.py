import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.attendee_cancellation_reason_description import (
    AttendeeCancellationReasonDescription,
    check_attendee_cancellation_reason_description,
)
from ..models.attendee_invoice_status import AttendeeInvoiceStatus, check_attendee_invoice_status
from ..models.attendee_treatment_note_status import AttendeeTreatmentNoteStatus, check_attendee_treatment_note_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attendee_booking import AttendeeBooking
    from ..models.attendee_invoices import AttendeeInvoices
    from ..models.attendee_links import AttendeeLinks
    from ..models.attendee_patient import AttendeePatient
    from ..models.attendee_patient_case import AttendeePatientCase
    from ..models.attendee_patient_forms import AttendeePatientForms


T = TypeVar("T", bound="Attendee")


@_attrs_define
class Attendee:
    """
    Attributes:
        archived_at (Union[None, Unset, datetime.datetime]):
        arrived (Union[None, Unset, bool]):
        booking (Union[Unset, AttendeeBooking]):
        booking_ip_address (Union[None, Unset, str]):  Example: 10.0.0.43.
        cancellation_note (Union[None, Unset, str]):
        cancellation_reason (Union[None, Unset, int]):
        cancellation_reason_description (Union[Unset, AttendeeCancellationReasonDescription]):
        cancellation_url (Union[None, Unset, str]):
        cancelled_at (Union[None, Unset, datetime.datetime]):
        created_at (Union[Unset, datetime.datetime]):
        deleted_at (Union[None, Unset, datetime.datetime]):
        email_reminder_sent (Union[None, Unset, bool]):
        id (Union[Unset, str]):
        invoice_status (Union[Unset, AttendeeInvoiceStatus]): | Enum Value | Description |
            |---|---|
            |10|Open|
            |20|Paid|
            |30|Closed|
            |40|Open credit|
        invoices (Union[Unset, AttendeeInvoices]):
        links (Union[Unset, AttendeeLinks]):
        notes (Union[None, Unset, str]):
        online_booking_policy_accepted (Union[None, Unset, bool]):
        patient (Union[Unset, AttendeePatient]):
        patient_case (Union[Unset, AttendeePatientCase]):
        patient_forms (Union[Unset, AttendeePatientForms]):
        sent_email_reminders_count (Union[None, Unset, int]):
        sent_sms_reminders_count (Union[None, Unset, int]):
        sms_reminder_sent (Union[None, Unset, bool]):
        telehealth_url (Union[None, Unset, str]):
        treatment_note_status (Union[Unset, AttendeeTreatmentNoteStatus]): | Enum Value | Description |
            |---|---|
            |10|Draft|
            |90|Final|
        updated_at (Union[Unset, datetime.datetime]):
    """

    archived_at: Union[None, Unset, datetime.datetime] = UNSET
    arrived: Union[None, Unset, bool] = UNSET
    booking: Union[Unset, "AttendeeBooking"] = UNSET
    booking_ip_address: Union[None, Unset, str] = UNSET
    cancellation_note: Union[None, Unset, str] = UNSET
    cancellation_reason: Union[None, Unset, int] = UNSET
    cancellation_reason_description: Union[Unset, AttendeeCancellationReasonDescription] = UNSET
    cancellation_url: Union[None, Unset, str] = UNSET
    cancelled_at: Union[None, Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    deleted_at: Union[None, Unset, datetime.datetime] = UNSET
    email_reminder_sent: Union[None, Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    invoice_status: Union[Unset, AttendeeInvoiceStatus] = UNSET
    invoices: Union[Unset, "AttendeeInvoices"] = UNSET
    links: Union[Unset, "AttendeeLinks"] = UNSET
    notes: Union[None, Unset, str] = UNSET
    online_booking_policy_accepted: Union[None, Unset, bool] = UNSET
    patient: Union[Unset, "AttendeePatient"] = UNSET
    patient_case: Union[Unset, "AttendeePatientCase"] = UNSET
    patient_forms: Union[Unset, "AttendeePatientForms"] = UNSET
    sent_email_reminders_count: Union[None, Unset, int] = UNSET
    sent_sms_reminders_count: Union[None, Unset, int] = UNSET
    sms_reminder_sent: Union[None, Unset, bool] = UNSET
    telehealth_url: Union[None, Unset, str] = UNSET
    treatment_note_status: Union[Unset, AttendeeTreatmentNoteStatus] = UNSET
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

        arrived: Union[None, Unset, bool]
        if isinstance(self.arrived, Unset):
            arrived = UNSET
        else:
            arrived = self.arrived

        booking: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.booking, Unset):
            booking = self.booking.to_dict()

        booking_ip_address: Union[None, Unset, str]
        if isinstance(self.booking_ip_address, Unset):
            booking_ip_address = UNSET
        else:
            booking_ip_address = self.booking_ip_address

        cancellation_note: Union[None, Unset, str]
        if isinstance(self.cancellation_note, Unset):
            cancellation_note = UNSET
        else:
            cancellation_note = self.cancellation_note

        cancellation_reason: Union[None, Unset, int]
        if isinstance(self.cancellation_reason, Unset):
            cancellation_reason = UNSET
        else:
            cancellation_reason = self.cancellation_reason

        cancellation_reason_description: Union[Unset, str] = UNSET
        if not isinstance(self.cancellation_reason_description, Unset):
            cancellation_reason_description = self.cancellation_reason_description

        cancellation_url: Union[None, Unset, str]
        if isinstance(self.cancellation_url, Unset):
            cancellation_url = UNSET
        else:
            cancellation_url = self.cancellation_url

        cancelled_at: Union[None, Unset, str]
        if isinstance(self.cancelled_at, Unset):
            cancelled_at = UNSET
        elif isinstance(self.cancelled_at, datetime.datetime):
            cancelled_at = self.cancelled_at.isoformat()
        else:
            cancelled_at = self.cancelled_at

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

        email_reminder_sent: Union[None, Unset, bool]
        if isinstance(self.email_reminder_sent, Unset):
            email_reminder_sent = UNSET
        else:
            email_reminder_sent = self.email_reminder_sent

        id = self.id

        invoice_status: Union[Unset, int] = UNSET
        if not isinstance(self.invoice_status, Unset):
            invoice_status = self.invoice_status

        invoices: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.invoices, Unset):
            invoices = self.invoices.to_dict()

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        online_booking_policy_accepted: Union[None, Unset, bool]
        if isinstance(self.online_booking_policy_accepted, Unset):
            online_booking_policy_accepted = UNSET
        else:
            online_booking_policy_accepted = self.online_booking_policy_accepted

        patient: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.patient, Unset):
            patient = self.patient.to_dict()

        patient_case: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.patient_case, Unset):
            patient_case = self.patient_case.to_dict()

        patient_forms: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.patient_forms, Unset):
            patient_forms = self.patient_forms.to_dict()

        sent_email_reminders_count: Union[None, Unset, int]
        if isinstance(self.sent_email_reminders_count, Unset):
            sent_email_reminders_count = UNSET
        else:
            sent_email_reminders_count = self.sent_email_reminders_count

        sent_sms_reminders_count: Union[None, Unset, int]
        if isinstance(self.sent_sms_reminders_count, Unset):
            sent_sms_reminders_count = UNSET
        else:
            sent_sms_reminders_count = self.sent_sms_reminders_count

        sms_reminder_sent: Union[None, Unset, bool]
        if isinstance(self.sms_reminder_sent, Unset):
            sms_reminder_sent = UNSET
        else:
            sms_reminder_sent = self.sms_reminder_sent

        telehealth_url: Union[None, Unset, str]
        if isinstance(self.telehealth_url, Unset):
            telehealth_url = UNSET
        else:
            telehealth_url = self.telehealth_url

        treatment_note_status: Union[Unset, int] = UNSET
        if not isinstance(self.treatment_note_status, Unset):
            treatment_note_status = self.treatment_note_status

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if arrived is not UNSET:
            field_dict["arrived"] = arrived
        if booking is not UNSET:
            field_dict["booking"] = booking
        if booking_ip_address is not UNSET:
            field_dict["booking_ip_address"] = booking_ip_address
        if cancellation_note is not UNSET:
            field_dict["cancellation_note"] = cancellation_note
        if cancellation_reason is not UNSET:
            field_dict["cancellation_reason"] = cancellation_reason
        if cancellation_reason_description is not UNSET:
            field_dict["cancellation_reason_description"] = cancellation_reason_description
        if cancellation_url is not UNSET:
            field_dict["cancellation_url"] = cancellation_url
        if cancelled_at is not UNSET:
            field_dict["cancelled_at"] = cancelled_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if email_reminder_sent is not UNSET:
            field_dict["email_reminder_sent"] = email_reminder_sent
        if id is not UNSET:
            field_dict["id"] = id
        if invoice_status is not UNSET:
            field_dict["invoice_status"] = invoice_status
        if invoices is not UNSET:
            field_dict["invoices"] = invoices
        if links is not UNSET:
            field_dict["links"] = links
        if notes is not UNSET:
            field_dict["notes"] = notes
        if online_booking_policy_accepted is not UNSET:
            field_dict["online_booking_policy_accepted"] = online_booking_policy_accepted
        if patient is not UNSET:
            field_dict["patient"] = patient
        if patient_case is not UNSET:
            field_dict["patient_case"] = patient_case
        if patient_forms is not UNSET:
            field_dict["patient_forms"] = patient_forms
        if sent_email_reminders_count is not UNSET:
            field_dict["sent_email_reminders_count"] = sent_email_reminders_count
        if sent_sms_reminders_count is not UNSET:
            field_dict["sent_sms_reminders_count"] = sent_sms_reminders_count
        if sms_reminder_sent is not UNSET:
            field_dict["sms_reminder_sent"] = sms_reminder_sent
        if telehealth_url is not UNSET:
            field_dict["telehealth_url"] = telehealth_url
        if treatment_note_status is not UNSET:
            field_dict["treatment_note_status"] = treatment_note_status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attendee_booking import AttendeeBooking
        from ..models.attendee_invoices import AttendeeInvoices
        from ..models.attendee_links import AttendeeLinks
        from ..models.attendee_patient import AttendeePatient
        from ..models.attendee_patient_case import AttendeePatientCase
        from ..models.attendee_patient_forms import AttendeePatientForms

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

        def _parse_arrived(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        arrived = _parse_arrived(d.pop("arrived", UNSET))

        _booking = d.pop("booking", UNSET)
        booking: Union[Unset, AttendeeBooking]
        if isinstance(_booking, Unset):
            booking = UNSET
        else:
            booking = AttendeeBooking.from_dict(_booking)

        def _parse_booking_ip_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        booking_ip_address = _parse_booking_ip_address(d.pop("booking_ip_address", UNSET))

        def _parse_cancellation_note(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cancellation_note = _parse_cancellation_note(d.pop("cancellation_note", UNSET))

        def _parse_cancellation_reason(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        cancellation_reason = _parse_cancellation_reason(d.pop("cancellation_reason", UNSET))

        _cancellation_reason_description = d.pop("cancellation_reason_description", UNSET)
        cancellation_reason_description: Union[Unset, AttendeeCancellationReasonDescription]
        if isinstance(_cancellation_reason_description, Unset):
            cancellation_reason_description = UNSET
        else:
            cancellation_reason_description = check_attendee_cancellation_reason_description(
                _cancellation_reason_description
            )

        def _parse_cancellation_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cancellation_url = _parse_cancellation_url(d.pop("cancellation_url", UNSET))

        def _parse_cancelled_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cancelled_at_type_0 = isoparse(data)

                return cancelled_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        cancelled_at = _parse_cancelled_at(d.pop("cancelled_at", UNSET))

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

        def _parse_email_reminder_sent(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        email_reminder_sent = _parse_email_reminder_sent(d.pop("email_reminder_sent", UNSET))

        id = d.pop("id", UNSET)

        _invoice_status = d.pop("invoice_status", UNSET)
        invoice_status: Union[Unset, AttendeeInvoiceStatus]
        if isinstance(_invoice_status, Unset):
            invoice_status = UNSET
        else:
            invoice_status = check_attendee_invoice_status(_invoice_status)

        _invoices = d.pop("invoices", UNSET)
        invoices: Union[Unset, AttendeeInvoices]
        if isinstance(_invoices, Unset):
            invoices = UNSET
        else:
            invoices = AttendeeInvoices.from_dict(_invoices)

        _links = d.pop("links", UNSET)
        links: Union[Unset, AttendeeLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = AttendeeLinks.from_dict(_links)

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_online_booking_policy_accepted(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        online_booking_policy_accepted = _parse_online_booking_policy_accepted(
            d.pop("online_booking_policy_accepted", UNSET)
        )

        _patient = d.pop("patient", UNSET)
        patient: Union[Unset, AttendeePatient]
        if isinstance(_patient, Unset):
            patient = UNSET
        else:
            patient = AttendeePatient.from_dict(_patient)

        _patient_case = d.pop("patient_case", UNSET)
        patient_case: Union[Unset, AttendeePatientCase]
        if isinstance(_patient_case, Unset):
            patient_case = UNSET
        else:
            patient_case = AttendeePatientCase.from_dict(_patient_case)

        _patient_forms = d.pop("patient_forms", UNSET)
        patient_forms: Union[Unset, AttendeePatientForms]
        if isinstance(_patient_forms, Unset):
            patient_forms = UNSET
        else:
            patient_forms = AttendeePatientForms.from_dict(_patient_forms)

        def _parse_sent_email_reminders_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        sent_email_reminders_count = _parse_sent_email_reminders_count(d.pop("sent_email_reminders_count", UNSET))

        def _parse_sent_sms_reminders_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        sent_sms_reminders_count = _parse_sent_sms_reminders_count(d.pop("sent_sms_reminders_count", UNSET))

        def _parse_sms_reminder_sent(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        sms_reminder_sent = _parse_sms_reminder_sent(d.pop("sms_reminder_sent", UNSET))

        def _parse_telehealth_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        telehealth_url = _parse_telehealth_url(d.pop("telehealth_url", UNSET))

        _treatment_note_status = d.pop("treatment_note_status", UNSET)
        treatment_note_status: Union[Unset, AttendeeTreatmentNoteStatus]
        if isinstance(_treatment_note_status, Unset):
            treatment_note_status = UNSET
        else:
            treatment_note_status = check_attendee_treatment_note_status(_treatment_note_status)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        attendee = cls(
            archived_at=archived_at,
            arrived=arrived,
            booking=booking,
            booking_ip_address=booking_ip_address,
            cancellation_note=cancellation_note,
            cancellation_reason=cancellation_reason,
            cancellation_reason_description=cancellation_reason_description,
            cancellation_url=cancellation_url,
            cancelled_at=cancelled_at,
            created_at=created_at,
            deleted_at=deleted_at,
            email_reminder_sent=email_reminder_sent,
            id=id,
            invoice_status=invoice_status,
            invoices=invoices,
            links=links,
            notes=notes,
            online_booking_policy_accepted=online_booking_policy_accepted,
            patient=patient,
            patient_case=patient_case,
            patient_forms=patient_forms,
            sent_email_reminders_count=sent_email_reminders_count,
            sent_sms_reminders_count=sent_sms_reminders_count,
            sms_reminder_sent=sms_reminder_sent,
            telehealth_url=telehealth_url,
            treatment_note_status=treatment_note_status,
            updated_at=updated_at,
        )

        attendee.additional_properties = d
        return attendee

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
