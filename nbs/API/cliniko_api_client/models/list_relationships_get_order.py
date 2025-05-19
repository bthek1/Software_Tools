from typing import Literal, Set, cast

ListRelationshipsGetOrder = Literal["asc", "desc"]

LIST_RELATIONSHIPS_GET_ORDER_VALUES: Set[ListRelationshipsGetOrder] = {
    "asc",
    "desc",
}


def check_list_relationships_get_order(value: str) -> ListRelationshipsGetOrder:
    if value in LIST_RELATIONSHIPS_GET_ORDER_VALUES:
        return cast(ListRelationshipsGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_RELATIONSHIPS_GET_ORDER_VALUES!r}")
