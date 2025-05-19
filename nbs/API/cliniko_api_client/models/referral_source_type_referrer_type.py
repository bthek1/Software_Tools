from typing import Literal, Set, cast

ReferralSourceTypeReferrerType = Literal["Contact", "Patient"]

REFERRAL_SOURCE_TYPE_REFERRER_TYPE_VALUES: Set[ReferralSourceTypeReferrerType] = {
    "Contact",
    "Patient",
}


def check_referral_source_type_referrer_type(value: str) -> ReferralSourceTypeReferrerType:
    if value in REFERRAL_SOURCE_TYPE_REFERRER_TYPE_VALUES:
        return cast(ReferralSourceTypeReferrerType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REFERRAL_SOURCE_TYPE_REFERRER_TYPE_VALUES!r}")
