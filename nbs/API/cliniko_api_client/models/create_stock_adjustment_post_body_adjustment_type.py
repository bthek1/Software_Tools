from typing import Literal, Set, cast

CreateStockAdjustmentPostBodyAdjustmentType = Literal[
    "Damaged", "Item Sold", "Other", "Out of Date", "Returned", "Stock Purchase"
]

CREATE_STOCK_ADJUSTMENT_POST_BODY_ADJUSTMENT_TYPE_VALUES: Set[CreateStockAdjustmentPostBodyAdjustmentType] = {
    "Damaged",
    "Item Sold",
    "Other",
    "Out of Date",
    "Returned",
    "Stock Purchase",
}


def check_create_stock_adjustment_post_body_adjustment_type(value: str) -> CreateStockAdjustmentPostBodyAdjustmentType:
    if value in CREATE_STOCK_ADJUSTMENT_POST_BODY_ADJUSTMENT_TYPE_VALUES:
        return cast(CreateStockAdjustmentPostBodyAdjustmentType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_STOCK_ADJUSTMENT_POST_BODY_ADJUSTMENT_TYPE_VALUES!r}"
    )
