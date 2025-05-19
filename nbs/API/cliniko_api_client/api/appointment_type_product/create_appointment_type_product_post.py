from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.appointment_type_product import AppointmentTypeProduct
from ...models.create_appointment_type_product_post_body import CreateAppointmentTypeProductPostBody
from ...types import Response


def _get_kwargs(
    *,
    body: CreateAppointmentTypeProductPostBody,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/appointment_type_products",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, AppointmentTypeProduct]]:
    if response.status_code == 201:
        response_201 = AppointmentTypeProduct.from_dict(response.json())

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
) -> Response[Union[Any, AppointmentTypeProduct]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateAppointmentTypeProductPostBody,
) -> Response[Union[Any, AppointmentTypeProduct]]:
    """Create appointment type product

    Args:
        body (CreateAppointmentTypeProductPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AppointmentTypeProduct]]
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
    body: CreateAppointmentTypeProductPostBody,
) -> Optional[Union[Any, AppointmentTypeProduct]]:
    """Create appointment type product

    Args:
        body (CreateAppointmentTypeProductPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AppointmentTypeProduct]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateAppointmentTypeProductPostBody,
) -> Response[Union[Any, AppointmentTypeProduct]]:
    """Create appointment type product

    Args:
        body (CreateAppointmentTypeProductPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AppointmentTypeProduct]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateAppointmentTypeProductPostBody,
) -> Optional[Union[Any, AppointmentTypeProduct]]:
    """Create appointment type product

    Args:
        body (CreateAppointmentTypeProductPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AppointmentTypeProduct]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
