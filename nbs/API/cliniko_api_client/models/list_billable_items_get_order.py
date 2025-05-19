from typing import Literal, Set, cast

ListBillableItemsGetOrder = Literal["asc", "desc"]

LIST_BILLABLE_ITEMS_GET_ORDER_VALUES: Set[ListBillableItemsGetOrder] = {
    "asc",
    "desc",
}


def check_list_billable_items_get_order(value: str) -> ListBillableItemsGetOrder:
    if value in LIST_BILLABLE_ITEMS_GET_ORDER_VALUES:
        return cast(ListBillableItemsGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_BILLABLE_ITEMS_GET_ORDER_VALUES!r}")
