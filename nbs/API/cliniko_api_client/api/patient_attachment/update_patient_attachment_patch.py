from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.full_patient_export import FullPatientExport
from ...models.full_patient_export_update_body import FullPatientExportUpdateBody
from ...models.uploaded_patient_attachment import UploadedPatientAttachment
from ...models.uploaded_patient_attachment_update_body import UploadedPatientAttachmentUpdateBody
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: Union["FullPatientExportUpdateBody", "UploadedPatientAttachmentUpdateBody"],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/patient_attachments/{id}",
    }

    _body: Dict[str, Any]
    if isinstance(body, FullPatientExportUpdateBody):
        _body = body.to_dict()
    else:
        _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Union["FullPatientExport", "UploadedPatientAttachment"]]]:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Union["FullPatientExport", "UploadedPatientAttachment"]:
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

        response_200 = _parse_response_200(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = cast(Any, None)
        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, Union["FullPatientExport", "UploadedPatientAttachment"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["FullPatientExportUpdateBody", "UploadedPatientAttachmentUpdateBody"],
) -> Response[Union[Any, Union["FullPatientExport", "UploadedPatientAttachment"]]]:
    """Update patient attachment

    Args:
        id (str):
        body (Union['FullPatientExportUpdateBody', 'UploadedPatientAttachmentUpdateBody']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['FullPatientExport', 'UploadedPatientAttachment']]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["FullPatientExportUpdateBody", "UploadedPatientAttachmentUpdateBody"],
) -> Optional[Union[Any, Union["FullPatientExport", "UploadedPatientAttachment"]]]:
    """Update patient attachment

    Args:
        id (str):
        body (Union['FullPatientExportUpdateBody', 'UploadedPatientAttachmentUpdateBody']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Union['FullPatientExport', 'UploadedPatientAttachment']]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["FullPatientExportUpdateBody", "UploadedPatientAttachmentUpdateBody"],
) -> Response[Union[Any, Union["FullPatientExport", "UploadedPatientAttachment"]]]:
    """Update patient attachment

    Args:
        id (str):
        body (Union['FullPatientExportUpdateBody', 'UploadedPatientAttachmentUpdateBody']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Union['FullPatientExport', 'UploadedPatientAttachment']]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["FullPatientExportUpdateBody", "UploadedPatientAttachmentUpdateBody"],
) -> Optional[Union[Any, Union["FullPatientExport", "UploadedPatientAttachment"]]]:
    """Update patient attachment

    Args:
        id (str):
        body (Union['FullPatientExportUpdateBody', 'UploadedPatientAttachmentUpdateBody']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Union['FullPatientExport', 'UploadedPatientAttachment']]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
