from typing import Literal, Set, cast

InvoiceStatusDescription = Literal["Closed", "Open", "Open credit", "Paid"]

INVOICE_STATUS_DESCRIPTION_VALUES: Set[InvoiceStatusDescription] = {
    "Closed",
    "Open",
    "Open credit",
    "Paid",
}


def check_invoice_status_description(value: str) -> InvoiceStatusDescription:
    if value in INVOICE_STATUS_DESCRIPTION_VALUES:
        return cast(InvoiceStatusDescription, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVOICE_STATUS_DESCRIPTION_VALUES!r}")
