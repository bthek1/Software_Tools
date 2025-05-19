from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attachment_presigned_post_fields_type_0 import AttachmentPresignedPostFieldsType0


T = TypeVar("T", bound="AttachmentPresignedPost")


@_attrs_define
class AttachmentPresignedPost:
    """
    Attributes:
        fields (Union['AttachmentPresignedPostFieldsType0', None, Unset]):
        url (Union[None, Unset, str]):
    """

    fields: Union["AttachmentPresignedPostFieldsType0", None, Unset] = UNSET
    url: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.attachment_presigned_post_fields_type_0 import AttachmentPresignedPostFieldsType0

        fields: Union[Dict[str, Any], None, Unset]
        if isinstance(self.fields, Unset):
            fields = UNSET
        elif isinstance(self.fields, AttachmentPresignedPostFieldsType0):
            fields = self.fields.to_dict()
        else:
            fields = self.fields

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fields is not UNSET:
            field_dict["fields"] = fields
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.attachment_presigned_post_fields_type_0 import AttachmentPresignedPostFieldsType0

        d = src_dict.copy()

        def _parse_fields(data: object) -> Union["AttachmentPresignedPostFieldsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                fields_type_0 = AttachmentPresignedPostFieldsType0.from_dict(data)

                return fields_type_0
            except:  # noqa: E722
                pass
            return cast(Union["AttachmentPresignedPostFieldsType0", None, Unset], data)

        fields = _parse_fields(d.pop("fields", UNSET))

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))

        attachment_presigned_post = cls(
            fields=fields,
            url=url,
        )

        attachment_presigned_post.additional_properties = d
        return attachment_presigned_post

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
