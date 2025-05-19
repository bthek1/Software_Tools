from typing import Literal, Set, cast

SmsCommunicationTypeCode = Literal[1, 2, 3, 4]

SMS_COMMUNICATION_TYPE_CODE_VALUES: Set[SmsCommunicationTypeCode] = {
    1,
    2,
    3,
    4,
}


def check_sms_communication_type_code(value: int) -> SmsCommunicationTypeCode:
    if value in SMS_COMMUNICATION_TYPE_CODE_VALUES:
        return cast(SmsCommunicationTypeCode, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SMS_COMMUNICATION_TYPE_CODE_VALUES!r}")
