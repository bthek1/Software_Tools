from typing import Literal, Set, cast

ListPatientFormsGetOrder = Literal["asc", "desc"]

LIST_PATIENT_FORMS_GET_ORDER_VALUES: Set[ListPatientFormsGetOrder] = {
    "asc",
    "desc",
}


def check_list_patient_forms_get_order(value: str) -> ListPatientFormsGetOrder:
    if value in LIST_PATIENT_FORMS_GET_ORDER_VALUES:
        return cast(ListPatientFormsGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_PATIENT_FORMS_GET_ORDER_VALUES!r}")
