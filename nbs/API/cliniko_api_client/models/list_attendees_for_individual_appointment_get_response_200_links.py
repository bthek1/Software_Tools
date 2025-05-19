from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListAttendeesForIndividualAppointmentGetResponse200Links")


@_attrs_define
class ListAttendeesForIndividualAppointmentGetResponse200Links:
    """
    Attributes:
        self_ (Union[Unset, str]):  Example: https://api.au1.cliniko.com/v1/individual_appointments/1/attendees?page=2.
        previous (Union[Unset, str]):  Example:
            https://api.au1.cliniko.com/v1/individual_appointments/1/attendees?page=1.
        next_ (Union[Unset, str]):  Example: https://api.au1.cliniko.com/v1/individual_appointments/1/attendees?page=3.
    """

    self_: Union[Unset, str] = UNSET
    previous: Union[Unset, str] = UNSET
    next_: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        self_ = self.self_

        previous = self.previous

        next_ = self.next_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if previous is not UNSET:
            field_dict["previous"] = previous
        if next_ is not UNSET:
            field_dict["next"] = next_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        self_ = d.pop("self", UNSET)

        previous = d.pop("previous", UNSET)

        next_ = d.pop("next", UNSET)

        list_attendees_for_individual_appointment_get_response_200_links = cls(
            self_=self_,
            previous=previous,
            next_=next_,
        )

        list_attendees_for_individual_appointment_get_response_200_links.additional_properties = d
        return list_attendees_for_individual_appointment_get_response_200_links

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
