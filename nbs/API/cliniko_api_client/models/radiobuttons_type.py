from typing import Literal, Set, cast

RadiobuttonsType = Literal["radiobuttons"]

RADIOBUTTONS_TYPE_VALUES: Set[RadiobuttonsType] = {
    "radiobuttons",
}


def check_radiobuttons_type(value: str) -> RadiobuttonsType:
    if value in RADIOBUTTONS_TYPE_VALUES:
        return cast(RadiobuttonsType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RADIOBUTTONS_TYPE_VALUES!r}")
