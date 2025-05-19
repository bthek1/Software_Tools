from typing import Literal, Set, cast

ListTaxesGetOrder = Literal["asc", "desc"]

LIST_TAXES_GET_ORDER_VALUES: Set[ListTaxesGetOrder] = {
    "asc",
    "desc",
}


def check_list_taxes_get_order(value: str) -> ListTaxesGetOrder:
    if value in LIST_TAXES_GET_ORDER_VALUES:
        return cast(ListTaxesGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_TAXES_GET_ORDER_VALUES!r}")
