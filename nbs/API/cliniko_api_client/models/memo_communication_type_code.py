from typing import Literal, Set, cast

MemoCommunicationTypeCode = Literal[1, 2, 3, 4]

MEMO_COMMUNICATION_TYPE_CODE_VALUES: Set[MemoCommunicationTypeCode] = {
    1,
    2,
    3,
    4,
}


def check_memo_communication_type_code(value: int) -> MemoCommunicationTypeCode:
    if value in MEMO_COMMUNICATION_TYPE_CODE_VALUES:
        return cast(MemoCommunicationTypeCode, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MEMO_COMMUNICATION_TYPE_CODE_VALUES!r}")
