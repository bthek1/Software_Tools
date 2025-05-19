from typing import Literal, Set, cast

ListAppointmentTypesGetOrder = Literal["asc", "desc"]

LIST_APPOINTMENT_TYPES_GET_ORDER_VALUES: Set[ListAppointmentTypesGetOrder] = {
    "asc",
    "desc",
}


def check_list_appointment_types_get_order(value: str) -> ListAppointmentTypesGetOrder:
    if value in LIST_APPOINTMENT_TYPES_GET_ORDER_VALUES:
        return cast(ListAppointmentTypesGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_APPOINTMENT_TYPES_GET_ORDER_VALUES!r}")
