from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_appointment_type import ServiceAppointmentType
    from ..models.service_business import ServiceBusiness
    from ..models.service_practitioners_type_0_item import ServicePractitionersType0Item


T = TypeVar("T", bound="Service")


@_attrs_define
class Service:
    """
    Attributes:
        appointment_type (Union[Unset, ServiceAppointmentType]):
        business (Union[Unset, ServiceBusiness]):
        practitioners (Union[List['ServicePractitionersType0Item'], None, Unset]):
    """

    appointment_type: Union[Unset, "ServiceAppointmentType"] = UNSET
    business: Union[Unset, "ServiceBusiness"] = UNSET
    practitioners: Union[List["ServicePractitionersType0Item"], None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        appointment_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.appointment_type, Unset):
            appointment_type = self.appointment_type.to_dict()

        business: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.business, Unset):
            business = self.business.to_dict()

        practitioners: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.practitioners, Unset):
            practitioners = UNSET
        elif isinstance(self.practitioners, list):
            practitioners = []
            for practitioners_type_0_item_data in self.practitioners:
                practitioners_type_0_item = practitioners_type_0_item_data.to_dict()
                practitioners.append(practitioners_type_0_item)

        else:
            practitioners = self.practitioners

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if appointment_type is not UNSET:
            field_dict["appointment_type"] = appointment_type
        if business is not UNSET:
            field_dict["business"] = business
        if practitioners is not UNSET:
            field_dict["practitioners"] = practitioners

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.service_appointment_type import ServiceAppointmentType
        from ..models.service_business import ServiceBusiness
        from ..models.service_practitioners_type_0_item import ServicePractitionersType0Item

        d = src_dict.copy()
        _appointment_type = d.pop("appointment_type", UNSET)
        appointment_type: Union[Unset, ServiceAppointmentType]
        if isinstance(_appointment_type, Unset):
            appointment_type = UNSET
        else:
            appointment_type = ServiceAppointmentType.from_dict(_appointment_type)

        _business = d.pop("business", UNSET)
        business: Union[Unset, ServiceBusiness]
        if isinstance(_business, Unset):
            business = UNSET
        else:
            business = ServiceBusiness.from_dict(_business)

        def _parse_practitioners(data: object) -> Union[List["ServicePractitionersType0Item"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                practitioners_type_0 = []
                _practitioners_type_0 = data
                for practitioners_type_0_item_data in _practitioners_type_0:
                    practitioners_type_0_item = ServicePractitionersType0Item.from_dict(practitioners_type_0_item_data)

                    practitioners_type_0.append(practitioners_type_0_item)

                return practitioners_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ServicePractitionersType0Item"], None, Unset], data)

        practitioners = _parse_practitioners(d.pop("practitioners", UNSET))

        service = cls(
            appointment_type=appointment_type,
            business=business,
            practitioners=practitioners,
        )

        service.additional_properties = d
        return service

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
