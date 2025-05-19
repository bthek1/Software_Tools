from typing import Literal, Set, cast

ListPatientAttachmentsGetOrder = Literal["asc", "desc"]

LIST_PATIENT_ATTACHMENTS_GET_ORDER_VALUES: Set[ListPatientAttachmentsGetOrder] = {
    "asc",
    "desc",
}


def check_list_patient_attachments_get_order(value: str) -> ListPatientAttachmentsGetOrder:
    if value in LIST_PATIENT_ATTACHMENTS_GET_ORDER_VALUES:
        return cast(ListPatientAttachmentsGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_PATIENT_ATTACHMENTS_GET_ORDER_VALUES!r}")
