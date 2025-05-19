from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_contacts_get_order import ListContactsGetOrder
from ...models.list_contacts_get_response_200 import ListContactsGetResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: Union[Unset, int] = UNSET,
    per_page: Union[Unset, int] = UNSET,
    sort: Union[Unset, List[str]] = UNSET,
    order: Union[Unset, ListContactsGetOrder] = UNSET,
    q: Union[Unset, List[str]] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    json_sort: Union[Unset, List[str]] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order

    params["order"] = json_order

    json_q: Union[Unset, List[str]] = UNSET
    if not isinstance(q, Unset):
        json_q = q

    params["q[]"] = json_q

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/contacts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ListContactsGetResponse200]:
    if response.status_code == 200:
        response_200 = ListContactsGetResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ListContactsGetResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = UNSET,
    per_page: Union[Unset, int] = UNSET,
    sort: Union[Unset, List[str]] = UNSET,
    order: Union[Unset, ListContactsGetOrder] = UNSET,
    q: Union[Unset, List[str]] = UNSET,
) -> Response[ListContactsGetResponse200]:
    """List contacts

    Args:
        page (Union[Unset, int]):
        per_page (Union[Unset, int]):
        sort (Union[Unset, List[str]]):
        order (Union[Unset, ListContactsGetOrder]):
        q (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListContactsGetResponse200]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        sort=sort,
        order=order,
        q=q,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = UNSET,
    per_page: Union[Unset, int] = UNSET,
    sort: Union[Unset, List[str]] = UNSET,
    order: Union[Unset, ListContactsGetOrder] = UNSET,
    q: Union[Unset, List[str]] = UNSET,
) -> Optional[ListContactsGetResponse200]:
    """List contacts

    Args:
        page (Union[Unset, int]):
        per_page (Union[Unset, int]):
        sort (Union[Unset, List[str]]):
        order (Union[Unset, ListContactsGetOrder]):
        q (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListContactsGetResponse200
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        sort=sort,
        order=order,
        q=q,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = UNSET,
    per_page: Union[Unset, int] = UNSET,
    sort: Union[Unset, List[str]] = UNSET,
    order: Union[Unset, ListContactsGetOrder] = UNSET,
    q: Union[Unset, List[str]] = UNSET,
) -> Response[ListContactsGetResponse200]:
    """List contacts

    Args:
        page (Union[Unset, int]):
        per_page (Union[Unset, int]):
        sort (Union[Unset, List[str]]):
        order (Union[Unset, ListContactsGetOrder]):
        q (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListContactsGetResponse200]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        sort=sort,
        order=order,
        q=q,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    page: Union[Unset, int] = UNSET,
    per_page: Union[Unset, int] = UNSET,
    sort: Union[Unset, List[str]] = UNSET,
    order: Union[Unset, ListContactsGetOrder] = UNSET,
    q: Union[Unset, List[str]] = UNSET,
) -> Optional[ListContactsGetResponse200]:
    """List contacts

    Args:
        page (Union[Unset, int]):
        per_page (Union[Unset, int]):
        sort (Union[Unset, List[str]]):
        order (Union[Unset, ListContactsGetOrder]):
        q (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListContactsGetResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            sort=sort,
            order=order,
            q=q,
        )
    ).parsed
