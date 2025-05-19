from typing import Literal, Set, cast

ListProductSuppliersGetOrder = Literal["asc", "desc"]

LIST_PRODUCT_SUPPLIERS_GET_ORDER_VALUES: Set[ListProductSuppliersGetOrder] = {
    "asc",
    "desc",
}


def check_list_product_suppliers_get_order(value: str) -> ListProductSuppliersGetOrder:
    if value in LIST_PRODUCT_SUPPLIERS_GET_ORDER_VALUES:
        return cast(ListProductSuppliersGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_PRODUCT_SUPPLIERS_GET_ORDER_VALUES!r}")
