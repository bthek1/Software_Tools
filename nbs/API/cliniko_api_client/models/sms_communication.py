import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.sms_communication_category import SmsCommunicationCategory, check_sms_communication_category
from ..models.sms_communication_category_code import SmsCommunicationCategoryCode, check_sms_communication_category_code
from ..models.sms_communication_direction_code import (
    SmsCommunicationDirectionCode,
    check_sms_communication_direction_code,
)
from ..models.sms_communication_direction_description import (
    SmsCommunicationDirectionDescription,
    check_sms_communication_direction_description,
)
from ..models.sms_communication_type import SmsCommunicationType, check_sms_communication_type
from ..models.sms_communication_type_code import SmsCommunicationTypeCode, check_sms_communication_type_code
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sms_communication_attendee import SmsCommunicationAttendee
    from ..models.sms_communication_booking import SmsCommunicationBooking
    from ..models.sms_communication_invoice import SmsCommunicationInvoice
    from ..models.sms_communication_letter import SmsCommunicationLetter
    from ..models.sms_communication_links import SmsCommunicationLinks
    from ..models.sms_communication_patient import SmsCommunicationPatient
    from ..models.sms_communication_payment import SmsCommunicationPayment


T = TypeVar("T", bound="SmsCommunication")


@_attrs_define
class SmsCommunication:
    """
    Attributes:
        archived_at (Union[None, Unset, datetime.datetime]):
        attendee (Union[Unset, SmsCommunicationAttendee]):
        booking (Union[Unset, SmsCommunicationBooking]):
        category (Union[Unset, SmsCommunicationCategory]):
        category_code (Union[Unset, SmsCommunicationCategoryCode]): | Enum Value | Description |
            |---|---|
            | 1 | Appointment Reminder |
            | 2 | Patient Reply Forwarded |
            | 3 | Invoice |
            | 4 | Appointment Confirmation |
            | 5 | Letter |
            | 6 | Practitioner Appointment Notification |
            | 7 | SMS Message |
            | 8 | Reply from Patient |
            | 9 | Account Statement |
            | 10 | Cancelled appointment notification |
            | 11 | Auth Code |
            | 12 | Memo |
            | 13 | Reply from Practitioner |
            | 14 | Payment Receipt |
            | 15 | Bulk Email |
            | 16 | Appointment Cancellation |
            | 17 | Patient Form |
            | 18 | Upcoming appointments |
            | 19 | Completed Patient Form |
            | 20 | Online payment request |
            | 21 | New user |
            | 22 | Referred user signed up |
            | 23 | Referring user bonus notification |
            | 24 | Referred user bonus notification |
            | 25 | Password changed |
            | 26 | Data export complete notification |
            | 27 | SMS credit purchase reminder |
            | 28 | SMS credit purchase failed |
            | 29 | SMS credit purchase requires confirmation |
            | 30 | SMS credit purchase receipt |
            | 31 | Xero sync error notification |
            | 32 | Xero OAuth error |
            | 33 | Mailchimp integration disconnected |
            | 34 | Card automatically updated notification |
            | 35 | Card expiring notification |
            | 36 | Upcoming yearly payment alert |
            | 37 | Trial payment failure |
            | 38 | Subscription payment failure |
            | 39 | Trial ending reminder |
            | 40 | Stripe receipt |
            | 41 | Today's appointments for practitioner |
            | 42 | User email confirmation instructions |
            | 43 | User email changed |
            | 44 | Unlock instructions |
            | 45 | Reset password instructions |
            | 46 | Account ownership information updated |
            | 47 | Email OTP code |
        content (Union[None, Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        direction_code (Union[Unset, SmsCommunicationDirectionCode]): | Enum Value | Description |
            |---|---|
            | 1 | Sent |
            | 2 | Received |
        direction_description (Union[Unset, SmsCommunicationDirectionDescription]):
        from_ (Union[None, Unset, str]):
        id (Union[Unset, str]):
        invoice (Union[Unset, SmsCommunicationInvoice]):
        letter (Union[Unset, SmsCommunicationLetter]):
        links (Union[Unset, SmsCommunicationLinks]):
        patient (Union[Unset, SmsCommunicationPatient]):
        payment (Union[Unset, SmsCommunicationPayment]):
        to (Union[None, Unset, str]):
        type (Union[Unset, SmsCommunicationType]):
        type_code (Union[Unset, SmsCommunicationTypeCode]): | Enum Value | Description |
            |---|---|
            | 1 | SMS |
            | 2 | Email |
            | 3 | Phone call |
            | 4 | Other |
        updated_at (Union[Unset, datetime.datetime]):
    """

    archived_at: Union[None, Unset, datetime.datetime] = UNSET
    attendee: Union[Unset, "SmsCommunicationAttendee"] = UNSET
    booking: Union[Unset, "SmsCommunicationBooking"] = UNSET
    category: Union[Unset, SmsCommunicationCategory] = UNSET
    category_code: Union[Unset, SmsCommunicationCategoryCode] = UNSET
    content: Union[None, Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    direction_code: Union[Unset, SmsCommunicationDirectionCode] = UNSET
    direction_description: Union[Unset, SmsCommunicationDirectionDescription] = UNSET
    from_: Union[None, Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    invoice: Union[Unset, "SmsCommunicationInvoice"] = UNSET
    letter: Union[Unset, "SmsCommunicationLetter"] = UNSET
    links: Union[Unset, "SmsCommunicationLinks"] = UNSET
    patient: Union[Unset, "SmsCommunicationPatient"] = UNSET
    payment: Union[Unset, "SmsCommunicationPayment"] = UNSET
    to: Union[None, Unset, str] = UNSET
    type: Union[Unset, SmsCommunicationType] = UNSET
    type_code: Union[Unset, SmsCommunicationTypeCode] = UNSET
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

        attendee: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attendee, Unset):
            attendee = self.attendee.to_dict()

        booking: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.booking, Unset):
            booking = self.booking.to_dict()

        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category

        category_code: Union[Unset, int] = UNSET
        if not isinstance(self.category_code, Unset):
            category_code = self.category_code

        content: Union[None, Unset, str]
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        direction_code: Union[Unset, int] = UNSET
        if not isinstance(self.direction_code, Unset):
            direction_code = self.direction_code

        direction_description: Union[Unset, str] = UNSET
        if not isinstance(self.direction_description, Unset):
            direction_description = self.direction_description

        from_: Union[None, Unset, str]
        if isinstance(self.from_, Unset):
            from_ = UNSET
        else:
            from_ = self.from_

        id = self.id

        invoice: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.invoice, Unset):
            invoice = self.invoice.to_dict()

        letter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.letter, Unset):
            letter = self.letter.to_dict()

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        patient: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.patient, Unset):
            patient = self.patient.to_dict()

        payment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payment, Unset):
            payment = self.payment.to_dict()

        to: Union[None, Unset, str]
        if isinstance(self.to, Unset):
            to = UNSET
        else:
            to = self.to

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        type_code: Union[Unset, int] = UNSET
        if not isinstance(self.type_code, Unset):
            type_code = self.type_code

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if attendee is not UNSET:
            field_dict["attendee"] = attendee
        if booking is not UNSET:
            field_dict["booking"] = booking
        if category is not UNSET:
            field_dict["category"] = category
        if category_code is not UNSET:
            field_dict["category_code"] = category_code
        if content is not UNSET:
            field_dict["content"] = content
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if direction_code is not UNSET:
            field_dict["direction_code"] = direction_code
        if direction_description is not UNSET:
            field_dict["direction_description"] = direction_description
        if from_ is not UNSET:
            field_dict["from"] = from_
        if id is not UNSET:
            field_dict["id"] = id
        if invoice is not UNSET:
            field_dict["invoice"] = invoice
        if letter is not UNSET:
            field_dict["letter"] = letter
        if links is not UNSET:
            field_dict["links"] = links
        if patient is not UNSET:
            field_dict["patient"] = patient
        if payment is not UNSET:
            field_dict["payment"] = payment
        if to is not UNSET:
            field_dict["to"] = to
        if type is not UNSET:
            field_dict["type"] = type
        if type_code is not UNSET:
            field_dict["type_code"] = type_code
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.sms_communication_attendee import SmsCommunicationAttendee
        from ..models.sms_communication_booking import SmsCommunicationBooking
        from ..models.sms_communication_invoice import SmsCommunicationInvoice
        from ..models.sms_communication_letter import SmsCommunicationLetter
        from ..models.sms_communication_links import SmsCommunicationLinks
        from ..models.sms_communication_patient import SmsCommunicationPatient
        from ..models.sms_communication_payment import SmsCommunicationPayment

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

        _attendee = d.pop("attendee", UNSET)
        attendee: Union[Unset, SmsCommunicationAttendee]
        if isinstance(_attendee, Unset):
            attendee = UNSET
        else:
            attendee = SmsCommunicationAttendee.from_dict(_attendee)

        _booking = d.pop("booking", UNSET)
        booking: Union[Unset, SmsCommunicationBooking]
        if isinstance(_booking, Unset):
            booking = UNSET
        else:
            booking = SmsCommunicationBooking.from_dict(_booking)

        _category = d.pop("category", UNSET)
        category: Union[Unset, SmsCommunicationCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = check_sms_communication_category(_category)

        _category_code = d.pop("category_code", UNSET)
        category_code: Union[Unset, SmsCommunicationCategoryCode]
        if isinstance(_category_code, Unset):
            category_code = UNSET
        else:
            category_code = check_sms_communication_category_code(_category_code)

        def _parse_content(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        content = _parse_content(d.pop("content", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _direction_code = d.pop("direction_code", UNSET)
        direction_code: Union[Unset, SmsCommunicationDirectionCode]
        if isinstance(_direction_code, Unset):
            direction_code = UNSET
        else:
            direction_code = check_sms_communication_direction_code(_direction_code)

        _direction_description = d.pop("direction_description", UNSET)
        direction_description: Union[Unset, SmsCommunicationDirectionDescription]
        if isinstance(_direction_description, Unset):
            direction_description = UNSET
        else:
            direction_description = check_sms_communication_direction_description(_direction_description)

        def _parse_from_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        from_ = _parse_from_(d.pop("from", UNSET))

        id = d.pop("id", UNSET)

        _invoice = d.pop("invoice", UNSET)
        invoice: Union[Unset, SmsCommunicationInvoice]
        if isinstance(_invoice, Unset):
            invoice = UNSET
        else:
            invoice = SmsCommunicationInvoice.from_dict(_invoice)

        _letter = d.pop("letter", UNSET)
        letter: Union[Unset, SmsCommunicationLetter]
        if isinstance(_letter, Unset):
            letter = UNSET
        else:
            letter = SmsCommunicationLetter.from_dict(_letter)

        _links = d.pop("links", UNSET)
        links: Union[Unset, SmsCommunicationLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = SmsCommunicationLinks.from_dict(_links)

        _patient = d.pop("patient", UNSET)
        patient: Union[Unset, SmsCommunicationPatient]
        if isinstance(_patient, Unset):
            patient = UNSET
        else:
            patient = SmsCommunicationPatient.from_dict(_patient)

        _payment = d.pop("payment", UNSET)
        payment: Union[Unset, SmsCommunicationPayment]
        if isinstance(_payment, Unset):
            payment = UNSET
        else:
            payment = SmsCommunicationPayment.from_dict(_payment)

        def _parse_to(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        to = _parse_to(d.pop("to", UNSET))

        _type = d.pop("type", UNSET)
        type: Union[Unset, SmsCommunicationType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = check_sms_communication_type(_type)

        _type_code = d.pop("type_code", UNSET)
        type_code: Union[Unset, SmsCommunicationTypeCode]
        if isinstance(_type_code, Unset):
            type_code = UNSET
        else:
            type_code = check_sms_communication_type_code(_type_code)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        sms_communication = cls(
            archived_at=archived_at,
            attendee=attendee,
            booking=booking,
            category=category,
            category_code=category_code,
            content=content,
            created_at=created_at,
            direction_code=direction_code,
            direction_description=direction_description,
            from_=from_,
            id=id,
            invoice=invoice,
            letter=letter,
            links=links,
            patient=patient,
            payment=payment,
            to=to,
            type=type,
            type_code=type_code,
            updated_at=updated_at,
        )

        sms_communication.additional_properties = d
        return sms_communication

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
