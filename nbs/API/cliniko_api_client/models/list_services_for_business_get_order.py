from typing import Literal, Set, cast

ListServicesForBusinessGetOrder = Literal["asc", "desc"]

LIST_SERVICES_FOR_BUSINESS_GET_ORDER_VALUES: Set[ListServicesForBusinessGetOrder] = {
    "asc",
    "desc",
}


def check_list_services_for_business_get_order(value: str) -> ListServicesForBusinessGetOrder:
    if value in LIST_SERVICES_FOR_BUSINESS_GET_ORDER_VALUES:
        return cast(ListServicesForBusinessGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_SERVICES_FOR_BUSINESS_GET_ORDER_VALUES!r}")
