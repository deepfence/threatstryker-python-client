from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_docs_bad_request_response import ApiDocsBadRequestResponse
from ...models.api_docs_failure_response import ApiDocsFailureResponse
from ...models.controls_threat_intel_info import ControlsThreatIntelInfo
from ...types import Response


def _get_kwargs(
    *,
    body: ControlsThreatIntelInfo,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/deepfence/configs/agent/threatintel/",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


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
    body: ControlsThreatIntelInfo,
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse]]:
    """Register threat intel config

     Register threat intel config

    Args:
        body (ControlsThreatIntelInfo):  Example: {'cloud_posture_controls_hash':
            'cloud_posture_controls_hash', 'cloud_posture_controls_url': 'cloud_posture_controls_url',
            'updated_at': 0, 'network_alert_rules_url': 'network_alert_rules_url',
            'ignored_alert_rule_ids': ['ignored_alert_rule_ids', 'ignored_alert_rule_ids'],
            'internal_ips': ['internal_ips', 'internal_ips'], 'secret_scanner_rules_hash':
            'secret_scanner_rules_hash', 'secret_scanner_rules_url': 'secret_scanner_rules_url',
            'malware_scanner_rules_hash': 'malware_scanner_rules_hash', 'malware_scanner_rules_url':
            'malware_scanner_rules_url', 'rules_hash': 'rules_hash'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse]]
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
    client: AuthenticatedClient,
    body: ControlsThreatIntelInfo,
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse]]:
    """Register threat intel config

     Register threat intel config

    Args:
        body (ControlsThreatIntelInfo):  Example: {'cloud_posture_controls_hash':
            'cloud_posture_controls_hash', 'cloud_posture_controls_url': 'cloud_posture_controls_url',
            'updated_at': 0, 'network_alert_rules_url': 'network_alert_rules_url',
            'ignored_alert_rule_ids': ['ignored_alert_rule_ids', 'ignored_alert_rule_ids'],
            'internal_ips': ['internal_ips', 'internal_ips'], 'secret_scanner_rules_hash':
            'secret_scanner_rules_hash', 'secret_scanner_rules_url': 'secret_scanner_rules_url',
            'malware_scanner_rules_hash': 'malware_scanner_rules_hash', 'malware_scanner_rules_url':
            'malware_scanner_rules_url', 'rules_hash': 'rules_hash'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ControlsThreatIntelInfo,
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse]]:
    """Register threat intel config

     Register threat intel config

    Args:
        body (ControlsThreatIntelInfo):  Example: {'cloud_posture_controls_hash':
            'cloud_posture_controls_hash', 'cloud_posture_controls_url': 'cloud_posture_controls_url',
            'updated_at': 0, 'network_alert_rules_url': 'network_alert_rules_url',
            'ignored_alert_rule_ids': ['ignored_alert_rule_ids', 'ignored_alert_rule_ids'],
            'internal_ips': ['internal_ips', 'internal_ips'], 'secret_scanner_rules_hash':
            'secret_scanner_rules_hash', 'secret_scanner_rules_url': 'secret_scanner_rules_url',
            'malware_scanner_rules_hash': 'malware_scanner_rules_hash', 'malware_scanner_rules_url':
            'malware_scanner_rules_url', 'rules_hash': 'rules_hash'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ControlsThreatIntelInfo,
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse]]:
    """Register threat intel config

     Register threat intel config

    Args:
        body (ControlsThreatIntelInfo):  Example: {'cloud_posture_controls_hash':
            'cloud_posture_controls_hash', 'cloud_posture_controls_url': 'cloud_posture_controls_url',
            'updated_at': 0, 'network_alert_rules_url': 'network_alert_rules_url',
            'ignored_alert_rule_ids': ['ignored_alert_rule_ids', 'ignored_alert_rule_ids'],
            'internal_ips': ['internal_ips', 'internal_ips'], 'secret_scanner_rules_hash':
            'secret_scanner_rules_hash', 'secret_scanner_rules_url': 'secret_scanner_rules_url',
            'malware_scanner_rules_hash': 'malware_scanner_rules_hash', 'malware_scanner_rules_url':
            'malware_scanner_rules_url', 'rules_hash': 'rules_hash'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
