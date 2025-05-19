from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bodycharts_type import BodychartsType, check_bodycharts_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="Bodycharts")


@_attrs_define
class Bodycharts:
    """
    Attributes:
        name (str):
        type (BodychartsType):
        body_chart_ids (Union[Unset, List[str]]):
    """

    name: str
    type: BodychartsType
    body_chart_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        type: str = self.type

        body_chart_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.body_chart_ids, Unset):
            body_chart_ids = self.body_chart_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type,
            }
        )
        if body_chart_ids is not UNSET:
            field_dict["body_chart_ids"] = body_chart_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        type = check_bodycharts_type(d.pop("type"))

        body_chart_ids = cast(List[str], d.pop("body_chart_ids", UNSET))

        bodycharts = cls(
            name=name,
            type=type,
            body_chart_ids=body_chart_ids,
        )

        bodycharts.additional_properties = d
        return bodycharts

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
