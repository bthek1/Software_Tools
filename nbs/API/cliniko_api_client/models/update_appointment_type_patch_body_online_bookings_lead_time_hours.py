from typing import Literal, Set, cast

UpdateAppointmentTypePatchBodyOnlineBookingsLeadTimeHours = Literal[0, 1, 2, 4, 12, 18, 24, 48, 72, 168, 336, 504, 672]

UPDATE_APPOINTMENT_TYPE_PATCH_BODY_ONLINE_BOOKINGS_LEAD_TIME_HOURS_VALUES: Set[
    UpdateAppointmentTypePatchBodyOnlineBookingsLeadTimeHours
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


def check_update_appointment_type_patch_body_online_bookings_lead_time_hours(
    value: int,
) -> UpdateAppointmentTypePatchBodyOnlineBookingsLeadTimeHours:
    if value in UPDATE_APPOINTMENT_TYPE_PATCH_BODY_ONLINE_BOOKINGS_LEAD_TIME_HOURS_VALUES:
        return cast(UpdateAppointmentTypePatchBodyOnlineBookingsLeadTimeHours, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_APPOINTMENT_TYPE_PATCH_BODY_ONLINE_BOOKINGS_LEAD_TIME_HOURS_VALUES!r}"
    )
