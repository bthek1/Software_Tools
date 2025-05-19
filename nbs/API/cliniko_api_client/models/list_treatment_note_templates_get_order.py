from typing import Literal, Set, cast

ListTreatmentNoteTemplatesGetOrder = Literal["asc", "desc"]

LIST_TREATMENT_NOTE_TEMPLATES_GET_ORDER_VALUES: Set[ListTreatmentNoteTemplatesGetOrder] = {
    "asc",
    "desc",
}


def check_list_treatment_note_templates_get_order(value: str) -> ListTreatmentNoteTemplatesGetOrder:
    if value in LIST_TREATMENT_NOTE_TEMPLATES_GET_ORDER_VALUES:
        return cast(ListTreatmentNoteTemplatesGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_TREATMENT_NOTE_TEMPLATES_GET_ORDER_VALUES!r}")
