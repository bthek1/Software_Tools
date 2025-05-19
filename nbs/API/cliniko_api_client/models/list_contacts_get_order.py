from typing import Literal, Set, cast

ListContactsGetOrder = Literal["asc", "desc"]

LIST_CONTACTS_GET_ORDER_VALUES: Set[ListContactsGetOrder] = {
    "asc",
    "desc",
}


def check_list_contacts_get_order(value: str) -> ListContactsGetOrder:
    if value in LIST_CONTACTS_GET_ORDER_VALUES:
        return cast(ListContactsGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_CONTACTS_GET_ORDER_VALUES!r}")
