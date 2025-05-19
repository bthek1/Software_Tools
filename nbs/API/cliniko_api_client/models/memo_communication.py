import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.memo_communication_category import MemoCommunicationCategory, check_memo_communication_category
from ..models.memo_communication_category_code import (
    MemoCommunicationCategoryCode,
    check_memo_communication_category_code,
)
from ..models.memo_communication_direction_code import (
    MemoCommunicationDirectionCode,
    check_memo_communication_direction_code,
)
from ..models.memo_communication_direction_description import (
    MemoCommunicationDirectionDescription,
    check_memo_communication_direction_description,
)
from ..models.memo_communication_type import MemoCommunicationType, check_memo_communication_type
from ..models.memo_communication_type_code import MemoCommunicationTypeCode, check_memo_communication_type_code
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.memo_communication_links import MemoCommunicationLinks
    from ..models.memo_communication_patient import MemoCommunicationPatient


T = TypeVar("T", bound="MemoCommunication")


@_attrs_define
class MemoCommunication:
    """
    Attributes:
        archived_at (Union[None, Unset, datetime.datetime]):
        category (Union[Unset, MemoCommunicationCategory]):
        category_code (Union[Unset, MemoCommunicationCategoryCode]): | Enum Value | Description |
            |---|---|
            |12|Memo|
        confidential (Union[None, Unset, bool]):
        content (Union[None, Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        direction_code (Union[Unset, MemoCommunicationDirectionCode]): | Enum Value | Description |
            |---|---|
            | 1 | Sent |
            | 2 | Received |
        direction_description (Union[Unset, MemoCommunicationDirectionDescription]):
        from_ (Union[None, Unset, str]):
        id (Union[Unset, str]):
        links (Union[Unset, MemoCommunicationLinks]):
        patient (Union[Unset, MemoCommunicationPatient]):
        to (Union[None, Unset, str]):
        type (Union[Unset, MemoCommunicationType]):
        type_code (Union[Unset, MemoCommunicationTypeCode]): | Enum Value | Description |
            |---|---|
            | 1 | SMS |
            | 2 | Email |
            | 3 | Phone call |
            | 4 | Other |
        updated_at (Union[Unset, datetime.datetime]):
    """

    archived_at: Union[None, Unset, datetime.datetime] = UNSET
    category: Union[Unset, MemoCommunicationCategory] = UNSET
    category_code: Union[Unset, MemoCommunicationCategoryCode] = UNSET
    confidential: Union[None, Unset, bool] = UNSET
    content: Union[None, Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    direction_code: Union[Unset, MemoCommunicationDirectionCode] = UNSET
    direction_description: Union[Unset, MemoCommunicationDirectionDescription] = UNSET
    from_: Union[None, Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    links: Union[Unset, "MemoCommunicationLinks"] = UNSET
    patient: Union[Unset, "MemoCommunicationPatient"] = UNSET
    to: Union[None, Unset, str] = UNSET
    type: Union[Unset, MemoCommunicationType] = UNSET
    type_code: Union[Unset, MemoCommunicationTypeCode] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        archived_at: Union[None, Unset, str]
        if isinstance(self.archived_at, Unset):
            archived_at = UNSET
        elif isinstance(self.archived_at, datetime.datetime):
            archived_at = self.archived_at.isoformat()
        else:
            archived_at = self.archived_at

        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category

        category_code: Union[Unset, int] = UNSET
        if not isinstance(self.category_code, Unset):
            category_code = self.category_code

        confidential: Union[None, Unset, bool]
        if isinstance(self.confidential, Unset):
            confidential = UNSET
        else:
            confidential = self.confidential

        content: Union[None, Unset, str]
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        direction_code: Union[Unset, int] = UNSET
        if not isinstance(self.direction_code, Unset):
            direction_code = self.direction_code

        direction_description: Union[Unset, str] = UNSET
        if not isinstance(self.direction_description, Unset):
            direction_description = self.direction_description

        from_: Union[None, Unset, str]
        if isinstance(self.from_, Unset):
            from_ = UNSET
        else:
            from_ = self.from_

        id = self.id

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        patient: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.patient, Unset):
            patient = self.patient.to_dict()

        to: Union[None, Unset, str]
        if isinstance(self.to, Unset):
            to = UNSET
        else:
            to = self.to

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type

        type_code: Union[Unset, int] = UNSET
        if not isinstance(self.type_code, Unset):
            type_code = self.type_code

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at
        if category is not UNSET:
            field_dict["category"] = category
        if category_code is not UNSET:
            field_dict["category_code"] = category_code
        if confidential is not UNSET:
            field_dict["confidential"] = confidential
        if content is not UNSET:
            field_dict["content"] = content
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if direction_code is not UNSET:
            field_dict["direction_code"] = direction_code
        if direction_description is not UNSET:
            field_dict["direction_description"] = direction_description
        if from_ is not UNSET:
            field_dict["from"] = from_
        if id is not UNSET:
            field_dict["id"] = id
        if links is not UNSET:
            field_dict["links"] = links
        if patient is not UNSET:
            field_dict["patient"] = patient
        if to is not UNSET:
            field_dict["to"] = to
        if type is not UNSET:
            field_dict["type"] = type
        if type_code is not UNSET:
            field_dict["type_code"] = type_code
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.memo_communication_links import MemoCommunicationLinks
        from ..models.memo_communication_patient import MemoCommunicationPatient

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

        _category = d.pop("category", UNSET)
        category: Union[Unset, MemoCommunicationCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = check_memo_communication_category(_category)

        _category_code = d.pop("category_code", UNSET)
        category_code: Union[Unset, MemoCommunicationCategoryCode]
        if isinstance(_category_code, Unset):
            category_code = UNSET
        else:
            category_code = check_memo_communication_category_code(_category_code)

        def _parse_confidential(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        confidential = _parse_confidential(d.pop("confidential", UNSET))

        def _parse_content(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        content = _parse_content(d.pop("content", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _direction_code = d.pop("direction_code", UNSET)
        direction_code: Union[Unset, MemoCommunicationDirectionCode]
        if isinstance(_direction_code, Unset):
            direction_code = UNSET
        else:
            direction_code = check_memo_communication_direction_code(_direction_code)

        _direction_description = d.pop("direction_description", UNSET)
        direction_description: Union[Unset, MemoCommunicationDirectionDescription]
        if isinstance(_direction_description, Unset):
            direction_description = UNSET
        else:
            direction_description = check_memo_communication_direction_description(_direction_description)

        def _parse_from_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        from_ = _parse_from_(d.pop("from", UNSET))

        id = d.pop("id", UNSET)

        _links = d.pop("links", UNSET)
        links: Union[Unset, MemoCommunicationLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = MemoCommunicationLinks.from_dict(_links)

        _patient = d.pop("patient", UNSET)
        patient: Union[Unset, MemoCommunicationPatient]
        if isinstance(_patient, Unset):
            patient = UNSET
        else:
            patient = MemoCommunicationPatient.from_dict(_patient)

        def _parse_to(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        to = _parse_to(d.pop("to", UNSET))

        _type = d.pop("type", UNSET)
        type: Union[Unset, MemoCommunicationType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = check_memo_communication_type(_type)

        _type_code = d.pop("type_code", UNSET)
        type_code: Union[Unset, MemoCommunicationTypeCode]
        if isinstance(_type_code, Unset):
            type_code = UNSET
        else:
            type_code = check_memo_communication_type_code(_type_code)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        memo_communication = cls(
            archived_at=archived_at,
            category=category,
            category_code=category_code,
            confidential=confidential,
            content=content,
            created_at=created_at,
            direction_code=direction_code,
            direction_description=direction_description,
            from_=from_,
            id=id,
            links=links,
            patient=patient,
            to=to,
            type=type,
            type_code=type_code,
            updated_at=updated_at,
        )

        memo_communication.additional_properties = d
        return memo_communication

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
