from typing import Literal, Set, cast

ListMedicalAlertsGetOrder = Literal["asc", "desc"]

LIST_MEDICAL_ALERTS_GET_ORDER_VALUES: Set[ListMedicalAlertsGetOrder] = {
    "asc",
    "desc",
}


def check_list_medical_alerts_get_order(value: str) -> ListMedicalAlertsGetOrder:
    if value in LIST_MEDICAL_ALERTS_GET_ORDER_VALUES:
        return cast(ListMedicalAlertsGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_MEDICAL_ALERTS_GET_ORDER_VALUES!r}")
