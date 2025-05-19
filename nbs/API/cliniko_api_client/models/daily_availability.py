import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.daily_availability_day_of_week import DailyAvailabilityDayOfWeek, check_daily_availability_day_of_week
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.daily_availability_availabilities_type_0_item import DailyAvailabilityAvailabilitiesType0Item
    from ..models.daily_availability_business import DailyAvailabilityBusiness
    from ..models.daily_availability_links import DailyAvailabilityLinks
    from ..models.daily_availability_practitioner import DailyAvailabilityPractitioner


T = TypeVar("T", bound="DailyAvailability")


@_attrs_define
class DailyAvailability:
    """
    Attributes:
        availabilities (Union[List['DailyAvailabilityAvailabilitiesType0Item'], None, Unset]):
        business (Union[Unset, DailyAvailabilityBusiness]):
        created_at (Union[Unset, datetime.datetime]):
        day_of_week (Union[Unset, DailyAvailabilityDayOfWeek]):
        id (Union[Unset, str]):
        links (Union[Unset, DailyAvailabilityLinks]):
        practitioner (Union[Unset, DailyAvailabilityPractitioner]):
        time_zone (Union[None, Unset, str]): See: [supported time zones](/developer-
            portal/guides/time_zone_support/#accepted-values-for-time_zone) Example: Melbourne.
        time_zone_identifier (Union[None, Unset, str]): See: [supported time zone identifiers](/developer-
            portal/guides/time_zone_support/#accepted-values-for-time_zone_identifier) Example: Australia/Melbourne.
        updated_at (Union[Unset, datetime.datetime]):
    """

    availabilities: Union[List["DailyAvailabilityAvailabilitiesType0Item"], None, Unset] = UNSET
    business: Union[Unset, "DailyAvailabilityBusiness"] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    day_of_week: Union[Unset, DailyAvailabilityDayOfWeek] = UNSET
    id: Union[Unset, str] = UNSET
    links: Union[Unset, "DailyAvailabilityLinks"] = UNSET
    practitioner: Union[Unset, "DailyAvailabilityPractitioner"] = UNSET
    time_zone: Union[None, Unset, str] = UNSET
    time_zone_identifier: Union[None, Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        availabilities: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.availabilities, Unset):
            availabilities = UNSET
        elif isinstance(self.availabilities, list):
            availabilities = []
            for availabilities_type_0_item_data in self.availabilities:
                availabilities_type_0_item = availabilities_type_0_item_data.to_dict()
                availabilities.append(availabilities_type_0_item)

        else:
            availabilities = self.availabilities

        business: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.business, Unset):
            business = self.business.to_dict()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        day_of_week: Union[Unset, int] = UNSET
        if not isinstance(self.day_of_week, Unset):
            day_of_week = self.day_of_week

        id = self.id

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        practitioner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.practitioner, Unset):
            practitioner = self.practitioner.to_dict()

        time_zone: Union[None, Unset, str]
        if isinstance(self.time_zone, Unset):
            time_zone = UNSET
        else:
            time_zone = self.time_zone

        time_zone_identifier: Union[None, Unset, str]
        if isinstance(self.time_zone_identifier, Unset):
            time_zone_identifier = UNSET
        else:
            time_zone_identifier = self.time_zone_identifier

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if availabilities is not UNSET:
            field_dict["availabilities"] = availabilities
        if business is not UNSET:
            field_dict["business"] = business
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if day_of_week is not UNSET:
            field_dict["day_of_week"] = day_of_week
        if id is not UNSET:
            field_dict["id"] = id
        if links is not UNSET:
            field_dict["links"] = links
        if practitioner is not UNSET:
            field_dict["practitioner"] = practitioner
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone
        if time_zone_identifier is not UNSET:
            field_dict["time_zone_identifier"] = time_zone_identifier
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.daily_availability_availabilities_type_0_item import DailyAvailabilityAvailabilitiesType0Item
        from ..models.daily_availability_business import DailyAvailabilityBusiness
        from ..models.daily_availability_links import DailyAvailabilityLinks
        from ..models.daily_availability_practitioner import DailyAvailabilityPractitioner

        d = src_dict.copy()

        def _parse_availabilities(data: object) -> Union[List["DailyAvailabilityAvailabilitiesType0Item"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                availabilities_type_0 = []
                _availabilities_type_0 = data
                for availabilities_type_0_item_data in _availabilities_type_0:
                    availabilities_type_0_item = DailyAvailabilityAvailabilitiesType0Item.from_dict(
                        availabilities_type_0_item_data
                    )

                    availabilities_type_0.append(availabilities_type_0_item)

                return availabilities_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["DailyAvailabilityAvailabilitiesType0Item"], None, Unset], data)

        availabilities = _parse_availabilities(d.pop("availabilities", UNSET))

        _business = d.pop("business", UNSET)
        business: Union[Unset, DailyAvailabilityBusiness]
        if isinstance(_business, Unset):
            business = UNSET
        else:
            business = DailyAvailabilityBusiness.from_dict(_business)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _day_of_week = d.pop("day_of_week", UNSET)
        day_of_week: Union[Unset, DailyAvailabilityDayOfWeek]
        if isinstance(_day_of_week, Unset):
            day_of_week = UNSET
        else:
            day_of_week = check_daily_availability_day_of_week(_day_of_week)

        id = d.pop("id", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, DailyAvailabilityLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = DailyAvailabilityLinks.from_dict(_links)

        _practitioner = d.pop("practitioner", UNSET)
        practitioner: Union[Unset, DailyAvailabilityPractitioner]
        if isinstance(_practitioner, Unset):
            practitioner = UNSET
        else:
            practitioner = DailyAvailabilityPractitioner.from_dict(_practitioner)

        def _parse_time_zone(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        time_zone = _parse_time_zone(d.pop("time_zone", UNSET))

        def _parse_time_zone_identifier(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        time_zone_identifier = _parse_time_zone_identifier(d.pop("time_zone_identifier", UNSET))

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        daily_availability = cls(
            availabilities=availabilities,
            business=business,
            created_at=created_at,
            day_of_week=day_of_week,
            id=id,
            links=links,
            practitioner=practitioner,
            time_zone=time_zone,
            time_zone_identifier=time_zone_identifier,
            updated_at=updated_at,
        )

        daily_availability.additional_properties = d
        return daily_availability

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
