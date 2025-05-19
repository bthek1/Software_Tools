from typing import Literal, Set, cast

ListDailyAvailabilitiesForPractitionerGetOrder = Literal["asc", "desc"]

LIST_DAILY_AVAILABILITIES_FOR_PRACTITIONER_GET_ORDER_VALUES: Set[ListDailyAvailabilitiesForPractitionerGetOrder] = {
    "asc",
    "desc",
}


def check_list_daily_availabilities_for_practitioner_get_order(
    value: str,
) -> ListDailyAvailabilitiesForPractitionerGetOrder:
    if value in LIST_DAILY_AVAILABILITIES_FOR_PRACTITIONER_GET_ORDER_VALUES:
        return cast(ListDailyAvailabilitiesForPractitionerGetOrder, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_DAILY_AVAILABILITIES_FOR_PRACTITIONER_GET_ORDER_VALUES!r}"
    )
