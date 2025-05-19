from typing import Literal, Set, cast

ListBusinessesGetOrder = Literal["asc", "desc"]

LIST_BUSINESSES_GET_ORDER_VALUES: Set[ListBusinessesGetOrder] = {
    "asc",
    "desc",
}


def check_list_businesses_get_order(value: str) -> ListBusinessesGetOrder:
    if value in LIST_BUSINESSES_GET_ORDER_VALUES:
        return cast(ListBusinessesGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_BUSINESSES_GET_ORDER_VALUES!r}")
