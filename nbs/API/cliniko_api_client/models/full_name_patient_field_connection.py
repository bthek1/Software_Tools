from typing import Literal, Set, cast

FullNamePatientFieldConnection = Literal["full_name"]

FULL_NAME_PATIENT_FIELD_CONNECTION_VALUES: Set[FullNamePatientFieldConnection] = {
    "full_name",
}


def check_full_name_patient_field_connection(value: str) -> FullNamePatientFieldConnection:
    if value in FULL_NAME_PATIENT_FIELD_CONNECTION_VALUES:
        return cast(FullNamePatientFieldConnection, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FULL_NAME_PATIENT_FIELD_CONNECTION_VALUES!r}")
