from typing import Literal, Set, cast

ListPatientFormTemplatesGetOrder = Literal["asc", "desc"]

LIST_PATIENT_FORM_TEMPLATES_GET_ORDER_VALUES: Set[ListPatientFormTemplatesGetOrder] = {
    "asc",
    "desc",
}


def check_list_patient_form_templates_get_order(value: str) -> ListPatientFormTemplatesGetOrder:
    if value in LIST_PATIENT_FORM_TEMPLATES_GET_ORDER_VALUES:
        return cast(ListPatientFormTemplatesGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_PATIENT_FORM_TEMPLATES_GET_ORDER_VALUES!r}")
