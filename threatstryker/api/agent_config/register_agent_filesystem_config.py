from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_docs_bad_request_response import ApiDocsBadRequestResponse
from ...models.api_docs_failure_response import ApiDocsFailureResponse
from ...models.controls_filesystem_tracer_config import ControlsFilesystemTracerConfig
from ...types import Response


def _get_kwargs(
    *,
    json_body: ControlsFilesystemTracerConfig,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/deepfence/configs/agent/filemon/",
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ApiDocsBadRequestResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ApiDocsFailureResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ApiDocsFailureResponse.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: ControlsFilesystemTracerConfig,
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse]]:
    """Register Agent Filesystem config

     Register Agent Filesystem config

    Args:
        json_body (ControlsFilesystemTracerConfig):  Example: {'updated_at': 0, 'watchedentries':
            [{'severity': 'severity', 'accesstypes': ['accesstypes', 'accesstypes'], 'root': 'root',
            'recursive': True}, {'severity': 'severity', 'accesstypes': ['accesstypes',
            'accesstypes'], 'root': 'root', 'recursive': True}], 'node_id': 'node_id'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: ControlsFilesystemTracerConfig,
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse]]:
    """Register Agent Filesystem config

     Register Agent Filesystem config

    Args:
        json_body (ControlsFilesystemTracerConfig):  Example: {'updated_at': 0, 'watchedentries':
            [{'severity': 'severity', 'accesstypes': ['accesstypes', 'accesstypes'], 'root': 'root',
            'recursive': True}, {'severity': 'severity', 'accesstypes': ['accesstypes',
            'accesstypes'], 'root': 'root', 'recursive': True}], 'node_id': 'node_id'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: ControlsFilesystemTracerConfig,
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse]]:
    """Register Agent Filesystem config

     Register Agent Filesystem config

    Args:
        json_body (ControlsFilesystemTracerConfig):  Example: {'updated_at': 0, 'watchedentries':
            [{'severity': 'severity', 'accesstypes': ['accesstypes', 'accesstypes'], 'root': 'root',
            'recursive': True}, {'severity': 'severity', 'accesstypes': ['accesstypes',
            'accesstypes'], 'root': 'root', 'recursive': True}], 'node_id': 'node_id'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: ControlsFilesystemTracerConfig,
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse]]:
    """Register Agent Filesystem config

     Register Agent Filesystem config

    Args:
        json_body (ControlsFilesystemTracerConfig):  Example: {'updated_at': 0, 'watchedentries':
            [{'severity': 'severity', 'accesstypes': ['accesstypes', 'accesstypes'], 'root': 'root',
            'recursive': True}, {'severity': 'severity', 'accesstypes': ['accesstypes',
            'accesstypes'], 'root': 'root', 'recursive': True}], 'node_id': 'node_id'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
