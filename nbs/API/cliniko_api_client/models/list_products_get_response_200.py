from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_products_get_response_200_links import ListProductsGetResponse200Links
    from ..models.product import Product


T = TypeVar("T", bound="ListProductsGetResponse200")


@_attrs_define
class ListProductsGetResponse200:
    """
    Attributes:
        products (Union[Unset, List['Product']]):
        total_entries (Union[Unset, int]):  Example: 1.
        links (Union[Unset, ListProductsGetResponse200Links]):
    """

    products: Union[Unset, List["Product"]] = UNSET
    total_entries: Union[Unset, int] = UNSET
    links: Union[Unset, "ListProductsGetResponse200Links"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        products: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)

        total_entries = self.total_entries

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if products is not UNSET:
            field_dict["products"] = products
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.list_products_get_response_200_links import ListProductsGetResponse200Links
        from ..models.product import Product

        d = src_dict.copy()
        products = []
        _products = d.pop("products", UNSET)
        for products_item_data in _products or []:
            products_item = Product.from_dict(products_item_data)

            products.append(products_item)

        total_entries = d.pop("total_entries", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ListProductsGetResponse200Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ListProductsGetResponse200Links.from_dict(_links)

        list_products_get_response_200 = cls(
            products=products,
            total_entries=total_entries,
            links=links,
        )

        list_products_get_response_200.additional_properties = d
        return list_products_get_response_200

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
