from typing import Literal, Set, cast

CreateAppointmentTypePostBodyOnlinePaymentsMode = Literal["deposit_required", "optional", "required"]

CREATE_APPOINTMENT_TYPE_POST_BODY_ONLINE_PAYMENTS_MODE_VALUES: Set[CreateAppointmentTypePostBodyOnlinePaymentsMode] = {
    "deposit_required",
    "optional",
    "required",
}


def check_create_appointment_type_post_body_online_payments_mode(
    value: str,
) -> CreateAppointmentTypePostBodyOnlinePaymentsMode:
    if value in CREATE_APPOINTMENT_TYPE_POST_BODY_ONLINE_PAYMENTS_MODE_VALUES:
        return cast(CreateAppointmentTypePostBodyOnlinePaymentsMode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_APPOINTMENT_TYPE_POST_BODY_ONLINE_PAYMENTS_MODE_VALUES!r}"
    )
