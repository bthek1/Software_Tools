import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.uploaded_patient_attachment_content_type_0 import UploadedPatientAttachmentContentType0
    from ..models.uploaded_patient_attachment_links import UploadedPatientAttachmentLinks
    from ..models.uploaded_patient_attachment_patient import UploadedPatientAttachmentPatient
    from ..models.uploaded_patient_attachment_user import UploadedPatientAttachmentUser


T = TypeVar("T", bound="UploadedPatientAttachment")


@_attrs_define
class UploadedPatientAttachment:
    """
    Attributes:
        archived_at (Union[None, Unset, datetime.datetime]):
        content (Union['UploadedPatientAttachmentContentType0', None, Unset]):
        content_type (Union[None, Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        description (Union[None, Unset, str]):
        filename (Union[None, Unset, str]):
        id (Union[Unset, str]):
        links (Union[Unset, UploadedPatientAttachmentLinks]):
        patient (Union[Unset, UploadedPatientAttachmentPatient]):
        pinned_at (Union[None, Unset, datetime.datetime]):
        processed_at (Union[None, Unset, datetime.datetime]):
        processing_completed (Union[None, Unset, bool]):
        size (Union[None, Unset, int]):
        updated_at (Union[Unset, datetime.datetime]):
        user (Union[Unset, UploadedPatientAttachmentUser]):
    """

    archived_at: Union[None, Unset, datetime.datetime] = UNSET
    content: Union["UploadedPatientAttachmentContentType0", None, Unset] = UNSET
    content_type: Union[None, Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    description: Union[None, Unset, str] = UNSET
    filename: Union[None, Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    links: Union[Unset, "UploadedPatientAttachmentLinks"] = UNSET
    patient: Union[Unset, "UploadedPatientAttachmentPatient"] = UNSET
    pinned_at: Union[None, Unset, datetime.datetime] = UNSET
    processed_at: Union[None, Unset, datetime.datetime] = UNSET
    processing_completed: Union[None, Unset, bool] = UNSET
    size: Union[None, Unset, int] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    user: Union[Unset, "UploadedPatientAttachmentUser"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.uploaded_patient_attachment_content_type_0 import UploadedPatientAttachmentContentType0

        archived_at: Union[None, Unset, str]
        if isinstance(self.archived_at, Unset):
            archived_at = UNSET
        elif isinstance(self.archived_at, datetime.datetime):
            archived_at = self.archived_at.isoformat()
        else:
            archived_at = self.archived_at

        content: Union[Dict[str, Any], None, Unset]
        if isinstance(self.content, Unset):
            content = UNSET
        elif isinstance(self.content, UploadedPatientAttachmentContentType0):
            content = self.content.to_dict()
        else:
            content = self.content

        content_type: Union[None, Unset, str]
        if isinstance(self.content_type, Unset):
            content_type = UNSET
        else:
            content_type = self.content_type

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        filename: Union[None, Unset, str]
        if isinstance(self.filename, Unset):
            filename = UNSET
        else:
            filename = self.filename

        id = self.id

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        patient: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.patient, Unset):
            patient = self.patient.to_dict()

        pinned_at: Union[None, Unset, str]
        if isinstance(self.pinned_at, Unset):
            pinned_at = UNSET
        elif isinstance(self.pinned_at, datetime.datetime):
            pinned_at = self.pinned_at.isoformat()
        else:
            pinned_at = self.pinned_at

        processed_at: Union[None, Unset, str]
        if isinstance(self.processed_at, Unset):
            processed_at = UNSET
        elif isinstance(self.processed_at, datetime.datetime):
            processed_at = self.processed_at.isoformat()
        else:
            processed_at = self.processed_at

        processing_completed: Union[None, Unset, bool]
        if isinstance(self.processing_completed, Unset):
            processing_completed = UNSET
        else:
            processing_completed = self.processing_completed

        size: Union[None, Unset, int]
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if content is not UNSET:
            field_dict["content"] = content
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if filename is not UNSET:
            field_dict["filename"] = filename
        if id is not UNSET:
            field_dict["id"] = id
        if links is not UNSET:
            field_dict["links"] = links
        if patient is not UNSET:
            field_dict["patient"] = patient
        if pinned_at is not UNSET:
            field_dict["pinned_at"] = pinned_at
        if processed_at is not UNSET:
            field_dict["processed_at"] = processed_at
        if processing_completed is not UNSET:
            field_dict["processing_completed"] = processing_completed
        if size is not UNSET:
            field_dict["size"] = size
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.uploaded_patient_attachment_content_type_0 import UploadedPatientAttachmentContentType0
        from ..models.uploaded_patient_attachment_links import UploadedPatientAttachmentLinks
        from ..models.uploaded_patient_attachment_patient import UploadedPatientAttachmentPatient
        from ..models.uploaded_patient_attachment_user import UploadedPatientAttachmentUser

        d = src_dict.copy()

        def _parse_archived_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                archived_at_type_0 = isoparse(data)

                return archived_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        archived_at = _parse_archived_at(d.pop("archived_at", UNSET))

        def _parse_content(data: object) -> Union["UploadedPatientAttachmentContentType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_0 = UploadedPatientAttachmentContentType0.from_dict(data)

                return content_type_0
            except:  # noqa: E722
                pass
            return cast(Union["UploadedPatientAttachmentContentType0", None, Unset], data)

        content = _parse_content(d.pop("content", UNSET))

        def _parse_content_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        content_type = _parse_content_type(d.pop("content_type", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_filename(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        filename = _parse_filename(d.pop("filename", UNSET))

        id = d.pop("id", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, UploadedPatientAttachmentLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = UploadedPatientAttachmentLinks.from_dict(_links)

        _patient = d.pop("patient", UNSET)
        patient: Union[Unset, UploadedPatientAttachmentPatient]
        if isinstance(_patient, Unset):
            patient = UNSET
        else:
            patient = UploadedPatientAttachmentPatient.from_dict(_patient)

        def _parse_pinned_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pinned_at_type_0 = isoparse(data)

                return pinned_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        pinned_at = _parse_pinned_at(d.pop("pinned_at", UNSET))

        def _parse_processed_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                processed_at_type_0 = isoparse(data)

                return processed_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        processed_at = _parse_processed_at(d.pop("processed_at", UNSET))

        def _parse_processing_completed(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        processing_completed = _parse_processing_completed(d.pop("processing_completed", UNSET))

        def _parse_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        size = _parse_size(d.pop("size", UNSET))

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        _user = d.pop("user", UNSET)
        user: Union[Unset, UploadedPatientAttachmentUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UploadedPatientAttachmentUser.from_dict(_user)

        uploaded_patient_attachment = cls(
            archived_at=archived_at,
            content=content,
            content_type=content_type,
            created_at=created_at,
            description=description,
            filename=filename,
            id=id,
            links=links,
            patient=patient,
            pinned_at=pinned_at,
            processed_at=processed_at,
            processing_completed=processing_completed,
            size=size,
            updated_at=updated_at,
            user=user,
        )

        uploaded_patient_attachment.additional_properties = d
        return uploaded_patient_attachment

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
