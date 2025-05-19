from typing import Literal, Set, cast

CancelAttendeePatchBodyCancellationReason = Literal[10, 20, 30, 40, 50, 60]

CANCEL_ATTENDEE_PATCH_BODY_CANCELLATION_REASON_VALUES: Set[CancelAttendeePatchBodyCancellationReason] = {
    10,
    20,
    30,
    40,
    50,
    60,
}


def check_cancel_attendee_patch_body_cancellation_reason(value: int) -> CancelAttendeePatchBodyCancellationReason:
    if value in CANCEL_ATTENDEE_PATCH_BODY_CANCELLATION_REASON_VALUES:
        return cast(CancelAttendeePatchBodyCancellationReason, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CANCEL_ATTENDEE_PATCH_BODY_CANCELLATION_REASON_VALUES!r}"
    )
