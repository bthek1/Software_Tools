from typing import Literal, Set, cast

ListStockAdjustmentsGetOrder = Literal["asc", "desc"]

LIST_STOCK_ADJUSTMENTS_GET_ORDER_VALUES: Set[ListStockAdjustmentsGetOrder] = {
    "asc",
    "desc",
}


def check_list_stock_adjustments_get_order(value: str) -> ListStockAdjustmentsGetOrder:
    if value in LIST_STOCK_ADJUSTMENTS_GET_ORDER_VALUES:
        return cast(ListStockAdjustmentsGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_STOCK_ADJUSTMENTS_GET_ORDER_VALUES!r}")
