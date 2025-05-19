from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_billable_item_patch_body_item_type import (
    UpdateBillableItemPatchBodyItemType,
    check_update_billable_item_patch_body_item_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateBillableItemPatchBody")


@_attrs_define
class UpdateBillableItemPatchBody:
    """
    Attributes:
        item_code (Union[None, Unset, str]):
        item_type (Union[Unset, UpdateBillableItemPatchBodyItemType]):
        name (Union[Unset, str]):
        price (Union[Unset, str]):
        tax_id (Union[Unset, str]): tax id Example: 1.
    """

    item_code: Union[None, Unset, str] = UNSET
    item_type: Union[Unset, UpdateBillableItemPatchBodyItemType] = UNSET
    name: Union[Unset, str] = UNSET
    price: Union[Unset, str] = UNSET
    tax_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        item_code: Union[None, Unset, str]
        if isinstance(self.item_code, Unset):
            item_code = UNSET
        else:
            item_code = self.item_code

        item_type: Union[Unset, str] = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type

        name = self.name

        price = self.price

        tax_id = self.tax_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if item_code is not UNSET:
            field_dict["item_code"] = item_code
        if item_type is not UNSET:
            field_dict["item_type"] = item_type
        if name is not UNSET:
            field_dict["name"] = name
        if price is not UNSET:
            field_dict["price"] = price
        if tax_id is not UNSET:
            field_dict["tax_id"] = tax_id

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

        _item_type = d.pop("item_type", UNSET)
        item_type: Union[Unset, UpdateBillableItemPatchBodyItemType]
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = check_update_billable_item_patch_body_item_type(_item_type)

        name = d.pop("name", UNSET)

        price = d.pop("price", UNSET)

        tax_id = d.pop("tax_id", UNSET)

        update_billable_item_patch_body = cls(
            item_code=item_code,
            item_type=item_type,
            name=name,
            price=price,
            tax_id=tax_id,
        )

        update_billable_item_patch_body.additional_properties = d
        return update_billable_item_patch_body

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
