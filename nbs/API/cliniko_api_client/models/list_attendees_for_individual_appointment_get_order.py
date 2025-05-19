from typing import Literal, Set, cast

ListAttendeesForIndividualAppointmentGetOrder = Literal["asc", "desc"]

LIST_ATTENDEES_FOR_INDIVIDUAL_APPOINTMENT_GET_ORDER_VALUES: Set[ListAttendeesForIndividualAppointmentGetOrder] = {
    "asc",
    "desc",
}


def check_list_attendees_for_individual_appointment_get_order(
    value: str,
) -> ListAttendeesForIndividualAppointmentGetOrder:
    if value in LIST_ATTENDEES_FOR_INDIVIDUAL_APPOINTMENT_GET_ORDER_VALUES:
        return cast(ListAttendeesForIndividualAppointmentGetOrder, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_ATTENDEES_FOR_INDIVIDUAL_APPOINTMENT_GET_ORDER_VALUES!r}"
    )
