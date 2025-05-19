from typing import Literal, Set, cast

ListReferralSourceTypesGetOrder = Literal["asc", "desc"]

LIST_REFERRAL_SOURCE_TYPES_GET_ORDER_VALUES: Set[ListReferralSourceTypesGetOrder] = {
    "asc",
    "desc",
}


def check_list_referral_source_types_get_order(value: str) -> ListReferralSourceTypesGetOrder:
    if value in LIST_REFERRAL_SOURCE_TYPES_GET_ORDER_VALUES:
        return cast(ListReferralSourceTypesGetOrder, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_REFERRAL_SOURCE_TYPES_GET_ORDER_VALUES!r}")
