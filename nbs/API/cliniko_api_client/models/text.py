from typing import Any, Dict, List, Type, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.text_type import TextType, check_text_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="Text")


@_attrs_define
class Text:
    """
    Attributes:
        name (str):
        token (UUID):  Example: ef4c43ec-105d-489c-88cc-0f3c5f67dc70.
        type (TextType):
        archived (Union[Unset, bool]):
    """

    name: str
    token: UUID
    type: TextType
    archived: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        token = str(self.token)

        type: str = self.type

        archived = self.archived

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "token": token,
                "type": type,
            }
        )
        if archived is not UNSET:
            field_dict["archived"] = archived

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        token = UUID(d.pop("token"))

        type = check_text_type(d.pop("type"))

        archived = d.pop("archived", UNSET)

        text = cls(
            name=name,
            token=token,
            type=type,
            archived=archived,
        )

        text.additional_properties = d
        return text

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
