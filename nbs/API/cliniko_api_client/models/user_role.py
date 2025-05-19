from typing import Literal, Set, cast

UserRole = Literal["administrator", "bookkeeper", "power receptionist", "practitioner", "receptionist", "scheduler"]

USER_ROLE_VALUES: Set[UserRole] = {
    "administrator",
    "bookkeeper",
    "power receptionist",
    "practitioner",
    "receptionist",
    "scheduler",
}


def check_user_role(value: str) -> UserRole:
    if value in USER_ROLE_VALUES:
        return cast(UserRole, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USER_ROLE_VALUES!r}")
