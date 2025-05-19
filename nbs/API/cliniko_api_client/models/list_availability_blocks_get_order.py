from typing import Literal, Set, cast

ListAvailabilityBlocksGetOrder = Literal["asc", "desc"]

LIST_AVAILABILITY_BLOCKS_GET_ORDER_VALUES: Set[ListAvailabilityBlocksGetOrder] = {
    "asc",
    "desc",
}


def check_list_availability_blocks_get_order(value: str) -> ListAvailabilityBlocksGetOrder:
    if value in LIST_AVAILABILITY_BLOCKS_GET_ORDER_VALUES:
        return cast(ListAvailabilityBlocksGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_AVAILABILITY_BLOCKS_GET_ORDER_VALUES!r}")
