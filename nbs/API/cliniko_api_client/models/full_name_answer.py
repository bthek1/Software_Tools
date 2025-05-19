from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FullNameAnswer")


@_attrs_define
class FullNameAnswer:
    """
    Attributes:
        first_name (str):
        last_name (str):
        title (Union[Unset, str]):
        preferred_first_name (Union[Unset, str]):
    """

    first_name: str
    last_name: str
    title: Union[Unset, str] = UNSET
    preferred_first_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name

        title = self.title

        preferred_first_name = self.preferred_first_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "first_name": first_name,
                "last_name": last_name,
            }
        )
        if title is not UNSET:
            field_dict["title"] = title
        if preferred_first_name is not UNSET:
            field_dict["preferred_first_name"] = preferred_first_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        title = d.pop("title", UNSET)

        preferred_first_name = d.pop("preferred_first_name", UNSET)

        full_name_answer = cls(
            first_name=first_name,
            last_name=last_name,
            title=title,
            preferred_first_name=preferred_first_name,
        )

        full_name_answer.additional_properties = d
        return full_name_answer

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
