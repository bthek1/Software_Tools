from typing import Literal, Set, cast

ListPatientAttachmentsForPatientGetOrder = Literal["asc", "desc"]

LIST_PATIENT_ATTACHMENTS_FOR_PATIENT_GET_ORDER_VALUES: Set[ListPatientAttachmentsForPatientGetOrder] = {
    "asc",
    "desc",
}


def check_list_patient_attachments_for_patient_get_order(value: str) -> ListPatientAttachmentsForPatientGetOrder:
    if value in LIST_PATIENT_ATTACHMENTS_FOR_PATIENT_GET_ORDER_VALUES:
        return cast(ListPatientAttachmentsForPatientGetOrder, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_PATIENT_ATTACHMENTS_FOR_PATIENT_GET_ORDER_VALUES!r}"
    )
