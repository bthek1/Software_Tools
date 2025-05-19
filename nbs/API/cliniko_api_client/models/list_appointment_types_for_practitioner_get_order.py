from typing import Literal, Set, cast

ListAppointmentTypesForPractitionerGetOrder = Literal["asc", "desc"]

LIST_APPOINTMENT_TYPES_FOR_PRACTITIONER_GET_ORDER_VALUES: Set[ListAppointmentTypesForPractitionerGetOrder] = {
    "asc",
    "desc",
}


def check_list_appointment_types_for_practitioner_get_order(value: str) -> ListAppointmentTypesForPractitionerGetOrder:
    if value in LIST_APPOINTMENT_TYPES_FOR_PRACTITIONER_GET_ORDER_VALUES:
        return cast(ListAppointmentTypesForPractitionerGetOrder, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_APPOINTMENT_TYPES_FOR_PRACTITIONER_GET_ORDER_VALUES!r}"
    )
