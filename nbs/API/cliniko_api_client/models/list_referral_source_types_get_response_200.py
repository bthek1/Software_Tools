from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_referral_source_types_get_response_200_links import ListReferralSourceTypesGetResponse200Links
    from ..models.referral_source_type import ReferralSourceType


T = TypeVar("T", bound="ListReferralSourceTypesGetResponse200")


@_attrs_define
class ListReferralSourceTypesGetResponse200:
    """
    Attributes:
        referral_source_types (Union[Unset, List['ReferralSourceType']]):
        total_entries (Union[Unset, int]):  Example: 1.
        links (Union[Unset, ListReferralSourceTypesGetResponse200Links]):
    """

    referral_source_types: Union[Unset, List["ReferralSourceType"]] = UNSET
    total_entries: Union[Unset, int] = UNSET
    links: Union[Unset, "ListReferralSourceTypesGetResponse200Links"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        referral_source_types: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.referral_source_types, Unset):
            referral_source_types = []
            for referral_source_types_item_data in self.referral_source_types:
                referral_source_types_item = referral_source_types_item_data.to_dict()
                referral_source_types.append(referral_source_types_item)

        total_entries = self.total_entries

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if referral_source_types is not UNSET:
            field_dict["referral_source_types"] = referral_source_types
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.list_referral_source_types_get_response_200_links import (
            ListReferralSourceTypesGetResponse200Links,
        )
        from ..models.referral_source_type import ReferralSourceType

        d = src_dict.copy()
        referral_source_types = []
        _referral_source_types = d.pop("referral_source_types", UNSET)
        for referral_source_types_item_data in _referral_source_types or []:
            referral_source_types_item = ReferralSourceType.from_dict(referral_source_types_item_data)

            referral_source_types.append(referral_source_types_item)

        total_entries = d.pop("total_entries", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ListReferralSourceTypesGetResponse200Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ListReferralSourceTypesGetResponse200Links.from_dict(_links)

        list_referral_source_types_get_response_200 = cls(
            referral_source_types=referral_source_types,
            total_entries=total_entries,
            links=links,
        )

        list_referral_source_types_get_response_200.additional_properties = d
        return list_referral_source_types_get_response_200

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
