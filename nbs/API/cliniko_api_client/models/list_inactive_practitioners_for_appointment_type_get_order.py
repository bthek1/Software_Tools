from typing import Literal, Set, cast

ListInactivePractitionersForAppointmentTypeGetOrder = Literal["asc", "desc"]

LIST_INACTIVE_PRACTITIONERS_FOR_APPOINTMENT_TYPE_GET_ORDER_VALUES: Set[
    ListInactivePractitionersForAppointmentTypeGetOrder
] = {
    "asc",
    "desc",
}


def check_list_inactive_practitioners_for_appointment_type_get_order(
    value: str,
) -> ListInactivePractitionersForAppointmentTypeGetOrder:
    if value in LIST_INACTIVE_PRACTITIONERS_FOR_APPOINTMENT_TYPE_GET_ORDER_VALUES:
        return cast(ListInactivePractitionersForAppointmentTypeGetOrder, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_INACTIVE_PRACTITIONERS_FOR_APPOINTMENT_TYPE_GET_ORDER_VALUES!r}"
    )
