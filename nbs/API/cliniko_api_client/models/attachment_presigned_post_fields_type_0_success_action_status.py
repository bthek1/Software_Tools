from typing import Literal, Set, cast

AttachmentPresignedPostFieldsType0SuccessActionStatus = Literal["201"]

ATTACHMENT_PRESIGNED_POST_FIELDS_TYPE_0_SUCCESS_ACTION_STATUS_VALUES: Set[
    AttachmentPresignedPostFieldsType0SuccessActionStatus
] = {
    "201",
}


def check_attachment_presigned_post_fields_type_0_success_action_status(
    value: str,
) -> AttachmentPresignedPostFieldsType0SuccessActionStatus:
    if value in ATTACHMENT_PRESIGNED_POST_FIELDS_TYPE_0_SUCCESS_ACTION_STATUS_VALUES:
        return cast(AttachmentPresignedPostFieldsType0SuccessActionStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ATTACHMENT_PRESIGNED_POST_FIELDS_TYPE_0_SUCCESS_ACTION_STATUS_VALUES!r}"
    )
