from typing import Literal, Set, cast

UpdatePatientCasePatchBodyReferralType = Literal["dva", "medicare"]

UPDATE_PATIENT_CASE_PATCH_BODY_REFERRAL_TYPE_VALUES: Set[UpdatePatientCasePatchBodyReferralType] = {
    "dva",
    "medicare",
}


def check_update_patient_case_patch_body_referral_type(value: str) -> UpdatePatientCasePatchBodyReferralType:
    if value in UPDATE_PATIENT_CASE_PATCH_BODY_REFERRAL_TYPE_VALUES:
        return cast(UpdatePatientCasePatchBodyReferralType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_PATIENT_CASE_PATCH_BODY_REFERRAL_TYPE_VALUES!r}"
    )
