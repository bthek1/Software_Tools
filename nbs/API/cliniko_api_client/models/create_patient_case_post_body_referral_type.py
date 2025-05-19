from typing import Literal, Set, cast

CreatePatientCasePostBodyReferralType = Literal["dva", "medicare"]

CREATE_PATIENT_CASE_POST_BODY_REFERRAL_TYPE_VALUES: Set[CreatePatientCasePostBodyReferralType] = {
    "dva",
    "medicare",
}


def check_create_patient_case_post_body_referral_type(value: str) -> CreatePatientCasePostBodyReferralType:
    if value in CREATE_PATIENT_CASE_POST_BODY_REFERRAL_TYPE_VALUES:
        return cast(CreatePatientCasePostBodyReferralType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_PATIENT_CASE_POST_BODY_REFERRAL_TYPE_VALUES!r}"
    )
