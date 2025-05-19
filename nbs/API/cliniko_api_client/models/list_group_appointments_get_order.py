from typing import Literal, Set, cast

ListGroupAppointmentsGetOrder = Literal["asc", "desc"]

LIST_GROUP_APPOINTMENTS_GET_ORDER_VALUES: Set[ListGroupAppointmentsGetOrder] = {
    "asc",
    "desc",
}


def check_list_group_appointments_get_order(value: str) -> ListGroupAppointmentsGetOrder:
    if value in LIST_GROUP_APPOINTMENTS_GET_ORDER_VALUES:
        return cast(ListGroupAppointmentsGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_GROUP_APPOINTMENTS_GET_ORDER_VALUES!r}")
