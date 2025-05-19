from typing import Literal, Set, cast

CreateContactPostBodyDoctorType = Literal["general_practitioner", "specialist"]

CREATE_CONTACT_POST_BODY_DOCTOR_TYPE_VALUES: Set[CreateContactPostBodyDoctorType] = {
    "general_practitioner",
    "specialist",
}


def check_create_contact_post_body_doctor_type(value: str) -> CreateContactPostBodyDoctorType:
    if value in CREATE_CONTACT_POST_BODY_DOCTOR_TYPE_VALUES:
        return cast(CreateContactPostBodyDoctorType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_CONTACT_POST_BODY_DOCTOR_TYPE_VALUES!r}")
