from typing import Literal, Set, cast

CreateAvailabilityBlockPostBodyRepeatRuleType0RepeatType = Literal["Daily", "Monthly", "Weekly"]

CREATE_AVAILABILITY_BLOCK_POST_BODY_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES: Set[
    CreateAvailabilityBlockPostBodyRepeatRuleType0RepeatType
] = {
    "Daily",
    "Monthly",
    "Weekly",
}


def check_create_availability_block_post_body_repeat_rule_type_0_repeat_type(
    value: str,
) -> CreateAvailabilityBlockPostBodyRepeatRuleType0RepeatType:
    if value in CREATE_AVAILABILITY_BLOCK_POST_BODY_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES:
        return cast(CreateAvailabilityBlockPostBodyRepeatRuleType0RepeatType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_AVAILABILITY_BLOCK_POST_BODY_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES!r}"
    )
