import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.billable_item_item_type import BillableItemItemType, check_billable_item_item_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.billable_item_links import BillableItemLinks
    from ..models.billable_item_tax import BillableItemTax


T = TypeVar("T", bound="BillableItem")


@_attrs_define
class BillableItem:
    """
    Attributes:
        archived_at (Union[None, Unset, datetime.datetime]):
        created_at (Union[Unset, datetime.datetime]):
        id (Union[Unset, str]):
        item_code (Union[None, Unset, str]):
        item_type (Union[Unset, BillableItemItemType]):
        links (Union[Unset, BillableItemLinks]):
        name (Union[Unset, str]):
        price (Union[Unset, str]):
        tax (Union[Unset, BillableItemTax]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    archived_at: Union[None, Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    item_code: Union[None, Unset, str] = UNSET
    item_type: Union[Unset, BillableItemItemType] = UNSET
    links: Union[Unset, "BillableItemLinks"] = UNSET
    name: Union[Unset, str] = UNSET
    price: Union[Unset, str] = UNSET
    tax: Union[Unset, "BillableItemTax"] = UNSET
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

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        id = self.id

        item_code: Union[None, Unset, str]
        if isinstance(self.item_code, Unset):
            item_code = UNSET
        else:
            item_code = self.item_code

        item_type: Union[Unset, str] = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        name = self.name

        price = self.price

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
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if item_code is not UNSET:
            field_dict["item_code"] = item_code
        if item_type is not UNSET:
            field_dict["item_type"] = item_type
        if links is not UNSET:
            field_dict["links"] = links
        if name is not UNSET:
            field_dict["name"] = name
        if price is not UNSET:
            field_dict["price"] = price
        if tax is not UNSET:
            field_dict["tax"] = tax
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.billable_item_links import BillableItemLinks
        from ..models.billable_item_tax import BillableItemTax

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

        _item_type = d.pop("item_type", UNSET)
        item_type: Union[Unset, BillableItemItemType]
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = check_billable_item_item_type(_item_type)

        _links = d.pop("links", UNSET)
        links: Union[Unset, BillableItemLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = BillableItemLinks.from_dict(_links)

        name = d.pop("name", UNSET)

        price = d.pop("price", UNSET)

        _tax = d.pop("tax", UNSET)
        tax: Union[Unset, BillableItemTax]
        if isinstance(_tax, Unset):
            tax = UNSET
        else:
            tax = BillableItemTax.from_dict(_tax)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        billable_item = cls(
            archived_at=archived_at,
            created_at=created_at,
            id=id,
            item_code=item_code,
            item_type=item_type,
            links=links,
            name=name,
            price=price,
            tax=tax,
            updated_at=updated_at,
        )

        billable_item.additional_properties = d
        return billable_item

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
