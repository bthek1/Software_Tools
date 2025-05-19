from typing import Literal, Set, cast

ListInvoicesForAppointmentGetOrder = Literal["asc", "desc"]

LIST_INVOICES_FOR_APPOINTMENT_GET_ORDER_VALUES: Set[ListInvoicesForAppointmentGetOrder] = {
    "asc",
    "desc",
}


def check_list_invoices_for_appointment_get_order(value: str) -> ListInvoicesForAppointmentGetOrder:
    if value in LIST_INVOICES_FOR_APPOINTMENT_GET_ORDER_VALUES:
        return cast(ListInvoicesForAppointmentGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_FOR_APPOINTMENT_GET_ORDER_VALUES!r}")
