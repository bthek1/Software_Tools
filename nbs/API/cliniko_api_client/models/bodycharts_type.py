from typing import Literal, Set, cast

BodychartsType = Literal["bodycharts"]

BODYCHARTS_TYPE_VALUES: Set[BodychartsType] = {
    "bodycharts",
}


def check_bodycharts_type(value: str) -> BodychartsType:
    if value in BODYCHARTS_TYPE_VALUES:
        return cast(BodychartsType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BODYCHARTS_TYPE_VALUES!r}")
