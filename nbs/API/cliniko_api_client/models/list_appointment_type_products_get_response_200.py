from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.appointment_type_product import AppointmentTypeProduct
    from ..models.list_appointment_type_products_get_response_200_links import (
        ListAppointmentTypeProductsGetResponse200Links,
    )


T = TypeVar("T", bound="ListAppointmentTypeProductsGetResponse200")


@_attrs_define
class ListAppointmentTypeProductsGetResponse200:
    """
    Attributes:
        appointment_type_products (Union[Unset, List['AppointmentTypeProduct']]):
        total_entries (Union[Unset, int]):  Example: 1.
        links (Union[Unset, ListAppointmentTypeProductsGetResponse200Links]):
    """

    appointment_type_products: Union[Unset, List["AppointmentTypeProduct"]] = UNSET
    total_entries: Union[Unset, int] = UNSET
    links: Union[Unset, "ListAppointmentTypeProductsGetResponse200Links"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        appointment_type_products: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.appointment_type_products, Unset):
            appointment_type_products = []
            for appointment_type_products_item_data in self.appointment_type_products:
                appointment_type_products_item = appointment_type_products_item_data.to_dict()
                appointment_type_products.append(appointment_type_products_item)

        total_entries = self.total_entries

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if appointment_type_products is not UNSET:
            field_dict["appointment_type_products"] = appointment_type_products
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.appointment_type_product import AppointmentTypeProduct
        from ..models.list_appointment_type_products_get_response_200_links import (
            ListAppointmentTypeProductsGetResponse200Links,
        )

        d = src_dict.copy()
        appointment_type_products = []
        _appointment_type_products = d.pop("appointment_type_products", UNSET)
        for appointment_type_products_item_data in _appointment_type_products or []:
            appointment_type_products_item = AppointmentTypeProduct.from_dict(appointment_type_products_item_data)

            appointment_type_products.append(appointment_type_products_item)

        total_entries = d.pop("total_entries", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ListAppointmentTypeProductsGetResponse200Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ListAppointmentTypeProductsGetResponse200Links.from_dict(_links)

        list_appointment_type_products_get_response_200 = cls(
            appointment_type_products=appointment_type_products,
            total_entries=total_entries,
            links=links,
        )

        list_appointment_type_products_get_response_200.additional_properties = d
        return list_appointment_type_products_get_response_200

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
