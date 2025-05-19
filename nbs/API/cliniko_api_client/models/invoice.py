import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.invoice_status import InvoiceStatus, check_invoice_status
from ..models.invoice_status_description import InvoiceStatusDescription, check_invoice_status_description
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_appointment import InvoiceAppointment
    from ..models.invoice_attendee import InvoiceAttendee
    from ..models.invoice_business import InvoiceBusiness
    from ..models.invoice_invoice_items import InvoiceInvoiceItems
    from ..models.invoice_links import InvoiceLinks
    from ..models.invoice_original_invoice import InvoiceOriginalInvoice
    from ..models.invoice_patient import InvoicePatient
    from ..models.invoice_practitioner import InvoicePractitioner
    from ..models.invoice_reversed_invoices import InvoiceReversedInvoices
    from ..models.invoice_signature import InvoiceSignature


T = TypeVar("T", bound="Invoice")


@_attrs_define
class Invoice:
    """
    Attributes:
        appointment (Union[Unset, InvoiceAppointment]):
        archived_at (Union[None, Unset, datetime.datetime]):
        attendee (Union[Unset, InvoiceAttendee]):
        business (Union[Unset, InvoiceBusiness]):
        closed_at (Union[None, Unset, datetime.datetime]):
        created_at (Union[Unset, datetime.datetime]):
        deleted_at (Union[None, Unset, datetime.datetime]):
        discounted_amount (Union[None, Unset, str]):
        id (Union[Unset, str]):
        invoice_items (Union[Unset, InvoiceInvoiceItems]):
        invoice_to (Union[None, Unset, str]):
        issue_date (Union[Unset, datetime.date]):
        links (Union[Unset, InvoiceLinks]):
        net_amount (Union[None, Unset, str]):
        notes (Union[None, Unset, str]):
        number (Union[Unset, int]):
        online_payment_url (Union[None, Unset, str]):
        original_invoice (Union[Unset, InvoiceOriginalInvoice]):
        patient (Union[Unset, InvoicePatient]):
        patient_extra_information (Union[None, Unset, str]):
        practitioner (Union[Unset, InvoicePractitioner]):
        reversed_invoices (Union[Unset, InvoiceReversedInvoices]):
        signature (Union[Unset, InvoiceSignature]):
        status (Union[Unset, InvoiceStatus]): | Enum Value | Description |
            |---|---|
            | 10 | Open |
            | 20 | Paid |
            | 30 | Closed |
            | 40 | Open credit |
        status_description (Union[Unset, InvoiceStatusDescription]):
        tax_amount (Union[None, Unset, str]):
        total_amount (Union[None, Unset, str]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    appointment: Union[Unset, "InvoiceAppointment"] = UNSET
    archived_at: Union[None, Unset, datetime.datetime] = UNSET
    attendee: Union[Unset, "InvoiceAttendee"] = UNSET
    business: Union[Unset, "InvoiceBusiness"] = UNSET
    closed_at: Union[None, Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    deleted_at: Union[None, Unset, datetime.datetime] = UNSET
    discounted_amount: Union[None, Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    invoice_items: Union[Unset, "InvoiceInvoiceItems"] = UNSET
    invoice_to: Union[None, Unset, str] = UNSET
    issue_date: Union[Unset, datetime.date] = UNSET
    links: Union[Unset, "InvoiceLinks"] = UNSET
    net_amount: Union[None, Unset, str] = UNSET
    notes: Union[None, Unset, str] = UNSET
    number: Union[Unset, int] = UNSET
    online_payment_url: Union[None, Unset, str] = UNSET
    original_invoice: Union[Unset, "InvoiceOriginalInvoice"] = UNSET
    patient: Union[Unset, "InvoicePatient"] = UNSET
    patient_extra_information: Union[None, Unset, str] = UNSET
    practitioner: Union[Unset, "InvoicePractitioner"] = UNSET
    reversed_invoices: Union[Unset, "InvoiceReversedInvoices"] = UNSET
    signature: Union[Unset, "InvoiceSignature"] = UNSET
    status: Union[Unset, InvoiceStatus] = UNSET
    status_description: Union[Unset, InvoiceStatusDescription] = UNSET
    tax_amount: Union[None, Unset, str] = UNSET
    total_amount: Union[None, Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        appointment: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.appointment, Unset):
            appointment = self.appointment.to_dict()

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

        business: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.business, Unset):
            business = self.business.to_dict()

        closed_at: Union[None, Unset, str]
        if isinstance(self.closed_at, Unset):
            closed_at = UNSET
        elif isinstance(self.closed_at, datetime.datetime):
            closed_at = self.closed_at.isoformat()
        else:
            closed_at = self.closed_at

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

        discounted_amount: Union[None, Unset, str]
        if isinstance(self.discounted_amount, Unset):
            discounted_amount = UNSET
        else:
            discounted_amount = self.discounted_amount

        id = self.id

        invoice_items: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.invoice_items, Unset):
            invoice_items = self.invoice_items.to_dict()

        invoice_to: Union[None, Unset, str]
        if isinstance(self.invoice_to, Unset):
            invoice_to = UNSET
        else:
            invoice_to = self.invoice_to

        issue_date: Union[Unset, str] = UNSET
        if not isinstance(self.issue_date, Unset):
            issue_date = self.issue_date.isoformat()

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        net_amount: Union[None, Unset, str]
        if isinstance(self.net_amount, Unset):
            net_amount = UNSET
        else:
            net_amount = self.net_amount

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        number = self.number

        online_payment_url: Union[None, Unset, str]
        if isinstance(self.online_payment_url, Unset):
            online_payment_url = UNSET
        else:
            online_payment_url = self.online_payment_url

        original_invoice: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.original_invoice, Unset):
            original_invoice = self.original_invoice.to_dict()

        patient: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.patient, Unset):
            patient = self.patient.to_dict()

        patient_extra_information: Union[None, Unset, str]
        if isinstance(self.patient_extra_information, Unset):
            patient_extra_information = UNSET
        else:
            patient_extra_information = self.patient_extra_information

        practitioner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.practitioner, Unset):
            practitioner = self.practitioner.to_dict()

        reversed_invoices: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reversed_invoices, Unset):
            reversed_invoices = self.reversed_invoices.to_dict()

        signature: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.signature, Unset):
            signature = self.signature.to_dict()

        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        status_description: Union[Unset, str] = UNSET
        if not isinstance(self.status_description, Unset):
            status_description = self.status_description

        tax_amount: Union[None, Unset, str]
        if isinstance(self.tax_amount, Unset):
            tax_amount = UNSET
        else:
            tax_amount = self.tax_amount

        total_amount: Union[None, Unset, str]
        if isinstance(self.total_amount, Unset):
            total_amount = UNSET
        else:
            total_amount = self.total_amount

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if appointment is not UNSET:
            field_dict["appointment"] = appointment
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if attendee is not UNSET:
            field_dict["attendee"] = attendee
        if business is not UNSET:
            field_dict["business"] = business
        if closed_at is not UNSET:
            field_dict["closed_at"] = closed_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if discounted_amount is not UNSET:
            field_dict["discounted_amount"] = discounted_amount
        if id is not UNSET:
            field_dict["id"] = id
        if invoice_items is not UNSET:
            field_dict["invoice_items"] = invoice_items
        if invoice_to is not UNSET:
            field_dict["invoice_to"] = invoice_to
        if issue_date is not UNSET:
            field_dict["issue_date"] = issue_date
        if links is not UNSET:
            field_dict["links"] = links
        if net_amount is not UNSET:
            field_dict["net_amount"] = net_amount
        if notes is not UNSET:
            field_dict["notes"] = notes
        if number is not UNSET:
            field_dict["number"] = number
        if online_payment_url is not UNSET:
            field_dict["online_payment_url"] = online_payment_url
        if original_invoice is not UNSET:
            field_dict["original_invoice"] = original_invoice
        if patient is not UNSET:
            field_dict["patient"] = patient
        if patient_extra_information is not UNSET:
            field_dict["patient_extra_information"] = patient_extra_information
        if practitioner is not UNSET:
            field_dict["practitioner"] = practitioner
        if reversed_invoices is not UNSET:
            field_dict["reversed_invoices"] = reversed_invoices
        if signature is not UNSET:
            field_dict["signature"] = signature
        if status is not UNSET:
            field_dict["status"] = status
        if status_description is not UNSET:
            field_dict["status_description"] = status_description
        if tax_amount is not UNSET:
            field_dict["tax_amount"] = tax_amount
        if total_amount is not UNSET:
            field_dict["total_amount"] = total_amount
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_appointment import InvoiceAppointment
        from ..models.invoice_attendee import InvoiceAttendee
        from ..models.invoice_business import InvoiceBusiness
        from ..models.invoice_invoice_items import InvoiceInvoiceItems
        from ..models.invoice_links import InvoiceLinks
        from ..models.invoice_original_invoice import InvoiceOriginalInvoice
        from ..models.invoice_patient import InvoicePatient
        from ..models.invoice_practitioner import InvoicePractitioner
        from ..models.invoice_reversed_invoices import InvoiceReversedInvoices
        from ..models.invoice_signature import InvoiceSignature

        d = src_dict.copy()
        _appointment = d.pop("appointment", UNSET)
        appointment: Union[Unset, InvoiceAppointment]
        if isinstance(_appointment, Unset):
            appointment = UNSET
        else:
            appointment = InvoiceAppointment.from_dict(_appointment)

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
        attendee: Union[Unset, InvoiceAttendee]
        if isinstance(_attendee, Unset):
            attendee = UNSET
        else:
            attendee = InvoiceAttendee.from_dict(_attendee)

        _business = d.pop("business", UNSET)
        business: Union[Unset, InvoiceBusiness]
        if isinstance(_business, Unset):
            business = UNSET
        else:
            business = InvoiceBusiness.from_dict(_business)

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

        def _parse_discounted_amount(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        discounted_amount = _parse_discounted_amount(d.pop("discounted_amount", UNSET))

        id = d.pop("id", UNSET)

        _invoice_items = d.pop("invoice_items", UNSET)
        invoice_items: Union[Unset, InvoiceInvoiceItems]
        if isinstance(_invoice_items, Unset):
            invoice_items = UNSET
        else:
            invoice_items = InvoiceInvoiceItems.from_dict(_invoice_items)

        def _parse_invoice_to(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        invoice_to = _parse_invoice_to(d.pop("invoice_to", UNSET))

        _issue_date = d.pop("issue_date", UNSET)
        issue_date: Union[Unset, datetime.date]
        if isinstance(_issue_date, Unset):
            issue_date = UNSET
        else:
            issue_date = isoparse(_issue_date).date()

        _links = d.pop("links", UNSET)
        links: Union[Unset, InvoiceLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = InvoiceLinks.from_dict(_links)

        def _parse_net_amount(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        net_amount = _parse_net_amount(d.pop("net_amount", UNSET))

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        number = d.pop("number", UNSET)

        def _parse_online_payment_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        online_payment_url = _parse_online_payment_url(d.pop("online_payment_url", UNSET))

        _original_invoice = d.pop("original_invoice", UNSET)
        original_invoice: Union[Unset, InvoiceOriginalInvoice]
        if isinstance(_original_invoice, Unset):
            original_invoice = UNSET
        else:
            original_invoice = InvoiceOriginalInvoice.from_dict(_original_invoice)

        _patient = d.pop("patient", UNSET)
        patient: Union[Unset, InvoicePatient]
        if isinstance(_patient, Unset):
            patient = UNSET
        else:
            patient = InvoicePatient.from_dict(_patient)

        def _parse_patient_extra_information(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        patient_extra_information = _parse_patient_extra_information(d.pop("patient_extra_information", UNSET))

        _practitioner = d.pop("practitioner", UNSET)
        practitioner: Union[Unset, InvoicePractitioner]
        if isinstance(_practitioner, Unset):
            practitioner = UNSET
        else:
            practitioner = InvoicePractitioner.from_dict(_practitioner)

        _reversed_invoices = d.pop("reversed_invoices", UNSET)
        reversed_invoices: Union[Unset, InvoiceReversedInvoices]
        if isinstance(_reversed_invoices, Unset):
            reversed_invoices = UNSET
        else:
            reversed_invoices = InvoiceReversedInvoices.from_dict(_reversed_invoices)

        _signature = d.pop("signature", UNSET)
        signature: Union[Unset, InvoiceSignature]
        if isinstance(_signature, Unset):
            signature = UNSET
        else:
            signature = InvoiceSignature.from_dict(_signature)

        _status = d.pop("status", UNSET)
        status: Union[Unset, InvoiceStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_invoice_status(_status)

        _status_description = d.pop("status_description", UNSET)
        status_description: Union[Unset, InvoiceStatusDescription]
        if isinstance(_status_description, Unset):
            status_description = UNSET
        else:
            status_description = check_invoice_status_description(_status_description)

        def _parse_tax_amount(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tax_amount = _parse_tax_amount(d.pop("tax_amount", UNSET))

        def _parse_total_amount(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        total_amount = _parse_total_amount(d.pop("total_amount", UNSET))

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        invoice = cls(
            appointment=appointment,
            archived_at=archived_at,
            attendee=attendee,
            business=business,
            closed_at=closed_at,
            created_at=created_at,
            deleted_at=deleted_at,
            discounted_amount=discounted_amount,
            id=id,
            invoice_items=invoice_items,
            invoice_to=invoice_to,
            issue_date=issue_date,
            links=links,
            net_amount=net_amount,
            notes=notes,
            number=number,
            online_payment_url=online_payment_url,
            original_invoice=original_invoice,
            patient=patient,
            patient_extra_information=patient_extra_information,
            practitioner=practitioner,
            reversed_invoices=reversed_invoices,
            signature=signature,
            status=status,
            status_description=status_description,
            tax_amount=tax_amount,
            total_amount=total_amount,
            updated_at=updated_at,
        )

        invoice.additional_properties = d
        return invoice

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
