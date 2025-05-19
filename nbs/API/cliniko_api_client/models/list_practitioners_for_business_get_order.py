from typing import Literal, Set, cast

ListPractitionersForBusinessGetOrder = Literal["asc", "desc"]

LIST_PRACTITIONERS_FOR_BUSINESS_GET_ORDER_VALUES: Set[ListPractitionersForBusinessGetOrder] = {
    "asc",
    "desc",
}


def check_list_practitioners_for_business_get_order(value: str) -> ListPractitionersForBusinessGetOrder:
    if value in LIST_PRACTITIONERS_FOR_BUSINESS_GET_ORDER_VALUES:
        return cast(ListPractitionersForBusinessGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_PRACTITIONERS_FOR_BUSINESS_GET_ORDER_VALUES!r}")
