from typing import Literal, Set, cast

ListPractitionerReferenceNumbersForPractitionerGetOrder = Literal["asc", "desc"]

LIST_PRACTITIONER_REFERENCE_NUMBERS_FOR_PRACTITIONER_GET_ORDER_VALUES: Set[
    ListPractitionerReferenceNumbersForPractitionerGetOrder
] = {
    "asc",
    "desc",
}


def check_list_practitioner_reference_numbers_for_practitioner_get_order(
    value: str,
) -> ListPractitionerReferenceNumbersForPractitionerGetOrder:
    if value in LIST_PRACTITIONER_REFERENCE_NUMBERS_FOR_PRACTITIONER_GET_ORDER_VALUES:
        return cast(ListPractitionerReferenceNumbersForPractitionerGetOrder, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_PRACTITIONER_REFERENCE_NUMBERS_FOR_PRACTITIONER_GET_ORDER_VALUES!r}"
    )
