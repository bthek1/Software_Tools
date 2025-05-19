from typing import Literal, Set, cast

EmailCommunicationDirectionDescription = Literal["Received", "Sent"]

EMAIL_COMMUNICATION_DIRECTION_DESCRIPTION_VALUES: Set[EmailCommunicationDirectionDescription] = {
    "Received",
    "Sent",
}


def check_email_communication_direction_description(value: str) -> EmailCommunicationDirectionDescription:
    if value in EMAIL_COMMUNICATION_DIRECTION_DESCRIPTION_VALUES:
        return cast(EmailCommunicationDirectionDescription, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EMAIL_COMMUNICATION_DIRECTION_DESCRIPTION_VALUES!r}")
