from typing import Literal, Set, cast

ContactType = Literal["3rd Party Payer", "Doctor", "Standard"]

CONTACT_TYPE_VALUES: Set[ContactType] = {
    "3rd Party Payer",
    "Doctor",
    "Standard",
}


def check_contact_type(value: str) -> ContactType:
    if value in CONTACT_TYPE_VALUES:
        return cast(ContactType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_TYPE_VALUES!r}")
