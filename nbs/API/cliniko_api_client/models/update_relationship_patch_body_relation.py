from typing import Literal, Set, cast

UpdateRelationshipPatchBodyRelation = Literal[10, 20, 30, 40, 50, 60, 70]

UPDATE_RELATIONSHIP_PATCH_BODY_RELATION_VALUES: Set[UpdateRelationshipPatchBodyRelation] = {
    10,
    20,
    30,
    40,
    50,
    60,
    70,
}


def check_update_relationship_patch_body_relation(value: int) -> UpdateRelationshipPatchBodyRelation:
    if value in UPDATE_RELATIONSHIP_PATCH_BODY_RELATION_VALUES:
        return cast(UpdateRelationshipPatchBodyRelation, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UPDATE_RELATIONSHIP_PATCH_BODY_RELATION_VALUES!r}")
