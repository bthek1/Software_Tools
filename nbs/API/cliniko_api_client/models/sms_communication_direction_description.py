from typing import Literal, Set, cast

SmsCommunicationDirectionDescription = Literal["Received", "Sent"]

SMS_COMMUNICATION_DIRECTION_DESCRIPTION_VALUES: Set[SmsCommunicationDirectionDescription] = {
    "Received",
    "Sent",
}


def check_sms_communication_direction_description(value: str) -> SmsCommunicationDirectionDescription:
    if value in SMS_COMMUNICATION_DIRECTION_DESCRIPTION_VALUES:
        return cast(SmsCommunicationDirectionDescription, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SMS_COMMUNICATION_DIRECTION_DESCRIPTION_VALUES!r}")
