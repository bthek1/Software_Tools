from typing import Literal, Set, cast

ListPractitionerReferenceNumbersGetOrder = Literal["asc", "desc"]

LIST_PRACTITIONER_REFERENCE_NUMBERS_GET_ORDER_VALUES: Set[ListPractitionerReferenceNumbersGetOrder] = {
    "asc",
    "desc",
}


def check_list_practitioner_reference_numbers_get_order(value: str) -> ListPractitionerReferenceNumbersGetOrder:
    if value in LIST_PRACTITIONER_REFERENCE_NUMBERS_GET_ORDER_VALUES:
        return cast(ListPractitionerReferenceNumbersGetOrder, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_PRACTITIONER_REFERENCE_NUMBERS_GET_ORDER_VALUES!r}"
    )
