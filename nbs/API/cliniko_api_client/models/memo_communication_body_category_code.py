from typing import Literal, Set, cast

MemoCommunicationBodyCategoryCode = Literal[12]

MEMO_COMMUNICATION_BODY_CATEGORY_CODE_VALUES: Set[MemoCommunicationBodyCategoryCode] = {
    12,
}


def check_memo_communication_body_category_code(value: int) -> MemoCommunicationBodyCategoryCode:
    if value in MEMO_COMMUNICATION_BODY_CATEGORY_CODE_VALUES:
        return cast(MemoCommunicationBodyCategoryCode, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MEMO_COMMUNICATION_BODY_CATEGORY_CODE_VALUES!r}")
