from typing import Literal, Set, cast

UpdateGroupAppointmentPatchBodyRepeatRuleType0RepeatType = Literal["Daily", "Monthly", "Weekly"]

UPDATE_GROUP_APPOINTMENT_PATCH_BODY_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES: Set[
    UpdateGroupAppointmentPatchBodyRepeatRuleType0RepeatType
] = {
    "Daily",
    "Monthly",
    "Weekly",
}


def check_update_group_appointment_patch_body_repeat_rule_type_0_repeat_type(
    value: str,
) -> UpdateGroupAppointmentPatchBodyRepeatRuleType0RepeatType:
    if value in UPDATE_GROUP_APPOINTMENT_PATCH_BODY_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES:
        return cast(UpdateGroupAppointmentPatchBodyRepeatRuleType0RepeatType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_GROUP_APPOINTMENT_PATCH_BODY_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES!r}"
    )
