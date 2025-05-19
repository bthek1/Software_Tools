from typing import Literal, Set, cast

EmailCommunicationType = Literal["Email", "Other", "Phone call", "SMS"]

EMAIL_COMMUNICATION_TYPE_VALUES: Set[EmailCommunicationType] = {
    "Email",
    "Other",
    "Phone call",
    "SMS",
}


def check_email_communication_type(value: str) -> EmailCommunicationType:
    if value in EMAIL_COMMUNICATION_TYPE_VALUES:
        return cast(EmailCommunicationType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EMAIL_COMMUNICATION_TYPE_VALUES!r}")
