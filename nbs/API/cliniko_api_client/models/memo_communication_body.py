from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.memo_communication_body_category_code import (
    MemoCommunicationBodyCategoryCode,
    check_memo_communication_body_category_code,
)
from ..models.memo_communication_body_direction_code import (
    MemoCommunicationBodyDirectionCode,
    check_memo_communication_body_direction_code,
)
from ..models.memo_communication_body_type_code import (
    MemoCommunicationBodyTypeCode,
    check_memo_communication_body_type_code,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="MemoCommunicationBody")


@_attrs_define
class MemoCommunicationBody:
    """
    Attributes:
        category_code (Union[Unset, MemoCommunicationBodyCategoryCode]): | Enum Value | Description |
            |---|---|
            |12|Memo|
        confidential (Union[None, Unset, bool]):
        content (Union[None, Unset, str]):
        direction_code (Union[Unset, MemoCommunicationBodyDirectionCode]): | Enum Value | Description |
            |---|---|
            | 1 | Sent |
            | 2 | Received |
        from_ (Union[None, Unset, str]):
        patient_id (Union[Unset, str]): patient id Example: 1.
        to (Union[None, Unset, str]):
        type_code (Union[Unset, MemoCommunicationBodyTypeCode]): | Enum Value | Description |
            |---|---|
            | 1 | SMS |
            | 2 | Email |
            | 3 | Phone call |
            | 4 | Other |
    """

    category_code: Union[Unset, MemoCommunicationBodyCategoryCode] = UNSET
    confidential: Union[None, Unset, bool] = UNSET
    content: Union[None, Unset, str] = UNSET
    direction_code: Union[Unset, MemoCommunicationBodyDirectionCode] = UNSET
    from_: Union[None, Unset, str] = UNSET
    patient_id: Union[Unset, str] = UNSET
    to: Union[None, Unset, str] = UNSET
    type_code: Union[Unset, MemoCommunicationBodyTypeCode] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category_code: Union[Unset, int] = UNSET
        if not isinstance(self.category_code, Unset):
            category_code = self.category_code

        confidential: Union[None, Unset, bool]
        if isinstance(self.confidential, Unset):
            confidential = UNSET
        else:
            confidential = self.confidential

        content: Union[None, Unset, str]
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        direction_code: Union[Unset, int] = UNSET
        if not isinstance(self.direction_code, Unset):
            direction_code = self.direction_code

        from_: Union[None, Unset, str]
        if isinstance(self.from_, Unset):
            from_ = UNSET
        else:
            from_ = self.from_

        patient_id = self.patient_id

        to: Union[None, Unset, str]
        if isinstance(self.to, Unset):
            to = UNSET
        else:
            to = self.to

        type_code: Union[Unset, int] = UNSET
        if not isinstance(self.type_code, Unset):
            type_code = self.type_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category_code is not UNSET:
            field_dict["category_code"] = category_code
        if confidential is not UNSET:
            field_dict["confidential"] = confidential
        if content is not UNSET:
            field_dict["content"] = content
        if direction_code is not UNSET:
            field_dict["direction_code"] = direction_code
        if from_ is not UNSET:
            field_dict["from"] = from_
        if patient_id is not UNSET:
            field_dict["patient_id"] = patient_id
        if to is not UNSET:
            field_dict["to"] = to
        if type_code is not UNSET:
            field_dict["type_code"] = type_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _category_code = d.pop("category_code", UNSET)
        category_code: Union[Unset, MemoCommunicationBodyCategoryCode]
        if isinstance(_category_code, Unset):
            category_code = UNSET
        else:
            category_code = check_memo_communication_body_category_code(_category_code)

        def _parse_confidential(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        confidential = _parse_confidential(d.pop("confidential", UNSET))

        def _parse_content(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        content = _parse_content(d.pop("content", UNSET))

        _direction_code = d.pop("direction_code", UNSET)
        direction_code: Union[Unset, MemoCommunicationBodyDirectionCode]
        if isinstance(_direction_code, Unset):
            direction_code = UNSET
        else:
            direction_code = check_memo_communication_body_direction_code(_direction_code)

        def _parse_from_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        from_ = _parse_from_(d.pop("from", UNSET))

        patient_id = d.pop("patient_id", UNSET)

        def _parse_to(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        to = _parse_to(d.pop("to", UNSET))

        _type_code = d.pop("type_code", UNSET)
        type_code: Union[Unset, MemoCommunicationBodyTypeCode]
        if isinstance(_type_code, Unset):
            type_code = UNSET
        else:
            type_code = check_memo_communication_body_type_code(_type_code)

        memo_communication_body = cls(
            category_code=category_code,
            confidential=confidential,
            content=content,
            direction_code=direction_code,
            from_=from_,
            patient_id=patient_id,
            to=to,
            type_code=type_code,
        )

        memo_communication_body.additional_properties = d
        return memo_communication_body

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
