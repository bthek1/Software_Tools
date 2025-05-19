from typing import Literal, Set, cast

ListInvoiceItemsGetOrder = Literal["asc", "desc"]

LIST_INVOICE_ITEMS_GET_ORDER_VALUES: Set[ListInvoiceItemsGetOrder] = {
    "asc",
    "desc",
}


def check_list_invoice_items_get_order(value: str) -> ListInvoiceItemsGetOrder:
    if value in LIST_INVOICE_ITEMS_GET_ORDER_VALUES:
        return cast(ListInvoiceItemsGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_INVOICE_ITEMS_GET_ORDER_VALUES!r}")
