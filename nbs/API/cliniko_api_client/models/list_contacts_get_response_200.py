from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact import Contact
    from ..models.list_contacts_get_response_200_links import ListContactsGetResponse200Links


T = TypeVar("T", bound="ListContactsGetResponse200")


@_attrs_define
class ListContactsGetResponse200:
    """
    Attributes:
        contacts (Union[Unset, List['Contact']]):
        total_entries (Union[Unset, int]):  Example: 1.
        links (Union[Unset, ListContactsGetResponse200Links]):
    """

    contacts: Union[Unset, List["Contact"]] = UNSET
    total_entries: Union[Unset, int] = UNSET
    links: Union[Unset, "ListContactsGetResponse200Links"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contacts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = []
            for contacts_item_data in self.contacts:
                contacts_item = contacts_item_data.to_dict()
                contacts.append(contacts_item)

        total_entries = self.total_entries

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.contact import Contact
        from ..models.list_contacts_get_response_200_links import ListContactsGetResponse200Links

        d = src_dict.copy()
        contacts = []
        _contacts = d.pop("contacts", UNSET)
        for contacts_item_data in _contacts or []:
            contacts_item = Contact.from_dict(contacts_item_data)

            contacts.append(contacts_item)

        total_entries = d.pop("total_entries", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ListContactsGetResponse200Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ListContactsGetResponse200Links.from_dict(_links)

        list_contacts_get_response_200 = cls(
            contacts=contacts,
            total_entries=total_entries,
            links=links,
        )

        list_contacts_get_response_200.additional_properties = d
        return list_contacts_get_response_200

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
