from typing import Literal, Set, cast

CreateUnavailableBlockPostBodyRepeatRuleType0RepeatType = Literal["Daily", "Monthly", "Weekly"]

CREATE_UNAVAILABLE_BLOCK_POST_BODY_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES: Set[
    CreateUnavailableBlockPostBodyRepeatRuleType0RepeatType
] = {
    "Daily",
    "Monthly",
    "Weekly",
}


def check_create_unavailable_block_post_body_repeat_rule_type_0_repeat_type(
    value: str,
) -> CreateUnavailableBlockPostBodyRepeatRuleType0RepeatType:
    if value in CREATE_UNAVAILABLE_BLOCK_POST_BODY_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES:
        return cast(CreateUnavailableBlockPostBodyRepeatRuleType0RepeatType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_UNAVAILABLE_BLOCK_POST_BODY_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES!r}"
    )
