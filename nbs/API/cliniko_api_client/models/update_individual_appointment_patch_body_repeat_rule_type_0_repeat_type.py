from typing import Literal, Set, cast

UpdateIndividualAppointmentPatchBodyRepeatRuleType0RepeatType = Literal["Daily", "Monthly", "Weekly"]

UPDATE_INDIVIDUAL_APPOINTMENT_PATCH_BODY_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES: Set[
    UpdateIndividualAppointmentPatchBodyRepeatRuleType0RepeatType
] = {
    "Daily",
    "Monthly",
    "Weekly",
}


def check_update_individual_appointment_patch_body_repeat_rule_type_0_repeat_type(
    value: str,
) -> UpdateIndividualAppointmentPatchBodyRepeatRuleType0RepeatType:
    if value in UPDATE_INDIVIDUAL_APPOINTMENT_PATCH_BODY_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES:
        return cast(UpdateIndividualAppointmentPatchBodyRepeatRuleType0RepeatType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_INDIVIDUAL_APPOINTMENT_PATCH_BODY_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES!r}"
    )
