from typing import Literal, Set, cast

UpdateContactPatchBodyPhoneNumbersItemPhoneType = Literal["Fax", "Home", "Mobile", "Other", "Work"]

UPDATE_CONTACT_PATCH_BODY_PHONE_NUMBERS_ITEM_PHONE_TYPE_VALUES: Set[UpdateContactPatchBodyPhoneNumbersItemPhoneType] = {
    "Fax",
    "Home",
    "Mobile",
    "Other",
    "Work",
}


def check_update_contact_patch_body_phone_numbers_item_phone_type(
    value: str,
) -> UpdateContactPatchBodyPhoneNumbersItemPhoneType:
    if value in UPDATE_CONTACT_PATCH_BODY_PHONE_NUMBERS_ITEM_PHONE_TYPE_VALUES:
        return cast(UpdateContactPatchBodyPhoneNumbersItemPhoneType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_CONTACT_PATCH_BODY_PHONE_NUMBERS_ITEM_PHONE_TYPE_VALUES!r}"
    )
