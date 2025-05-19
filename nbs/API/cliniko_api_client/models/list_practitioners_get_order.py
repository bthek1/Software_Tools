from typing import Literal, Set, cast

ListPractitionersGetOrder = Literal["asc", "desc"]

LIST_PRACTITIONERS_GET_ORDER_VALUES: Set[ListPractitionersGetOrder] = {
    "asc",
    "desc",
}


def check_list_practitioners_get_order(value: str) -> ListPractitionersGetOrder:
    if value in LIST_PRACTITIONERS_GET_ORDER_VALUES:
        return cast(ListPractitionersGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_PRACTITIONERS_GET_ORDER_VALUES!r}")
