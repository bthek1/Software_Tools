from typing import Literal, Set, cast

MemoCommunicationDirectionDescription = Literal["Received", "Sent"]

MEMO_COMMUNICATION_DIRECTION_DESCRIPTION_VALUES: Set[MemoCommunicationDirectionDescription] = {
    "Received",
    "Sent",
}


def check_memo_communication_direction_description(value: str) -> MemoCommunicationDirectionDescription:
    if value in MEMO_COMMUNICATION_DIRECTION_DESCRIPTION_VALUES:
        return cast(MemoCommunicationDirectionDescription, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MEMO_COMMUNICATION_DIRECTION_DESCRIPTION_VALUES!r}")
