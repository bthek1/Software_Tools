import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_links import ProductLinks
    from ..models.product_product_supplier import ProductProductSupplier
    from ..models.product_stock_adjustments import ProductStockAdjustments
    from ..models.product_tax import ProductTax


T = TypeVar("T", bound="Product")


@_attrs_define
class Product:
    """
    Attributes:
        archived_at (Union[None, Unset, datetime.datetime]):
        cost_price (Union[None, Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        id (Union[Unset, str]):
        item_code (Union[None, Unset, str]):
        links (Union[Unset, ProductLinks]):
        name (Union[Unset, str]):
        notes (Union[None, Unset, str]):
        price_ex_tax (Union[None, Unset, str]):
        price_including_tax (Union[None, Unset, str]):
        product_supplier (Union[Unset, ProductProductSupplier]):
        product_supplier_name (Union[None, Unset, str]):
        serial_number (Union[None, Unset, str]):
        stock_adjustments (Union[Unset, ProductStockAdjustments]):
        stock_level (Union[None, Unset, int]):
        tax (Union[Unset, ProductTax]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    archived_at: Union[None, Unset, datetime.datetime] = UNSET
    cost_price: Union[None, Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    item_code: Union[None, Unset, str] = UNSET
    links: Union[Unset, "ProductLinks"] = UNSET
    name: Union[Unset, str] = UNSET
    notes: Union[None, Unset, str] = UNSET
    price_ex_tax: Union[None, Unset, str] = UNSET
    price_including_tax: Union[None, Unset, str] = UNSET
    product_supplier: Union[Unset, "ProductProductSupplier"] = UNSET
    product_supplier_name: Union[None, Unset, str] = UNSET
    serial_number: Union[None, Unset, str] = UNSET
    stock_adjustments: Union[Unset, "ProductStockAdjustments"] = UNSET
    stock_level: Union[None, Unset, int] = UNSET
    tax: Union[Unset, "ProductTax"] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        archived_at: Union[None, Unset, str]
        if isinstance(self.archived_at, Unset):
            archived_at = UNSET
        elif isinstance(self.archived_at, datetime.datetime):
            archived_at = self.archived_at.isoformat()
        else:
            archived_at = self.archived_at

        cost_price: Union[None, Unset, str]
        if isinstance(self.cost_price, Unset):
            cost_price = UNSET
        else:
            cost_price = self.cost_price

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        id = self.id

        item_code: Union[None, Unset, str]
        if isinstance(self.item_code, Unset):
            item_code = UNSET
        else:
            item_code = self.item_code

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        name = self.name

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        price_ex_tax: Union[None, Unset, str]
        if isinstance(self.price_ex_tax, Unset):
            price_ex_tax = UNSET
        else:
            price_ex_tax = self.price_ex_tax

        price_including_tax: Union[None, Unset, str]
        if isinstance(self.price_including_tax, Unset):
            price_including_tax = UNSET
        else:
            price_including_tax = self.price_including_tax

        product_supplier: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.product_supplier, Unset):
            product_supplier = self.product_supplier.to_dict()

        product_supplier_name: Union[None, Unset, str]
        if isinstance(self.product_supplier_name, Unset):
            product_supplier_name = UNSET
        else:
            product_supplier_name = self.product_supplier_name

        serial_number: Union[None, Unset, str]
        if isinstance(self.serial_number, Unset):
            serial_number = UNSET
        else:
            serial_number = self.serial_number

        stock_adjustments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.stock_adjustments, Unset):
            stock_adjustments = self.stock_adjustments.to_dict()

        stock_level: Union[None, Unset, int]
        if isinstance(self.stock_level, Unset):
            stock_level = UNSET
        else:
            stock_level = self.stock_level

        tax: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tax, Unset):
            tax = self.tax.to_dict()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if cost_price is not UNSET:
            field_dict["cost_price"] = cost_price
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if item_code is not UNSET:
            field_dict["item_code"] = item_code
        if links is not UNSET:
            field_dict["links"] = links
        if name is not UNSET:
            field_dict["name"] = name
        if notes is not UNSET:
            field_dict["notes"] = notes
        if price_ex_tax is not UNSET:
            field_dict["price_ex_tax"] = price_ex_tax
        if price_including_tax is not UNSET:
            field_dict["price_including_tax"] = price_including_tax
        if product_supplier is not UNSET:
            field_dict["product_supplier"] = product_supplier
        if product_supplier_name is not UNSET:
            field_dict["product_supplier_name"] = product_supplier_name
        if serial_number is not UNSET:
            field_dict["serial_number"] = serial_number
        if stock_adjustments is not UNSET:
            field_dict["stock_adjustments"] = stock_adjustments
        if stock_level is not UNSET:
            field_dict["stock_level"] = stock_level
        if tax is not UNSET:
            field_dict["tax"] = tax
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.product_links import ProductLinks
        from ..models.product_product_supplier import ProductProductSupplier
        from ..models.product_stock_adjustments import ProductStockAdjustments
        from ..models.product_tax import ProductTax

        d = src_dict.copy()

        def _parse_archived_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                archived_at_type_0 = isoparse(data)

                return archived_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        archived_at = _parse_archived_at(d.pop("archived_at", UNSET))

        def _parse_cost_price(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cost_price = _parse_cost_price(d.pop("cost_price", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        id = d.pop("id", UNSET)

        def _parse_item_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        item_code = _parse_item_code(d.pop("item_code", UNSET))

        _links = d.pop("links", UNSET)
        links: Union[Unset, ProductLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ProductLinks.from_dict(_links)

        name = d.pop("name", UNSET)

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_price_ex_tax(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        price_ex_tax = _parse_price_ex_tax(d.pop("price_ex_tax", UNSET))

        def _parse_price_including_tax(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        price_including_tax = _parse_price_including_tax(d.pop("price_including_tax", UNSET))

        _product_supplier = d.pop("product_supplier", UNSET)
        product_supplier: Union[Unset, ProductProductSupplier]
        if isinstance(_product_supplier, Unset):
            product_supplier = UNSET
        else:
            product_supplier = ProductProductSupplier.from_dict(_product_supplier)

        def _parse_product_supplier_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        product_supplier_name = _parse_product_supplier_name(d.pop("product_supplier_name", UNSET))

        def _parse_serial_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        serial_number = _parse_serial_number(d.pop("serial_number", UNSET))

        _stock_adjustments = d.pop("stock_adjustments", UNSET)
        stock_adjustments: Union[Unset, ProductStockAdjustments]
        if isinstance(_stock_adjustments, Unset):
            stock_adjustments = UNSET
        else:
            stock_adjustments = ProductStockAdjustments.from_dict(_stock_adjustments)

        def _parse_stock_level(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        stock_level = _parse_stock_level(d.pop("stock_level", UNSET))

        _tax = d.pop("tax", UNSET)
        tax: Union[Unset, ProductTax]
        if isinstance(_tax, Unset):
            tax = UNSET
        else:
            tax = ProductTax.from_dict(_tax)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        product = cls(
            archived_at=archived_at,
            cost_price=cost_price,
            created_at=created_at,
            id=id,
            item_code=item_code,
            links=links,
            name=name,
            notes=notes,
            price_ex_tax=price_ex_tax,
            price_including_tax=price_including_tax,
            product_supplier=product_supplier,
            product_supplier_name=product_supplier_name,
            serial_number=serial_number,
            stock_adjustments=stock_adjustments,
            stock_level=stock_level,
            tax=tax,
            updated_at=updated_at,
        )

        product.additional_properties = d
        return product

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
