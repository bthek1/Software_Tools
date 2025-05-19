from typing import Literal, Set, cast

ListServicesGetOrder = Literal["asc", "desc"]

LIST_SERVICES_GET_ORDER_VALUES: Set[ListServicesGetOrder] = {
    "asc",
    "desc",
}


def check_list_services_get_order(value: str) -> ListServicesGetOrder:
    if value in LIST_SERVICES_GET_ORDER_VALUES:
        return cast(ListServicesGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_SERVICES_GET_ORDER_VALUES!r}")
