from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAttendeePostBody")


@_attrs_define
class CreateAttendeePostBody:
    """
    Attributes:
        booking_id (Union[Unset, str]): booking id Example: 1.
        arrived (Union[None, Unset, bool]):
        notes (Union[None, Unset, str]):
        patient_id (Union[Unset, str]): patient id Example: 1.
        patient_case_id (Union[Unset, str]): patient case id Example: 1.
    """

    booking_id: Union[Unset, str] = UNSET
    arrived: Union[None, Unset, bool] = UNSET
    notes: Union[None, Unset, str] = UNSET
    patient_id: Union[Unset, str] = UNSET
    patient_case_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        booking_id = self.booking_id

        arrived: Union[None, Unset, bool]
        if isinstance(self.arrived, Unset):
            arrived = UNSET
        else:
            arrived = self.arrived

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        patient_id = self.patient_id

        patient_case_id = self.patient_case_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if booking_id is not UNSET:
            field_dict["booking_id"] = booking_id
        if arrived is not UNSET:
            field_dict["arrived"] = arrived
        if notes is not UNSET:
            field_dict["notes"] = notes
        if patient_id is not UNSET:
            field_dict["patient_id"] = patient_id
        if patient_case_id is not UNSET:
            field_dict["patient_case_id"] = patient_case_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        booking_id = d.pop("booking_id", UNSET)

        def _parse_arrived(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        arrived = _parse_arrived(d.pop("arrived", UNSET))

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        patient_id = d.pop("patient_id", UNSET)

        patient_case_id = d.pop("patient_case_id", UNSET)

        create_attendee_post_body = cls(
            booking_id=booking_id,
            arrived=arrived,
            notes=notes,
            patient_id=patient_id,
            patient_case_id=patient_case_id,
        )

        create_attendee_post_body.additional_properties = d
        return create_attendee_post_body

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
