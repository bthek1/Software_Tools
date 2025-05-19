from typing import Literal, Set, cast

SignatureType = Literal["signature"]

SIGNATURE_TYPE_VALUES: Set[SignatureType] = {
    "signature",
}


def check_signature_type(value: str) -> SignatureType:
    if value in SIGNATURE_TYPE_VALUES:
        return cast(SignatureType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SIGNATURE_TYPE_VALUES!r}")
