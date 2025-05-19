from typing import Literal, Set, cast

ListAppointmentTypeBillableItemsGetOrder = Literal["asc", "desc"]

LIST_APPOINTMENT_TYPE_BILLABLE_ITEMS_GET_ORDER_VALUES: Set[ListAppointmentTypeBillableItemsGetOrder] = {
    "asc",
    "desc",
}


def check_list_appointment_type_billable_items_get_order(value: str) -> ListAppointmentTypeBillableItemsGetOrder:
    if value in LIST_APPOINTMENT_TYPE_BILLABLE_ITEMS_GET_ORDER_VALUES:
        return cast(ListAppointmentTypeBillableItemsGetOrder, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_APPOINTMENT_TYPE_BILLABLE_ITEMS_GET_ORDER_VALUES!r}"
    )
