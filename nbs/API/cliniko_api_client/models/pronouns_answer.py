from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PronounsAnswer")


@_attrs_define
class PronounsAnswer:
    """
    Attributes:
        accusative (str):
        nominative (str):
        predicative_possessive (str):
        pronominal_possessive (str):
        reflexive (str):
    """

    accusative: str
    nominative: str
    predicative_possessive: str
    pronominal_possessive: str
    reflexive: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        accusative = self.accusative

        nominative = self.nominative

        predicative_possessive = self.predicative_possessive

        pronominal_possessive = self.pronominal_possessive

        reflexive = self.reflexive

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accusative": accusative,
                "nominative": nominative,
                "predicative_possessive": predicative_possessive,
                "pronominal_possessive": pronominal_possessive,
                "reflexive": reflexive,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        accusative = d.pop("accusative")

        nominative = d.pop("nominative")

        predicative_possessive = d.pop("predicative_possessive")

        pronominal_possessive = d.pop("pronominal_possessive")

        reflexive = d.pop("reflexive")

        pronouns_answer = cls(
            accusative=accusative,
            nominative=nominative,
            predicative_possessive=predicative_possessive,
            pronominal_possessive=pronominal_possessive,
            reflexive=reflexive,
        )

        pronouns_answer.additional_properties = d
        return pronouns_answer

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
