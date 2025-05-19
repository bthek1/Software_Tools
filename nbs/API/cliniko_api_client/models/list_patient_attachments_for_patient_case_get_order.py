from typing import Literal, Set, cast

ListPatientAttachmentsForPatientCaseGetOrder = Literal["asc", "desc"]

LIST_PATIENT_ATTACHMENTS_FOR_PATIENT_CASE_GET_ORDER_VALUES: Set[ListPatientAttachmentsForPatientCaseGetOrder] = {
    "asc",
    "desc",
}


def check_list_patient_attachments_for_patient_case_get_order(
    value: str,
) -> ListPatientAttachmentsForPatientCaseGetOrder:
    if value in LIST_PATIENT_ATTACHMENTS_FOR_PATIENT_CASE_GET_ORDER_VALUES:
        return cast(ListPatientAttachmentsForPatientCaseGetOrder, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_PATIENT_ATTACHMENTS_FOR_PATIENT_CASE_GET_ORDER_VALUES!r}"
    )
