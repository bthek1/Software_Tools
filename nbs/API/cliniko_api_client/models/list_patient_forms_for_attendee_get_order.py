from typing import Literal, Set, cast

ListPatientFormsForAttendeeGetOrder = Literal["asc", "desc"]

LIST_PATIENT_FORMS_FOR_ATTENDEE_GET_ORDER_VALUES: Set[ListPatientFormsForAttendeeGetOrder] = {
    "asc",
    "desc",
}


def check_list_patient_forms_for_attendee_get_order(value: str) -> ListPatientFormsForAttendeeGetOrder:
    if value in LIST_PATIENT_FORMS_FOR_ATTENDEE_GET_ORDER_VALUES:
        return cast(ListPatientFormsForAttendeeGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_PATIENT_FORMS_FOR_ATTENDEE_GET_ORDER_VALUES!r}")
