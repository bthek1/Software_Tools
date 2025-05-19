from typing import Literal, Set, cast

ListAttendeesForGroupAppointmentGetOrder = Literal["asc", "desc"]

LIST_ATTENDEES_FOR_GROUP_APPOINTMENT_GET_ORDER_VALUES: Set[ListAttendeesForGroupAppointmentGetOrder] = {
    "asc",
    "desc",
}


def check_list_attendees_for_group_appointment_get_order(value: str) -> ListAttendeesForGroupAppointmentGetOrder:
    if value in LIST_ATTENDEES_FOR_GROUP_APPOINTMENT_GET_ORDER_VALUES:
        return cast(ListAttendeesForGroupAppointmentGetOrder, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_ATTENDEES_FOR_GROUP_APPOINTMENT_GET_ORDER_VALUES!r}"
    )
