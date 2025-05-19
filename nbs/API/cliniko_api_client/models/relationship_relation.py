from typing import Literal, Set, cast

RelationshipRelation = Literal[10, 20, 30, 40, 50, 60, 70]

RELATIONSHIP_RELATION_VALUES: Set[RelationshipRelation] = {
    10,
    20,
    30,
    40,
    50,
    60,
    70,
}


def check_relationship_relation(value: int) -> RelationshipRelation:
    if value in RELATIONSHIP_RELATION_VALUES:
        return cast(RelationshipRelation, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RELATIONSHIP_RELATION_VALUES!r}")
