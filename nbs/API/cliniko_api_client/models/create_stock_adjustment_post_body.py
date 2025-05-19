from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_stock_adjustment_post_body_adjustment_type import (
    CreateStockAdjustmentPostBodyAdjustmentType,
    check_create_stock_adjustment_post_body_adjustment_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateStockAdjustmentPostBody")


@_attrs_define
class CreateStockAdjustmentPostBody:
    """
    Attributes:
        quantity (Union[None, Unset, int]): A negative value is only allowed when a decreasing adjustment type has been
            selected and vice versa.
        adjustment_type (Union[Unset, CreateStockAdjustmentPostBodyAdjustmentType]): The reason for modifying the stock
            level.

            **Increase types**: `Stock Purchase`, `Returned`, `Other`

            **Decrease types**: `Damaged`, `Out of Date`, `Item Sold`, `Other`
        comment (Union[None, Unset, str]):
        product_id (Union[Unset, str]): The existing product you want to adjust the stock level of. Example: 1.
    """

    quantity: Union[None, Unset, int] = UNSET
    adjustment_type: Union[Unset, CreateStockAdjustmentPostBodyAdjustmentType] = UNSET
    comment: Union[None, Unset, str] = UNSET
    product_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        quantity: Union[None, Unset, int]
        if isinstance(self.quantity, Unset):
            quantity = UNSET
        else:
            quantity = self.quantity

        adjustment_type: Union[Unset, str] = UNSET
        if not isinstance(self.adjustment_type, Unset):
            adjustment_type = self.adjustment_type

        comment: Union[None, Unset, str]
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        product_id = self.product_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if adjustment_type is not UNSET:
            field_dict["adjustment_type"] = adjustment_type
        if comment is not UNSET:
            field_dict["comment"] = comment
        if product_id is not UNSET:
            field_dict["product_id"] = product_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_quantity(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        quantity = _parse_quantity(d.pop("quantity", UNSET))

        _adjustment_type = d.pop("adjustment_type", UNSET)
        adjustment_type: Union[Unset, CreateStockAdjustmentPostBodyAdjustmentType]
        if isinstance(_adjustment_type, Unset):
            adjustment_type = UNSET
        else:
            adjustment_type = check_create_stock_adjustment_post_body_adjustment_type(_adjustment_type)

        def _parse_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment = _parse_comment(d.pop("comment", UNSET))

        product_id = d.pop("product_id", UNSET)

        create_stock_adjustment_post_body = cls(
            quantity=quantity,
            adjustment_type=adjustment_type,
            comment=comment,
            product_id=product_id,
        )

        create_stock_adjustment_post_body.additional_properties = d
        return create_stock_adjustment_post_body

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
