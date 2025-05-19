from typing import Literal, Set, cast

ListDailyAvailabilitiesForBusinessGetOrder = Literal["asc", "desc"]

LIST_DAILY_AVAILABILITIES_FOR_BUSINESS_GET_ORDER_VALUES: Set[ListDailyAvailabilitiesForBusinessGetOrder] = {
    "asc",
    "desc",
}


def check_list_daily_availabilities_for_business_get_order(value: str) -> ListDailyAvailabilitiesForBusinessGetOrder:
    if value in LIST_DAILY_AVAILABILITIES_FOR_BUSINESS_GET_ORDER_VALUES:
        return cast(ListDailyAvailabilitiesForBusinessGetOrder, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_DAILY_AVAILABILITIES_FOR_BUSINESS_GET_ORDER_VALUES!r}"
    )
