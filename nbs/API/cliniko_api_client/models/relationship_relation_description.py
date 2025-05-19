from typing import Literal, Set, cast

RelationshipRelationDescription = Literal["Child", "Other", "Parent", "Partner", "Relative", "Sibling", "Spouse"]

RELATIONSHIP_RELATION_DESCRIPTION_VALUES: Set[RelationshipRelationDescription] = {
    "Child",
    "Other",
    "Parent",
    "Partner",
    "Relative",
    "Sibling",
    "Spouse",
}


def check_relationship_relation_description(value: str) -> RelationshipRelationDescription:
    if value in RELATIONSHIP_RELATION_DESCRIPTION_VALUES:
        return cast(RelationshipRelationDescription, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RELATIONSHIP_RELATION_DESCRIPTION_VALUES!r}")
