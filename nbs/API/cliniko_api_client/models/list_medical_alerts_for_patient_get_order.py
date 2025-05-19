from typing import Literal, Set, cast

ListMedicalAlertsForPatientGetOrder = Literal["asc", "desc"]

LIST_MEDICAL_ALERTS_FOR_PATIENT_GET_ORDER_VALUES: Set[ListMedicalAlertsForPatientGetOrder] = {
    "asc",
    "desc",
}


def check_list_medical_alerts_for_patient_get_order(value: str) -> ListMedicalAlertsForPatientGetOrder:
    if value in LIST_MEDICAL_ALERTS_FOR_PATIENT_GET_ORDER_VALUES:
        return cast(ListMedicalAlertsForPatientGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_MEDICAL_ALERTS_FOR_PATIENT_GET_ORDER_VALUES!r}")
