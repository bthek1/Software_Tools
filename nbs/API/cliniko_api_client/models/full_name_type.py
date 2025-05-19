from typing import Literal, Set, cast

FullNameType = Literal["full_name"]

FULL_NAME_TYPE_VALUES: Set[FullNameType] = {
    "full_name",
}


def check_full_name_type(value: str) -> FullNameType:
    if value in FULL_NAME_TYPE_VALUES:
        return cast(FullNameType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FULL_NAME_TYPE_VALUES!r}")
