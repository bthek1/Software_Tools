import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stock_adjustment_links import StockAdjustmentLinks
    from ..models.stock_adjustment_product import StockAdjustmentProduct
    from ..models.stock_adjustment_user import StockAdjustmentUser


T = TypeVar("T", bound="StockAdjustment")


@_attrs_define
class StockAdjustment:
    """
    Attributes:
        adjustment_type (Union[Unset, str]):
        archived_at (Union[None, Unset, datetime.datetime]):
        comment (Union[None, Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        id (Union[Unset, str]):
        links (Union[Unset, StockAdjustmentLinks]):
        product (Union[Unset, StockAdjustmentProduct]):
        quantity (Union[None, Unset, int]):
        updated_at (Union[Unset, datetime.datetime]):
        user (Union[Unset, StockAdjustmentUser]):
    """

    adjustment_type: Union[Unset, str] = UNSET
    archived_at: Union[None, Unset, datetime.datetime] = UNSET
    comment: Union[None, Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    links: Union[Unset, "StockAdjustmentLinks"] = UNSET
    product: Union[Unset, "StockAdjustmentProduct"] = UNSET
    quantity: Union[None, Unset, int] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    user: Union[Unset, "StockAdjustmentUser"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        adjustment_type = self.adjustment_type

        archived_at: Union[None, Unset, str]
        if isinstance(self.archived_at, Unset):
            archived_at = UNSET
        elif isinstance(self.archived_at, datetime.datetime):
            archived_at = self.archived_at.isoformat()
        else:
            archived_at = self.archived_at

        comment: Union[None, Unset, str]
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        id = self.id

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        product: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()

        quantity: Union[None, Unset, int]
        if isinstance(self.quantity, Unset):
            quantity = UNSET
        else:
            quantity = self.quantity

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if adjustment_type is not UNSET:
            field_dict["adjustment_type"] = adjustment_type
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if comment is not UNSET:
            field_dict["comment"] = comment
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if links is not UNSET:
            field_dict["links"] = links
        if product is not UNSET:
            field_dict["product"] = product
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.stock_adjustment_links import StockAdjustmentLinks
        from ..models.stock_adjustment_product import StockAdjustmentProduct
        from ..models.stock_adjustment_user import StockAdjustmentUser

        d = src_dict.copy()
        adjustment_type = d.pop("adjustment_type", UNSET)

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

        def _parse_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment = _parse_comment(d.pop("comment", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        id = d.pop("id", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, StockAdjustmentLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = StockAdjustmentLinks.from_dict(_links)

        _product = d.pop("product", UNSET)
        product: Union[Unset, StockAdjustmentProduct]
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = StockAdjustmentProduct.from_dict(_product)

        def _parse_quantity(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        quantity = _parse_quantity(d.pop("quantity", UNSET))

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        _user = d.pop("user", UNSET)
        user: Union[Unset, StockAdjustmentUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = StockAdjustmentUser.from_dict(_user)

        stock_adjustment = cls(
            adjustment_type=adjustment_type,
            archived_at=archived_at,
            comment=comment,
            created_at=created_at,
            id=id,
            links=links,
            product=product,
            quantity=quantity,
            updated_at=updated_at,
            user=user,
        )

        stock_adjustment.additional_properties = d
        return stock_adjustment

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
