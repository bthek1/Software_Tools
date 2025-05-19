from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.cancel_individual_appointment_patch_body_cancellation_reason import (
    CancelIndividualAppointmentPatchBodyCancellationReason,
    check_cancel_individual_appointment_patch_body_cancellation_reason,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CancelIndividualAppointmentPatchBody")


@_attrs_define
class CancelIndividualAppointmentPatchBody:
    """
    Attributes:
        cancellation_note (Union[None, Unset, str]):
        cancellation_reason (Union[Unset, CancelIndividualAppointmentPatchBodyCancellationReason]): | Enum Value |
            Description |
            |---|---|
            |10|Feeling better|
            |20|Condition worse|
            |30|Sick|
            |40|Away|
            |50|Other|
            |60|Work|
        apply_to_repeats (Union[Unset, bool]):
    """

    cancellation_note: Union[None, Unset, str] = UNSET
    cancellation_reason: Union[Unset, CancelIndividualAppointmentPatchBodyCancellationReason] = UNSET
    apply_to_repeats: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cancellation_note: Union[None, Unset, str]
        if isinstance(self.cancellation_note, Unset):
            cancellation_note = UNSET
        else:
            cancellation_note = self.cancellation_note

        cancellation_reason: Union[Unset, int] = UNSET
        if not isinstance(self.cancellation_reason, Unset):
            cancellation_reason = self.cancellation_reason

        apply_to_repeats = self.apply_to_repeats

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cancellation_note is not UNSET:
            field_dict["cancellation_note"] = cancellation_note
        if cancellation_reason is not UNSET:
            field_dict["cancellation_reason"] = cancellation_reason
        if apply_to_repeats is not UNSET:
            field_dict["apply_to_repeats"] = apply_to_repeats

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_cancellation_note(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cancellation_note = _parse_cancellation_note(d.pop("cancellation_note", UNSET))

        _cancellation_reason = d.pop("cancellation_reason", UNSET)
        cancellation_reason: Union[Unset, CancelIndividualAppointmentPatchBodyCancellationReason]
        if isinstance(_cancellation_reason, Unset):
            cancellation_reason = UNSET
        else:
            cancellation_reason = check_cancel_individual_appointment_patch_body_cancellation_reason(
                _cancellation_reason
            )

        apply_to_repeats = d.pop("apply_to_repeats", UNSET)

        cancel_individual_appointment_patch_body = cls(
            cancellation_note=cancellation_note,
            cancellation_reason=cancellation_reason,
            apply_to_repeats=apply_to_repeats,
        )

        cancel_individual_appointment_patch_body.additional_properties = d
        return cancel_individual_appointment_patch_body

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
