from typing import Literal, Set, cast

InvoiceStatus = Literal[10, 20, 30, 40]

INVOICE_STATUS_VALUES: Set[InvoiceStatus] = {
    10,
    20,
    30,
    40,
}


def check_invoice_status(value: int) -> InvoiceStatus:
    if value in INVOICE_STATUS_VALUES:
        return cast(InvoiceStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INVOICE_STATUS_VALUES!r}")
