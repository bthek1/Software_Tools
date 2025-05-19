from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_services_for_business_get_response_200_links import ListServicesForBusinessGetResponse200Links
    from ..models.service import Service


T = TypeVar("T", bound="ListServicesForBusinessGetResponse200")


@_attrs_define
class ListServicesForBusinessGetResponse200:
    """
    Attributes:
        services (Union[Unset, List['Service']]):
        total_entries (Union[Unset, int]):  Example: 1.
        links (Union[Unset, ListServicesForBusinessGetResponse200Links]):
    """

    services: Union[Unset, List["Service"]] = UNSET
    total_entries: Union[Unset, int] = UNSET
    links: Union[Unset, "ListServicesForBusinessGetResponse200Links"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        services: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.services, Unset):
            services = []
            for services_item_data in self.services:
                services_item = services_item_data.to_dict()
                services.append(services_item)

        total_entries = self.total_entries

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if services is not UNSET:
            field_dict["services"] = services
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.list_services_for_business_get_response_200_links import (
            ListServicesForBusinessGetResponse200Links,
        )
        from ..models.service import Service

        d = src_dict.copy()
        services = []
        _services = d.pop("services", UNSET)
        for services_item_data in _services or []:
            services_item = Service.from_dict(services_item_data)

            services.append(services_item)

        total_entries = d.pop("total_entries", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ListServicesForBusinessGetResponse200Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ListServicesForBusinessGetResponse200Links.from_dict(_links)

        list_services_for_business_get_response_200 = cls(
            services=services,
            total_entries=total_entries,
            links=links,
        )

        list_services_for_business_get_response_200.additional_properties = d
        return list_services_for_business_get_response_200

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
