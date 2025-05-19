from typing import Literal, Set, cast

ListBookingsForPatientCaseGetOrder = Literal["asc", "desc"]

LIST_BOOKINGS_FOR_PATIENT_CASE_GET_ORDER_VALUES: Set[ListBookingsForPatientCaseGetOrder] = {
    "asc",
    "desc",
}


def check_list_bookings_for_patient_case_get_order(value: str) -> ListBookingsForPatientCaseGetOrder:
    if value in LIST_BOOKINGS_FOR_PATIENT_CASE_GET_ORDER_VALUES:
        return cast(ListBookingsForPatientCaseGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_BOOKINGS_FOR_PATIENT_CASE_GET_ORDER_VALUES!r}")
