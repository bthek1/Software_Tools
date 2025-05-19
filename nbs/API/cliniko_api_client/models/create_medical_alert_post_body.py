from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateMedicalAlertPostBody")


@_attrs_define
class CreateMedicalAlertPostBody:
    """
    Attributes:
        name (Union[Unset, str]):
        patient_id (Union[Unset, str]): patient id Example: 1.
    """

    name: Union[Unset, str] = UNSET
    patient_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        patient_id = self.patient_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if patient_id is not UNSET:
            field_dict["patient_id"] = patient_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        patient_id = d.pop("patient_id", UNSET)

        create_medical_alert_post_body = cls(
            name=name,
            patient_id=patient_id,
        )

        create_medical_alert_post_body.additional_properties = d
        return create_medical_alert_post_body

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
