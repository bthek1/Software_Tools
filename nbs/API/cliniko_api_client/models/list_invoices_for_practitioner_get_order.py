from typing import Literal, Set, cast

ListInvoicesForPractitionerGetOrder = Literal["asc", "desc"]

LIST_INVOICES_FOR_PRACTITIONER_GET_ORDER_VALUES: Set[ListInvoicesForPractitionerGetOrder] = {
    "asc",
    "desc",
}


def check_list_invoices_for_practitioner_get_order(value: str) -> ListInvoicesForPractitionerGetOrder:
    if value in LIST_INVOICES_FOR_PRACTITIONER_GET_ORDER_VALUES:
        return cast(ListInvoicesForPractitionerGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_FOR_PRACTITIONER_GET_ORDER_VALUES!r}")
