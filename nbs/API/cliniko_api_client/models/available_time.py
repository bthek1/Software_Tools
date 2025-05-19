import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AvailableTime")


@_attrs_define
class AvailableTime:
    """
    Attributes:
        appointment_start (Union[Unset, datetime.datetime]):
    """

    appointment_start: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        appointment_start: Union[Unset, str] = UNSET
        if not isinstance(self.appointment_start, Unset):
            appointment_start = self.appointment_start.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if appointment_start is not UNSET:
            field_dict["appointment_start"] = appointment_start

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _appointment_start = d.pop("appointment_start", UNSET)
        appointment_start: Union[Unset, datetime.datetime]
        if isinstance(_appointment_start, Unset):
            appointment_start = UNSET
        else:
            appointment_start = isoparse(_appointment_start)

        available_time = cls(
            appointment_start=appointment_start,
        )

        available_time.additional_properties = d
        return available_time

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
