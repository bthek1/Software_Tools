from typing import Literal, Set, cast

ContactDoctorType = Literal["general_practitioner", "specialist"]

CONTACT_DOCTOR_TYPE_VALUES: Set[ContactDoctorType] = {
    "general_practitioner",
    "specialist",
}


def check_contact_doctor_type(value: str) -> ContactDoctorType:
    if value in CONTACT_DOCTOR_TYPE_VALUES:
        return cast(ContactDoctorType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_DOCTOR_TYPE_VALUES!r}")
