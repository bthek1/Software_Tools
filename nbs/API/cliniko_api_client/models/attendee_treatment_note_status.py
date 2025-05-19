from typing import Literal, Set, cast

AttendeeTreatmentNoteStatus = Literal[10, 90]

ATTENDEE_TREATMENT_NOTE_STATUS_VALUES: Set[AttendeeTreatmentNoteStatus] = {
    10,
    90,
}


def check_attendee_treatment_note_status(value: int) -> AttendeeTreatmentNoteStatus:
    if value in ATTENDEE_TREATMENT_NOTE_STATUS_VALUES:
        return cast(AttendeeTreatmentNoteStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ATTENDEE_TREATMENT_NOTE_STATUS_VALUES!r}")
