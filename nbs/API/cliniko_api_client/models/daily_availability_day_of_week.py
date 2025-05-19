from typing import Literal, Set, cast

DailyAvailabilityDayOfWeek = Literal[0, 1, 2, 3, 4, 5, 6]

DAILY_AVAILABILITY_DAY_OF_WEEK_VALUES: Set[DailyAvailabilityDayOfWeek] = {
    0,
    1,
    2,
    3,
    4,
    5,
    6,
}


def check_daily_availability_day_of_week(value: int) -> DailyAvailabilityDayOfWeek:
    if value in DAILY_AVAILABILITY_DAY_OF_WEEK_VALUES:
        return cast(DailyAvailabilityDayOfWeek, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DAILY_AVAILABILITY_DAY_OF_WEEK_VALUES!r}")
