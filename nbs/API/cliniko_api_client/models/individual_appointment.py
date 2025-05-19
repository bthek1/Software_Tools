import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.individual_appointment_cancellation_reason_description import (
    IndividualAppointmentCancellationReasonDescription,
    check_individual_appointment_cancellation_reason_description,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.individual_appointment_appointment_type import IndividualAppointmentAppointmentType
    from ..models.individual_appointment_attendees import IndividualAppointmentAttendees
    from ..models.individual_appointment_business import IndividualAppointmentBusiness
    from ..models.individual_appointment_conflicts_type_0 import IndividualAppointmentConflictsType0
    from ..models.individual_appointment_links import IndividualAppointmentLinks
    from ..models.individual_appointment_patient import IndividualAppointmentPatient
    from ..models.individual_appointment_patient_case import IndividualAppointmentPatientCase
    from ..models.individual_appointment_practitioner import IndividualAppointmentPractitioner
    from ..models.individual_appointment_repeat_rule_type_0 import IndividualAppointmentRepeatRuleType0
    from ..models.individual_appointment_repeated_from import IndividualAppointmentRepeatedFrom
    from ..models.individual_appointment_repeats_type_0 import IndividualAppointmentRepeatsType0


T = TypeVar("T", bound="IndividualAppointment")


@_attrs_define
class IndividualAppointment:
    """
    Attributes:
        appointment_type (Union[Unset, IndividualAppointmentAppointmentType]):
        archived_at (Union[None, Unset, datetime.datetime]):
        attendees (Union[Unset, IndividualAppointmentAttendees]):
        booking_ip_address (Union[None, Unset, str]):  Example: 10.0.0.43.
        business (Union[Unset, IndividualAppointmentBusiness]):
        cancellation_note (Union[None, Unset, str]):
        cancellation_reason (Union[None, Unset, int]):
        cancellation_reason_description (Union[Unset, IndividualAppointmentCancellationReasonDescription]):
        cancelled_at (Union[None, Unset, datetime.datetime]):
        conflicts (Union['IndividualAppointmentConflictsType0', None, Unset]):
        created_at (Union[Unset, datetime.datetime]):
        deleted_at (Union[None, Unset, datetime.datetime]):
        did_not_arrive (Union[None, Unset, bool]):
        email_reminder_sent (Union[None, Unset, bool]):
        ends_at (Union[Unset, datetime.datetime]):
        has_patient_appointment_notes (Union[None, Unset, bool]):
        id (Union[Unset, str]):
        invoice_status (Union[None, Unset, int]):
        links (Union[Unset, IndividualAppointmentLinks]):
        notes (Union[None, Unset, str]):
        online_booking_policy_accepted (Union[None, Unset, bool]):
        patient (Union[Unset, IndividualAppointmentPatient]):
        patient_arrived (Union[None, Unset, bool]):
        patient_case (Union[Unset, IndividualAppointmentPatientCase]):
        patient_name (Union[None, Unset, str]):
        practitioner (Union[Unset, IndividualAppointmentPractitioner]):
        repeat_rule (Union['IndividualAppointmentRepeatRuleType0', None, Unset]):
        repeated_from (Union[Unset, IndividualAppointmentRepeatedFrom]):
        repeats (Union['IndividualAppointmentRepeatsType0', None, Unset]):
        sms_reminder_sent (Union[None, Unset, bool]):
        starts_at (Union[Unset, datetime.datetime]):
        telehealth_url (Union[None, Unset, str]):
        treatment_note_status (Union[None, Unset, int]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    appointment_type: Union[Unset, "IndividualAppointmentAppointmentType"] = UNSET
    archived_at: Union[None, Unset, datetime.datetime] = UNSET
    attendees: Union[Unset, "IndividualAppointmentAttendees"] = UNSET
    booking_ip_address: Union[None, Unset, str] = UNSET
    business: Union[Unset, "IndividualAppointmentBusiness"] = UNSET
    cancellation_note: Union[None, Unset, str] = UNSET
    cancellation_reason: Union[None, Unset, int] = UNSET
    cancellation_reason_description: Union[Unset, IndividualAppointmentCancellationReasonDescription] = UNSET
    cancelled_at: Union[None, Unset, datetime.datetime] = UNSET
    conflicts: Union["IndividualAppointmentConflictsType0", None, Unset] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    deleted_at: Union[None, Unset, datetime.datetime] = UNSET
    did_not_arrive: Union[None, Unset, bool] = UNSET
    email_reminder_sent: Union[None, Unset, bool] = UNSET
    ends_at: Union[Unset, datetime.datetime] = UNSET
    has_patient_appointment_notes: Union[None, Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    invoice_status: Union[None, Unset, int] = UNSET
    links: Union[Unset, "IndividualAppointmentLinks"] = UNSET
    notes: Union[None, Unset, str] = UNSET
    online_booking_policy_accepted: Union[None, Unset, bool] = UNSET
    patient: Union[Unset, "IndividualAppointmentPatient"] = UNSET
    patient_arrived: Union[None, Unset, bool] = UNSET
    patient_case: Union[Unset, "IndividualAppointmentPatientCase"] = UNSET
    patient_name: Union[None, Unset, str] = UNSET
    practitioner: Union[Unset, "IndividualAppointmentPractitioner"] = UNSET
    repeat_rule: Union["IndividualAppointmentRepeatRuleType0", None, Unset] = UNSET
    repeated_from: Union[Unset, "IndividualAppointmentRepeatedFrom"] = UNSET
    repeats: Union["IndividualAppointmentRepeatsType0", None, Unset] = UNSET
    sms_reminder_sent: Union[None, Unset, bool] = UNSET
    starts_at: Union[Unset, datetime.datetime] = UNSET
    telehealth_url: Union[None, Unset, str] = UNSET
    treatment_note_status: Union[None, Unset, int] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.individual_appointment_conflicts_type_0 import IndividualAppointmentConflictsType0
        from ..models.individual_appointment_repeat_rule_type_0 import IndividualAppointmentRepeatRuleType0
        from ..models.individual_appointment_repeats_type_0 import IndividualAppointmentRepeatsType0

        appointment_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.appointment_type, Unset):
            appointment_type = self.appointment_type.to_dict()

        archived_at: Union[None, Unset, str]
        if isinstance(self.archived_at, Unset):
            archived_at = UNSET
        elif isinstance(self.archived_at, datetime.datetime):
            archived_at = self.archived_at.isoformat()
        else:
            archived_at = self.archived_at

        attendees: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attendees, Unset):
            attendees = self.attendees.to_dict()

        booking_ip_address: Union[None, Unset, str]
        if isinstance(self.booking_ip_address, Unset):
            booking_ip_address = UNSET
        else:
            booking_ip_address = self.booking_ip_address

        business: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.business, Unset):
            business = self.business.to_dict()

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

        cancelled_at: Union[None, Unset, str]
        if isinstance(self.cancelled_at, Unset):
            cancelled_at = UNSET
        elif isinstance(self.cancelled_at, datetime.datetime):
            cancelled_at = self.cancelled_at.isoformat()
        else:
            cancelled_at = self.cancelled_at

        conflicts: Union[Dict[str, Any], None, Unset]
        if isinstance(self.conflicts, Unset):
            conflicts = UNSET
        elif isinstance(self.conflicts, IndividualAppointmentConflictsType0):
            conflicts = self.conflicts.to_dict()
        else:
            conflicts = self.conflicts

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

        did_not_arrive: Union[None, Unset, bool]
        if isinstance(self.did_not_arrive, Unset):
            did_not_arrive = UNSET
        else:
            did_not_arrive = self.did_not_arrive

        email_reminder_sent: Union[None, Unset, bool]
        if isinstance(self.email_reminder_sent, Unset):
            email_reminder_sent = UNSET
        else:
            email_reminder_sent = self.email_reminder_sent

        ends_at: Union[Unset, str] = UNSET
        if not isinstance(self.ends_at, Unset):
            ends_at = self.ends_at.isoformat()

        has_patient_appointment_notes: Union[None, Unset, bool]
        if isinstance(self.has_patient_appointment_notes, Unset):
            has_patient_appointment_notes = UNSET
        else:
            has_patient_appointment_notes = self.has_patient_appointment_notes

        id = self.id

        invoice_status: Union[None, Unset, int]
        if isinstance(self.invoice_status, Unset):
            invoice_status = UNSET
        else:
            invoice_status = self.invoice_status

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

        patient_arrived: Union[None, Unset, bool]
        if isinstance(self.patient_arrived, Unset):
            patient_arrived = UNSET
        else:
            patient_arrived = self.patient_arrived

        patient_case: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.patient_case, Unset):
            patient_case = self.patient_case.to_dict()

        patient_name: Union[None, Unset, str]
        if isinstance(self.patient_name, Unset):
            patient_name = UNSET
        else:
            patient_name = self.patient_name

        practitioner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.practitioner, Unset):
            practitioner = self.practitioner.to_dict()

        repeat_rule: Union[Dict[str, Any], None, Unset]
        if isinstance(self.repeat_rule, Unset):
            repeat_rule = UNSET
        elif isinstance(self.repeat_rule, IndividualAppointmentRepeatRuleType0):
            repeat_rule = self.repeat_rule.to_dict()
        else:
            repeat_rule = self.repeat_rule

        repeated_from: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.repeated_from, Unset):
            repeated_from = self.repeated_from.to_dict()

        repeats: Union[Dict[str, Any], None, Unset]
        if isinstance(self.repeats, Unset):
            repeats = UNSET
        elif isinstance(self.repeats, IndividualAppointmentRepeatsType0):
            repeats = self.repeats.to_dict()
        else:
            repeats = self.repeats

        sms_reminder_sent: Union[None, Unset, bool]
        if isinstance(self.sms_reminder_sent, Unset):
            sms_reminder_sent = UNSET
        else:
            sms_reminder_sent = self.sms_reminder_sent

        starts_at: Union[Unset, str] = UNSET
        if not isinstance(self.starts_at, Unset):
            starts_at = self.starts_at.isoformat()

        telehealth_url: Union[None, Unset, str]
        if isinstance(self.telehealth_url, Unset):
            telehealth_url = UNSET
        else:
            telehealth_url = self.telehealth_url

        treatment_note_status: Union[None, Unset, int]
        if isinstance(self.treatment_note_status, Unset):
            treatment_note_status = UNSET
        else:
            treatment_note_status = self.treatment_note_status

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if appointment_type is not UNSET:
            field_dict["appointment_type"] = appointment_type
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if attendees is not UNSET:
            field_dict["attendees"] = attendees
        if booking_ip_address is not UNSET:
            field_dict["booking_ip_address"] = booking_ip_address
        if business is not UNSET:
            field_dict["business"] = business
        if cancellation_note is not UNSET:
            field_dict["cancellation_note"] = cancellation_note
        if cancellation_reason is not UNSET:
            field_dict["cancellation_reason"] = cancellation_reason
        if cancellation_reason_description is not UNSET:
            field_dict["cancellation_reason_description"] = cancellation_reason_description
        if cancelled_at is not UNSET:
            field_dict["cancelled_at"] = cancelled_at
        if conflicts is not UNSET:
            field_dict["conflicts"] = conflicts
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if did_not_arrive is not UNSET:
            field_dict["did_not_arrive"] = did_not_arrive
        if email_reminder_sent is not UNSET:
            field_dict["email_reminder_sent"] = email_reminder_sent
        if ends_at is not UNSET:
            field_dict["ends_at"] = ends_at
        if has_patient_appointment_notes is not UNSET:
            field_dict["has_patient_appointment_notes"] = has_patient_appointment_notes
        if id is not UNSET:
            field_dict["id"] = id
        if invoice_status is not UNSET:
            field_dict["invoice_status"] = invoice_status
        if links is not UNSET:
            field_dict["links"] = links
        if notes is not UNSET:
            field_dict["notes"] = notes
        if online_booking_policy_accepted is not UNSET:
            field_dict["online_booking_policy_accepted"] = online_booking_policy_accepted
        if patient is not UNSET:
            field_dict["patient"] = patient
        if patient_arrived is not UNSET:
            field_dict["patient_arrived"] = patient_arrived
        if patient_case is not UNSET:
            field_dict["patient_case"] = patient_case
        if patient_name is not UNSET:
            field_dict["patient_name"] = patient_name
        if practitioner is not UNSET:
            field_dict["practitioner"] = practitioner
        if repeat_rule is not UNSET:
            field_dict["repeat_rule"] = repeat_rule
        if repeated_from is not UNSET:
            field_dict["repeated_from"] = repeated_from
        if repeats is not UNSET:
            field_dict["repeats"] = repeats
        if sms_reminder_sent is not UNSET:
            field_dict["sms_reminder_sent"] = sms_reminder_sent
        if starts_at is not UNSET:
            field_dict["starts_at"] = starts_at
        if telehealth_url is not UNSET:
            field_dict["telehealth_url"] = telehealth_url
        if treatment_note_status is not UNSET:
            field_dict["treatment_note_status"] = treatment_note_status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.individual_appointment_appointment_type import IndividualAppointmentAppointmentType
        from ..models.individual_appointment_attendees import IndividualAppointmentAttendees
        from ..models.individual_appointment_business import IndividualAppointmentBusiness
        from ..models.individual_appointment_conflicts_type_0 import IndividualAppointmentConflictsType0
        from ..models.individual_appointment_links import IndividualAppointmentLinks
        from ..models.individual_appointment_patient import IndividualAppointmentPatient
        from ..models.individual_appointment_patient_case import IndividualAppointmentPatientCase
        from ..models.individual_appointment_practitioner import IndividualAppointmentPractitioner
        from ..models.individual_appointment_repeat_rule_type_0 import IndividualAppointmentRepeatRuleType0
        from ..models.individual_appointment_repeated_from import IndividualAppointmentRepeatedFrom
        from ..models.individual_appointment_repeats_type_0 import IndividualAppointmentRepeatsType0

        d = src_dict.copy()
        _appointment_type = d.pop("appointment_type", UNSET)
        appointment_type: Union[Unset, IndividualAppointmentAppointmentType]
        if isinstance(_appointment_type, Unset):
            appointment_type = UNSET
        else:
            appointment_type = IndividualAppointmentAppointmentType.from_dict(_appointment_type)

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

        _attendees = d.pop("attendees", UNSET)
        attendees: Union[Unset, IndividualAppointmentAttendees]
        if isinstance(_attendees, Unset):
            attendees = UNSET
        else:
            attendees = IndividualAppointmentAttendees.from_dict(_attendees)

        def _parse_booking_ip_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        booking_ip_address = _parse_booking_ip_address(d.pop("booking_ip_address", UNSET))

        _business = d.pop("business", UNSET)
        business: Union[Unset, IndividualAppointmentBusiness]
        if isinstance(_business, Unset):
            business = UNSET
        else:
            business = IndividualAppointmentBusiness.from_dict(_business)

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
        cancellation_reason_description: Union[Unset, IndividualAppointmentCancellationReasonDescription]
        if isinstance(_cancellation_reason_description, Unset):
            cancellation_reason_description = UNSET
        else:
            cancellation_reason_description = check_individual_appointment_cancellation_reason_description(
                _cancellation_reason_description
            )

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

        def _parse_conflicts(data: object) -> Union["IndividualAppointmentConflictsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                conflicts_type_0 = IndividualAppointmentConflictsType0.from_dict(data)

                return conflicts_type_0
            except:  # noqa: E722
                pass
            return cast(Union["IndividualAppointmentConflictsType0", None, Unset], data)

        conflicts = _parse_conflicts(d.pop("conflicts", UNSET))

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

        def _parse_did_not_arrive(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        did_not_arrive = _parse_did_not_arrive(d.pop("did_not_arrive", UNSET))

        def _parse_email_reminder_sent(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        email_reminder_sent = _parse_email_reminder_sent(d.pop("email_reminder_sent", UNSET))

        _ends_at = d.pop("ends_at", UNSET)
        ends_at: Union[Unset, datetime.datetime]
        if isinstance(_ends_at, Unset):
            ends_at = UNSET
        else:
            ends_at = isoparse(_ends_at)

        def _parse_has_patient_appointment_notes(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        has_patient_appointment_notes = _parse_has_patient_appointment_notes(
            d.pop("has_patient_appointment_notes", UNSET)
        )

        id = d.pop("id", UNSET)

        def _parse_invoice_status(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        invoice_status = _parse_invoice_status(d.pop("invoice_status", UNSET))

        _links = d.pop("links", UNSET)
        links: Union[Unset, IndividualAppointmentLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = IndividualAppointmentLinks.from_dict(_links)

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
        patient: Union[Unset, IndividualAppointmentPatient]
        if isinstance(_patient, Unset):
            patient = UNSET
        else:
            patient = IndividualAppointmentPatient.from_dict(_patient)

        def _parse_patient_arrived(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        patient_arrived = _parse_patient_arrived(d.pop("patient_arrived", UNSET))

        _patient_case = d.pop("patient_case", UNSET)
        patient_case: Union[Unset, IndividualAppointmentPatientCase]
        if isinstance(_patient_case, Unset):
            patient_case = UNSET
        else:
            patient_case = IndividualAppointmentPatientCase.from_dict(_patient_case)

        def _parse_patient_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        patient_name = _parse_patient_name(d.pop("patient_name", UNSET))

        _practitioner = d.pop("practitioner", UNSET)
        practitioner: Union[Unset, IndividualAppointmentPractitioner]
        if isinstance(_practitioner, Unset):
            practitioner = UNSET
        else:
            practitioner = IndividualAppointmentPractitioner.from_dict(_practitioner)

        def _parse_repeat_rule(data: object) -> Union["IndividualAppointmentRepeatRuleType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                repeat_rule_type_0 = IndividualAppointmentRepeatRuleType0.from_dict(data)

                return repeat_rule_type_0
            except:  # noqa: E722
                pass
            return cast(Union["IndividualAppointmentRepeatRuleType0", None, Unset], data)

        repeat_rule = _parse_repeat_rule(d.pop("repeat_rule", UNSET))

        _repeated_from = d.pop("repeated_from", UNSET)
        repeated_from: Union[Unset, IndividualAppointmentRepeatedFrom]
        if isinstance(_repeated_from, Unset):
            repeated_from = UNSET
        else:
            repeated_from = IndividualAppointmentRepeatedFrom.from_dict(_repeated_from)

        def _parse_repeats(data: object) -> Union["IndividualAppointmentRepeatsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                repeats_type_0 = IndividualAppointmentRepeatsType0.from_dict(data)

                return repeats_type_0
            except:  # noqa: E722
                pass
            return cast(Union["IndividualAppointmentRepeatsType0", None, Unset], data)

        repeats = _parse_repeats(d.pop("repeats", UNSET))

        def _parse_sms_reminder_sent(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        sms_reminder_sent = _parse_sms_reminder_sent(d.pop("sms_reminder_sent", UNSET))

        _starts_at = d.pop("starts_at", UNSET)
        starts_at: Union[Unset, datetime.datetime]
        if isinstance(_starts_at, Unset):
            starts_at = UNSET
        else:
            starts_at = isoparse(_starts_at)

        def _parse_telehealth_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        telehealth_url = _parse_telehealth_url(d.pop("telehealth_url", UNSET))

        def _parse_treatment_note_status(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        treatment_note_status = _parse_treatment_note_status(d.pop("treatment_note_status", UNSET))

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        individual_appointment = cls(
            appointment_type=appointment_type,
            archived_at=archived_at,
            attendees=attendees,
            booking_ip_address=booking_ip_address,
            business=business,
            cancellation_note=cancellation_note,
            cancellation_reason=cancellation_reason,
            cancellation_reason_description=cancellation_reason_description,
            cancelled_at=cancelled_at,
            conflicts=conflicts,
            created_at=created_at,
            deleted_at=deleted_at,
            did_not_arrive=did_not_arrive,
            email_reminder_sent=email_reminder_sent,
            ends_at=ends_at,
            has_patient_appointment_notes=has_patient_appointment_notes,
            id=id,
            invoice_status=invoice_status,
            links=links,
            notes=notes,
            online_booking_policy_accepted=online_booking_policy_accepted,
            patient=patient,
            patient_arrived=patient_arrived,
            patient_case=patient_case,
            patient_name=patient_name,
            practitioner=practitioner,
            repeat_rule=repeat_rule,
            repeated_from=repeated_from,
            repeats=repeats,
            sms_reminder_sent=sms_reminder_sent,
            starts_at=starts_at,
            telehealth_url=telehealth_url,
            treatment_note_status=treatment_note_status,
            updated_at=updated_at,
        )

        individual_appointment.additional_properties = d
        return individual_appointment

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
