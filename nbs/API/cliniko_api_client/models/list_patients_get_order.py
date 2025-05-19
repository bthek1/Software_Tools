from typing import Literal, Set, cast

ListPatientsGetOrder = Literal["asc", "desc"]

LIST_PATIENTS_GET_ORDER_VALUES: Set[ListPatientsGetOrder] = {
    "asc",
    "desc",
}


def check_list_patients_get_order(value: str) -> ListPatientsGetOrder:
    if value in LIST_PATIENTS_GET_ORDER_VALUES:
        return cast(ListPatientsGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_PATIENTS_GET_ORDER_VALUES!r}")
