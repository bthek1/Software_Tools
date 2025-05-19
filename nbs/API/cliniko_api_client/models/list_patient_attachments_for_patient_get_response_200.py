from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.full_patient_export import FullPatientExport
    from ..models.list_patient_attachments_for_patient_get_response_200_links import (
        ListPatientAttachmentsForPatientGetResponse200Links,
    )
    from ..models.uploaded_patient_attachment import UploadedPatientAttachment


T = TypeVar("T", bound="ListPatientAttachmentsForPatientGetResponse200")


@_attrs_define
class ListPatientAttachmentsForPatientGetResponse200:
    """
    Attributes:
        patient_attachments (Union[Unset, List[Union['FullPatientExport', 'UploadedPatientAttachment']]]):
        total_entries (Union[Unset, int]):  Example: 1.
        links (Union[Unset, ListPatientAttachmentsForPatientGetResponse200Links]):
    """

    patient_attachments: Union[Unset, List[Union["FullPatientExport", "UploadedPatientAttachment"]]] = UNSET
    total_entries: Union[Unset, int] = UNSET
    links: Union[Unset, "ListPatientAttachmentsForPatientGetResponse200Links"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.full_patient_export import FullPatientExport

        patient_attachments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.patient_attachments, Unset):
            patient_attachments = []
            for patient_attachments_item_data in self.patient_attachments:
                patient_attachments_item: Dict[str, Any]
                if isinstance(patient_attachments_item_data, FullPatientExport):
                    patient_attachments_item = patient_attachments_item_data.to_dict()
                else:
                    patient_attachments_item = patient_attachments_item_data.to_dict()

                patient_attachments.append(patient_attachments_item)

        total_entries = self.total_entries

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if patient_attachments is not UNSET:
            field_dict["patient_attachments"] = patient_attachments
        if total_entries is not UNSET:
            field_dict["total_entries"] = total_entries
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.full_patient_export import FullPatientExport
        from ..models.list_patient_attachments_for_patient_get_response_200_links import (
            ListPatientAttachmentsForPatientGetResponse200Links,
        )
        from ..models.uploaded_patient_attachment import UploadedPatientAttachment

        d = src_dict.copy()
        patient_attachments = []
        _patient_attachments = d.pop("patient_attachments", UNSET)
        for patient_attachments_item_data in _patient_attachments or []:

            def _parse_patient_attachments_item(
                data: object,
            ) -> Union["FullPatientExport", "UploadedPatientAttachment"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_patient_attachment_type_0 = FullPatientExport.from_dict(data)

                    return componentsschemas_patient_attachment_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_patient_attachment_type_1 = UploadedPatientAttachment.from_dict(data)

                return componentsschemas_patient_attachment_type_1

            patient_attachments_item = _parse_patient_attachments_item(patient_attachments_item_data)

            patient_attachments.append(patient_attachments_item)

        total_entries = d.pop("total_entries", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ListPatientAttachmentsForPatientGetResponse200Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ListPatientAttachmentsForPatientGetResponse200Links.from_dict(_links)

        list_patient_attachments_for_patient_get_response_200 = cls(
            patient_attachments=patient_attachments,
            total_entries=total_entries,
            links=links,
        )

        list_patient_attachments_for_patient_get_response_200.additional_properties = d
        return list_patient_attachments_for_patient_get_response_200

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
