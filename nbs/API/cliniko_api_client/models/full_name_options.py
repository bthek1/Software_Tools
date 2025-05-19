from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FullNameOptions")


@_attrs_define
class FullNameOptions:
    """
    Attributes:
        title_enabled (Union[Unset, bool]):
        preferred_first_name_enabled (Union[Unset, bool]):
    """

    title_enabled: Union[Unset, bool] = UNSET
    preferred_first_name_enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title_enabled = self.title_enabled

        preferred_first_name_enabled = self.preferred_first_name_enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title_enabled is not UNSET:
            field_dict["title_enabled"] = title_enabled
        if preferred_first_name_enabled is not UNSET:
            field_dict["preferred_first_name_enabled"] = preferred_first_name_enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title_enabled = d.pop("title_enabled", UNSET)

        preferred_first_name_enabled = d.pop("preferred_first_name_enabled", UNSET)

        full_name_options = cls(
            title_enabled=title_enabled,
            preferred_first_name_enabled=preferred_first_name_enabled,
        )

        full_name_options.additional_properties = d
        return full_name_options

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
