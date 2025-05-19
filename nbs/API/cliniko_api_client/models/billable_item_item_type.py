from typing import Literal, Set, cast

BillableItemItemType = Literal["Other", "Product", "Service"]

BILLABLE_ITEM_ITEM_TYPE_VALUES: Set[BillableItemItemType] = {
    "Other",
    "Product",
    "Service",
}


def check_billable_item_item_type(value: str) -> BillableItemItemType:
    if value in BILLABLE_ITEM_ITEM_TYPE_VALUES:
        return cast(BillableItemItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BILLABLE_ITEM_ITEM_TYPE_VALUES!r}")
