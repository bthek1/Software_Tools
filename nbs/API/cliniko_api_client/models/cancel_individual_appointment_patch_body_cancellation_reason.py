from typing import Literal, Set, cast

CancelIndividualAppointmentPatchBodyCancellationReason = Literal[10, 20, 30, 40, 50, 60]

CANCEL_INDIVIDUAL_APPOINTMENT_PATCH_BODY_CANCELLATION_REASON_VALUES: Set[
    CancelIndividualAppointmentPatchBodyCancellationReason
] = {
    10,
    20,
    30,
    40,
    50,
    60,
}


def check_cancel_individual_appointment_patch_body_cancellation_reason(
    value: int,
) -> CancelIndividualAppointmentPatchBodyCancellationReason:
    if value in CANCEL_INDIVIDUAL_APPOINTMENT_PATCH_BODY_CANCELLATION_REASON_VALUES:
        return cast(CancelIndividualAppointmentPatchBodyCancellationReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CANCEL_INDIVIDUAL_APPOINTMENT_PATCH_BODY_CANCELLATION_REASON_VALUES!r}"
    )
