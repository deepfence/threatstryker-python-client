from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_docs_bad_request_response import ApiDocsBadRequestResponse
from ...models.api_docs_failure_response import ApiDocsFailureResponse
from ...models.singlesignon_sso_response import SinglesignonSSOResponse
from ...models.singlesignon_update_sso_provider_config import SinglesignonUpdateSSOProviderConfig
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: SinglesignonUpdateSSOProviderConfig,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/deepfence/single-sign-on/{id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, SinglesignonSSOResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SinglesignonSSOResponse.from_dict(response.json())

        return response_200
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
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, SinglesignonSSOResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: SinglesignonUpdateSSOProviderConfig,
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, SinglesignonSSOResponse]]:
    """Update Single sign-on

     Update Single sign-on (OIDC, Google, Microsoft, Github)

    Args:
        id (int):
        body (SinglesignonUpdateSSOProviderConfig):  Example: {'issuer_alias_url':
            'issuer_alias_url', 'issuer_url': 'issuer_url', 'disable_password_login': True,
            'client_secret': 'client_secret', 'client_id': 'client_id'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, SinglesignonSSOResponse]]
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
    id: int,
    *,
    client: AuthenticatedClient,
    body: SinglesignonUpdateSSOProviderConfig,
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, SinglesignonSSOResponse]]:
    """Update Single sign-on

     Update Single sign-on (OIDC, Google, Microsoft, Github)

    Args:
        id (int):
        body (SinglesignonUpdateSSOProviderConfig):  Example: {'issuer_alias_url':
            'issuer_alias_url', 'issuer_url': 'issuer_url', 'disable_password_login': True,
            'client_secret': 'client_secret', 'client_id': 'client_id'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, SinglesignonSSOResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: SinglesignonUpdateSSOProviderConfig,
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, SinglesignonSSOResponse]]:
    """Update Single sign-on

     Update Single sign-on (OIDC, Google, Microsoft, Github)

    Args:
        id (int):
        body (SinglesignonUpdateSSOProviderConfig):  Example: {'issuer_alias_url':
            'issuer_alias_url', 'issuer_url': 'issuer_url', 'disable_password_login': True,
            'client_secret': 'client_secret', 'client_id': 'client_id'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, SinglesignonSSOResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: SinglesignonUpdateSSOProviderConfig,
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, SinglesignonSSOResponse]]:
    """Update Single sign-on

     Update Single sign-on (OIDC, Google, Microsoft, Github)

    Args:
        id (int):
        body (SinglesignonUpdateSSOProviderConfig):  Example: {'issuer_alias_url':
            'issuer_alias_url', 'issuer_url': 'issuer_url', 'disable_password_login': True,
            'client_secret': 'client_secret', 'client_id': 'client_id'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, SinglesignonSSOResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
