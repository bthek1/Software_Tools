from typing import Literal, Set, cast

AttendeeCancellationReasonDescription = Literal[
    "", "Away", "Condition Worse", "COVID-19 related", "Feeling Better", "Other", "Sick", "Work"
]

ATTENDEE_CANCELLATION_REASON_DESCRIPTION_VALUES: Set[AttendeeCancellationReasonDescription] = {
    "",
    "Away",
    "Condition Worse",
    "COVID-19 related",
    "Feeling Better",
    "Other",
    "Sick",
    "Work",
}


def check_attendee_cancellation_reason_description(value: str) -> AttendeeCancellationReasonDescription:
    if value in ATTENDEE_CANCELLATION_REASON_DESCRIPTION_VALUES:
        return cast(AttendeeCancellationReasonDescription, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ATTENDEE_CANCELLATION_REASON_DESCRIPTION_VALUES!r}")
