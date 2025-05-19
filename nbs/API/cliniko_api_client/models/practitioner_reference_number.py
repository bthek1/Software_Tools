import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.practitioner_reference_number_business import PractitionerReferenceNumberBusiness
    from ..models.practitioner_reference_number_links import PractitionerReferenceNumberLinks
    from ..models.practitioner_reference_number_practitioner import PractitionerReferenceNumberPractitioner


T = TypeVar("T", bound="PractitionerReferenceNumber")


@_attrs_define
class PractitionerReferenceNumber:
    """
    Attributes:
        business (Union[Unset, PractitionerReferenceNumberBusiness]):
        created_at (Union[Unset, datetime.datetime]):
        id (Union[Unset, str]):
        links (Union[Unset, PractitionerReferenceNumberLinks]):
        name (Union[None, Unset, str]):
        practitioner (Union[Unset, PractitionerReferenceNumberPractitioner]):
        reference_number (Union[None, Unset, str]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    business: Union[Unset, "PractitionerReferenceNumberBusiness"] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    links: Union[Unset, "PractitionerReferenceNumberLinks"] = UNSET
    name: Union[None, Unset, str] = UNSET
    practitioner: Union[Unset, "PractitionerReferenceNumberPractitioner"] = UNSET
    reference_number: Union[None, Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        business: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.business, Unset):
            business = self.business.to_dict()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        id = self.id

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        practitioner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.practitioner, Unset):
            practitioner = self.practitioner.to_dict()

        reference_number: Union[None, Unset, str]
        if isinstance(self.reference_number, Unset):
            reference_number = UNSET
        else:
            reference_number = self.reference_number

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if business is not UNSET:
            field_dict["business"] = business
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if links is not UNSET:
            field_dict["links"] = links
        if name is not UNSET:
            field_dict["name"] = name
        if practitioner is not UNSET:
            field_dict["practitioner"] = practitioner
        if reference_number is not UNSET:
            field_dict["reference_number"] = reference_number
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.practitioner_reference_number_business import PractitionerReferenceNumberBusiness
        from ..models.practitioner_reference_number_links import PractitionerReferenceNumberLinks
        from ..models.practitioner_reference_number_practitioner import PractitionerReferenceNumberPractitioner

        d = src_dict.copy()
        _business = d.pop("business", UNSET)
        business: Union[Unset, PractitionerReferenceNumberBusiness]
        if isinstance(_business, Unset):
            business = UNSET
        else:
            business = PractitionerReferenceNumberBusiness.from_dict(_business)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        id = d.pop("id", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, PractitionerReferenceNumberLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = PractitionerReferenceNumberLinks.from_dict(_links)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        _practitioner = d.pop("practitioner", UNSET)
        practitioner: Union[Unset, PractitionerReferenceNumberPractitioner]
        if isinstance(_practitioner, Unset):
            practitioner = UNSET
        else:
            practitioner = PractitionerReferenceNumberPractitioner.from_dict(_practitioner)

        def _parse_reference_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reference_number = _parse_reference_number(d.pop("reference_number", UNSET))

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        practitioner_reference_number = cls(
            business=business,
            created_at=created_at,
            id=id,
            links=links,
            name=name,
            practitioner=practitioner,
            reference_number=reference_number,
            updated_at=updated_at,
        )

        practitioner_reference_number.additional_properties = d
        return practitioner_reference_number

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
