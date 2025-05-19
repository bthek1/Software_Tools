import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.concession_price_billable_item import ConcessionPriceBillableItem
    from ..models.concession_price_concession_type import ConcessionPriceConcessionType
    from ..models.concession_price_links import ConcessionPriceLinks


T = TypeVar("T", bound="ConcessionPrice")


@_attrs_define
class ConcessionPrice:
    """
    Attributes:
        billable_item (Union[Unset, ConcessionPriceBillableItem]):
        concession_type (Union[Unset, ConcessionPriceConcessionType]):
        created_at (Union[Unset, datetime.datetime]):
        id (Union[Unset, str]):
        links (Union[Unset, ConcessionPriceLinks]):
        price (Union[None, Unset, str]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    billable_item: Union[Unset, "ConcessionPriceBillableItem"] = UNSET
    concession_type: Union[Unset, "ConcessionPriceConcessionType"] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    links: Union[Unset, "ConcessionPriceLinks"] = UNSET
    price: Union[None, Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        billable_item: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.billable_item, Unset):
            billable_item = self.billable_item.to_dict()

        concession_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.concession_type, Unset):
            concession_type = self.concession_type.to_dict()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        id = self.id

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        price: Union[None, Unset, str]
        if isinstance(self.price, Unset):
            price = UNSET
        else:
            price = self.price

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if billable_item is not UNSET:
            field_dict["billable_item"] = billable_item
        if concession_type is not UNSET:
            field_dict["concession_type"] = concession_type
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if links is not UNSET:
            field_dict["links"] = links
        if price is not UNSET:
            field_dict["price"] = price
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.concession_price_billable_item import ConcessionPriceBillableItem
        from ..models.concession_price_concession_type import ConcessionPriceConcessionType
        from ..models.concession_price_links import ConcessionPriceLinks

        d = src_dict.copy()
        _billable_item = d.pop("billable_item", UNSET)
        billable_item: Union[Unset, ConcessionPriceBillableItem]
        if isinstance(_billable_item, Unset):
            billable_item = UNSET
        else:
            billable_item = ConcessionPriceBillableItem.from_dict(_billable_item)

        _concession_type = d.pop("concession_type", UNSET)
        concession_type: Union[Unset, ConcessionPriceConcessionType]
        if isinstance(_concession_type, Unset):
            concession_type = UNSET
        else:
            concession_type = ConcessionPriceConcessionType.from_dict(_concession_type)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        id = d.pop("id", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ConcessionPriceLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ConcessionPriceLinks.from_dict(_links)

        def _parse_price(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        price = _parse_price(d.pop("price", UNSET))

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        concession_price = cls(
            billable_item=billable_item,
            concession_type=concession_type,
            created_at=created_at,
            id=id,
            links=links,
            price=price,
            updated_at=updated_at,
        )

        concession_price.additional_properties = d
        return concession_price

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
