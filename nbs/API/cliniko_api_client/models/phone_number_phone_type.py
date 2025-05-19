from typing import Literal, Set, cast

PhoneNumberPhoneType = Literal["Fax", "Home", "Mobile", "Other", "Work"]

PHONE_NUMBER_PHONE_TYPE_VALUES: Set[PhoneNumberPhoneType] = {
    "Fax",
    "Home",
    "Mobile",
    "Other",
    "Work",
}


def check_phone_number_phone_type(value: str) -> PhoneNumberPhoneType:
    if value in PHONE_NUMBER_PHONE_TYPE_VALUES:
        return cast(PhoneNumberPhoneType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PHONE_NUMBER_PHONE_TYPE_VALUES!r}")
