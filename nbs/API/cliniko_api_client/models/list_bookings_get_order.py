from typing import Literal, Set, cast

ListBookingsGetOrder = Literal["asc", "desc"]

LIST_BOOKINGS_GET_ORDER_VALUES: Set[ListBookingsGetOrder] = {
    "asc",
    "desc",
}


def check_list_bookings_get_order(value: str) -> ListBookingsGetOrder:
    if value in LIST_BOOKINGS_GET_ORDER_VALUES:
        return cast(ListBookingsGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_BOOKINGS_GET_ORDER_VALUES!r}")
