from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_users_get_response_200_links import ListUsersGetResponse200Links
    from ..models.user import User


T = TypeVar("T", bound="ListUsersGetResponse200")


@_attrs_define
class ListUsersGetResponse200:
    """
    Attributes:
        users (Union[Unset, List['User']]):
        total_entries (Union[Unset, int]):  Example: 1.
        links (Union[Unset, ListUsersGetResponse200Links]):
    """

    users: Union[Unset, List["User"]] = UNSET
    total_entries: Union[Unset, int] = UNSET
    links: Union[Unset, "ListUsersGetResponse200Links"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        users: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        total_entries = self.total_entries

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if users is not UNSET:
            field_dict["users"] = users
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.list_users_get_response_200_links import ListUsersGetResponse200Links
        from ..models.user import User

        d = src_dict.copy()
        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = User.from_dict(users_item_data)

            users.append(users_item)

        total_entries = d.pop("total_entries", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ListUsersGetResponse200Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ListUsersGetResponse200Links.from_dict(_links)

        list_users_get_response_200 = cls(
            users=users,
            total_entries=total_entries,
            links=links,
        )

        list_users_get_response_200.additional_properties = d
        return list_users_get_response_200

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
