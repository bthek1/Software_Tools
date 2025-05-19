import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_next_available_time_get_response_200 import GetNextAvailableTimeGetResponse200
from ...types import UNSET, Response


def _get_kwargs(
    business_id: str,
    practitioner_id: str,
    appointment_type_id: str,
    *,
    from_: datetime.date,
    to: datetime.date,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to = to.isoformat()
    params["to"] = json_to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/businesses/{business_id}/practitioners/{practitioner_id}/appointment_types/{appointment_type_id}/next_available_time",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetNextAvailableTimeGetResponse200]:
    if response.status_code == 200:
        response_200 = GetNextAvailableTimeGetResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetNextAvailableTimeGetResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    business_id: str,
    practitioner_id: str,
    appointment_type_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    from_: datetime.date,
    to: datetime.date,
) -> Response[GetNextAvailableTimeGetResponse200]:
    """Get next available time

    Args:
        business_id (str):  Example: 1.
        practitioner_id (str):  Example: 1.
        appointment_type_id (str):  Example: 1.
        from_ (datetime.date):
        to (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetNextAvailableTimeGetResponse200]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
        practitioner_id=practitioner_id,
        appointment_type_id=appointment_type_id,
        from_=from_,
        to=to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    business_id: str,
    practitioner_id: str,
    appointment_type_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    from_: datetime.date,
    to: datetime.date,
) -> Optional[GetNextAvailableTimeGetResponse200]:
    """Get next available time

    Args:
        business_id (str):  Example: 1.
        practitioner_id (str):  Example: 1.
        appointment_type_id (str):  Example: 1.
        from_ (datetime.date):
        to (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetNextAvailableTimeGetResponse200
    """

    return sync_detailed(
        business_id=business_id,
        practitioner_id=practitioner_id,
        appointment_type_id=appointment_type_id,
        client=client,
        from_=from_,
        to=to,
    ).parsed


async def asyncio_detailed(
    business_id: str,
    practitioner_id: str,
    appointment_type_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    from_: datetime.date,
    to: datetime.date,
) -> Response[GetNextAvailableTimeGetResponse200]:
    """Get next available time

    Args:
        business_id (str):  Example: 1.
        practitioner_id (str):  Example: 1.
        appointment_type_id (str):  Example: 1.
        from_ (datetime.date):
        to (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetNextAvailableTimeGetResponse200]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
        practitioner_id=practitioner_id,
        appointment_type_id=appointment_type_id,
        from_=from_,
        to=to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    business_id: str,
    practitioner_id: str,
    appointment_type_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    from_: datetime.date,
    to: datetime.date,
) -> Optional[GetNextAvailableTimeGetResponse200]:
    """Get next available time

    Args:
        business_id (str):  Example: 1.
        practitioner_id (str):  Example: 1.
        appointment_type_id (str):  Example: 1.
        from_ (datetime.date):
        to (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetNextAvailableTimeGetResponse200
    """

    return (
        await asyncio_detailed(
            business_id=business_id,
            practitioner_id=practitioner_id,
            appointment_type_id=appointment_type_id,
            client=client,
            from_=from_,
            to=to,
        )
    ).parsed
