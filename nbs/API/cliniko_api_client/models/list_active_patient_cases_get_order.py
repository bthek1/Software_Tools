from typing import Literal, Set, cast

ListActivePatientCasesGetOrder = Literal["asc", "desc"]

LIST_ACTIVE_PATIENT_CASES_GET_ORDER_VALUES: Set[ListActivePatientCasesGetOrder] = {
    "asc",
    "desc",
}


def check_list_active_patient_cases_get_order(value: str) -> ListActivePatientCasesGetOrder:
    if value in LIST_ACTIVE_PATIENT_CASES_GET_ORDER_VALUES:
        return cast(ListActivePatientCasesGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_ACTIVE_PATIENT_CASES_GET_ORDER_VALUES!r}")
