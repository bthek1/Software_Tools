from typing import Literal, Set, cast

SmsCommunicationType = Literal["Email", "Other", "Phone call", "SMS"]

SMS_COMMUNICATION_TYPE_VALUES: Set[SmsCommunicationType] = {
    "Email",
    "Other",
    "Phone call",
    "SMS",
}


def check_sms_communication_type(value: str) -> SmsCommunicationType:
    if value in SMS_COMMUNICATION_TYPE_VALUES:
        return cast(SmsCommunicationType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SMS_COMMUNICATION_TYPE_VALUES!r}")
