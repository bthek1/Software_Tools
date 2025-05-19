from typing import Literal, Set, cast

IndividualAppointmentRepeatRuleType0RepeatType = Literal["Daily", "Monthly", "Weekly"]

INDIVIDUAL_APPOINTMENT_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES: Set[IndividualAppointmentRepeatRuleType0RepeatType] = {
    "Daily",
    "Monthly",
    "Weekly",
}


def check_individual_appointment_repeat_rule_type_0_repeat_type(
    value: str,
) -> IndividualAppointmentRepeatRuleType0RepeatType:
    if value in INDIVIDUAL_APPOINTMENT_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES:
        return cast(IndividualAppointmentRepeatRuleType0RepeatType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {INDIVIDUAL_APPOINTMENT_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES!r}"
    )
