from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attendee import Attendee
    from ..models.list_attendees_for_patient_case_get_response_200_links import (
        ListAttendeesForPatientCaseGetResponse200Links,
    )


T = TypeVar("T", bound="ListAttendeesForPatientCaseGetResponse200")


@_attrs_define
class ListAttendeesForPatientCaseGetResponse200:
    """
    Attributes:
        attendees (Union[Unset, List['Attendee']]):
        total_entries (Union[Unset, int]):  Example: 1.
        links (Union[Unset, ListAttendeesForPatientCaseGetResponse200Links]):
    """

    attendees: Union[Unset, List["Attendee"]] = UNSET
    total_entries: Union[Unset, int] = UNSET
    links: Union[Unset, "ListAttendeesForPatientCaseGetResponse200Links"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attendees: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attendees, Unset):
            attendees = []
            for attendees_item_data in self.attendees:
                attendees_item = attendees_item_data.to_dict()
                attendees.append(attendees_item)

        total_entries = self.total_entries

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attendees is not UNSET:
            field_dict["attendees"] = attendees
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attendee import Attendee
        from ..models.list_attendees_for_patient_case_get_response_200_links import (
            ListAttendeesForPatientCaseGetResponse200Links,
        )

        d = src_dict.copy()
        attendees = []
        _attendees = d.pop("attendees", UNSET)
        for attendees_item_data in _attendees or []:
            attendees_item = Attendee.from_dict(attendees_item_data)

            attendees.append(attendees_item)

        total_entries = d.pop("total_entries", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ListAttendeesForPatientCaseGetResponse200Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ListAttendeesForPatientCaseGetResponse200Links.from_dict(_links)

        list_attendees_for_patient_case_get_response_200 = cls(
            attendees=attendees,
            total_entries=total_entries,
            links=links,
        )

        list_attendees_for_patient_case_get_response_200.additional_properties = d
        return list_attendees_for_patient_case_get_response_200

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
