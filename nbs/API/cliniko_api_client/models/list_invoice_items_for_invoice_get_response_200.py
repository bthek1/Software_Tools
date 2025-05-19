from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_item import InvoiceItem
    from ..models.list_invoice_items_for_invoice_get_response_200_links import (
        ListInvoiceItemsForInvoiceGetResponse200Links,
    )


T = TypeVar("T", bound="ListInvoiceItemsForInvoiceGetResponse200")


@_attrs_define
class ListInvoiceItemsForInvoiceGetResponse200:
    """
    Attributes:
        invoice_items (Union[Unset, List['InvoiceItem']]):
        total_entries (Union[Unset, int]):  Example: 1.
        links (Union[Unset, ListInvoiceItemsForInvoiceGetResponse200Links]):
    """

    invoice_items: Union[Unset, List["InvoiceItem"]] = UNSET
    total_entries: Union[Unset, int] = UNSET
    links: Union[Unset, "ListInvoiceItemsForInvoiceGetResponse200Links"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        invoice_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.invoice_items, Unset):
            invoice_items = []
            for invoice_items_item_data in self.invoice_items:
                invoice_items_item = invoice_items_item_data.to_dict()
                invoice_items.append(invoice_items_item)

        total_entries = self.total_entries

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if invoice_items is not UNSET:
            field_dict["invoice_items"] = invoice_items
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_item import InvoiceItem
        from ..models.list_invoice_items_for_invoice_get_response_200_links import (
            ListInvoiceItemsForInvoiceGetResponse200Links,
        )

        d = src_dict.copy()
        invoice_items = []
        _invoice_items = d.pop("invoice_items", UNSET)
        for invoice_items_item_data in _invoice_items or []:
            invoice_items_item = InvoiceItem.from_dict(invoice_items_item_data)

            invoice_items.append(invoice_items_item)

        total_entries = d.pop("total_entries", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ListInvoiceItemsForInvoiceGetResponse200Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ListInvoiceItemsForInvoiceGetResponse200Links.from_dict(_links)

        list_invoice_items_for_invoice_get_response_200 = cls(
            invoice_items=invoice_items,
            total_entries=total_entries,
            links=links,
        )

        list_invoice_items_for_invoice_get_response_200.additional_properties = d
        return list_invoice_items_for_invoice_get_response_200

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
