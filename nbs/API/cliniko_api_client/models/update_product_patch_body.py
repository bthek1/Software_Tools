from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateProductPatchBody")


@_attrs_define
class UpdateProductPatchBody:
    """
    Attributes:
        item_code (Union[None, Unset, str]):
        name (Union[Unset, str]):
        serial_number (Union[None, Unset, str]):
        price (Union[Unset, float]):
        product_supplier_name (Union[None, Unset, str]):
        price_includes_tax (Union[None, Unset, bool]):
        stock_level (Union[None, Unset, float]):
        tax_id (Union[Unset, str]): tax id Example: 1.
        cost_price (Union[None, Unset, str]):
        notes (Union[None, Unset, str]):
    """

    item_code: Union[None, Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    serial_number: Union[None, Unset, str] = UNSET
    price: Union[Unset, float] = UNSET
    product_supplier_name: Union[None, Unset, str] = UNSET
    price_includes_tax: Union[None, Unset, bool] = UNSET
    stock_level: Union[None, Unset, float] = UNSET
    tax_id: Union[Unset, str] = UNSET
    cost_price: Union[None, Unset, str] = UNSET
    notes: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        item_code: Union[None, Unset, str]
        if isinstance(self.item_code, Unset):
            item_code = UNSET
        else:
            item_code = self.item_code

        name = self.name

        serial_number: Union[None, Unset, str]
        if isinstance(self.serial_number, Unset):
            serial_number = UNSET
        else:
            serial_number = self.serial_number

        price = self.price

        product_supplier_name: Union[None, Unset, str]
        if isinstance(self.product_supplier_name, Unset):
            product_supplier_name = UNSET
        else:
            product_supplier_name = self.product_supplier_name

        price_includes_tax: Union[None, Unset, bool]
        if isinstance(self.price_includes_tax, Unset):
            price_includes_tax = UNSET
        else:
            price_includes_tax = self.price_includes_tax

        stock_level: Union[None, Unset, float]
        if isinstance(self.stock_level, Unset):
            stock_level = UNSET
        else:
            stock_level = self.stock_level

        tax_id = self.tax_id

        cost_price: Union[None, Unset, str]
        if isinstance(self.cost_price, Unset):
            cost_price = UNSET
        else:
            cost_price = self.cost_price

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item_code is not UNSET:
            field_dict["item_code"] = item_code
        if name is not UNSET:
            field_dict["name"] = name
        if serial_number is not UNSET:
            field_dict["serial_number"] = serial_number
        if price is not UNSET:
            field_dict["price"] = price
        if product_supplier_name is not UNSET:
            field_dict["product_supplier_name"] = product_supplier_name
        if price_includes_tax is not UNSET:
            field_dict["price_includes_tax"] = price_includes_tax
        if stock_level is not UNSET:
            field_dict["stock_level"] = stock_level
        if tax_id is not UNSET:
            field_dict["tax_id"] = tax_id
        if cost_price is not UNSET:
            field_dict["cost_price"] = cost_price
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_item_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        item_code = _parse_item_code(d.pop("item_code", UNSET))

        name = d.pop("name", UNSET)

        def _parse_serial_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        serial_number = _parse_serial_number(d.pop("serial_number", UNSET))

        price = d.pop("price", UNSET)

        def _parse_product_supplier_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        product_supplier_name = _parse_product_supplier_name(d.pop("product_supplier_name", UNSET))

        def _parse_price_includes_tax(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        price_includes_tax = _parse_price_includes_tax(d.pop("price_includes_tax", UNSET))

        def _parse_stock_level(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        stock_level = _parse_stock_level(d.pop("stock_level", UNSET))

        tax_id = d.pop("tax_id", UNSET)

        def _parse_cost_price(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cost_price = _parse_cost_price(d.pop("cost_price", UNSET))

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        update_product_patch_body = cls(
            item_code=item_code,
            name=name,
            serial_number=serial_number,
            price=price,
            product_supplier_name=product_supplier_name,
            price_includes_tax=price_includes_tax,
            stock_level=stock_level,
            tax_id=tax_id,
            cost_price=cost_price,
            notes=notes,
        )

        update_product_patch_body.additional_properties = d
        return update_product_patch_body

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
