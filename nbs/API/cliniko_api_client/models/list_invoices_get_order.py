from typing import Literal, Set, cast

ListInvoicesGetOrder = Literal["asc", "desc"]

LIST_INVOICES_GET_ORDER_VALUES: Set[ListInvoicesGetOrder] = {
    "asc",
    "desc",
}


def check_list_invoices_get_order(value: str) -> ListInvoicesGetOrder:
    if value in LIST_INVOICES_GET_ORDER_VALUES:
        return cast(ListInvoicesGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_GET_ORDER_VALUES!r}")
