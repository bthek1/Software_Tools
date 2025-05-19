from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pronouns_patient_field_connection import (
    PronounsPatientFieldConnection,
    check_pronouns_patient_field_connection,
)
from ..models.pronouns_type import PronounsType, check_pronouns_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pronouns_answer import PronounsAnswer


T = TypeVar("T", bound="Pronouns")


@_attrs_define
class Pronouns:
    """
    Attributes:
        name (str):
        type (PronounsType):
        answer (Union[Unset, PronounsAnswer]):
        required (Union[Unset, bool]):
        patient_field_connection (Union[Unset, PronounsPatientFieldConnection]):
    """

    name: str
    type: PronounsType
    answer: Union[Unset, "PronounsAnswer"] = UNSET
    required: Union[Unset, bool] = UNSET
    patient_field_connection: Union[Unset, PronounsPatientFieldConnection] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        type: str = self.type

        answer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.answer, Unset):
            answer = self.answer.to_dict()

        required = self.required

        patient_field_connection: Union[Unset, str] = UNSET
        if not isinstance(self.patient_field_connection, Unset):
            patient_field_connection = self.patient_field_connection

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type,
            }
        )
        if answer is not UNSET:
            field_dict["answer"] = answer
        if required is not UNSET:
            field_dict["required"] = required
        if patient_field_connection is not UNSET:
            field_dict["patient_field_connection"] = patient_field_connection

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pronouns_answer import PronounsAnswer

        d = src_dict.copy()
        name = d.pop("name")

        type = check_pronouns_type(d.pop("type"))

        _answer = d.pop("answer", UNSET)
        answer: Union[Unset, PronounsAnswer]
        if isinstance(_answer, Unset):
            answer = UNSET
        else:
            answer = PronounsAnswer.from_dict(_answer)

        required = d.pop("required", UNSET)

        _patient_field_connection = d.pop("patient_field_connection", UNSET)
        patient_field_connection: Union[Unset, PronounsPatientFieldConnection]
        if isinstance(_patient_field_connection, Unset):
            patient_field_connection = UNSET
        else:
            patient_field_connection = check_pronouns_patient_field_connection(_patient_field_connection)

        pronouns = cls(
            name=name,
            type=type,
            answer=answer,
            required=required,
            patient_field_connection=patient_field_connection,
        )

        pronouns.additional_properties = d
        return pronouns

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
