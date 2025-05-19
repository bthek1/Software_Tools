from typing import Literal, Set, cast

ListAttendeesGetOrder = Literal["asc", "desc"]

LIST_ATTENDEES_GET_ORDER_VALUES: Set[ListAttendeesGetOrder] = {
    "asc",
    "desc",
}


def check_list_attendees_get_order(value: str) -> ListAttendeesGetOrder:
    if value in LIST_ATTENDEES_GET_ORDER_VALUES:
        return cast(ListAttendeesGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_ATTENDEES_GET_ORDER_VALUES!r}")
