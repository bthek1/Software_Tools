from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_product_suppliers_get_response_200_links import ListProductSuppliersGetResponse200Links
    from ..models.product_supplier import ProductSupplier


T = TypeVar("T", bound="ListProductSuppliersGetResponse200")


@_attrs_define
class ListProductSuppliersGetResponse200:
    """
    Attributes:
        product_suppliers (Union[Unset, List['ProductSupplier']]):
        total_entries (Union[Unset, int]):  Example: 1.
        links (Union[Unset, ListProductSuppliersGetResponse200Links]):
    """

    product_suppliers: Union[Unset, List["ProductSupplier"]] = UNSET
    total_entries: Union[Unset, int] = UNSET
    links: Union[Unset, "ListProductSuppliersGetResponse200Links"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        product_suppliers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.product_suppliers, Unset):
            product_suppliers = []
            for product_suppliers_item_data in self.product_suppliers:
                product_suppliers_item = product_suppliers_item_data.to_dict()
                product_suppliers.append(product_suppliers_item)

        total_entries = self.total_entries

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_suppliers is not UNSET:
            field_dict["product_suppliers"] = product_suppliers
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.list_product_suppliers_get_response_200_links import ListProductSuppliersGetResponse200Links
        from ..models.product_supplier import ProductSupplier

        d = src_dict.copy()
        product_suppliers = []
        _product_suppliers = d.pop("product_suppliers", UNSET)
        for product_suppliers_item_data in _product_suppliers or []:
            product_suppliers_item = ProductSupplier.from_dict(product_suppliers_item_data)

            product_suppliers.append(product_suppliers_item)

        total_entries = d.pop("total_entries", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ListProductSuppliersGetResponse200Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ListProductSuppliersGetResponse200Links.from_dict(_links)

        list_product_suppliers_get_response_200 = cls(
            product_suppliers=product_suppliers,
            total_entries=total_entries,
            links=links,
        )

        list_product_suppliers_get_response_200.additional_properties = d
        return list_product_suppliers_get_response_200

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
