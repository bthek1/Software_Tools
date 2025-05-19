from typing import Literal, Set, cast

AttachmentPresignedPostFieldsType0Acl = Literal["private"]

ATTACHMENT_PRESIGNED_POST_FIELDS_TYPE_0_ACL_VALUES: Set[AttachmentPresignedPostFieldsType0Acl] = {
    "private",
}


def check_attachment_presigned_post_fields_type_0_acl(value: str) -> AttachmentPresignedPostFieldsType0Acl:
    if value in ATTACHMENT_PRESIGNED_POST_FIELDS_TYPE_0_ACL_VALUES:
        return cast(AttachmentPresignedPostFieldsType0Acl, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ATTACHMENT_PRESIGNED_POST_FIELDS_TYPE_0_ACL_VALUES!r}"
    )
