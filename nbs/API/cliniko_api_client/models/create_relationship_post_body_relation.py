from typing import Literal, Set, cast

CreateRelationshipPostBodyRelation = Literal[10, 20, 30, 40, 50, 60, 70]

CREATE_RELATIONSHIP_POST_BODY_RELATION_VALUES: Set[CreateRelationshipPostBodyRelation] = {
    10,
    20,
    30,
    40,
    50,
    60,
    70,
}


def check_create_relationship_post_body_relation(value: int) -> CreateRelationshipPostBodyRelation:
    if value in CREATE_RELATIONSHIP_POST_BODY_RELATION_VALUES:
        return cast(CreateRelationshipPostBodyRelation, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_RELATIONSHIP_POST_BODY_RELATION_VALUES!r}")
