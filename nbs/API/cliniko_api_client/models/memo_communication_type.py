from typing import Literal, Set, cast

MemoCommunicationType = Literal["Email", "Other", "Phone call", "SMS"]

MEMO_COMMUNICATION_TYPE_VALUES: Set[MemoCommunicationType] = {
    "Email",
    "Other",
    "Phone call",
    "SMS",
}


def check_memo_communication_type(value: str) -> MemoCommunicationType:
    if value in MEMO_COMMUNICATION_TYPE_VALUES:
        return cast(MemoCommunicationType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MEMO_COMMUNICATION_TYPE_VALUES!r}")
