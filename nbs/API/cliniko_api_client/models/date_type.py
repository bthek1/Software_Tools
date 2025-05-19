from typing import Literal, Set, cast

DateType = Literal["date"]

DATE_TYPE_VALUES: Set[DateType] = {
    "date",
}


def check_date_type(value: str) -> DateType:
    if value in DATE_TYPE_VALUES:
        return cast(DateType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATE_TYPE_VALUES!r}")
