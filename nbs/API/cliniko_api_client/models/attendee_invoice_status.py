from typing import Literal, Set, cast

AttendeeInvoiceStatus = Literal[10, 20, 30, 40]

ATTENDEE_INVOICE_STATUS_VALUES: Set[AttendeeInvoiceStatus] = {
    10,
    20,
    30,
    40,
}


def check_attendee_invoice_status(value: int) -> AttendeeInvoiceStatus:
    if value in ATTENDEE_INVOICE_STATUS_VALUES:
        return cast(AttendeeInvoiceStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ATTENDEE_INVOICE_STATUS_VALUES!r}")
