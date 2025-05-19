from typing import Literal, Set, cast

CreateGroupAppointmentPostBodyRepeatRuleType0RepeatType = Literal["Daily", "Monthly", "Weekly"]

CREATE_GROUP_APPOINTMENT_POST_BODY_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES: Set[
    CreateGroupAppointmentPostBodyRepeatRuleType0RepeatType
] = {
    "Daily",
    "Monthly",
    "Weekly",
}


def check_create_group_appointment_post_body_repeat_rule_type_0_repeat_type(
    value: str,
) -> CreateGroupAppointmentPostBodyRepeatRuleType0RepeatType:
    if value in CREATE_GROUP_APPOINTMENT_POST_BODY_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES:
        return cast(CreateGroupAppointmentPostBodyRepeatRuleType0RepeatType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_GROUP_APPOINTMENT_POST_BODY_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES!r}"
    )
