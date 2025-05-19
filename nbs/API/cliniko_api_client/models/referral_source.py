import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.referral_source_referrer_type import ReferralSourceReferrerType, check_referral_source_referrer_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.referral_source_links import ReferralSourceLinks
    from ..models.referral_source_patient import ReferralSourcePatient
    from ..models.referral_source_referral_source_type import ReferralSourceReferralSourceType
    from ..models.referral_source_referrer_type_0 import ReferralSourceReferrerType0


T = TypeVar("T", bound="ReferralSource")


@_attrs_define
class ReferralSource:
    """
    Attributes:
        created_at (Union[Unset, datetime.datetime]):
        id (Union[Unset, str]):
        links (Union[Unset, ReferralSourceLinks]):
        notes (Union[None, Unset, str]):
        patient (Union[Unset, ReferralSourcePatient]):
        referral_source_type (Union[Unset, ReferralSourceReferralSourceType]):
        referrer (Union['ReferralSourceReferrerType0', None, Unset]):
        referrer_type (Union[Unset, ReferralSourceReferrerType]):
        subcategory (Union[None, Unset, str]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    links: Union[Unset, "ReferralSourceLinks"] = UNSET
    notes: Union[None, Unset, str] = UNSET
    patient: Union[Unset, "ReferralSourcePatient"] = UNSET
    referral_source_type: Union[Unset, "ReferralSourceReferralSourceType"] = UNSET
    referrer: Union["ReferralSourceReferrerType0", None, Unset] = UNSET
    referrer_type: Union[Unset, ReferralSourceReferrerType] = UNSET
    subcategory: Union[None, Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.referral_source_referrer_type_0 import ReferralSourceReferrerType0

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        id = self.id

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        patient: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.patient, Unset):
            patient = self.patient.to_dict()

        referral_source_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.referral_source_type, Unset):
            referral_source_type = self.referral_source_type.to_dict()

        referrer: Union[Dict[str, Any], None, Unset]
        if isinstance(self.referrer, Unset):
            referrer = UNSET
        elif isinstance(self.referrer, ReferralSourceReferrerType0):
            referrer = self.referrer.to_dict()
        else:
            referrer = self.referrer

        referrer_type: Union[Unset, str] = UNSET
        if not isinstance(self.referrer_type, Unset):
            referrer_type = self.referrer_type

        subcategory: Union[None, Unset, str]
        if isinstance(self.subcategory, Unset):
            subcategory = UNSET
        else:
            subcategory = self.subcategory

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if links is not UNSET:
            field_dict["links"] = links
        if notes is not UNSET:
            field_dict["notes"] = notes
        if patient is not UNSET:
            field_dict["patient"] = patient
        if referral_source_type is not UNSET:
            field_dict["referral_source_type"] = referral_source_type
        if referrer is not UNSET:
            field_dict["referrer"] = referrer
        if referrer_type is not UNSET:
            field_dict["referrer_type"] = referrer_type
        if subcategory is not UNSET:
            field_dict["subcategory"] = subcategory
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.referral_source_links import ReferralSourceLinks
        from ..models.referral_source_patient import ReferralSourcePatient
        from ..models.referral_source_referral_source_type import ReferralSourceReferralSourceType
        from ..models.referral_source_referrer_type_0 import ReferralSourceReferrerType0

        d = src_dict.copy()
        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        id = d.pop("id", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ReferralSourceLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ReferralSourceLinks.from_dict(_links)

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        _patient = d.pop("patient", UNSET)
        patient: Union[Unset, ReferralSourcePatient]
        if isinstance(_patient, Unset):
            patient = UNSET
        else:
            patient = ReferralSourcePatient.from_dict(_patient)

        _referral_source_type = d.pop("referral_source_type", UNSET)
        referral_source_type: Union[Unset, ReferralSourceReferralSourceType]
        if isinstance(_referral_source_type, Unset):
            referral_source_type = UNSET
        else:
            referral_source_type = ReferralSourceReferralSourceType.from_dict(_referral_source_type)

        def _parse_referrer(data: object) -> Union["ReferralSourceReferrerType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                referrer_type_0 = ReferralSourceReferrerType0.from_dict(data)

                return referrer_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ReferralSourceReferrerType0", None, Unset], data)

        referrer = _parse_referrer(d.pop("referrer", UNSET))

        _referrer_type = d.pop("referrer_type", UNSET)
        referrer_type: Union[Unset, ReferralSourceReferrerType]
        if isinstance(_referrer_type, Unset):
            referrer_type = UNSET
        else:
            referrer_type = check_referral_source_referrer_type(_referrer_type)

        def _parse_subcategory(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        subcategory = _parse_subcategory(d.pop("subcategory", UNSET))

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        referral_source = cls(
            created_at=created_at,
            id=id,
            links=links,
            notes=notes,
            patient=patient,
            referral_source_type=referral_source_type,
            referrer=referrer,
            referrer_type=referrer_type,
            subcategory=subcategory,
            updated_at=updated_at,
        )

        referral_source.additional_properties = d
        return referral_source

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
