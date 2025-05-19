from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_taxes_get_response_200_links import ListTaxesGetResponse200Links
    from ..models.tax import Tax


T = TypeVar("T", bound="ListTaxesGetResponse200")


@_attrs_define
class ListTaxesGetResponse200:
    """
    Attributes:
        taxes (Union[Unset, List['Tax']]):
        total_entries (Union[Unset, int]):  Example: 1.
        links (Union[Unset, ListTaxesGetResponse200Links]):
    """

    taxes: Union[Unset, List["Tax"]] = UNSET
    total_entries: Union[Unset, int] = UNSET
    links: Union[Unset, "ListTaxesGetResponse200Links"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        taxes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.taxes, Unset):
            taxes = []
            for taxes_item_data in self.taxes:
                taxes_item = taxes_item_data.to_dict()
                taxes.append(taxes_item)

        total_entries = self.total_entries

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if taxes is not UNSET:
            field_dict["taxes"] = taxes
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.list_taxes_get_response_200_links import ListTaxesGetResponse200Links
        from ..models.tax import Tax

        d = src_dict.copy()
        taxes = []
        _taxes = d.pop("taxes", UNSET)
        for taxes_item_data in _taxes or []:
            taxes_item = Tax.from_dict(taxes_item_data)

            taxes.append(taxes_item)

        total_entries = d.pop("total_entries", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ListTaxesGetResponse200Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ListTaxesGetResponse200Links.from_dict(_links)

        list_taxes_get_response_200 = cls(
            taxes=taxes,
            total_entries=total_entries,
            links=links,
        )

        list_taxes_get_response_200.additional_properties = d
        return list_taxes_get_response_200

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
