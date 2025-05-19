from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.appointment_type_billable_item import AppointmentTypeBillableItem
from ...models.update_appointment_type_billable_item_patch_body import UpdateAppointmentTypeBillableItemPatchBody
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: UpdateAppointmentTypeBillableItemPatchBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/appointment_type_billable_items/{id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, AppointmentTypeBillableItem]]:
    if response.status_code == 200:
        response_200 = AppointmentTypeBillableItem.from_dict(response.json())

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
) -> Response[Union[Any, AppointmentTypeBillableItem]]:
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
    body: UpdateAppointmentTypeBillableItemPatchBody,
) -> Response[Union[Any, AppointmentTypeBillableItem]]:
    """Update appointment type billable item

    Args:
        id (str):
        body (UpdateAppointmentTypeBillableItemPatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AppointmentTypeBillableItem]]
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
    body: UpdateAppointmentTypeBillableItemPatchBody,
) -> Optional[Union[Any, AppointmentTypeBillableItem]]:
    """Update appointment type billable item

    Args:
        id (str):
        body (UpdateAppointmentTypeBillableItemPatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AppointmentTypeBillableItem]
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
    body: UpdateAppointmentTypeBillableItemPatchBody,
) -> Response[Union[Any, AppointmentTypeBillableItem]]:
    """Update appointment type billable item

    Args:
        id (str):
        body (UpdateAppointmentTypeBillableItemPatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AppointmentTypeBillableItem]]
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
    body: UpdateAppointmentTypeBillableItemPatchBody,
) -> Optional[Union[Any, AppointmentTypeBillableItem]]:
    """Update appointment type billable item

    Args:
        id (str):
        body (UpdateAppointmentTypeBillableItemPatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AppointmentTypeBillableItem]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
