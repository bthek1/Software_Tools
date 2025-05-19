import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_group_appointment_patch_body_repeat_rule_type_0 import (
        UpdateGroupAppointmentPatchBodyRepeatRuleType0,
    )


T = TypeVar("T", bound="UpdateGroupAppointmentPatchBody")


@_attrs_define
class UpdateGroupAppointmentPatchBody:
    """
    Attributes:
        appointment_type_id (Union[Unset, str]): appointment type id Example: 1.
        business_id (Union[Unset, str]): business id Example: 1.
        ends_at (Union[Unset, datetime.datetime]): If not provided on create or set to null on update, this will be
            based on the duration of the appointment type.
        max_attendees (Union[Unset, int]): If not provided on create, this will be based on the max_attendees of the
            appointment type.
        notes (Union[None, Unset, str]):
        practitioner_id (Union[Unset, str]): practitioner id Example: 1.
        starts_at (Union[Unset, datetime.datetime]):
        repeat_rule (Union['UpdateGroupAppointmentPatchBodyRepeatRuleType0', None, Unset]):
    """

    appointment_type_id: Union[Unset, str] = UNSET
    business_id: Union[Unset, str] = UNSET
    ends_at: Union[Unset, datetime.datetime] = UNSET
    max_attendees: Union[Unset, int] = UNSET
    notes: Union[None, Unset, str] = UNSET
    practitioner_id: Union[Unset, str] = UNSET
    starts_at: Union[Unset, datetime.datetime] = UNSET
    repeat_rule: Union["UpdateGroupAppointmentPatchBodyRepeatRuleType0", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.update_group_appointment_patch_body_repeat_rule_type_0 import (
            UpdateGroupAppointmentPatchBodyRepeatRuleType0,
        )

        appointment_type_id = self.appointment_type_id

        business_id = self.business_id

        ends_at: Union[Unset, str] = UNSET
        if not isinstance(self.ends_at, Unset):
            ends_at = self.ends_at.isoformat()

        max_attendees = self.max_attendees

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        practitioner_id = self.practitioner_id

        starts_at: Union[Unset, str] = UNSET
        if not isinstance(self.starts_at, Unset):
            starts_at = self.starts_at.isoformat()

        repeat_rule: Union[Dict[str, Any], None, Unset]
        if isinstance(self.repeat_rule, Unset):
            repeat_rule = UNSET
        elif isinstance(self.repeat_rule, UpdateGroupAppointmentPatchBodyRepeatRuleType0):
            repeat_rule = self.repeat_rule.to_dict()
        else:
            repeat_rule = self.repeat_rule

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if appointment_type_id is not UNSET:
            field_dict["appointment_type_id"] = appointment_type_id
        if business_id is not UNSET:
            field_dict["business_id"] = business_id
        if ends_at is not UNSET:
            field_dict["ends_at"] = ends_at
        if max_attendees is not UNSET:
            field_dict["max_attendees"] = max_attendees
        if notes is not UNSET:
            field_dict["notes"] = notes
        if practitioner_id is not UNSET:
            field_dict["practitioner_id"] = practitioner_id
        if starts_at is not UNSET:
            field_dict["starts_at"] = starts_at
        if repeat_rule is not UNSET:
            field_dict["repeat_rule"] = repeat_rule

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.update_group_appointment_patch_body_repeat_rule_type_0 import (
            UpdateGroupAppointmentPatchBodyRepeatRuleType0,
        )

        d = src_dict.copy()
        appointment_type_id = d.pop("appointment_type_id", UNSET)

        business_id = d.pop("business_id", UNSET)

        _ends_at = d.pop("ends_at", UNSET)
        ends_at: Union[Unset, datetime.datetime]
        if isinstance(_ends_at, Unset):
            ends_at = UNSET
        else:
            ends_at = isoparse(_ends_at)

        max_attendees = d.pop("max_attendees", UNSET)

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        practitioner_id = d.pop("practitioner_id", UNSET)

        _starts_at = d.pop("starts_at", UNSET)
        starts_at: Union[Unset, datetime.datetime]
        if isinstance(_starts_at, Unset):
            starts_at = UNSET
        else:
            starts_at = isoparse(_starts_at)

        def _parse_repeat_rule(data: object) -> Union["UpdateGroupAppointmentPatchBodyRepeatRuleType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                repeat_rule_type_0 = UpdateGroupAppointmentPatchBodyRepeatRuleType0.from_dict(data)

                return repeat_rule_type_0
            except:  # noqa: E722
                pass
            return cast(Union["UpdateGroupAppointmentPatchBodyRepeatRuleType0", None, Unset], data)

        repeat_rule = _parse_repeat_rule(d.pop("repeat_rule", UNSET))

        update_group_appointment_patch_body = cls(
            appointment_type_id=appointment_type_id,
            business_id=business_id,
            ends_at=ends_at,
            max_attendees=max_attendees,
            notes=notes,
            practitioner_id=practitioner_id,
            starts_at=starts_at,
            repeat_rule=repeat_rule,
        )

        update_group_appointment_patch_body.additional_properties = d
        return update_group_appointment_patch_body

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
