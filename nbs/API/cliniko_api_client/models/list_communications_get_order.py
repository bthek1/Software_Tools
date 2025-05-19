from typing import Literal, Set, cast

ListCommunicationsGetOrder = Literal["asc", "desc"]

LIST_COMMUNICATIONS_GET_ORDER_VALUES: Set[ListCommunicationsGetOrder] = {
    "asc",
    "desc",
}


def check_list_communications_get_order(value: str) -> ListCommunicationsGetOrder:
    if value in LIST_COMMUNICATIONS_GET_ORDER_VALUES:
        return cast(ListCommunicationsGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_COMMUNICATIONS_GET_ORDER_VALUES!r}")
