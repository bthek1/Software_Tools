from typing import Literal, Set, cast

ReferralSourceReferrerType = Literal["Contact", "Patient"]

REFERRAL_SOURCE_REFERRER_TYPE_VALUES: Set[ReferralSourceReferrerType] = {
    "Contact",
    "Patient",
}


def check_referral_source_referrer_type(value: str) -> ReferralSourceReferrerType:
    if value in REFERRAL_SOURCE_REFERRER_TYPE_VALUES:
        return cast(ReferralSourceReferrerType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REFERRAL_SOURCE_REFERRER_TYPE_VALUES!r}")
