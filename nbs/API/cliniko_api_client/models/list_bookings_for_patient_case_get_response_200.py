from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_appointment import GroupAppointment
    from ..models.individual_appointment import IndividualAppointment
    from ..models.list_bookings_for_patient_case_get_response_200_links import (
        ListBookingsForPatientCaseGetResponse200Links,
    )
    from ..models.unavailable_block import UnavailableBlock


T = TypeVar("T", bound="ListBookingsForPatientCaseGetResponse200")


@_attrs_define
class ListBookingsForPatientCaseGetResponse200:
    """
    Attributes:
        bookings (Union[Unset, List[Union['GroupAppointment', 'IndividualAppointment', 'UnavailableBlock']]]):
        total_entries (Union[Unset, int]):  Example: 1.
        links (Union[Unset, ListBookingsForPatientCaseGetResponse200Links]):
    """

    bookings: Union[Unset, List[Union["GroupAppointment", "IndividualAppointment", "UnavailableBlock"]]] = UNSET
    total_entries: Union[Unset, int] = UNSET
    links: Union[Unset, "ListBookingsForPatientCaseGetResponse200Links"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.group_appointment import GroupAppointment
        from ..models.individual_appointment import IndividualAppointment

        bookings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.bookings, Unset):
            bookings = []
            for bookings_item_data in self.bookings:
                bookings_item: Dict[str, Any]
                if isinstance(bookings_item_data, GroupAppointment):
                    bookings_item = bookings_item_data.to_dict()
                elif isinstance(bookings_item_data, IndividualAppointment):
                    bookings_item = bookings_item_data.to_dict()
                else:
                    bookings_item = bookings_item_data.to_dict()

                bookings.append(bookings_item)

        total_entries = self.total_entries

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bookings is not UNSET:
            field_dict["bookings"] = bookings
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.group_appointment import GroupAppointment
        from ..models.individual_appointment import IndividualAppointment
        from ..models.list_bookings_for_patient_case_get_response_200_links import (
            ListBookingsForPatientCaseGetResponse200Links,
        )
        from ..models.unavailable_block import UnavailableBlock

        d = src_dict.copy()
        bookings = []
        _bookings = d.pop("bookings", UNSET)
        for bookings_item_data in _bookings or []:

            def _parse_bookings_item(
                data: object,
            ) -> Union["GroupAppointment", "IndividualAppointment", "UnavailableBlock"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_booking_type_0 = GroupAppointment.from_dict(data)

                    return componentsschemas_booking_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_booking_type_1 = IndividualAppointment.from_dict(data)

                    return componentsschemas_booking_type_1
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_booking_type_2 = UnavailableBlock.from_dict(data)

                return componentsschemas_booking_type_2

            bookings_item = _parse_bookings_item(bookings_item_data)

            bookings.append(bookings_item)

        total_entries = d.pop("total_entries", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ListBookingsForPatientCaseGetResponse200Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ListBookingsForPatientCaseGetResponse200Links.from_dict(_links)

        list_bookings_for_patient_case_get_response_200 = cls(
            bookings=bookings,
            total_entries=total_entries,
            links=links,
        )

        list_bookings_for_patient_case_get_response_200.additional_properties = d
        return list_bookings_for_patient_case_get_response_200

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
