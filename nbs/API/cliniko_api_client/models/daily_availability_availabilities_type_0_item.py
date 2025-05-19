from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DailyAvailabilityAvailabilitiesType0Item")


@_attrs_define
class DailyAvailabilityAvailabilitiesType0Item:
    """
    Attributes:
        starts_at (Union[Unset, str]):  Example: 09:00.
        ends_at (Union[Unset, str]):  Example: 13:00.
    """

    starts_at: Union[Unset, str] = UNSET
    ends_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        starts_at = self.starts_at

        ends_at = self.ends_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if starts_at is not UNSET:
            field_dict["starts_at"] = starts_at
        if ends_at is not UNSET:
            field_dict["ends_at"] = ends_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        starts_at = d.pop("starts_at", UNSET)

        ends_at = d.pop("ends_at", UNSET)

        daily_availability_availabilities_type_0_item = cls(
            starts_at=starts_at,
            ends_at=ends_at,
        )

        daily_availability_availabilities_type_0_item.additional_properties = d
        return daily_availability_availabilities_type_0_item

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
