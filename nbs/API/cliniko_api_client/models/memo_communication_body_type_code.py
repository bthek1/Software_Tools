from typing import Literal, Set, cast

MemoCommunicationBodyTypeCode = Literal[1, 2, 3, 4]

MEMO_COMMUNICATION_BODY_TYPE_CODE_VALUES: Set[MemoCommunicationBodyTypeCode] = {
    1,
    2,
    3,
    4,
}


def check_memo_communication_body_type_code(value: int) -> MemoCommunicationBodyTypeCode:
    if value in MEMO_COMMUNICATION_BODY_TYPE_CODE_VALUES:
        return cast(MemoCommunicationBodyTypeCode, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MEMO_COMMUNICATION_BODY_TYPE_CODE_VALUES!r}")
