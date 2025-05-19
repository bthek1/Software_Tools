from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.daily_availability import DailyAvailability
    from ..models.list_daily_availabilities_for_practitioner_get_response_200_links import (
        ListDailyAvailabilitiesForPractitionerGetResponse200Links,
    )


T = TypeVar("T", bound="ListDailyAvailabilitiesForPractitionerGetResponse200")


@_attrs_define
class ListDailyAvailabilitiesForPractitionerGetResponse200:
    """
    Attributes:
        daily_availabilities (Union[Unset, List['DailyAvailability']]):
        total_entries (Union[Unset, int]):  Example: 1.
        links (Union[Unset, ListDailyAvailabilitiesForPractitionerGetResponse200Links]):
    """

    daily_availabilities: Union[Unset, List["DailyAvailability"]] = UNSET
    total_entries: Union[Unset, int] = UNSET
    links: Union[Unset, "ListDailyAvailabilitiesForPractitionerGetResponse200Links"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        daily_availabilities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.daily_availabilities, Unset):
            daily_availabilities = []
            for daily_availabilities_item_data in self.daily_availabilities:
                daily_availabilities_item = daily_availabilities_item_data.to_dict()
                daily_availabilities.append(daily_availabilities_item)

        total_entries = self.total_entries

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if daily_availabilities is not UNSET:
            field_dict["daily_availabilities"] = daily_availabilities
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.daily_availability import DailyAvailability
        from ..models.list_daily_availabilities_for_practitioner_get_response_200_links import (
            ListDailyAvailabilitiesForPractitionerGetResponse200Links,
        )

        d = src_dict.copy()
        daily_availabilities = []
        _daily_availabilities = d.pop("daily_availabilities", UNSET)
        for daily_availabilities_item_data in _daily_availabilities or []:
            daily_availabilities_item = DailyAvailability.from_dict(daily_availabilities_item_data)

            daily_availabilities.append(daily_availabilities_item)

        total_entries = d.pop("total_entries", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ListDailyAvailabilitiesForPractitionerGetResponse200Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ListDailyAvailabilitiesForPractitionerGetResponse200Links.from_dict(_links)

        list_daily_availabilities_for_practitioner_get_response_200 = cls(
            daily_availabilities=daily_availabilities,
            total_entries=total_entries,
            links=links,
        )

        list_daily_availabilities_for_practitioner_get_response_200.additional_properties = d
        return list_daily_availabilities_for_practitioner_get_response_200

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
