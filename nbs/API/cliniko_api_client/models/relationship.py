import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.relationship_relation import RelationshipRelation, check_relationship_relation
from ..models.relationship_relation_description import (
    RelationshipRelationDescription,
    check_relationship_relation_description,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.relationship_links import RelationshipLinks
    from ..models.relationship_patient import RelationshipPatient
    from ..models.relationship_related_patient import RelationshipRelatedPatient


T = TypeVar("T", bound="Relationship")


@_attrs_define
class Relationship:
    """
    Attributes:
        archived_at (Union[None, Unset, datetime.datetime]):
        created_at (Union[Unset, datetime.datetime]):
        id (Union[Unset, str]):
        links (Union[Unset, RelationshipLinks]):
        patient (Union[Unset, RelationshipPatient]):
        related_patient (Union[Unset, RelationshipRelatedPatient]):
        relation (Union[Unset, RelationshipRelation]):
        relation_description (Union[Unset, RelationshipRelationDescription]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    archived_at: Union[None, Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    links: Union[Unset, "RelationshipLinks"] = UNSET
    patient: Union[Unset, "RelationshipPatient"] = UNSET
    related_patient: Union[Unset, "RelationshipRelatedPatient"] = UNSET
    relation: Union[Unset, RelationshipRelation] = UNSET
    relation_description: Union[Unset, RelationshipRelationDescription] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        archived_at: Union[None, Unset, str]
        if isinstance(self.archived_at, Unset):
            archived_at = UNSET
        elif isinstance(self.archived_at, datetime.datetime):
            archived_at = self.archived_at.isoformat()
        else:
            archived_at = self.archived_at

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        id = self.id

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        patient: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.patient, Unset):
            patient = self.patient.to_dict()

        related_patient: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.related_patient, Unset):
            related_patient = self.related_patient.to_dict()

        relation: Union[Unset, int] = UNSET
        if not isinstance(self.relation, Unset):
            relation = self.relation

        relation_description: Union[Unset, str] = UNSET
        if not isinstance(self.relation_description, Unset):
            relation_description = self.relation_description

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if links is not UNSET:
            field_dict["links"] = links
        if patient is not UNSET:
            field_dict["patient"] = patient
        if related_patient is not UNSET:
            field_dict["related_patient"] = related_patient
        if relation is not UNSET:
            field_dict["relation"] = relation
        if relation_description is not UNSET:
            field_dict["relation_description"] = relation_description
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.relationship_links import RelationshipLinks
        from ..models.relationship_patient import RelationshipPatient
        from ..models.relationship_related_patient import RelationshipRelatedPatient

        d = src_dict.copy()

        def _parse_archived_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                archived_at_type_0 = isoparse(data)

                return archived_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        archived_at = _parse_archived_at(d.pop("archived_at", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        id = d.pop("id", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, RelationshipLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = RelationshipLinks.from_dict(_links)

        _patient = d.pop("patient", UNSET)
        patient: Union[Unset, RelationshipPatient]
        if isinstance(_patient, Unset):
            patient = UNSET
        else:
            patient = RelationshipPatient.from_dict(_patient)

        _related_patient = d.pop("related_patient", UNSET)
        related_patient: Union[Unset, RelationshipRelatedPatient]
        if isinstance(_related_patient, Unset):
            related_patient = UNSET
        else:
            related_patient = RelationshipRelatedPatient.from_dict(_related_patient)

        _relation = d.pop("relation", UNSET)
        relation: Union[Unset, RelationshipRelation]
        if isinstance(_relation, Unset):
            relation = UNSET
        else:
            relation = check_relationship_relation(_relation)

        _relation_description = d.pop("relation_description", UNSET)
        relation_description: Union[Unset, RelationshipRelationDescription]
        if isinstance(_relation_description, Unset):
            relation_description = UNSET
        else:
            relation_description = check_relationship_relation_description(_relation_description)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        relationship = cls(
            archived_at=archived_at,
            created_at=created_at,
            id=id,
            links=links,
            patient=patient,
            related_patient=related_patient,
            relation=relation,
            relation_description=relation_description,
            updated_at=updated_at,
        )

        relationship.additional_properties = d
        return relationship

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
