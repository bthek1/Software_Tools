from typing import Literal, Set, cast

CreateAppointmentTypePostBodyOnlineBookingsLeadTimeHours = Literal[0, 1, 2, 4, 12, 18, 24, 48, 72, 168, 336, 504, 672]

CREATE_APPOINTMENT_TYPE_POST_BODY_ONLINE_BOOKINGS_LEAD_TIME_HOURS_VALUES: Set[
    CreateAppointmentTypePostBodyOnlineBookingsLeadTimeHours
] = {
    0,
    1,
    2,
    4,
    12,
    18,
    24,
    48,
    72,
    168,
    336,
    504,
    672,
}


def check_create_appointment_type_post_body_online_bookings_lead_time_hours(
    value: int,
) -> CreateAppointmentTypePostBodyOnlineBookingsLeadTimeHours:
    if value in CREATE_APPOINTMENT_TYPE_POST_BODY_ONLINE_BOOKINGS_LEAD_TIME_HOURS_VALUES:
        return cast(CreateAppointmentTypePostBodyOnlineBookingsLeadTimeHours, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_APPOINTMENT_TYPE_POST_BODY_ONLINE_BOOKINGS_LEAD_TIME_HOURS_VALUES!r}"
    )
