from typing import Literal, Set, cast

ListInactivePractitionersGetOrder = Literal["asc", "desc"]

LIST_INACTIVE_PRACTITIONERS_GET_ORDER_VALUES: Set[ListInactivePractitionersGetOrder] = {
    "asc",
    "desc",
}


def check_list_inactive_practitioners_get_order(value: str) -> ListInactivePractitionersGetOrder:
    if value in LIST_INACTIVE_PRACTITIONERS_GET_ORDER_VALUES:
        return cast(ListInactivePractitionersGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_INACTIVE_PRACTITIONERS_GET_ORDER_VALUES!r}")
