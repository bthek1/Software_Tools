from typing import Literal, Set, cast

ListTreatmentNotesGetOrder = Literal["asc", "desc"]

LIST_TREATMENT_NOTES_GET_ORDER_VALUES: Set[ListTreatmentNotesGetOrder] = {
    "asc",
    "desc",
}


def check_list_treatment_notes_get_order(value: str) -> ListTreatmentNotesGetOrder:
    if value in LIST_TREATMENT_NOTES_GET_ORDER_VALUES:
        return cast(ListTreatmentNotesGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_TREATMENT_NOTES_GET_ORDER_VALUES!r}")
