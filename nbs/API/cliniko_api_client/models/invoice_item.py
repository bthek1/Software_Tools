import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice_item_billable_item import InvoiceItemBillableItem
    from ..models.invoice_item_invoice import InvoiceItemInvoice
    from ..models.invoice_item_links import InvoiceItemLinks
    from ..models.invoice_item_product import InvoiceItemProduct


T = TypeVar("T", bound="InvoiceItem")


@_attrs_define
class InvoiceItem:
    """
    Attributes:
        archived_at (Union[None, Unset, datetime.datetime]):
        billable_item (Union[Unset, InvoiceItemBillableItem]):
        code (Union[None, Unset, str]):
        concession_type_name (Union[None, Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        deleted_at (Union[None, Unset, datetime.datetime]):
        discount_percentage (Union[None, Unset, float]):
        discounted_amount (Union[None, Unset, str]):
        id (Union[Unset, str]):
        invoice (Union[Unset, InvoiceItemInvoice]):
        is_monetary_discount (Union[None, Unset, bool]):
        links (Union[Unset, InvoiceItemLinks]):
        name (Union[None, Unset, str]):
        net_price (Union[None, Unset, str]):
        product (Union[Unset, InvoiceItemProduct]):
        quantity (Union[Unset, int]):
        tax_amount (Union[None, Unset, float]):
        tax_name (Union[None, Unset, str]):
        tax_rate (Union[None, Unset, float]):
        total_including_tax (Union[None, Unset, float]):
        unit_price (Union[Unset, str]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    archived_at: Union[None, Unset, datetime.datetime] = UNSET
    billable_item: Union[Unset, "InvoiceItemBillableItem"] = UNSET
    code: Union[None, Unset, str] = UNSET
    concession_type_name: Union[None, Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    deleted_at: Union[None, Unset, datetime.datetime] = UNSET
    discount_percentage: Union[None, Unset, float] = UNSET
    discounted_amount: Union[None, Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    invoice: Union[Unset, "InvoiceItemInvoice"] = UNSET
    is_monetary_discount: Union[None, Unset, bool] = UNSET
    links: Union[Unset, "InvoiceItemLinks"] = UNSET
    name: Union[None, Unset, str] = UNSET
    net_price: Union[None, Unset, str] = UNSET
    product: Union[Unset, "InvoiceItemProduct"] = UNSET
    quantity: Union[Unset, int] = UNSET
    tax_amount: Union[None, Unset, float] = UNSET
    tax_name: Union[None, Unset, str] = UNSET
    tax_rate: Union[None, Unset, float] = UNSET
    total_including_tax: Union[None, Unset, float] = UNSET
    unit_price: Union[Unset, str] = UNSET
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

        billable_item: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.billable_item, Unset):
            billable_item = self.billable_item.to_dict()

        code: Union[None, Unset, str]
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code

        concession_type_name: Union[None, Unset, str]
        if isinstance(self.concession_type_name, Unset):
            concession_type_name = UNSET
        else:
            concession_type_name = self.concession_type_name

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        deleted_at: Union[None, Unset, str]
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        elif isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        discount_percentage: Union[None, Unset, float]
        if isinstance(self.discount_percentage, Unset):
            discount_percentage = UNSET
        else:
            discount_percentage = self.discount_percentage

        discounted_amount: Union[None, Unset, str]
        if isinstance(self.discounted_amount, Unset):
            discounted_amount = UNSET
        else:
            discounted_amount = self.discounted_amount

        id = self.id

        invoice: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.invoice, Unset):
            invoice = self.invoice.to_dict()

        is_monetary_discount: Union[None, Unset, bool]
        if isinstance(self.is_monetary_discount, Unset):
            is_monetary_discount = UNSET
        else:
            is_monetary_discount = self.is_monetary_discount

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        net_price: Union[None, Unset, str]
        if isinstance(self.net_price, Unset):
            net_price = UNSET
        else:
            net_price = self.net_price

        product: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()

        quantity = self.quantity

        tax_amount: Union[None, Unset, float]
        if isinstance(self.tax_amount, Unset):
            tax_amount = UNSET
        else:
            tax_amount = self.tax_amount

        tax_name: Union[None, Unset, str]
        if isinstance(self.tax_name, Unset):
            tax_name = UNSET
        else:
            tax_name = self.tax_name

        tax_rate: Union[None, Unset, float]
        if isinstance(self.tax_rate, Unset):
            tax_rate = UNSET
        else:
            tax_rate = self.tax_rate

        total_including_tax: Union[None, Unset, float]
        if isinstance(self.total_including_tax, Unset):
            total_including_tax = UNSET
        else:
            total_including_tax = self.total_including_tax

        unit_price = self.unit_price

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if billable_item is not UNSET:
            field_dict["billable_item"] = billable_item
        if code is not UNSET:
            field_dict["code"] = code
        if concession_type_name is not UNSET:
            field_dict["concession_type_name"] = concession_type_name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if discount_percentage is not UNSET:
            field_dict["discount_percentage"] = discount_percentage
        if discounted_amount is not UNSET:
            field_dict["discounted_amount"] = discounted_amount
        if id is not UNSET:
            field_dict["id"] = id
        if invoice is not UNSET:
            field_dict["invoice"] = invoice
        if is_monetary_discount is not UNSET:
            field_dict["is_monetary_discount"] = is_monetary_discount
        if links is not UNSET:
            field_dict["links"] = links
        if name is not UNSET:
            field_dict["name"] = name
        if net_price is not UNSET:
            field_dict["net_price"] = net_price
        if product is not UNSET:
            field_dict["product"] = product
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if tax_amount is not UNSET:
            field_dict["tax_amount"] = tax_amount
        if tax_name is not UNSET:
            field_dict["tax_name"] = tax_name
        if tax_rate is not UNSET:
            field_dict["tax_rate"] = tax_rate
        if total_including_tax is not UNSET:
            field_dict["total_including_tax"] = total_including_tax
        if unit_price is not UNSET:
            field_dict["unit_price"] = unit_price
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.invoice_item_billable_item import InvoiceItemBillableItem
        from ..models.invoice_item_invoice import InvoiceItemInvoice
        from ..models.invoice_item_links import InvoiceItemLinks
        from ..models.invoice_item_product import InvoiceItemProduct

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

        _billable_item = d.pop("billable_item", UNSET)
        billable_item: Union[Unset, InvoiceItemBillableItem]
        if isinstance(_billable_item, Unset):
            billable_item = UNSET
        else:
            billable_item = InvoiceItemBillableItem.from_dict(_billable_item)

        def _parse_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        code = _parse_code(d.pop("code", UNSET))

        def _parse_concession_type_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        concession_type_name = _parse_concession_type_name(d.pop("concession_type_name", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        def _parse_deleted_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_at_type_0 = isoparse(data)

                return deleted_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at", UNSET))

        def _parse_discount_percentage(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        discount_percentage = _parse_discount_percentage(d.pop("discount_percentage", UNSET))

        def _parse_discounted_amount(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        discounted_amount = _parse_discounted_amount(d.pop("discounted_amount", UNSET))

        id = d.pop("id", UNSET)

        _invoice = d.pop("invoice", UNSET)
        invoice: Union[Unset, InvoiceItemInvoice]
        if isinstance(_invoice, Unset):
            invoice = UNSET
        else:
            invoice = InvoiceItemInvoice.from_dict(_invoice)

        def _parse_is_monetary_discount(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_monetary_discount = _parse_is_monetary_discount(d.pop("is_monetary_discount", UNSET))

        _links = d.pop("links", UNSET)
        links: Union[Unset, InvoiceItemLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = InvoiceItemLinks.from_dict(_links)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_net_price(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        net_price = _parse_net_price(d.pop("net_price", UNSET))

        _product = d.pop("product", UNSET)
        product: Union[Unset, InvoiceItemProduct]
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = InvoiceItemProduct.from_dict(_product)

        quantity = d.pop("quantity", UNSET)

        def _parse_tax_amount(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        tax_amount = _parse_tax_amount(d.pop("tax_amount", UNSET))

        def _parse_tax_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tax_name = _parse_tax_name(d.pop("tax_name", UNSET))

        def _parse_tax_rate(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        tax_rate = _parse_tax_rate(d.pop("tax_rate", UNSET))

        def _parse_total_including_tax(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        total_including_tax = _parse_total_including_tax(d.pop("total_including_tax", UNSET))

        unit_price = d.pop("unit_price", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        invoice_item = cls(
            archived_at=archived_at,
            billable_item=billable_item,
            code=code,
            concession_type_name=concession_type_name,
            created_at=created_at,
            deleted_at=deleted_at,
            discount_percentage=discount_percentage,
            discounted_amount=discounted_amount,
            id=id,
            invoice=invoice,
            is_monetary_discount=is_monetary_discount,
            links=links,
            name=name,
            net_price=net_price,
            product=product,
            quantity=quantity,
            tax_amount=tax_amount,
            tax_name=tax_name,
            tax_rate=tax_rate,
            total_including_tax=total_including_tax,
            unit_price=unit_price,
            updated_at=updated_at,
        )

        invoice_item.additional_properties = d
        return invoice_item

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
