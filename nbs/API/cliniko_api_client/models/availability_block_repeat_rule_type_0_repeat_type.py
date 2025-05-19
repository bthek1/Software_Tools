from typing import Literal, Set, cast

AvailabilityBlockRepeatRuleType0RepeatType = Literal["Daily", "Monthly", "Weekly"]

AVAILABILITY_BLOCK_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES: Set[AvailabilityBlockRepeatRuleType0RepeatType] = {
    "Daily",
    "Monthly",
    "Weekly",
}


def check_availability_block_repeat_rule_type_0_repeat_type(value: str) -> AvailabilityBlockRepeatRuleType0RepeatType:
    if value in AVAILABILITY_BLOCK_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES:
        return cast(AvailabilityBlockRepeatRuleType0RepeatType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {AVAILABILITY_BLOCK_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES!r}"
    )
