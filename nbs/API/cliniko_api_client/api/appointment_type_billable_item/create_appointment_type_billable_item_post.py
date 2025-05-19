from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.appointment_type_billable_item import AppointmentTypeBillableItem
from ...models.create_appointment_type_billable_item_post_body import CreateAppointmentTypeBillableItemPostBody
from ...types import Response


def _get_kwargs(
    *,
    body: CreateAppointmentTypeBillableItemPostBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/appointment_type_billable_items",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, AppointmentTypeBillableItem]]:
    if response.status_code == 201:
        response_201 = AppointmentTypeBillableItem.from_dict(response.json())

        return response_201
    if response.status_code == 422:
        response_422 = cast(Any, None)
        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, AppointmentTypeBillableItem]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateAppointmentTypeBillableItemPostBody,
) -> Response[Union[Any, AppointmentTypeBillableItem]]:
    """Create appointment type billable item

    Args:
        body (CreateAppointmentTypeBillableItemPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AppointmentTypeBillableItem]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateAppointmentTypeBillableItemPostBody,
) -> Optional[Union[Any, AppointmentTypeBillableItem]]:
    """Create appointment type billable item

    Args:
        body (CreateAppointmentTypeBillableItemPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AppointmentTypeBillableItem]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateAppointmentTypeBillableItemPostBody,
) -> Response[Union[Any, AppointmentTypeBillableItem]]:
    """Create appointment type billable item

    Args:
        body (CreateAppointmentTypeBillableItemPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AppointmentTypeBillableItem]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateAppointmentTypeBillableItemPostBody,
) -> Optional[Union[Any, AppointmentTypeBillableItem]]:
    """Create appointment type billable item

    Args:
        body (CreateAppointmentTypeBillableItemPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AppointmentTypeBillableItem]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
