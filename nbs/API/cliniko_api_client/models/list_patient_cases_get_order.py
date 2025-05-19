from typing import Literal, Set, cast

ListPatientCasesGetOrder = Literal["asc", "desc"]

LIST_PATIENT_CASES_GET_ORDER_VALUES: Set[ListPatientCasesGetOrder] = {
    "asc",
    "desc",
}


def check_list_patient_cases_get_order(value: str) -> ListPatientCasesGetOrder:
    if value in LIST_PATIENT_CASES_GET_ORDER_VALUES:
        return cast(ListPatientCasesGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_PATIENT_CASES_GET_ORDER_VALUES!r}")
