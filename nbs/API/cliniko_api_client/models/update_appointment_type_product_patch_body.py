from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAppointmentTypeProductPatchBody")


@_attrs_define
class UpdateAppointmentTypeProductPatchBody:
    """
    Attributes:
        discount_percentage (Union[None, Unset, float]):
        discounted_amount (Union[None, Unset, str]):
        product_id (Union[Unset, str]): product id Example: 1.
        quantity (Union[Unset, float]):
    """

    discount_percentage: Union[None, Unset, float] = UNSET
    discounted_amount: Union[None, Unset, str] = UNSET
    product_id: Union[Unset, str] = UNSET
    quantity: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        product_id = self.product_id

        quantity = self.quantity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if discount_percentage is not UNSET:
            field_dict["discount_percentage"] = discount_percentage
        if discounted_amount is not UNSET:
            field_dict["discounted_amount"] = discounted_amount
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

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

        product_id = d.pop("product_id", UNSET)

        quantity = d.pop("quantity", UNSET)

        update_appointment_type_product_patch_body = cls(
            discount_percentage=discount_percentage,
            discounted_amount=discounted_amount,
            product_id=product_id,
            quantity=quantity,
        )

        update_appointment_type_product_patch_body.additional_properties = d
        return update_appointment_type_product_patch_body

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
