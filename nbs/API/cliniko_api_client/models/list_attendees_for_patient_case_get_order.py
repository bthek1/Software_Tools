from typing import Literal, Set, cast

ListAttendeesForPatientCaseGetOrder = Literal["asc", "desc"]

LIST_ATTENDEES_FOR_PATIENT_CASE_GET_ORDER_VALUES: Set[ListAttendeesForPatientCaseGetOrder] = {
    "asc",
    "desc",
}


def check_list_attendees_for_patient_case_get_order(value: str) -> ListAttendeesForPatientCaseGetOrder:
    if value in LIST_ATTENDEES_FOR_PATIENT_CASE_GET_ORDER_VALUES:
        return cast(ListAttendeesForPatientCaseGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_ATTENDEES_FOR_PATIENT_CASE_GET_ORDER_VALUES!r}")
