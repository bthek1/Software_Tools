from typing import Literal, Set, cast

ListInvoicesForPatientCaseGetOrder = Literal["asc", "desc"]

LIST_INVOICES_FOR_PATIENT_CASE_GET_ORDER_VALUES: Set[ListInvoicesForPatientCaseGetOrder] = {
    "asc",
    "desc",
}


def check_list_invoices_for_patient_case_get_order(value: str) -> ListInvoicesForPatientCaseGetOrder:
    if value in LIST_INVOICES_FOR_PATIENT_CASE_GET_ORDER_VALUES:
        return cast(ListInvoicesForPatientCaseGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_FOR_PATIENT_CASE_GET_ORDER_VALUES!r}")
