from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckboxesOther")


@_attrs_define
class CheckboxesOther:
    """
    Attributes:
        enabled (Union[None, Unset, bool]):
        archived (Union[None, Unset, bool]):
        selected (Union[Unset, bool]):
        value (Union[Unset, str]):
    """

    enabled: Union[None, Unset, bool] = UNSET
    archived: Union[None, Unset, bool] = UNSET
    selected: Union[Unset, bool] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled: Union[None, Unset, bool]
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        archived: Union[None, Unset, bool]
        if isinstance(self.archived, Unset):
            archived = UNSET
        else:
            archived = self.archived

        selected = self.selected

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if archived is not UNSET:
            field_dict["archived"] = archived
        if selected is not UNSET:
            field_dict["selected"] = selected
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_enabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_archived(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        archived = _parse_archived(d.pop("archived", UNSET))

        selected = d.pop("selected", UNSET)

        value = d.pop("value", UNSET)

        checkboxes_other = cls(
            enabled=enabled,
            archived=archived,
            selected=selected,
            value=value,
        )

        checkboxes_other.additional_properties = d
        return checkboxes_other

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
