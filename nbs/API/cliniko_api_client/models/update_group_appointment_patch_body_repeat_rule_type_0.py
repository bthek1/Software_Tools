from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_group_appointment_patch_body_repeat_rule_type_0_repeat_type import (
    UpdateGroupAppointmentPatchBodyRepeatRuleType0RepeatType,
    check_update_group_appointment_patch_body_repeat_rule_type_0_repeat_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateGroupAppointmentPatchBodyRepeatRuleType0")


@_attrs_define
class UpdateGroupAppointmentPatchBodyRepeatRuleType0:
    """
    Attributes:
        number_of_repeats (Union[None, Unset, int]):
        repeat_type (Union[Unset, UpdateGroupAppointmentPatchBodyRepeatRuleType0RepeatType]):
        repeating_interval (Union[None, Unset, int]):
    """

    number_of_repeats: Union[None, Unset, int] = UNSET
    repeat_type: Union[Unset, UpdateGroupAppointmentPatchBodyRepeatRuleType0RepeatType] = UNSET
    repeating_interval: Union[None, Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        number_of_repeats: Union[None, Unset, int]
        if isinstance(self.number_of_repeats, Unset):
            number_of_repeats = UNSET
        else:
            number_of_repeats = self.number_of_repeats

        repeat_type: Union[Unset, str] = UNSET
        if not isinstance(self.repeat_type, Unset):
            repeat_type = self.repeat_type

        repeating_interval: Union[None, Unset, int]
        if isinstance(self.repeating_interval, Unset):
            repeating_interval = UNSET
        else:
            repeating_interval = self.repeating_interval

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if number_of_repeats is not UNSET:
            field_dict["number_of_repeats"] = number_of_repeats
        if repeat_type is not UNSET:
            field_dict["repeat_type"] = repeat_type
        if repeating_interval is not UNSET:
            field_dict["repeating_interval"] = repeating_interval

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_number_of_repeats(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        number_of_repeats = _parse_number_of_repeats(d.pop("number_of_repeats", UNSET))

        _repeat_type = d.pop("repeat_type", UNSET)
        repeat_type: Union[Unset, UpdateGroupAppointmentPatchBodyRepeatRuleType0RepeatType]
        if isinstance(_repeat_type, Unset):
            repeat_type = UNSET
        else:
            repeat_type = check_update_group_appointment_patch_body_repeat_rule_type_0_repeat_type(_repeat_type)

        def _parse_repeating_interval(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        repeating_interval = _parse_repeating_interval(d.pop("repeating_interval", UNSET))

        update_group_appointment_patch_body_repeat_rule_type_0 = cls(
            number_of_repeats=number_of_repeats,
            repeat_type=repeat_type,
            repeating_interval=repeating_interval,
        )

        update_group_appointment_patch_body_repeat_rule_type_0.additional_properties = d
        return update_group_appointment_patch_body_repeat_rule_type_0

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
