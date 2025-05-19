from typing import Literal, Set, cast

CreateContactPostBodyTypeCode = Literal[0, 1, 2]

CREATE_CONTACT_POST_BODY_TYPE_CODE_VALUES: Set[CreateContactPostBodyTypeCode] = {
    0,
    1,
    2,
}


def check_create_contact_post_body_type_code(value: int) -> CreateContactPostBodyTypeCode:
    if value in CREATE_CONTACT_POST_BODY_TYPE_CODE_VALUES:
        return cast(CreateContactPostBodyTypeCode, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_CONTACT_POST_BODY_TYPE_CODE_VALUES!r}")
