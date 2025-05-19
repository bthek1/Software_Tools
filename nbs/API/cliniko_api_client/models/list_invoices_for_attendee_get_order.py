from typing import Literal, Set, cast

ListInvoicesForAttendeeGetOrder = Literal["asc", "desc"]

LIST_INVOICES_FOR_ATTENDEE_GET_ORDER_VALUES: Set[ListInvoicesForAttendeeGetOrder] = {
    "asc",
    "desc",
}


def check_list_invoices_for_attendee_get_order(value: str) -> ListInvoicesForAttendeeGetOrder:
    if value in LIST_INVOICES_FOR_ATTENDEE_GET_ORDER_VALUES:
        return cast(ListInvoicesForAttendeeGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_FOR_ATTENDEE_GET_ORDER_VALUES!r}")
