from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.individual_appointment import IndividualAppointment
    from ..models.list_individual_appointments_get_response_200_links import (
        ListIndividualAppointmentsGetResponse200Links,
    )


T = TypeVar("T", bound="ListIndividualAppointmentsGetResponse200")


@_attrs_define
class ListIndividualAppointmentsGetResponse200:
    """
    Attributes:
        individual_appointments (Union[Unset, List['IndividualAppointment']]):
        total_entries (Union[Unset, int]):  Example: 1.
        links (Union[Unset, ListIndividualAppointmentsGetResponse200Links]):
    """

    individual_appointments: Union[Unset, List["IndividualAppointment"]] = UNSET
    total_entries: Union[Unset, int] = UNSET
    links: Union[Unset, "ListIndividualAppointmentsGetResponse200Links"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        individual_appointments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.individual_appointments, Unset):
            individual_appointments = []
            for individual_appointments_item_data in self.individual_appointments:
                individual_appointments_item = individual_appointments_item_data.to_dict()
                individual_appointments.append(individual_appointments_item)

        total_entries = self.total_entries

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if individual_appointments is not UNSET:
            field_dict["individual_appointments"] = individual_appointments
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.individual_appointment import IndividualAppointment
        from ..models.list_individual_appointments_get_response_200_links import (
            ListIndividualAppointmentsGetResponse200Links,
        )

        d = src_dict.copy()
        individual_appointments = []
        _individual_appointments = d.pop("individual_appointments", UNSET)
        for individual_appointments_item_data in _individual_appointments or []:
            individual_appointments_item = IndividualAppointment.from_dict(individual_appointments_item_data)

            individual_appointments.append(individual_appointments_item)

        total_entries = d.pop("total_entries", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ListIndividualAppointmentsGetResponse200Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ListIndividualAppointmentsGetResponse200Links.from_dict(_links)

        list_individual_appointments_get_response_200 = cls(
            individual_appointments=individual_appointments,
            total_entries=total_entries,
            links=links,
        )

        list_individual_appointments_get_response_200.additional_properties = d
        return list_individual_appointments_get_response_200

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
