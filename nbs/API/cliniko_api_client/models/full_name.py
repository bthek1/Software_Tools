from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.full_name_patient_field_connection import (
    FullNamePatientFieldConnection,
    check_full_name_patient_field_connection,
)
from ..models.full_name_type import FullNameType, check_full_name_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.full_name_answer import FullNameAnswer
    from ..models.full_name_options import FullNameOptions


T = TypeVar("T", bound="FullName")


@_attrs_define
class FullName:
    """
    Attributes:
        name (str):
        type (FullNameType):
        answer (Union[Unset, FullNameAnswer]):
        options (Union[Unset, FullNameOptions]):
        required (Union[Unset, bool]):
        patient_field_connection (Union[Unset, FullNamePatientFieldConnection]):
    """

    name: str
    type: FullNameType
    answer: Union[Unset, "FullNameAnswer"] = UNSET
    options: Union[Unset, "FullNameOptions"] = UNSET
    required: Union[Unset, bool] = UNSET
    patient_field_connection: Union[Unset, FullNamePatientFieldConnection] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        type: str = self.type

        answer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.answer, Unset):
            answer = self.answer.to_dict()

        options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

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
        if options is not UNSET:
            field_dict["options"] = options
        if required is not UNSET:
            field_dict["required"] = required
        if patient_field_connection is not UNSET:
            field_dict["patient_field_connection"] = patient_field_connection

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.full_name_answer import FullNameAnswer
        from ..models.full_name_options import FullNameOptions

        d = src_dict.copy()
        name = d.pop("name")

        type = check_full_name_type(d.pop("type"))

        _answer = d.pop("answer", UNSET)
        answer: Union[Unset, FullNameAnswer]
        if isinstance(_answer, Unset):
            answer = UNSET
        else:
            answer = FullNameAnswer.from_dict(_answer)

        _options = d.pop("options", UNSET)
        options: Union[Unset, FullNameOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = FullNameOptions.from_dict(_options)

        required = d.pop("required", UNSET)

        _patient_field_connection = d.pop("patient_field_connection", UNSET)
        patient_field_connection: Union[Unset, FullNamePatientFieldConnection]
        if isinstance(_patient_field_connection, Unset):
            patient_field_connection = UNSET
        else:
            patient_field_connection = check_full_name_patient_field_connection(_patient_field_connection)

        full_name = cls(
            name=name,
            type=type,
            answer=answer,
            options=options,
            required=required,
            patient_field_connection=patient_field_connection,
        )

        full_name.additional_properties = d
        return full_name

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
