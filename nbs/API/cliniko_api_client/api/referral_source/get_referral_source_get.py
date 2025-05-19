from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.referral_source import ReferralSource
from ...types import Response


def _get_kwargs(
    patient_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/patients/{patient_id}/referral_source",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ReferralSource]:
    if response.status_code == 200:
        response_200 = ReferralSource.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ReferralSource]:
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
) -> Response[ReferralSource]:
    """Get referral source

    Args:
        patient_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReferralSource]
    """

    kwargs = _get_kwargs(
        patient_id=patient_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    patient_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ReferralSource]:
    """Get referral source

    Args:
        patient_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReferralSource
    """

    return sync_detailed(
        patient_id=patient_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    patient_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ReferralSource]:
    """Get referral source

    Args:
        patient_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ReferralSource]
    """

    kwargs = _get_kwargs(
        patient_id=patient_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    patient_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ReferralSource]:
    """Get referral source

    Args:
        patient_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ReferralSource
    """

    return (
        await asyncio_detailed(
            patient_id=patient_id,
            client=client,
        )
    ).parsed
