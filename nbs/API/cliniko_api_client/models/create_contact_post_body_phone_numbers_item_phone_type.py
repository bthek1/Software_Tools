from typing import Literal, Set, cast

CreateContactPostBodyPhoneNumbersItemPhoneType = Literal["Fax", "Home", "Mobile", "Other", "Work"]

CREATE_CONTACT_POST_BODY_PHONE_NUMBERS_ITEM_PHONE_TYPE_VALUES: Set[CreateContactPostBodyPhoneNumbersItemPhoneType] = {
    "Fax",
    "Home",
    "Mobile",
    "Other",
    "Work",
}


def check_create_contact_post_body_phone_numbers_item_phone_type(
    value: str,
) -> CreateContactPostBodyPhoneNumbersItemPhoneType:
    if value in CREATE_CONTACT_POST_BODY_PHONE_NUMBERS_ITEM_PHONE_TYPE_VALUES:
        return cast(CreateContactPostBodyPhoneNumbersItemPhoneType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_CONTACT_POST_BODY_PHONE_NUMBERS_ITEM_PHONE_TYPE_VALUES!r}"
    )
