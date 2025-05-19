from typing import Literal, Set, cast

ContactTypeCode = Literal[0, 1, 2]

CONTACT_TYPE_CODE_VALUES: Set[ContactTypeCode] = {
    0,
    1,
    2,
}


def check_contact_type_code(value: int) -> ContactTypeCode:
    if value in CONTACT_TYPE_CODE_VALUES:
        return cast(ContactTypeCode, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_TYPE_CODE_VALUES!r}")
