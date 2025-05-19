from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.referral_source import ReferralSource
from ...models.update_referral_source_patch_body import UpdateReferralSourcePatchBody
from ...types import Response


def _get_kwargs(
    patient_id: str,
    *,
    body: UpdateReferralSourcePatchBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/patients/{patient_id}/referral_source",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ReferralSource]]:
    if response.status_code == 200:
        response_200 = ReferralSource.from_dict(response.json())

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
) -> Response[Union[Any, ReferralSource]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    patient_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateReferralSourcePatchBody,
) -> Response[Union[Any, ReferralSource]]:
    """Update referral source

    Args:
        patient_id (str):
        body (UpdateReferralSourcePatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ReferralSource]]
    """

    kwargs = _get_kwargs(
        patient_id=patient_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    patient_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateReferralSourcePatchBody,
) -> Optional[Union[Any, ReferralSource]]:
    """Update referral source

    Args:
        patient_id (str):
        body (UpdateReferralSourcePatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ReferralSource]
    """

    return sync_detailed(
        patient_id=patient_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    patient_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateReferralSourcePatchBody,
) -> Response[Union[Any, ReferralSource]]:
    """Update referral source

    Args:
        patient_id (str):
        body (UpdateReferralSourcePatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ReferralSource]]
    """

    kwargs = _get_kwargs(
        patient_id=patient_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    patient_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateReferralSourcePatchBody,
) -> Optional[Union[Any, ReferralSource]]:
    """Update referral source

    Args:
        patient_id (str):
        body (UpdateReferralSourcePatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ReferralSource]
    """

    return (
        await asyncio_detailed(
            patient_id=patient_id,
            client=client,
            body=body,
        )
    ).parsed
