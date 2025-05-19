from typing import Literal, Set, cast

UpdateContactPatchBodyDoctorType = Literal["general_practitioner", "specialist"]

UPDATE_CONTACT_PATCH_BODY_DOCTOR_TYPE_VALUES: Set[UpdateContactPatchBodyDoctorType] = {
    "general_practitioner",
    "specialist",
}


def check_update_contact_patch_body_doctor_type(value: str) -> UpdateContactPatchBodyDoctorType:
    if value in UPDATE_CONTACT_PATCH_BODY_DOCTOR_TYPE_VALUES:
        return cast(UpdateContactPatchBodyDoctorType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_CONTACT_PATCH_BODY_DOCTOR_TYPE_VALUES!r}")
