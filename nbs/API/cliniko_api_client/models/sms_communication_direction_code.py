from typing import Literal, Set, cast

SmsCommunicationDirectionCode = Literal[1, 2]

SMS_COMMUNICATION_DIRECTION_CODE_VALUES: Set[SmsCommunicationDirectionCode] = {
    1,
    2,
}


def check_sms_communication_direction_code(value: int) -> SmsCommunicationDirectionCode:
    if value in SMS_COMMUNICATION_DIRECTION_CODE_VALUES:
        return cast(SmsCommunicationDirectionCode, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SMS_COMMUNICATION_DIRECTION_CODE_VALUES!r}")
