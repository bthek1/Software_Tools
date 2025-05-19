from typing import Literal, Set, cast

EmailCommunicationTypeCode = Literal[1, 2, 3, 4]

EMAIL_COMMUNICATION_TYPE_CODE_VALUES: Set[EmailCommunicationTypeCode] = {
    1,
    2,
    3,
    4,
}


def check_email_communication_type_code(value: int) -> EmailCommunicationTypeCode:
    if value in EMAIL_COMMUNICATION_TYPE_CODE_VALUES:
        return cast(EmailCommunicationTypeCode, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EMAIL_COMMUNICATION_TYPE_CODE_VALUES!r}")
