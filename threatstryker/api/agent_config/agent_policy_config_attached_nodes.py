from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_docs_bad_request_response import ApiDocsBadRequestResponse
from ...models.api_docs_failure_response import ApiDocsFailureResponse
from ...models.model_get_attached_nodes_resp import ModelGetAttachedNodesResp
from ...types import Response


def _get_kwargs(
    config_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/deepfence/configs/agent/policy/attached-nodes/{config_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelGetAttachedNodesResp]]:
    if response.status_code == 200:
        response_200 = ModelGetAttachedNodesResp.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ApiDocsBadRequestResponse.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = ApiDocsFailureResponse.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = ApiDocsFailureResponse.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelGetAttachedNodesResp]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    config_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelGetAttachedNodesResp]]:
    """Get Agent Policy config attached nodes

     Get Agent Policy config attached nodes

    Args:
        config_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelGetAttachedNodesResp]]
    """

    kwargs = _get_kwargs(
        config_id=config_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    config_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelGetAttachedNodesResp]]:
    """Get Agent Policy config attached nodes

     Get Agent Policy config attached nodes

    Args:
        config_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelGetAttachedNodesResp]
    """

    return sync_detailed(
        config_id=config_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    config_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelGetAttachedNodesResp]]:
    """Get Agent Policy config attached nodes

     Get Agent Policy config attached nodes

    Args:
        config_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelGetAttachedNodesResp]]
    """

    kwargs = _get_kwargs(
        config_id=config_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    config_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelGetAttachedNodesResp]]:
    """Get Agent Policy config attached nodes

     Get Agent Policy config attached nodes

    Args:
        config_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelGetAttachedNodesResp]
    """

    return (
        await asyncio_detailed(
            config_id=config_id,
            client=client,
        )
    ).parsed
