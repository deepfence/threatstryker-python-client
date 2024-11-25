from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_docs_bad_request_response import ApiDocsBadRequestResponse
from ...models.api_docs_failure_response import ApiDocsFailureResponse
from ...models.ingesters_report_ingestion_data import IngestersReportIngestionData
from ...types import Response


def _get_kwargs(
    *,
    body: IngestersReportIngestionData,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/deepfence/ingest/sync-report",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, None)
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
    body: IngestersReportIngestionData,
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse]]:
    """Ingest Topology Data

     Ingest data reported by one Agent

    Args:
        body (IngestersReportIngestionData):  Example: {'hosts': [{'key': ''}, {'key': ''}],
            'host_batch': [{'key': ''}, {'key': ''}], 'kubernetes_cluster_edge_batch': [{'key': ''},
            {'key': ''}], 'process_batch': [{'key': ''}, {'key': ''}], 'container_image_edge_batch':
            [{'key': ''}, {'key': ''}], 'num_merged': 0, 'container_process_edge_batch': [{'key': ''},
            {'key': ''}], 'pod_batch': [{'key': ''}, {'key': ''}], 'process_edges_batch': [{'key':
            ''}, {'key': ''}], 'container_edges_batch': [{'key': ''}, {'key': ''}],
            'api_endpoints_edge_batch': [{'key': ''}, {'key': ''}], 'container_batch': [{'key': ''},
            {'key': ''}], 'container_image_batch': [{'key': ''}, {'key': ''}],
            'kubernetes_cluster_batch': [{'key': ''}, {'key': ''}], 'api_endpoints_batch': [{'key':
            ''}, {'key': ''}], 'pod_edges_batch': [{'key': ''}, {'key': ''}], 'endpoint_edges_batch':
            [{'key': ''}, {'key': ''}], 'pod_host_edges_batch': [{'key': ''}, {'key': ''}]}.

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
    body: IngestersReportIngestionData,
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse]]:
    """Ingest Topology Data

     Ingest data reported by one Agent

    Args:
        body (IngestersReportIngestionData):  Example: {'hosts': [{'key': ''}, {'key': ''}],
            'host_batch': [{'key': ''}, {'key': ''}], 'kubernetes_cluster_edge_batch': [{'key': ''},
            {'key': ''}], 'process_batch': [{'key': ''}, {'key': ''}], 'container_image_edge_batch':
            [{'key': ''}, {'key': ''}], 'num_merged': 0, 'container_process_edge_batch': [{'key': ''},
            {'key': ''}], 'pod_batch': [{'key': ''}, {'key': ''}], 'process_edges_batch': [{'key':
            ''}, {'key': ''}], 'container_edges_batch': [{'key': ''}, {'key': ''}],
            'api_endpoints_edge_batch': [{'key': ''}, {'key': ''}], 'container_batch': [{'key': ''},
            {'key': ''}], 'container_image_batch': [{'key': ''}, {'key': ''}],
            'kubernetes_cluster_batch': [{'key': ''}, {'key': ''}], 'api_endpoints_batch': [{'key':
            ''}, {'key': ''}], 'pod_edges_batch': [{'key': ''}, {'key': ''}], 'endpoint_edges_batch':
            [{'key': ''}, {'key': ''}], 'pod_host_edges_batch': [{'key': ''}, {'key': ''}]}.

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
    body: IngestersReportIngestionData,
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse]]:
    """Ingest Topology Data

     Ingest data reported by one Agent

    Args:
        body (IngestersReportIngestionData):  Example: {'hosts': [{'key': ''}, {'key': ''}],
            'host_batch': [{'key': ''}, {'key': ''}], 'kubernetes_cluster_edge_batch': [{'key': ''},
            {'key': ''}], 'process_batch': [{'key': ''}, {'key': ''}], 'container_image_edge_batch':
            [{'key': ''}, {'key': ''}], 'num_merged': 0, 'container_process_edge_batch': [{'key': ''},
            {'key': ''}], 'pod_batch': [{'key': ''}, {'key': ''}], 'process_edges_batch': [{'key':
            ''}, {'key': ''}], 'container_edges_batch': [{'key': ''}, {'key': ''}],
            'api_endpoints_edge_batch': [{'key': ''}, {'key': ''}], 'container_batch': [{'key': ''},
            {'key': ''}], 'container_image_batch': [{'key': ''}, {'key': ''}],
            'kubernetes_cluster_batch': [{'key': ''}, {'key': ''}], 'api_endpoints_batch': [{'key':
            ''}, {'key': ''}], 'pod_edges_batch': [{'key': ''}, {'key': ''}], 'endpoint_edges_batch':
            [{'key': ''}, {'key': ''}], 'pod_host_edges_batch': [{'key': ''}, {'key': ''}]}.

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
    body: IngestersReportIngestionData,
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse]]:
    """Ingest Topology Data

     Ingest data reported by one Agent

    Args:
        body (IngestersReportIngestionData):  Example: {'hosts': [{'key': ''}, {'key': ''}],
            'host_batch': [{'key': ''}, {'key': ''}], 'kubernetes_cluster_edge_batch': [{'key': ''},
            {'key': ''}], 'process_batch': [{'key': ''}, {'key': ''}], 'container_image_edge_batch':
            [{'key': ''}, {'key': ''}], 'num_merged': 0, 'container_process_edge_batch': [{'key': ''},
            {'key': ''}], 'pod_batch': [{'key': ''}, {'key': ''}], 'process_edges_batch': [{'key':
            ''}, {'key': ''}], 'container_edges_batch': [{'key': ''}, {'key': ''}],
            'api_endpoints_edge_batch': [{'key': ''}, {'key': ''}], 'container_batch': [{'key': ''},
            {'key': ''}], 'container_image_batch': [{'key': ''}, {'key': ''}],
            'kubernetes_cluster_batch': [{'key': ''}, {'key': ''}], 'api_endpoints_batch': [{'key':
            ''}, {'key': ''}], 'pod_edges_batch': [{'key': ''}, {'key': ''}], 'endpoint_edges_batch':
            [{'key': ''}, {'key': ''}], 'pod_host_edges_batch': [{'key': ''}, {'key': ''}]}.

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
