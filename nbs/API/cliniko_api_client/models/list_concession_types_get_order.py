from typing import Literal, Set, cast

ListConcessionTypesGetOrder = Literal["asc", "desc"]

LIST_CONCESSION_TYPES_GET_ORDER_VALUES: Set[ListConcessionTypesGetOrder] = {
    "asc",
    "desc",
}


def check_list_concession_types_get_order(value: str) -> ListConcessionTypesGetOrder:
    if value in LIST_CONCESSION_TYPES_GET_ORDER_VALUES:
        return cast(ListConcessionTypesGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_CONCESSION_TYPES_GET_ORDER_VALUES!r}")
