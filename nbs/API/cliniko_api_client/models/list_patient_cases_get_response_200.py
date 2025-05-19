from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_patient_cases_get_response_200_links import ListPatientCasesGetResponse200Links
    from ..models.patient_case import PatientCase


T = TypeVar("T", bound="ListPatientCasesGetResponse200")


@_attrs_define
class ListPatientCasesGetResponse200:
    """
    Attributes:
        patient_cases (Union[Unset, List['PatientCase']]):
        total_entries (Union[Unset, int]):  Example: 1.
        links (Union[Unset, ListPatientCasesGetResponse200Links]):
    """

    patient_cases: Union[Unset, List["PatientCase"]] = UNSET
    total_entries: Union[Unset, int] = UNSET
    links: Union[Unset, "ListPatientCasesGetResponse200Links"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        patient_cases: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.patient_cases, Unset):
            patient_cases = []
            for patient_cases_item_data in self.patient_cases:
                patient_cases_item = patient_cases_item_data.to_dict()
                patient_cases.append(patient_cases_item)

        total_entries = self.total_entries

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if patient_cases is not UNSET:
            field_dict["patient_cases"] = patient_cases
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.list_patient_cases_get_response_200_links import ListPatientCasesGetResponse200Links
        from ..models.patient_case import PatientCase

        d = src_dict.copy()
        patient_cases = []
        _patient_cases = d.pop("patient_cases", UNSET)
        for patient_cases_item_data in _patient_cases or []:
            patient_cases_item = PatientCase.from_dict(patient_cases_item_data)

            patient_cases.append(patient_cases_item)

        total_entries = d.pop("total_entries", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ListPatientCasesGetResponse200Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ListPatientCasesGetResponse200Links.from_dict(_links)

        list_patient_cases_get_response_200 = cls(
            patient_cases=patient_cases,
            total_entries=total_entries,
            links=links,
        )

        list_patient_cases_get_response_200.additional_properties = d
        return list_patient_cases_get_response_200

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
