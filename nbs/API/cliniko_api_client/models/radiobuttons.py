from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.radiobuttons_type import RadiobuttonsType, check_radiobuttons_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.radiobuttons_options_item import RadiobuttonsOptionsItem
    from ..models.radiobuttons_other import RadiobuttonsOther


T = TypeVar("T", bound="Radiobuttons")


@_attrs_define
class Radiobuttons:
    """
    Attributes:
        options (List['RadiobuttonsOptionsItem']):
        name (str):
        token (UUID):  Example: ef4c43ec-105d-489c-88cc-0f3c5f67dc70.
        type (RadiobuttonsType):
        other (Union[Unset, RadiobuttonsOther]):
        archived (Union[Unset, bool]):
    """

    options: List["RadiobuttonsOptionsItem"]
    name: str
    token: UUID
    type: RadiobuttonsType
    other: Union[Unset, "RadiobuttonsOther"] = UNSET
    archived: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        options = []
        for options_item_data in self.options:
            options_item = options_item_data.to_dict()
            options.append(options_item)

        name = self.name

        token = str(self.token)

        type: str = self.type

        other: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.other, Unset):
            other = self.other.to_dict()

        archived = self.archived

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "options": options,
                "name": name,
                "token": token,
                "type": type,
            }
        )
        if other is not UNSET:
            field_dict["other"] = other
        if archived is not UNSET:
            field_dict["archived"] = archived

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.radiobuttons_options_item import RadiobuttonsOptionsItem
        from ..models.radiobuttons_other import RadiobuttonsOther

        d = src_dict.copy()
        options = []
        _options = d.pop("options")
        for options_item_data in _options:
            options_item = RadiobuttonsOptionsItem.from_dict(options_item_data)

            options.append(options_item)

        name = d.pop("name")

        token = UUID(d.pop("token"))

        type = check_radiobuttons_type(d.pop("type"))

        _other = d.pop("other", UNSET)
        other: Union[Unset, RadiobuttonsOther]
        if isinstance(_other, Unset):
            other = UNSET
        else:
            other = RadiobuttonsOther.from_dict(_other)

        archived = d.pop("archived", UNSET)

        radiobuttons = cls(
            options=options,
            name=name,
            token=token,
            type=type,
            other=other,
            archived=archived,
        )

        radiobuttons.additional_properties = d
        return radiobuttons

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
