import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.date_type import DateType, check_date_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="Date")


@_attrs_define
class Date:
    """
    Attributes:
        token (UUID):  Example: ef4c43ec-105d-489c-88cc-0f3c5f67dc70.
        value (Union[Unset, datetime.date]):
        archived (Union[None, Unset, bool]):
        name (Union[None, Unset, str]):
        type (Union[Unset, DateType]):
    """

    token: UUID
    value: Union[Unset, datetime.date] = UNSET
    archived: Union[None, Unset, bool] = UNSET
    name: Union[None, Unset, str] = UNSET
    type: Union[Unset, DateType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token = str(self.token)

        value: Union[Unset, str] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.isoformat()

        archived: Union[None, Unset, bool]
        if isinstance(self.archived, Unset):
            archived = UNSET
        else:
            archived = self.archived

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value
        if archived is not UNSET:
            field_dict["archived"] = archived
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        token = UUID(d.pop("token"))

        _value = d.pop("value", UNSET)
        value: Union[Unset, datetime.date]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = isoparse(_value).date()

        def _parse_archived(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        archived = _parse_archived(d.pop("archived", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        _type = d.pop("type", UNSET)
        type: Union[Unset, DateType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = check_date_type(_type)

        date = cls(
            token=token,
            value=value,
            archived=archived,
            name=name,
            type=type,
        )

        date.additional_properties = d
        return date

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
