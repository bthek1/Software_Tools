from typing import Literal, Set, cast

ParagraphType = Literal["paragraph"]

PARAGRAPH_TYPE_VALUES: Set[ParagraphType] = {
    "paragraph",
}


def check_paragraph_type(value: str) -> ParagraphType:
    if value in PARAGRAPH_TYPE_VALUES:
        return cast(ParagraphType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PARAGRAPH_TYPE_VALUES!r}")
