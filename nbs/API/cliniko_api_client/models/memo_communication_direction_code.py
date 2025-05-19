from typing import Literal, Set, cast

MemoCommunicationDirectionCode = Literal[1, 2]

MEMO_COMMUNICATION_DIRECTION_CODE_VALUES: Set[MemoCommunicationDirectionCode] = {
    1,
    2,
}


def check_memo_communication_direction_code(value: int) -> MemoCommunicationDirectionCode:
    if value in MEMO_COMMUNICATION_DIRECTION_CODE_VALUES:
        return cast(MemoCommunicationDirectionCode, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MEMO_COMMUNICATION_DIRECTION_CODE_VALUES!r}")
