from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.concession_type import ConcessionType
    from ..models.list_concession_types_get_response_200_links import ListConcessionTypesGetResponse200Links


T = TypeVar("T", bound="ListConcessionTypesGetResponse200")


@_attrs_define
class ListConcessionTypesGetResponse200:
    """
    Attributes:
        concession_types (Union[Unset, List['ConcessionType']]):
        total_entries (Union[Unset, int]):  Example: 1.
        links (Union[Unset, ListConcessionTypesGetResponse200Links]):
    """

    concession_types: Union[Unset, List["ConcessionType"]] = UNSET
    total_entries: Union[Unset, int] = UNSET
    links: Union[Unset, "ListConcessionTypesGetResponse200Links"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        concession_types: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.concession_types, Unset):
            concession_types = []
            for concession_types_item_data in self.concession_types:
                concession_types_item = concession_types_item_data.to_dict()
                concession_types.append(concession_types_item)

        total_entries = self.total_entries

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if concession_types is not UNSET:
            field_dict["concession_types"] = concession_types
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.concession_type import ConcessionType
        from ..models.list_concession_types_get_response_200_links import ListConcessionTypesGetResponse200Links

        d = src_dict.copy()
        concession_types = []
        _concession_types = d.pop("concession_types", UNSET)
        for concession_types_item_data in _concession_types or []:
            concession_types_item = ConcessionType.from_dict(concession_types_item_data)

            concession_types.append(concession_types_item)

        total_entries = d.pop("total_entries", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ListConcessionTypesGetResponse200Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ListConcessionTypesGetResponse200Links.from_dict(_links)

        list_concession_types_get_response_200 = cls(
            concession_types=concession_types,
            total_entries=total_entries,
            links=links,
        )

        list_concession_types_get_response_200.additional_properties = d
        return list_concession_types_get_response_200

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
