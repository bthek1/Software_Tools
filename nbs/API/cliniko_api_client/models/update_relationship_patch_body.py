from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_relationship_patch_body_relation import (
    UpdateRelationshipPatchBodyRelation,
    check_update_relationship_patch_body_relation,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateRelationshipPatchBody")


@_attrs_define
class UpdateRelationshipPatchBody:
    """
    Attributes:
        patient_id (Union[Unset, str]): patient id Example: 1.
        related_patient_id (Union[Unset, str]): patient id Example: 1.
        relation (Union[Unset, UpdateRelationshipPatchBodyRelation]): | Enum Value | Description |
            |---|---|
            |10|Parent|
            |20|Child|
            |30|Sibling|
            |40|Spouse|
            |50|Partner|
            |60|Relative|
            |70|Other|
    """

    patient_id: Union[Unset, str] = UNSET
    related_patient_id: Union[Unset, str] = UNSET
    relation: Union[Unset, UpdateRelationshipPatchBodyRelation] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        patient_id = self.patient_id

        related_patient_id = self.related_patient_id

        relation: Union[Unset, int] = UNSET
        if not isinstance(self.relation, Unset):
            relation = self.relation

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if patient_id is not UNSET:
            field_dict["patient_id"] = patient_id
        if related_patient_id is not UNSET:
            field_dict["related_patient_id"] = related_patient_id
        if relation is not UNSET:
            field_dict["relation"] = relation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        patient_id = d.pop("patient_id", UNSET)

        related_patient_id = d.pop("related_patient_id", UNSET)

        _relation = d.pop("relation", UNSET)
        relation: Union[Unset, UpdateRelationshipPatchBodyRelation]
        if isinstance(_relation, Unset):
            relation = UNSET
        else:
            relation = check_update_relationship_patch_body_relation(_relation)

        update_relationship_patch_body = cls(
            patient_id=patient_id,
            related_patient_id=related_patient_id,
            relation=relation,
        )

        update_relationship_patch_body.additional_properties = d
        return update_relationship_patch_body

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
