import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.update_patient_case_patch_body_referral_type import (
    UpdatePatientCasePatchBodyReferralType,
    check_update_patient_case_patch_body_referral_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdatePatientCasePatchBody")


@_attrs_define
class UpdatePatientCasePatchBody:
    """
    Attributes:
        closed (Union[None, Unset, bool]):
        contact_id (Union[Unset, str]): contact id Example: 1.
        expiry_date (Union[None, Unset, datetime.date]):
        include_cancelled_attendees (Union[None, Unset, bool]):
        include_dna_attendees (Union[None, Unset, bool]):
        issue_date (Union[None, Unset, datetime.date]):
        name (Union[Unset, str]):
        notes (Union[None, Unset, str]):
        max_invoiceable_amount (Union[None, Unset, str]):
        max_sessions (Union[None, Unset, int]):
        patient_id (Union[Unset, str]): patient id Example: 1.
        referral (Union[None, Unset, bool]):
        referral_type (Union[Unset, UpdatePatientCasePatchBodyReferralType]):
        attendee_ids (Union[List[str], None, Unset]):
        patient_attachment_ids (Union[Unset, List[str]]): Patient attachment ids
    """

    closed: Union[None, Unset, bool] = UNSET
    contact_id: Union[Unset, str] = UNSET
    expiry_date: Union[None, Unset, datetime.date] = UNSET
    include_cancelled_attendees: Union[None, Unset, bool] = UNSET
    include_dna_attendees: Union[None, Unset, bool] = UNSET
    issue_date: Union[None, Unset, datetime.date] = UNSET
    name: Union[Unset, str] = UNSET
    notes: Union[None, Unset, str] = UNSET
    max_invoiceable_amount: Union[None, Unset, str] = UNSET
    max_sessions: Union[None, Unset, int] = UNSET
    patient_id: Union[Unset, str] = UNSET
    referral: Union[None, Unset, bool] = UNSET
    referral_type: Union[Unset, UpdatePatientCasePatchBodyReferralType] = UNSET
    attendee_ids: Union[List[str], None, Unset] = UNSET
    patient_attachment_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        closed: Union[None, Unset, bool]
        if isinstance(self.closed, Unset):
            closed = UNSET
        else:
            closed = self.closed

        contact_id = self.contact_id

        expiry_date: Union[None, Unset, str]
        if isinstance(self.expiry_date, Unset):
            expiry_date = UNSET
        elif isinstance(self.expiry_date, datetime.date):
            expiry_date = self.expiry_date.isoformat()
        else:
            expiry_date = self.expiry_date

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

        issue_date: Union[None, Unset, str]
        if isinstance(self.issue_date, Unset):
            issue_date = UNSET
        elif isinstance(self.issue_date, datetime.date):
            issue_date = self.issue_date.isoformat()
        else:
            issue_date = self.issue_date

        name = self.name

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

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

        patient_id = self.patient_id

        referral: Union[None, Unset, bool]
        if isinstance(self.referral, Unset):
            referral = UNSET
        else:
            referral = self.referral

        referral_type: Union[Unset, str] = UNSET
        if not isinstance(self.referral_type, Unset):
            referral_type = self.referral_type

        attendee_ids: Union[List[str], None, Unset]
        if isinstance(self.attendee_ids, Unset):
            attendee_ids = UNSET
        elif isinstance(self.attendee_ids, list):
            attendee_ids = self.attendee_ids

        else:
            attendee_ids = self.attendee_ids

        patient_attachment_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.patient_attachment_ids, Unset):
            patient_attachment_ids = self.patient_attachment_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if closed is not UNSET:
            field_dict["closed"] = closed
        if contact_id is not UNSET:
            field_dict["contact_id"] = contact_id
        if expiry_date is not UNSET:
            field_dict["expiry_date"] = expiry_date
        if include_cancelled_attendees is not UNSET:
            field_dict["include_cancelled_attendees"] = include_cancelled_attendees
        if include_dna_attendees is not UNSET:
            field_dict["include_dna_attendees"] = include_dna_attendees
        if issue_date is not UNSET:
            field_dict["issue_date"] = issue_date
        if name is not UNSET:
            field_dict["name"] = name
        if notes is not UNSET:
            field_dict["notes"] = notes
        if max_invoiceable_amount is not UNSET:
            field_dict["max_invoiceable_amount"] = max_invoiceable_amount
        if max_sessions is not UNSET:
            field_dict["max_sessions"] = max_sessions
        if patient_id is not UNSET:
            field_dict["patient_id"] = patient_id
        if referral is not UNSET:
            field_dict["referral"] = referral
        if referral_type is not UNSET:
            field_dict["referral_type"] = referral_type
        if attendee_ids is not UNSET:
            field_dict["attendee_ids"] = attendee_ids
        if patient_attachment_ids is not UNSET:
            field_dict["patient_attachment_ids"] = patient_attachment_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_closed(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        closed = _parse_closed(d.pop("closed", UNSET))

        contact_id = d.pop("contact_id", UNSET)

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

        name = d.pop("name", UNSET)

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

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

        patient_id = d.pop("patient_id", UNSET)

        def _parse_referral(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        referral = _parse_referral(d.pop("referral", UNSET))

        _referral_type = d.pop("referral_type", UNSET)
        referral_type: Union[Unset, UpdatePatientCasePatchBodyReferralType]
        if isinstance(_referral_type, Unset):
            referral_type = UNSET
        else:
            referral_type = check_update_patient_case_patch_body_referral_type(_referral_type)

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

        patient_attachment_ids = cast(List[str], d.pop("patient_attachment_ids", UNSET))

        update_patient_case_patch_body = cls(
            closed=closed,
            contact_id=contact_id,
            expiry_date=expiry_date,
            include_cancelled_attendees=include_cancelled_attendees,
            include_dna_attendees=include_dna_attendees,
            issue_date=issue_date,
            name=name,
            notes=notes,
            max_invoiceable_amount=max_invoiceable_amount,
            max_sessions=max_sessions,
            patient_id=patient_id,
            referral=referral,
            referral_type=referral_type,
            attendee_ids=attendee_ids,
            patient_attachment_ids=patient_attachment_ids,
        )

        update_patient_case_patch_body.additional_properties = d
        return update_patient_case_patch_body

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
