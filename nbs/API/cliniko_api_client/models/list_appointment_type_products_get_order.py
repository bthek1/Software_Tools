from typing import Literal, Set, cast

ListAppointmentTypeProductsGetOrder = Literal["asc", "desc"]

LIST_APPOINTMENT_TYPE_PRODUCTS_GET_ORDER_VALUES: Set[ListAppointmentTypeProductsGetOrder] = {
    "asc",
    "desc",
}


def check_list_appointment_type_products_get_order(value: str) -> ListAppointmentTypeProductsGetOrder:
    if value in LIST_APPOINTMENT_TYPE_PRODUCTS_GET_ORDER_VALUES:
        return cast(ListAppointmentTypeProductsGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_APPOINTMENT_TYPE_PRODUCTS_GET_ORDER_VALUES!r}")
