from typing import Literal, Set, cast

UpdateUnavailableBlockPatchBodyRepeatRuleType0RepeatType = Literal["Daily", "Monthly", "Weekly"]

UPDATE_UNAVAILABLE_BLOCK_PATCH_BODY_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES: Set[
    UpdateUnavailableBlockPatchBodyRepeatRuleType0RepeatType
] = {
    "Daily",
    "Monthly",
    "Weekly",
}


def check_update_unavailable_block_patch_body_repeat_rule_type_0_repeat_type(
    value: str,
) -> UpdateUnavailableBlockPatchBodyRepeatRuleType0RepeatType:
    if value in UPDATE_UNAVAILABLE_BLOCK_PATCH_BODY_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES:
        return cast(UpdateUnavailableBlockPatchBodyRepeatRuleType0RepeatType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_UNAVAILABLE_BLOCK_PATCH_BODY_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES!r}"
    )
