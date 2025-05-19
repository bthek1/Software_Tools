from typing import Literal, Set, cast

ListIndividualAppointmentsGetOrder = Literal["asc", "desc"]

LIST_INDIVIDUAL_APPOINTMENTS_GET_ORDER_VALUES: Set[ListIndividualAppointmentsGetOrder] = {
    "asc",
    "desc",
}


def check_list_individual_appointments_get_order(value: str) -> ListIndividualAppointmentsGetOrder:
    if value in LIST_INDIVIDUAL_APPOINTMENTS_GET_ORDER_VALUES:
        return cast(ListIndividualAppointmentsGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_INDIVIDUAL_APPOINTMENTS_GET_ORDER_VALUES!r}")
