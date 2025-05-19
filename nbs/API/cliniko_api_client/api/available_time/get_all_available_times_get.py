import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_all_available_times_get_response_200 import GetAllAvailableTimesGetResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    business_id: str,
    practitioner_id: str,
    appointment_type_id: str,
    *,
    from_: datetime.date,
    to: datetime.date,
    page: Union[Unset, int] = UNSET,
    per_page: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to = to.isoformat()
    params["to"] = json_to

    params["page"] = page

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/businesses/{business_id}/practitioners/{practitioner_id}/appointment_types/{appointment_type_id}/available_times",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetAllAvailableTimesGetResponse200]:
    if response.status_code == 200:
        response_200 = GetAllAvailableTimesGetResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetAllAvailableTimesGetResponse200]:
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
    page: Union[Unset, int] = UNSET,
    per_page: Union[Unset, int] = UNSET,
) -> Response[GetAllAvailableTimesGetResponse200]:
    """Get all available times

     Find appointment start times that are currently available for the practitioner based on parameters
    provided.

    Args:
        business_id (str):  Example: 1.
        practitioner_id (str):  Example: 1.
        appointment_type_id (str):  Example: 1.
        from_ (datetime.date):
        to (datetime.date):
        page (Union[Unset, int]):
        per_page (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllAvailableTimesGetResponse200]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
        practitioner_id=practitioner_id,
        appointment_type_id=appointment_type_id,
        from_=from_,
        to=to,
        page=page,
        per_page=per_page,
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
    page: Union[Unset, int] = UNSET,
    per_page: Union[Unset, int] = UNSET,
) -> Optional[GetAllAvailableTimesGetResponse200]:
    """Get all available times

     Find appointment start times that are currently available for the practitioner based on parameters
    provided.

    Args:
        business_id (str):  Example: 1.
        practitioner_id (str):  Example: 1.
        appointment_type_id (str):  Example: 1.
        from_ (datetime.date):
        to (datetime.date):
        page (Union[Unset, int]):
        per_page (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllAvailableTimesGetResponse200
    """

    return sync_detailed(
        business_id=business_id,
        practitioner_id=practitioner_id,
        appointment_type_id=appointment_type_id,
        client=client,
        from_=from_,
        to=to,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    business_id: str,
    practitioner_id: str,
    appointment_type_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    from_: datetime.date,
    to: datetime.date,
    page: Union[Unset, int] = UNSET,
    per_page: Union[Unset, int] = UNSET,
) -> Response[GetAllAvailableTimesGetResponse200]:
    """Get all available times

     Find appointment start times that are currently available for the practitioner based on parameters
    provided.

    Args:
        business_id (str):  Example: 1.
        practitioner_id (str):  Example: 1.
        appointment_type_id (str):  Example: 1.
        from_ (datetime.date):
        to (datetime.date):
        page (Union[Unset, int]):
        per_page (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllAvailableTimesGetResponse200]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
        practitioner_id=practitioner_id,
        appointment_type_id=appointment_type_id,
        from_=from_,
        to=to,
        page=page,
        per_page=per_page,
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
    page: Union[Unset, int] = UNSET,
    per_page: Union[Unset, int] = UNSET,
) -> Optional[GetAllAvailableTimesGetResponse200]:
    """Get all available times

     Find appointment start times that are currently available for the practitioner based on parameters
    provided.

    Args:
        business_id (str):  Example: 1.
        practitioner_id (str):  Example: 1.
        appointment_type_id (str):  Example: 1.
        from_ (datetime.date):
        to (datetime.date):
        page (Union[Unset, int]):
        per_page (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllAvailableTimesGetResponse200
    """

    return (
        await asyncio_detailed(
            business_id=business_id,
            practitioner_id=practitioner_id,
            appointment_type_id=appointment_type_id,
            client=client,
            from_=from_,
            to=to,
            page=page,
            per_page=per_page,
        )
    ).parsed
