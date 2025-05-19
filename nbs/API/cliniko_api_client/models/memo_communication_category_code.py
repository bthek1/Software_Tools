from typing import Literal, Set, cast

MemoCommunicationCategoryCode = Literal[12]

MEMO_COMMUNICATION_CATEGORY_CODE_VALUES: Set[MemoCommunicationCategoryCode] = {
    12,
}


def check_memo_communication_category_code(value: int) -> MemoCommunicationCategoryCode:
    if value in MEMO_COMMUNICATION_CATEGORY_CODE_VALUES:
        return cast(MemoCommunicationCategoryCode, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MEMO_COMMUNICATION_CATEGORY_CODE_VALUES!r}")
