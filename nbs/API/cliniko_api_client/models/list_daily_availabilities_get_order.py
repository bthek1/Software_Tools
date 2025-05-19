from typing import Literal, Set, cast

ListDailyAvailabilitiesGetOrder = Literal["asc", "desc"]

LIST_DAILY_AVAILABILITIES_GET_ORDER_VALUES: Set[ListDailyAvailabilitiesGetOrder] = {
    "asc",
    "desc",
}


def check_list_daily_availabilities_get_order(value: str) -> ListDailyAvailabilitiesGetOrder:
    if value in LIST_DAILY_AVAILABILITIES_GET_ORDER_VALUES:
        return cast(ListDailyAvailabilitiesGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_DAILY_AVAILABILITIES_GET_ORDER_VALUES!r}")
