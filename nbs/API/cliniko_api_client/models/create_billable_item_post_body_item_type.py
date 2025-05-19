from typing import Literal, Set, cast

CreateBillableItemPostBodyItemType = Literal["Other", "Product", "Service"]

CREATE_BILLABLE_ITEM_POST_BODY_ITEM_TYPE_VALUES: Set[CreateBillableItemPostBodyItemType] = {
    "Other",
    "Product",
    "Service",
}


def check_create_billable_item_post_body_item_type(value: str) -> CreateBillableItemPostBodyItemType:
    if value in CREATE_BILLABLE_ITEM_POST_BODY_ITEM_TYPE_VALUES:
        return cast(CreateBillableItemPostBodyItemType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_BILLABLE_ITEM_POST_BODY_ITEM_TYPE_VALUES!r}")
