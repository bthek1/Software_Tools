from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attachment_presigned_post_fields_type_0_acl import (
    AttachmentPresignedPostFieldsType0Acl,
    check_attachment_presigned_post_fields_type_0_acl,
)
from ..models.attachment_presigned_post_fields_type_0_success_action_status import (
    AttachmentPresignedPostFieldsType0SuccessActionStatus,
    check_attachment_presigned_post_fields_type_0_success_action_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AttachmentPresignedPostFieldsType0")


@_attrs_define
class AttachmentPresignedPostFieldsType0:
    """
    Attributes:
        key (Union[Unset, str]):
        policy (Union[Unset, str]):
        x_amz_credential (Union[Unset, str]):
        x_amz_signature (Union[Unset, str]):
        x_amz_algorithm (Union[Unset, str]):
        success_action_status (Union[Unset, AttachmentPresignedPostFieldsType0SuccessActionStatus]):
        acl (Union[Unset, AttachmentPresignedPostFieldsType0Acl]):
    """

    key: Union[Unset, str] = UNSET
    policy: Union[Unset, str] = UNSET
    x_amz_credential: Union[Unset, str] = UNSET
    x_amz_signature: Union[Unset, str] = UNSET
    x_amz_algorithm: Union[Unset, str] = UNSET
    success_action_status: Union[Unset, AttachmentPresignedPostFieldsType0SuccessActionStatus] = UNSET
    acl: Union[Unset, AttachmentPresignedPostFieldsType0Acl] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key

        policy = self.policy

        x_amz_credential = self.x_amz_credential

        x_amz_signature = self.x_amz_signature

        x_amz_algorithm = self.x_amz_algorithm

        success_action_status: Union[Unset, str] = UNSET
        if not isinstance(self.success_action_status, Unset):
            success_action_status = self.success_action_status

        acl: Union[Unset, str] = UNSET
        if not isinstance(self.acl, Unset):
            acl = self.acl

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if policy is not UNSET:
            field_dict["policy"] = policy
        if x_amz_credential is not UNSET:
            field_dict["x-amz-credential"] = x_amz_credential
        if x_amz_signature is not UNSET:
            field_dict["x-amz-signature"] = x_amz_signature
        if x_amz_algorithm is not UNSET:
            field_dict["x-amz-algorithm"] = x_amz_algorithm
        if success_action_status is not UNSET:
            field_dict["success_action_status"] = success_action_status
        if acl is not UNSET:
            field_dict["acl"] = acl

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key", UNSET)

        policy = d.pop("policy", UNSET)

        x_amz_credential = d.pop("x-amz-credential", UNSET)

        x_amz_signature = d.pop("x-amz-signature", UNSET)

        x_amz_algorithm = d.pop("x-amz-algorithm", UNSET)

        _success_action_status = d.pop("success_action_status", UNSET)
        success_action_status: Union[Unset, AttachmentPresignedPostFieldsType0SuccessActionStatus]
        if isinstance(_success_action_status, Unset):
            success_action_status = UNSET
        else:
            success_action_status = check_attachment_presigned_post_fields_type_0_success_action_status(
                _success_action_status
            )

        _acl = d.pop("acl", UNSET)
        acl: Union[Unset, AttachmentPresignedPostFieldsType0Acl]
        if isinstance(_acl, Unset):
            acl = UNSET
        else:
            acl = check_attachment_presigned_post_fields_type_0_acl(_acl)

        attachment_presigned_post_fields_type_0 = cls(
            key=key,
            policy=policy,
            x_amz_credential=x_amz_credential,
            x_amz_signature=x_amz_signature,
            x_amz_algorithm=x_amz_algorithm,
            success_action_status=success_action_status,
            acl=acl,
        )

        attachment_presigned_post_fields_type_0.additional_properties = d
        return attachment_presigned_post_fields_type_0

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
