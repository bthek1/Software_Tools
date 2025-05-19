from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.business import Business
    from ..models.list_businesses_get_response_200_links import ListBusinessesGetResponse200Links


T = TypeVar("T", bound="ListBusinessesGetResponse200")


@_attrs_define
class ListBusinessesGetResponse200:
    """
    Attributes:
        businesses (Union[Unset, List['Business']]):
        total_entries (Union[Unset, int]):  Example: 1.
        links (Union[Unset, ListBusinessesGetResponse200Links]):
    """

    businesses: Union[Unset, List["Business"]] = UNSET
    total_entries: Union[Unset, int] = UNSET
    links: Union[Unset, "ListBusinessesGetResponse200Links"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        businesses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.businesses, Unset):
            businesses = []
            for businesses_item_data in self.businesses:
                businesses_item = businesses_item_data.to_dict()
                businesses.append(businesses_item)

        total_entries = self.total_entries

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if businesses is not UNSET:
            field_dict["businesses"] = businesses
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.business import Business
        from ..models.list_businesses_get_response_200_links import ListBusinessesGetResponse200Links

        d = src_dict.copy()
        businesses = []
        _businesses = d.pop("businesses", UNSET)
        for businesses_item_data in _businesses or []:
            businesses_item = Business.from_dict(businesses_item_data)

            businesses.append(businesses_item)

        total_entries = d.pop("total_entries", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ListBusinessesGetResponse200Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ListBusinessesGetResponse200Links.from_dict(_links)

        list_businesses_get_response_200 = cls(
            businesses=businesses,
            total_entries=total_entries,
            links=links,
        )

        list_businesses_get_response_200.additional_properties = d
        return list_businesses_get_response_200

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
