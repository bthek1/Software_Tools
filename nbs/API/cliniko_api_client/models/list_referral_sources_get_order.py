from typing import Literal, Set, cast

ListReferralSourcesGetOrder = Literal["asc", "desc"]

LIST_REFERRAL_SOURCES_GET_ORDER_VALUES: Set[ListReferralSourcesGetOrder] = {
    "asc",
    "desc",
}


def check_list_referral_sources_get_order(value: str) -> ListReferralSourcesGetOrder:
    if value in LIST_REFERRAL_SOURCES_GET_ORDER_VALUES:
        return cast(ListReferralSourcesGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_REFERRAL_SOURCES_GET_ORDER_VALUES!r}")
