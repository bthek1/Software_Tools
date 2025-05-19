from typing import Literal, Set, cast

ListUsersGetOrder = Literal["asc", "desc"]

LIST_USERS_GET_ORDER_VALUES: Set[ListUsersGetOrder] = {
    "asc",
    "desc",
}


def check_list_users_get_order(value: str) -> ListUsersGetOrder:
    if value in LIST_USERS_GET_ORDER_VALUES:
        return cast(ListUsersGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_USERS_GET_ORDER_VALUES!r}")
