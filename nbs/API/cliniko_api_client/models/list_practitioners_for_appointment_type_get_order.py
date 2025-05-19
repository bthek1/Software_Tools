from typing import Literal, Set, cast

ListPractitionersForAppointmentTypeGetOrder = Literal["asc", "desc"]

LIST_PRACTITIONERS_FOR_APPOINTMENT_TYPE_GET_ORDER_VALUES: Set[ListPractitionersForAppointmentTypeGetOrder] = {
    "asc",
    "desc",
}


def check_list_practitioners_for_appointment_type_get_order(value: str) -> ListPractitionersForAppointmentTypeGetOrder:
    if value in LIST_PRACTITIONERS_FOR_APPOINTMENT_TYPE_GET_ORDER_VALUES:
        return cast(ListPractitionersForAppointmentTypeGetOrder, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_PRACTITIONERS_FOR_APPOINTMENT_TYPE_GET_ORDER_VALUES!r}"
    )
