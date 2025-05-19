from typing import Literal, Set, cast

IndividualAppointmentCancellationReasonDescription = Literal[
    "Away", "Condition Worse", "COVID-19 related", "Feeling Better", "Other", "Sick", "Work"
]

INDIVIDUAL_APPOINTMENT_CANCELLATION_REASON_DESCRIPTION_VALUES: Set[
    IndividualAppointmentCancellationReasonDescription
] = {
    "Away",
    "Condition Worse",
    "COVID-19 related",
    "Feeling Better",
    "Other",
    "Sick",
    "Work",
}


def check_individual_appointment_cancellation_reason_description(
    value: str,
) -> IndividualAppointmentCancellationReasonDescription:
    if value in INDIVIDUAL_APPOINTMENT_CANCELLATION_REASON_DESCRIPTION_VALUES:
        return cast(IndividualAppointmentCancellationReasonDescription, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INDIVIDUAL_APPOINTMENT_CANCELLATION_REASON_DESCRIPTION_VALUES!r}"
    )
