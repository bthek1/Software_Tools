import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.appointment_type_product_appointment_type import AppointmentTypeProductAppointmentType
    from ..models.appointment_type_product_links import AppointmentTypeProductLinks
    from ..models.appointment_type_product_product import AppointmentTypeProductProduct


T = TypeVar("T", bound="AppointmentTypeProduct")


@_attrs_define
class AppointmentTypeProduct:
    """
    Attributes:
        appointment_type (Union[Unset, AppointmentTypeProductAppointmentType]):
        created_at (Union[Unset, datetime.datetime]):
        discount_percentage (Union[None, Unset, float]):
        discounted_amount (Union[None, Unset, str]):
        id (Union[Unset, str]):
        is_monetary_discount (Union[None, Unset, bool]):
        links (Union[Unset, AppointmentTypeProductLinks]):
        product (Union[Unset, AppointmentTypeProductProduct]):
        quantity (Union[Unset, int]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    appointment_type: Union[Unset, "AppointmentTypeProductAppointmentType"] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    discount_percentage: Union[None, Unset, float] = UNSET
    discounted_amount: Union[None, Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    is_monetary_discount: Union[None, Unset, bool] = UNSET
    links: Union[Unset, "AppointmentTypeProductLinks"] = UNSET
    product: Union[Unset, "AppointmentTypeProductProduct"] = UNSET
    quantity: Union[Unset, int] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        appointment_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.appointment_type, Unset):
            appointment_type = self.appointment_type.to_dict()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

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

        is_monetary_discount: Union[None, Unset, bool]
        if isinstance(self.is_monetary_discount, Unset):
            is_monetary_discount = UNSET
        else:
            is_monetary_discount = self.is_monetary_discount

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        product: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()

        quantity = self.quantity

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if appointment_type is not UNSET:
            field_dict["appointment_type"] = appointment_type
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if discount_percentage is not UNSET:
            field_dict["discount_percentage"] = discount_percentage
        if discounted_amount is not UNSET:
            field_dict["discounted_amount"] = discounted_amount
        if id is not UNSET:
            field_dict["id"] = id
        if is_monetary_discount is not UNSET:
            field_dict["is_monetary_discount"] = is_monetary_discount
        if links is not UNSET:
            field_dict["links"] = links
        if product is not UNSET:
            field_dict["product"] = product
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.appointment_type_product_appointment_type import AppointmentTypeProductAppointmentType
        from ..models.appointment_type_product_links import AppointmentTypeProductLinks
        from ..models.appointment_type_product_product import AppointmentTypeProductProduct

        d = src_dict.copy()
        _appointment_type = d.pop("appointment_type", UNSET)
        appointment_type: Union[Unset, AppointmentTypeProductAppointmentType]
        if isinstance(_appointment_type, Unset):
            appointment_type = UNSET
        else:
            appointment_type = AppointmentTypeProductAppointmentType.from_dict(_appointment_type)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

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

        def _parse_is_monetary_discount(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_monetary_discount = _parse_is_monetary_discount(d.pop("is_monetary_discount", UNSET))

        _links = d.pop("links", UNSET)
        links: Union[Unset, AppointmentTypeProductLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = AppointmentTypeProductLinks.from_dict(_links)

        _product = d.pop("product", UNSET)
        product: Union[Unset, AppointmentTypeProductProduct]
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = AppointmentTypeProductProduct.from_dict(_product)

        quantity = d.pop("quantity", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        appointment_type_product = cls(
            appointment_type=appointment_type,
            created_at=created_at,
            discount_percentage=discount_percentage,
            discounted_amount=discounted_amount,
            id=id,
            is_monetary_discount=is_monetary_discount,
            links=links,
            product=product,
            quantity=quantity,
            updated_at=updated_at,
        )

        appointment_type_product.additional_properties = d
        return appointment_type_product

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
