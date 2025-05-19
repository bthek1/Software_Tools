from typing import Literal, Set, cast

PronounsPatientFieldConnection = Literal["pronouns"]

PRONOUNS_PATIENT_FIELD_CONNECTION_VALUES: Set[PronounsPatientFieldConnection] = {
    "pronouns",
}


def check_pronouns_patient_field_connection(value: str) -> PronounsPatientFieldConnection:
    if value in PRONOUNS_PATIENT_FIELD_CONNECTION_VALUES:
        return cast(PronounsPatientFieldConnection, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRONOUNS_PATIENT_FIELD_CONNECTION_VALUES!r}")
