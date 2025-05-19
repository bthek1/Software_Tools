from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_appointment import GroupAppointment
    from ..models.list_group_appointments_get_response_200_links import ListGroupAppointmentsGetResponse200Links


T = TypeVar("T", bound="ListGroupAppointmentsGetResponse200")


@_attrs_define
class ListGroupAppointmentsGetResponse200:
    """
    Attributes:
        group_appointments (Union[Unset, List['GroupAppointment']]):
        total_entries (Union[Unset, int]):  Example: 1.
        links (Union[Unset, ListGroupAppointmentsGetResponse200Links]):
    """

    group_appointments: Union[Unset, List["GroupAppointment"]] = UNSET
    total_entries: Union[Unset, int] = UNSET
    links: Union[Unset, "ListGroupAppointmentsGetResponse200Links"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group_appointments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.group_appointments, Unset):
            group_appointments = []
            for group_appointments_item_data in self.group_appointments:
                group_appointments_item = group_appointments_item_data.to_dict()
                group_appointments.append(group_appointments_item)

        total_entries = self.total_entries

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_appointments is not UNSET:
            field_dict["group_appointments"] = group_appointments
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.group_appointment import GroupAppointment
        from ..models.list_group_appointments_get_response_200_links import ListGroupAppointmentsGetResponse200Links

        d = src_dict.copy()
        group_appointments = []
        _group_appointments = d.pop("group_appointments", UNSET)
        for group_appointments_item_data in _group_appointments or []:
            group_appointments_item = GroupAppointment.from_dict(group_appointments_item_data)

            group_appointments.append(group_appointments_item)

        total_entries = d.pop("total_entries", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ListGroupAppointmentsGetResponse200Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ListGroupAppointmentsGetResponse200Links.from_dict(_links)

        list_group_appointments_get_response_200 = cls(
            group_appointments=group_appointments,
            total_entries=total_entries,
            links=links,
        )

        list_group_appointments_get_response_200.additional_properties = d
        return list_group_appointments_get_response_200

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
