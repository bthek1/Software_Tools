from typing import Literal, Set, cast

ListProductsGetOrder = Literal["asc", "desc"]

LIST_PRODUCTS_GET_ORDER_VALUES: Set[ListProductsGetOrder] = {
    "asc",
    "desc",
}


def check_list_products_get_order(value: str) -> ListProductsGetOrder:
    if value in LIST_PRODUCTS_GET_ORDER_VALUES:
        return cast(ListProductsGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_PRODUCTS_GET_ORDER_VALUES!r}")
