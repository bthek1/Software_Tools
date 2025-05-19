from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.email_communication import EmailCommunication
from ...models.memo_communication import MemoCommunication
from ...models.sms_communication import SmsCommunication
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    q: Union[Unset, List[str]] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_q: Union[Unset, List[str]] = UNSET
    if not isinstance(q, Unset):
        json_q = q

    params["q[]"] = json_q

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/communications/{id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union["EmailCommunication", "MemoCommunication", "SmsCommunication"]]:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Union["EmailCommunication", "MemoCommunication", "SmsCommunication"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_communication_type_0 = MemoCommunication.from_dict(data)

                return componentsschemas_communication_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_communication_type_1 = EmailCommunication.from_dict(data)

                return componentsschemas_communication_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_communication_type_2 = SmsCommunication.from_dict(data)

            return componentsschemas_communication_type_2

        response_200 = _parse_response_200(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union["EmailCommunication", "MemoCommunication", "SmsCommunication"]]:
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
    q: Union[Unset, List[str]] = UNSET,
) -> Response[Union["EmailCommunication", "MemoCommunication", "SmsCommunication"]]:
    """Get communication

    Args:
        id (str):
        q (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['EmailCommunication', 'MemoCommunication', 'SmsCommunication']]
    """

    kwargs = _get_kwargs(
        id=id,
        q=q,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    q: Union[Unset, List[str]] = UNSET,
) -> Optional[Union["EmailCommunication", "MemoCommunication", "SmsCommunication"]]:
    """Get communication

    Args:
        id (str):
        q (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['EmailCommunication', 'MemoCommunication', 'SmsCommunication']
    """

    return sync_detailed(
        id=id,
        client=client,
        q=q,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    q: Union[Unset, List[str]] = UNSET,
) -> Response[Union["EmailCommunication", "MemoCommunication", "SmsCommunication"]]:
    """Get communication

    Args:
        id (str):
        q (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['EmailCommunication', 'MemoCommunication', 'SmsCommunication']]
    """

    kwargs = _get_kwargs(
        id=id,
        q=q,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    q: Union[Unset, List[str]] = UNSET,
) -> Optional[Union["EmailCommunication", "MemoCommunication", "SmsCommunication"]]:
    """Get communication

    Args:
        id (str):
        q (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['EmailCommunication', 'MemoCommunication', 'SmsCommunication']
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            q=q,
        )
    ).parsed
