from typing import Literal, Set, cast

ListTreatmentNotesForPatientGetOrder = Literal["asc", "desc"]

LIST_TREATMENT_NOTES_FOR_PATIENT_GET_ORDER_VALUES: Set[ListTreatmentNotesForPatientGetOrder] = {
    "asc",
    "desc",
}


def check_list_treatment_notes_for_patient_get_order(value: str) -> ListTreatmentNotesForPatientGetOrder:
    if value in LIST_TREATMENT_NOTES_FOR_PATIENT_GET_ORDER_VALUES:
        return cast(ListTreatmentNotesForPatientGetOrder, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_TREATMENT_NOTES_FOR_PATIENT_GET_ORDER_VALUES!r}"
    )
