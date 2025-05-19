from typing import Literal, Set, cast

UpdateContactPatchBodyTypeCode = Literal[0, 1, 2]

UPDATE_CONTACT_PATCH_BODY_TYPE_CODE_VALUES: Set[UpdateContactPatchBodyTypeCode] = {
    0,
    1,
    2,
}


def check_update_contact_patch_body_type_code(value: int) -> UpdateContactPatchBodyTypeCode:
    if value in UPDATE_CONTACT_PATCH_BODY_TYPE_CODE_VALUES:
        return cast(UpdateContactPatchBodyTypeCode, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_CONTACT_PATCH_BODY_TYPE_CODE_VALUES!r}")
