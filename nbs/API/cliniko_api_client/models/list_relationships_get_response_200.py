from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_relationships_get_response_200_links import ListRelationshipsGetResponse200Links
    from ..models.relationship import Relationship


T = TypeVar("T", bound="ListRelationshipsGetResponse200")


@_attrs_define
class ListRelationshipsGetResponse200:
    """
    Attributes:
        relationships (Union[Unset, List['Relationship']]):
        total_entries (Union[Unset, int]):  Example: 1.
        links (Union[Unset, ListRelationshipsGetResponse200Links]):
    """

    relationships: Union[Unset, List["Relationship"]] = UNSET
    total_entries: Union[Unset, int] = UNSET
    links: Union[Unset, "ListRelationshipsGetResponse200Links"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        relationships: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = []
            for relationships_item_data in self.relationships:
                relationships_item = relationships_item_data.to_dict()
                relationships.append(relationships_item)

        total_entries = self.total_entries

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if relationships is not UNSET:
            field_dict["relationships"] = relationships
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.list_relationships_get_response_200_links import ListRelationshipsGetResponse200Links
        from ..models.relationship import Relationship

        d = src_dict.copy()
        relationships = []
        _relationships = d.pop("relationships", UNSET)
        for relationships_item_data in _relationships or []:
            relationships_item = Relationship.from_dict(relationships_item_data)

            relationships.append(relationships_item)

        total_entries = d.pop("total_entries", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ListRelationshipsGetResponse200Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ListRelationshipsGetResponse200Links.from_dict(_links)

        list_relationships_get_response_200 = cls(
            relationships=relationships,
            total_entries=total_entries,
            links=links,
        )

        list_relationships_get_response_200.additional_properties = d
        return list_relationships_get_response_200

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
