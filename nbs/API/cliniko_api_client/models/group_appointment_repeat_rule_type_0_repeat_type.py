from typing import Literal, Set, cast

GroupAppointmentRepeatRuleType0RepeatType = Literal["Daily", "Monthly", "Weekly"]

GROUP_APPOINTMENT_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES: Set[GroupAppointmentRepeatRuleType0RepeatType] = {
    "Daily",
    "Monthly",
    "Weekly",
}


def check_group_appointment_repeat_rule_type_0_repeat_type(value: str) -> GroupAppointmentRepeatRuleType0RepeatType:
    if value in GROUP_APPOINTMENT_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES:
        return cast(GroupAppointmentRepeatRuleType0RepeatType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GROUP_APPOINTMENT_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES!r}"
    )
