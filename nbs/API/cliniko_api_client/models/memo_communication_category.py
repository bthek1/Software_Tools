from typing import Literal, Set, cast

MemoCommunicationCategory = Literal["Memo"]

MEMO_COMMUNICATION_CATEGORY_VALUES: Set[MemoCommunicationCategory] = {
    "Memo",
}


def check_memo_communication_category(value: str) -> MemoCommunicationCategory:
    if value in MEMO_COMMUNICATION_CATEGORY_VALUES:
        return cast(MemoCommunicationCategory, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MEMO_COMMUNICATION_CATEGORY_VALUES!r}")
