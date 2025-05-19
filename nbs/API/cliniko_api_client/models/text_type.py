from typing import Literal, Set, cast

TextType = Literal["text"]

TEXT_TYPE_VALUES: Set[TextType] = {
    "text",
}


def check_text_type(value: str) -> TextType:
    if value in TEXT_TYPE_VALUES:
        return cast(TextType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TEXT_TYPE_VALUES!r}")
