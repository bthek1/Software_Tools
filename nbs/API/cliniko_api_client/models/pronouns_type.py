from typing import Literal, Set, cast

PronounsType = Literal["pronouns"]

PRONOUNS_TYPE_VALUES: Set[PronounsType] = {
    "pronouns",
}


def check_pronouns_type(value: str) -> PronounsType:
    if value in PRONOUNS_TYPE_VALUES:
        return cast(PronounsType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRONOUNS_TYPE_VALUES!r}")
