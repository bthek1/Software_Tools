from typing import Literal, Set, cast

UnavailableBlockRepeatRuleType0RepeatType = Literal["Daily", "Monthly", "Weekly"]

UNAVAILABLE_BLOCK_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES: Set[UnavailableBlockRepeatRuleType0RepeatType] = {
    "Daily",
    "Monthly",
    "Weekly",
}


def check_unavailable_block_repeat_rule_type_0_repeat_type(value: str) -> UnavailableBlockRepeatRuleType0RepeatType:
    if value in UNAVAILABLE_BLOCK_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES:
        return cast(UnavailableBlockRepeatRuleType0RepeatType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UNAVAILABLE_BLOCK_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES!r}"
    )
