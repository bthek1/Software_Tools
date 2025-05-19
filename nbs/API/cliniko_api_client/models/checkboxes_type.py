from typing import Literal, Set, cast

CheckboxesType = Literal["checkboxes"]

CHECKBOXES_TYPE_VALUES: Set[CheckboxesType] = {
    "checkboxes",
}


def check_checkboxes_type(value: str) -> CheckboxesType:
    if value in CHECKBOXES_TYPE_VALUES:
        return cast(CheckboxesType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CHECKBOXES_TYPE_VALUES!r}")
