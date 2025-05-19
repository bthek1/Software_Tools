from typing import Literal, Set, cast

MemoCommunicationBodyDirectionCode = Literal[1, 2]

MEMO_COMMUNICATION_BODY_DIRECTION_CODE_VALUES: Set[MemoCommunicationBodyDirectionCode] = {
    1,
    2,
}


def check_memo_communication_body_direction_code(value: int) -> MemoCommunicationBodyDirectionCode:
    if value in MEMO_COMMUNICATION_BODY_DIRECTION_CODE_VALUES:
        return cast(MemoCommunicationBodyDirectionCode, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MEMO_COMMUNICATION_BODY_DIRECTION_CODE_VALUES!r}")
