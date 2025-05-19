from typing import Literal, Set, cast

ListUnavailableBlocksGetOrder = Literal["asc", "desc"]

LIST_UNAVAILABLE_BLOCKS_GET_ORDER_VALUES: Set[ListUnavailableBlocksGetOrder] = {
    "asc",
    "desc",
}


def check_list_unavailable_blocks_get_order(value: str) -> ListUnavailableBlocksGetOrder:
    if value in LIST_UNAVAILABLE_BLOCKS_GET_ORDER_VALUES:
        return cast(ListUnavailableBlocksGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_UNAVAILABLE_BLOCKS_GET_ORDER_VALUES!r}")
