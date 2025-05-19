from typing import Literal, Set, cast

UpdateBillableItemPatchBodyItemType = Literal["Other", "Product", "Service"]

UPDATE_BILLABLE_ITEM_PATCH_BODY_ITEM_TYPE_VALUES: Set[UpdateBillableItemPatchBodyItemType] = {
    "Other",
    "Product",
    "Service",
}


def check_update_billable_item_patch_body_item_type(value: str) -> UpdateBillableItemPatchBodyItemType:
    if value in UPDATE_BILLABLE_ITEM_PATCH_BODY_ITEM_TYPE_VALUES:
        return cast(UpdateBillableItemPatchBodyItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_BILLABLE_ITEM_PATCH_BODY_ITEM_TYPE_VALUES!r}")
