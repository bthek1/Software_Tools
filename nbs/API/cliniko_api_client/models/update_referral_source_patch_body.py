from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateReferralSourcePatchBody")


@_attrs_define
class UpdateReferralSourcePatchBody:
    """
    Attributes:
        notes (Union[None, Unset, str]):
        referrer_id (Union[Unset, str]):  Example: 1.
        referral_source_type_id (Union[Unset, str]): referral source type id Example: 1.
        subcategory (Union[None, Unset, str]):
    """

    notes: Union[None, Unset, str] = UNSET
    referrer_id: Union[Unset, str] = UNSET
    referral_source_type_id: Union[Unset, str] = UNSET
    subcategory: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        referrer_id = self.referrer_id

        referral_source_type_id = self.referral_source_type_id

        subcategory: Union[None, Unset, str]
        if isinstance(self.subcategory, Unset):
            subcategory = UNSET
        else:
            subcategory = self.subcategory

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if notes is not UNSET:
            field_dict["notes"] = notes
        if referrer_id is not UNSET:
            field_dict["referrer_id"] = referrer_id
        if referral_source_type_id is not UNSET:
            field_dict["referral_source_type_id"] = referral_source_type_id
        if subcategory is not UNSET:
            field_dict["subcategory"] = subcategory

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        referrer_id = d.pop("referrer_id", UNSET)

        referral_source_type_id = d.pop("referral_source_type_id", UNSET)

        def _parse_subcategory(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        subcategory = _parse_subcategory(d.pop("subcategory", UNSET))

        update_referral_source_patch_body = cls(
            notes=notes,
            referrer_id=referrer_id,
            referral_source_type_id=referral_source_type_id,
            subcategory=subcategory,
        )

        update_referral_source_patch_body.additional_properties = d
        return update_referral_source_patch_body

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
