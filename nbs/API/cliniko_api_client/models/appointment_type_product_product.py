from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.appointment_type_product_product_links import AppointmentTypeProductProductLinks


T = TypeVar("T", bound="AppointmentTypeProductProduct")


@_attrs_define
class AppointmentTypeProductProduct:
    """
    Attributes:
        links (Union[Unset, AppointmentTypeProductProductLinks]):
    """

    links: Union[Unset, "AppointmentTypeProductProductLinks"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.appointment_type_product_product_links import AppointmentTypeProductProductLinks

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, AppointmentTypeProductProductLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = AppointmentTypeProductProductLinks.from_dict(_links)

        appointment_type_product_product = cls(
            links=links,
        )

        appointment_type_product_product.additional_properties = d
        return appointment_type_product_product

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
