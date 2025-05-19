from typing import Literal, Set, cast

ListInvoicesForPatientGetOrder = Literal["asc", "desc"]

LIST_INVOICES_FOR_PATIENT_GET_ORDER_VALUES: Set[ListInvoicesForPatientGetOrder] = {
    "asc",
    "desc",
}


def check_list_invoices_for_patient_get_order(value: str) -> ListInvoicesForPatientGetOrder:
    if value in LIST_INVOICES_FOR_PATIENT_GET_ORDER_VALUES:
        return cast(ListInvoicesForPatientGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_INVOICES_FOR_PATIENT_GET_ORDER_VALUES!r}")
