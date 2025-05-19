from typing import Literal, Set, cast

ListInvoiceItemsForInvoiceGetOrder = Literal["asc", "desc"]

LIST_INVOICE_ITEMS_FOR_INVOICE_GET_ORDER_VALUES: Set[ListInvoiceItemsForInvoiceGetOrder] = {
    "asc",
    "desc",
}


def check_list_invoice_items_for_invoice_get_order(value: str) -> ListInvoiceItemsForInvoiceGetOrder:
    if value in LIST_INVOICE_ITEMS_FOR_INVOICE_GET_ORDER_VALUES:
        return cast(ListInvoiceItemsForInvoiceGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_INVOICE_ITEMS_FOR_INVOICE_GET_ORDER_VALUES!r}")
