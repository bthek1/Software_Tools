from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.checkboxes_type import CheckboxesType, check_checkboxes_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.checkboxes_options_item import CheckboxesOptionsItem
    from ..models.checkboxes_other import CheckboxesOther


T = TypeVar("T", bound="Checkboxes")


@_attrs_define
class Checkboxes:
    """
    Attributes:
        token (UUID):  Example: ef4c43ec-105d-489c-88cc-0f3c5f67dc70.
        options (Union[Unset, List['CheckboxesOptionsItem']]):
        other (Union[Unset, CheckboxesOther]):
        archived (Union[None, Unset, bool]):
        name (Union[None, Unset, str]):
        type (Union[Unset, CheckboxesType]):
    """

    token: UUID
    options: Union[Unset, List["CheckboxesOptionsItem"]] = UNSET
    other: Union[Unset, "CheckboxesOther"] = UNSET
    archived: Union[None, Unset, bool] = UNSET
    name: Union[None, Unset, str] = UNSET
    type: Union[Unset, CheckboxesType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token = str(self.token)

        options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        other: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.other, Unset):
            other = self.other.to_dict()

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
        if options is not UNSET:
            field_dict["options"] = options
        if other is not UNSET:
            field_dict["other"] = other
        if archived is not UNSET:
            field_dict["archived"] = archived
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.checkboxes_options_item import CheckboxesOptionsItem
        from ..models.checkboxes_other import CheckboxesOther

        d = src_dict.copy()
        token = UUID(d.pop("token"))

        options = []
        _options = d.pop("options", UNSET)
        for options_item_data in _options or []:
            options_item = CheckboxesOptionsItem.from_dict(options_item_data)

            options.append(options_item)

        _other = d.pop("other", UNSET)
        other: Union[Unset, CheckboxesOther]
        if isinstance(_other, Unset):
            other = UNSET
        else:
            other = CheckboxesOther.from_dict(_other)

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
        type: Union[Unset, CheckboxesType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = check_checkboxes_type(_type)

        checkboxes = cls(
            token=token,
            options=options,
            other=other,
            archived=archived,
            name=name,
            type=type,
        )

        checkboxes.additional_properties = d
        return checkboxes

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
