from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_group_appointment_conflicts_get_response_200_conflicts import (
        GetGroupAppointmentConflictsGetResponse200Conflicts,
    )


T = TypeVar("T", bound="GetGroupAppointmentConflictsGetResponse200")


@_attrs_define
class GetGroupAppointmentConflictsGetResponse200:
    """
    Attributes:
        conflicts (Union[Unset, GetGroupAppointmentConflictsGetResponse200Conflicts]):
    """

    conflicts: Union[Unset, "GetGroupAppointmentConflictsGetResponse200Conflicts"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        conflicts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.conflicts, Unset):
            conflicts = self.conflicts.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conflicts is not UNSET:
            field_dict["conflicts"] = conflicts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.get_group_appointment_conflicts_get_response_200_conflicts import (
            GetGroupAppointmentConflictsGetResponse200Conflicts,
        )

        d = src_dict.copy()
        _conflicts = d.pop("conflicts", UNSET)
        conflicts: Union[Unset, GetGroupAppointmentConflictsGetResponse200Conflicts]
        if isinstance(_conflicts, Unset):
            conflicts = UNSET
        else:
            conflicts = GetGroupAppointmentConflictsGetResponse200Conflicts.from_dict(_conflicts)

        get_group_appointment_conflicts_get_response_200 = cls(
            conflicts=conflicts,
        )

        get_group_appointment_conflicts_get_response_200.additional_properties = d
        return get_group_appointment_conflicts_get_response_200

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
