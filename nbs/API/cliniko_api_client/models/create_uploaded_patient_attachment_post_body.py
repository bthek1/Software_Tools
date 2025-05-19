from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateUploadedPatientAttachmentPostBody")


@_attrs_define
class CreateUploadedPatientAttachmentPostBody:
    """
    Attributes:
        patient_id (Union[Unset, str]): patient id Example: 1.
        description (Union[None, Unset, str]):
        upload_url (Union[Unset, str]): Must be a presigned URL returned by the [presigned URL upload
            process](/developer-portal/guides/uploading_patient_attachments/) Example: https://cliniko-files-example-
            bucket.s3.amazonaws.com/123/patients/456/attachments/temp/s0m3-w31rd-l0c4t10n-1na-t3mpd1r/the-name-of-the-
            file.txt.
    """

    patient_id: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    upload_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        patient_id = self.patient_id

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        upload_url = self.upload_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if patient_id is not UNSET:
            field_dict["patient_id"] = patient_id
        if description is not UNSET:
            field_dict["description"] = description
        if upload_url is not UNSET:
            field_dict["upload_url"] = upload_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        patient_id = d.pop("patient_id", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        upload_url = d.pop("upload_url", UNSET)

        create_uploaded_patient_attachment_post_body = cls(
            patient_id=patient_id,
            description=description,
            upload_url=upload_url,
        )

        create_uploaded_patient_attachment_post_body.additional_properties = d
        return create_uploaded_patient_attachment_post_body

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
