from typing import Literal, Set, cast

PatientCaseReferralType = Literal["dva", "medicare"]

PATIENT_CASE_REFERRAL_TYPE_VALUES: Set[PatientCaseReferralType] = {
    "dva",
    "medicare",
}


def check_patient_case_referral_type(value: str) -> PatientCaseReferralType:
    if value in PATIENT_CASE_REFERRAL_TYPE_VALUES:
        return cast(PatientCaseReferralType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATIENT_CASE_REFERRAL_TYPE_VALUES!r}")
