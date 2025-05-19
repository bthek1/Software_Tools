from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetIndividualAppointmentConflictsGetResponse200Conflicts")


@_attrs_define
class GetIndividualAppointmentConflictsGetResponse200Conflicts:
    """
    Attributes:
        exist (Union[Unset, bool]):
    """

    exist: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        exist = self.exist

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exist is not UNSET:
            field_dict["exist"] = exist

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        exist = d.pop("exist", UNSET)

        get_individual_appointment_conflicts_get_response_200_conflicts = cls(
            exist=exist,
        )

        get_individual_appointment_conflicts_get_response_200_conflicts.additional_properties = d
        return get_individual_appointment_conflicts_get_response_200_conflicts

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
