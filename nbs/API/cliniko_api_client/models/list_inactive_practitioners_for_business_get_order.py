from typing import Literal, Set, cast

ListInactivePractitionersForBusinessGetOrder = Literal["asc", "desc"]

LIST_INACTIVE_PRACTITIONERS_FOR_BUSINESS_GET_ORDER_VALUES: Set[ListInactivePractitionersForBusinessGetOrder] = {
    "asc",
    "desc",
}


def check_list_inactive_practitioners_for_business_get_order(
    value: str,
) -> ListInactivePractitionersForBusinessGetOrder:
    if value in LIST_INACTIVE_PRACTITIONERS_FOR_BUSINESS_GET_ORDER_VALUES:
        return cast(ListInactivePractitionersForBusinessGetOrder, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INACTIVE_PRACTITIONERS_FOR_BUSINESS_GET_ORDER_VALUES!r}"
    )
