from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_docs_bad_request_response import ApiDocsBadRequestResponse
from ...models.api_docs_failure_response import ApiDocsFailureResponse
from ...models.model_login_response import ModelLoginResponse
from ...models.singlesignon_verify_sso_auth_request import SinglesignonVerifySSOAuthRequest
from ...types import Response


def _get_kwargs(
    *,
    json_body: SinglesignonVerifySSOAuthRequest,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/deepfence/sso/verify",
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelLoginResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ModelLoginResponse.from_dict(response.json())

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
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelLoginResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: SinglesignonVerifySSOAuthRequest,
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelLoginResponse]]:
    """Verify SSO auth code

     Verify code and get access token

    Args:
        json_body (SinglesignonVerifySSOAuthRequest):  Example: {'code': 'code', 'user_id': 0,
            'namespace': 'namespace'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelLoginResponse]]
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
    client: Union[AuthenticatedClient, Client],
    json_body: SinglesignonVerifySSOAuthRequest,
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelLoginResponse]]:
    """Verify SSO auth code

     Verify code and get access token

    Args:
        json_body (SinglesignonVerifySSOAuthRequest):  Example: {'code': 'code', 'user_id': 0,
            'namespace': 'namespace'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelLoginResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: SinglesignonVerifySSOAuthRequest,
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelLoginResponse]]:
    """Verify SSO auth code

     Verify code and get access token

    Args:
        json_body (SinglesignonVerifySSOAuthRequest):  Example: {'code': 'code', 'user_id': 0,
            'namespace': 'namespace'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelLoginResponse]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: SinglesignonVerifySSOAuthRequest,
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelLoginResponse]]:
    """Verify SSO auth code

     Verify code and get access token

    Args:
        json_body (SinglesignonVerifySSOAuthRequest):  Example: {'code': 'code', 'user_id': 0,
            'namespace': 'namespace'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelLoginResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
