from typing import Literal, Set, cast

ListConcessionPricesGetOrder = Literal["asc", "desc"]

LIST_CONCESSION_PRICES_GET_ORDER_VALUES: Set[ListConcessionPricesGetOrder] = {
    "asc",
    "desc",
}


def check_list_concession_prices_get_order(value: str) -> ListConcessionPricesGetOrder:
    if value in LIST_CONCESSION_PRICES_GET_ORDER_VALUES:
        return cast(ListConcessionPricesGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_CONCESSION_PRICES_GET_ORDER_VALUES!r}")
