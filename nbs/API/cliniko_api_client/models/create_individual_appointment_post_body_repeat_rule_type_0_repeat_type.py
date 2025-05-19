from typing import Literal, Set, cast

CreateIndividualAppointmentPostBodyRepeatRuleType0RepeatType = Literal["Daily", "Monthly", "Weekly"]

CREATE_INDIVIDUAL_APPOINTMENT_POST_BODY_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES: Set[
    CreateIndividualAppointmentPostBodyRepeatRuleType0RepeatType
] = {
    "Daily",
    "Monthly",
    "Weekly",
}


def check_create_individual_appointment_post_body_repeat_rule_type_0_repeat_type(
    value: str,
) -> CreateIndividualAppointmentPostBodyRepeatRuleType0RepeatType:
    if value in CREATE_INDIVIDUAL_APPOINTMENT_POST_BODY_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES:
        return cast(CreateIndividualAppointmentPostBodyRepeatRuleType0RepeatType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_INDIVIDUAL_APPOINTMENT_POST_BODY_REPEAT_RULE_TYPE_0_REPEAT_TYPE_VALUES!r}"
    )
