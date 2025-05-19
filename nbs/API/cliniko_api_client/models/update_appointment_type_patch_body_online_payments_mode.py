from typing import Literal, Set, cast

UpdateAppointmentTypePatchBodyOnlinePaymentsMode = Literal["deposit_required", "optional", "required"]

UPDATE_APPOINTMENT_TYPE_PATCH_BODY_ONLINE_PAYMENTS_MODE_VALUES: Set[
    UpdateAppointmentTypePatchBodyOnlinePaymentsMode
] = {
    "deposit_required",
    "optional",
    "required",
}


def check_update_appointment_type_patch_body_online_payments_mode(
    value: str,
) -> UpdateAppointmentTypePatchBodyOnlinePaymentsMode:
    if value in UPDATE_APPOINTMENT_TYPE_PATCH_BODY_ONLINE_PAYMENTS_MODE_VALUES:
        return cast(UpdateAppointmentTypePatchBodyOnlinePaymentsMode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_APPOINTMENT_TYPE_PATCH_BODY_ONLINE_PAYMENTS_MODE_VALUES!r}"
    )
