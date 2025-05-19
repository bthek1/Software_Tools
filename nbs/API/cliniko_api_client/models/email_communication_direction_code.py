from typing import Literal, Set, cast

EmailCommunicationDirectionCode = Literal[1, 2]

EMAIL_COMMUNICATION_DIRECTION_CODE_VALUES: Set[EmailCommunicationDirectionCode] = {
    1,
    2,
}


def check_email_communication_direction_code(value: int) -> EmailCommunicationDirectionCode:
    if value in EMAIL_COMMUNICATION_DIRECTION_CODE_VALUES:
        return cast(EmailCommunicationDirectionCode, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EMAIL_COMMUNICATION_DIRECTION_CODE_VALUES!r}")
