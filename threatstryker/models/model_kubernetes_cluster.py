from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_host import ModelHost


T = TypeVar("T", bound="ModelKubernetesCluster")


@_attrs_define
class ModelKubernetesCluster:
    """
    Example:
        {'hosts': [{'public_ip': ['', ''], 'container_images': [{'is_deepfence_system': True, 'metadata': {'key': ''},
            'secret_scan_status': 'secret_scan_status', 'vulnerabilities_count': 4, 'secrets_count': 1,
            'malware_latest_scan_id': 'malware_latest_scan_id', 'malwares_count': 7, 'node_name': 'node_name',
            'secret_latest_scan_id': 'secret_latest_scan_id', 'vulnerability_latest_scan_id':
            'vulnerability_latest_scan_id', 'docker_image_created_at': 'docker_image_created_at', 'docker_image_tag':
            'docker_image_tag', 'malware_scan_status': 'malware_scan_status', 'docker_image_size': 'docker_image_size',
            'image_node_id': 'image_node_id', 'docker_image_virtual_size': 'docker_image_virtual_size', 'containers':
            [{'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count':
            2, 'threads': 1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'],
            'cmdline': 'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'},
            {'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads':
            1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'], 'cmdline':
            'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'},
            {'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count':
            2, 'threads': 1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'],
            'cmdline': 'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'},
            {'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads':
            1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'], 'cmdline':
            'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}],
            'docker_image_id': 'docker_image_id', 'vulnerability_scan_status': 'vulnerability_scan_status',
            'docker_image_name': 'docker_image_name', 'docker_image_tag_list': ['docker_image_tag_list',
            'docker_image_tag_list'], 'node_id': 'node_id'}, {'is_deepfence_system': True, 'metadata': {'key': ''},
            'secret_scan_status': 'secret_scan_status', 'vulnerabilities_count': 4, 'secrets_count': 1,
            'malware_latest_scan_id': 'malware_latest_scan_id', 'malwares_count': 7, 'node_name': 'node_name',
            'secret_latest_scan_id': 'secret_latest_scan_id', 'vulnerability_latest_scan_id':
            'vulnerability_latest_scan_id', 'docker_image_created_at': 'docker_image_created_at', 'docker_image_tag':
            'docker_image_tag', 'malware_scan_status': 'malware_scan_status', 'docker_image_size': 'docker_image_size',
            'image_node_id': 'image_node_id', 'docker_image_virtual_size': 'docker_image_virtual_size', 'containers':
            [{'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count':
            2, 'threads': 1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'],
            'cmdline': 'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'},
            {'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads':
            1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'], 'cmdline':
            'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'},
            {'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count':
            2, 'threads': 1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'],
            'cmdline': 'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'},
            {'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads':
            1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'], 'cmdline':
            'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}],
            'docker_image_id': 'docker_image_id', 'vulnerability_scan_status': 'vulnerability_scan_status',
            'docker_image_name': 'docker_image_name', 'docker_image_tag_list': ['docker_image_tag_list',
            'docker_image_tag_list'], 'node_id': 'node_id'}], 'cpu_max': 5.637376656633329, 'alerts_counts': {'key': 6},
            'secret_latest_scan_id': 'secret_latest_scan_id', 'config_names': {'policy_config_name': 'policy_config_name',
            'filesystem_config_name': 'filesystem_config_name', 'process_config_name': 'process_config_name',
            'network_config_name': 'network_config_name'}, 'network_tracer_status': 'network_tracer_status',
            'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id', 'api_endpoints': [{'host_ip': 'host_ip',
            'cloud_region': 'cloud_region', 'method': 'method', 'created_at': 0, 'cloud_provider': 'cloud_provider',
            'schema_info': 'schema_info', 'path': 'path', 'cloud_type': 'cloud_type', 'source_hosts': ['source_hosts',
            'source_hosts'], 'updated_at': 1, 'port': 0, 'host': 'host', 'direction': 'ingress'}, {'host_ip': 'host_ip',
            'cloud_region': 'cloud_region', 'method': 'method', 'created_at': 0, 'cloud_provider': 'cloud_provider',
            'schema_info': 'schema_info', 'path': 'path', 'cloud_type': 'cloud_type', 'source_hosts': ['source_hosts',
            'source_hosts'], 'updated_at': 1, 'port': 0, 'host': 'host', 'direction': 'ingress'}], 'plugin_status':
            {'network_tracer_status': {'description': 'description', 'status': 'status'}, 'network_filter_status':
            {'description': 'description', 'status': 'status'}, 'cloud_network_tracer_status': {'description':
            'description', 'status': 'status'}, 'filesystem_tracer_status': {'description': 'description', 'status':
            'status'}, 'process_tracer_status': {'description': 'description', 'status': 'status'},
            'agent_installer_tracer_status': {'description': 'description', 'status': 'status'}},
            'agent_installer_tracer_status': 'agent_installer_tracer_status', 'malware_latest_scan_id':
            'malware_latest_scan_id', 'version': 'version', 'instance_id': 'instance_id', 'kernel_id': 'kernel_id',
            'compliance_latest_scan_id': 'compliance_latest_scan_id', 'containers': [{'vulnerabilities_count': 6,
            'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name', 'docker_container_state':
            'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5, 'secret_latest_scan_id':
            'secret_latest_scan_id', 'docker_container_network_mode': 'docker_container_network_mode',
            'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id', 'kubernetes_namespace': 'kubernetes_namespace',
            'malware_scan_status': 'malware_scan_status', 'docker_container_ips': ['', ''], 'docker_labels': {'key': ''},
            'is_deepfence_system': True, 'image': None, 'processes': [{'cpu_max': 2.3021358869347655, 'node_name':
            'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'ppid': 7, 'memory_max': 9,
            'active_secrets': ['active_secrets', 'active_secrets'], 'cmdline': 'cmdline', 'active_cves': ['active_cves',
            'active_cves'], 'active_malwares': ['active_malwares', 'active_malwares'], 'short_name': 'short_name',
            'cpu_usage': 7.061401241503109, 'node_id': 'node_id'}, {'cpu_max': 2.3021358869347655, 'node_name': 'node_name',
            'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets':
            ['active_secrets', 'active_secrets'], 'cmdline': 'cmdline', 'active_cves': ['active_cves', 'active_cves'],
            'active_malwares': ['active_malwares', 'active_malwares'], 'short_name': 'short_name', 'cpu_usage':
            7.061401241503109, 'node_id': 'node_id'}], 'secret_scan_status': 'secret_scan_status', 'docker_container_name':
            'docker_container_name', 'docker_container_created': 'docker_container_created', 'malware_latest_scan_id':
            'malware_latest_scan_id', 'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name':
            'node_name', 'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'},
            {'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count':
            2, 'threads': 1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'],
            'cmdline': 'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'},
            {'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads':
            1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'], 'cmdline':
            'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}],
            'cpu_usage': 2.3021358869347655, 'instance_type': 'instance_type', 'local_networks': ['', ''],
            'vulnerabilities_count': 4, 'secrets_count': 7, 'cloud_region': 'cloud_region',
            'network_tracer_status_updated_at': 1, 'network_filter_status': 'network_filter_status', 'memory_usage': 1,
            'private_ip': ['', ''], 'exploitable_vulnerabilities_count': 3, 'cloud_account_id': 'cloud_account_id',
            'resource_group': 'resource_group', 'malware_scan_status': 'malware_scan_status', 'exploitable_malwares_count':
            7, 'agent_installer_tracer_status_updated_at': 0, 'filesystem_tracer_status_updated_at': 2,
            'filesystem_tracer_status': 'filesystem_tracer_status', 'inbound_connections': [{'count': 4, 'node_name':
            'node_name', 'ips': ['', ''], 'node_id': 'node_id'}, {'count': 4, 'node_name': 'node_name', 'ips': ['', ''],
            'node_id': 'node_id'}], 'availability_zone': 'availability_zone', 'is_console_vm': True, 'processes':
            [{'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads':
            1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'], 'cmdline':
            'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'},
            {'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads':
            1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'], 'cmdline':
            'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'}],
            'secret_scan_status': 'secret_scan_status', 'compliance_scan_status': 'compliance_scan_status',
            'outbound_connections': [{'count': 4, 'node_name': 'node_name', 'ips': ['', ''], 'node_id': 'node_id'},
            {'count': 4, 'node_name': 'node_name', 'ips': ['', ''], 'node_id': 'node_id'}], 'os': 'os', 'local_cidr': ['',
            ''], 'malwares_count': 7, 'node_name': 'node_name', 'cloud_provider': 'cloud_provider', 'process_tracer_status':
            'process_tracer_status', 'agent_running': True, 'cloud_warn_alarm_count': 1, 'exploitable_secrets_count': 9,
            'process_tracer_status_updated_at': 6, 'uptime': 1, 'memory_max': 1, 'account_id': 'account_id',
            'compliances_count': 5, 'kernel_version': 'kernel_version', 'warn_alarm_count': 5, 'pods':
            [{'is_deepfence_system': True, 'kubernetes_ip': 'kubernetes_ip', 'processes': [{'cpu_max': 2.3021358869347655,
            'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'ppid': 7,
            'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'], 'cmdline': 'cmdline', 'active_cves':
            ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares', 'active_malwares'], 'short_name':
            'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'}, {'cpu_max': 2.3021358869347655,
            'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'ppid': 7,
            'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'], 'cmdline': 'cmdline', 'active_cves':
            ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares', 'active_malwares'], 'short_name':
            'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'}], 'secret_scan_status':
            'secret_scan_status', 'kubernetes_cluster_id': 'kubernetes_cluster_id', 'kubernetes_cluster_name':
            'kubernetes_cluster_name', 'kubernetes_state': 'kubernetes_state', 'node_name': 'node_name',
            'kubernetes_created': 'kubernetes_created', 'pod_name': 'pod_name', 'kubernetes_namespace':
            'kubernetes_namespace', 'kubernetes_is_in_host_network': True, 'malware_scan_status': 'malware_scan_status',
            'kubernetes_labels': {'key': ''}, 'containers': [{'vulnerabilities_count': 6, 'secrets_count': 1,
            'kubernetes_cluster_name': 'kubernetes_cluster_name', 'docker_container_state': 'docker_container_state',
            'cpu_max': 0.8008281904610115, 'memory_usage': 5, 'secret_latest_scan_id': 'secret_latest_scan_id',
            'docker_container_network_mode': 'docker_container_network_mode', 'vulnerability_latest_scan_id':
            'vulnerability_latest_scan_id', 'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status':
            'malware_scan_status', 'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system':
            True, 'image': None, 'processes': [{'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3,
            'open_files_count': 2, 'threads': 1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets',
            'active_secrets'], 'cmdline': 'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares':
            ['active_malwares', 'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id':
            'node_id'}, {'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2,
            'threads': 1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'],
            'cmdline': 'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'},
            {'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count':
            2, 'threads': 1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'],
            'cmdline': 'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'},
            {'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads':
            1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'], 'cmdline':
            'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}],
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'},
            {'is_deepfence_system': True, 'kubernetes_ip': 'kubernetes_ip', 'processes': [{'cpu_max': 2.3021358869347655,
            'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'ppid': 7,
            'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'], 'cmdline': 'cmdline', 'active_cves':
            ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares', 'active_malwares'], 'short_name':
            'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'}, {'cpu_max': 2.3021358869347655,
            'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'ppid': 7,
            'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'], 'cmdline': 'cmdline', 'active_cves':
            ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares', 'active_malwares'], 'short_name':
            'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'}], 'secret_scan_status':
            'secret_scan_status', 'kubernetes_cluster_id': 'kubernetes_cluster_id', 'kubernetes_cluster_name':
            'kubernetes_cluster_name', 'kubernetes_state': 'kubernetes_state', 'node_name': 'node_name',
            'kubernetes_created': 'kubernetes_created', 'pod_name': 'pod_name', 'kubernetes_namespace':
            'kubernetes_namespace', 'kubernetes_is_in_host_network': True, 'malware_scan_status': 'malware_scan_status',
            'kubernetes_labels': {'key': ''}, 'containers': [{'vulnerabilities_count': 6, 'secrets_count': 1,
            'kubernetes_cluster_name': 'kubernetes_cluster_name', 'docker_container_state': 'docker_container_state',
            'cpu_max': 0.8008281904610115, 'memory_usage': 5, 'secret_latest_scan_id': 'secret_latest_scan_id',
            'docker_container_network_mode': 'docker_container_network_mode', 'vulnerability_latest_scan_id':
            'vulnerability_latest_scan_id', 'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status':
            'malware_scan_status', 'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system':
            True, 'image': None, 'processes': [{'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3,
            'open_files_count': 2, 'threads': 1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets',
            'active_secrets'], 'cmdline': 'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares':
            ['active_malwares', 'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id':
            'node_id'}, {'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2,
            'threads': 1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'],
            'cmdline': 'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'},
            {'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count':
            2, 'threads': 1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'],
            'cmdline': 'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'},
            {'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads':
            1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'], 'cmdline':
            'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}],
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}],
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'},
            {'public_ip': ['', ''], 'container_images': [{'is_deepfence_system': True, 'metadata': {'key': ''},
            'secret_scan_status': 'secret_scan_status', 'vulnerabilities_count': 4, 'secrets_count': 1,
            'malware_latest_scan_id': 'malware_latest_scan_id', 'malwares_count': 7, 'node_name': 'node_name',
            'secret_latest_scan_id': 'secret_latest_scan_id', 'vulnerability_latest_scan_id':
            'vulnerability_latest_scan_id', 'docker_image_created_at': 'docker_image_created_at', 'docker_image_tag':
            'docker_image_tag', 'malware_scan_status': 'malware_scan_status', 'docker_image_size': 'docker_image_size',
            'image_node_id': 'image_node_id', 'docker_image_virtual_size': 'docker_image_virtual_size', 'containers':
            [{'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count':
            2, 'threads': 1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'],
            'cmdline': 'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'},
            {'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads':
            1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'], 'cmdline':
            'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'},
            {'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count':
            2, 'threads': 1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'],
            'cmdline': 'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'},
            {'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads':
            1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'], 'cmdline':
            'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}],
            'docker_image_id': 'docker_image_id', 'vulnerability_scan_status': 'vulnerability_scan_status',
            'docker_image_name': 'docker_image_name', 'docker_image_tag_list': ['docker_image_tag_list',
            'docker_image_tag_list'], 'node_id': 'node_id'}, {'is_deepfence_system': True, 'metadata': {'key': ''},
            'secret_scan_status': 'secret_scan_status', 'vulnerabilities_count': 4, 'secrets_count': 1,
            'malware_latest_scan_id': 'malware_latest_scan_id', 'malwares_count': 7, 'node_name': 'node_name',
            'secret_latest_scan_id': 'secret_latest_scan_id', 'vulnerability_latest_scan_id':
            'vulnerability_latest_scan_id', 'docker_image_created_at': 'docker_image_created_at', 'docker_image_tag':
            'docker_image_tag', 'malware_scan_status': 'malware_scan_status', 'docker_image_size': 'docker_image_size',
            'image_node_id': 'image_node_id', 'docker_image_virtual_size': 'docker_image_virtual_size', 'containers':
            [{'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count':
            2, 'threads': 1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'],
            'cmdline': 'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'},
            {'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads':
            1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'], 'cmdline':
            'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'},
            {'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count':
            2, 'threads': 1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'],
            'cmdline': 'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'},
            {'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads':
            1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'], 'cmdline':
            'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}],
            'docker_image_id': 'docker_image_id', 'vulnerability_scan_status': 'vulnerability_scan_status',
            'docker_image_name': 'docker_image_name', 'docker_image_tag_list': ['docker_image_tag_list',
            'docker_image_tag_list'], 'node_id': 'node_id'}], 'cpu_max': 5.637376656633329, 'alerts_counts': {'key': 6},
            'secret_latest_scan_id': 'secret_latest_scan_id', 'config_names': {'policy_config_name': 'policy_config_name',
            'filesystem_config_name': 'filesystem_config_name', 'process_config_name': 'process_config_name',
            'network_config_name': 'network_config_name'}, 'network_tracer_status': 'network_tracer_status',
            'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id', 'api_endpoints': [{'host_ip': 'host_ip',
            'cloud_region': 'cloud_region', 'method': 'method', 'created_at': 0, 'cloud_provider': 'cloud_provider',
            'schema_info': 'schema_info', 'path': 'path', 'cloud_type': 'cloud_type', 'source_hosts': ['source_hosts',
            'source_hosts'], 'updated_at': 1, 'port': 0, 'host': 'host', 'direction': 'ingress'}, {'host_ip': 'host_ip',
            'cloud_region': 'cloud_region', 'method': 'method', 'created_at': 0, 'cloud_provider': 'cloud_provider',
            'schema_info': 'schema_info', 'path': 'path', 'cloud_type': 'cloud_type', 'source_hosts': ['source_hosts',
            'source_hosts'], 'updated_at': 1, 'port': 0, 'host': 'host', 'direction': 'ingress'}], 'plugin_status':
            {'network_tracer_status': {'description': 'description', 'status': 'status'}, 'network_filter_status':
            {'description': 'description', 'status': 'status'}, 'cloud_network_tracer_status': {'description':
            'description', 'status': 'status'}, 'filesystem_tracer_status': {'description': 'description', 'status':
            'status'}, 'process_tracer_status': {'description': 'description', 'status': 'status'},
            'agent_installer_tracer_status': {'description': 'description', 'status': 'status'}},
            'agent_installer_tracer_status': 'agent_installer_tracer_status', 'malware_latest_scan_id':
            'malware_latest_scan_id', 'version': 'version', 'instance_id': 'instance_id', 'kernel_id': 'kernel_id',
            'compliance_latest_scan_id': 'compliance_latest_scan_id', 'containers': [{'vulnerabilities_count': 6,
            'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name', 'docker_container_state':
            'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5, 'secret_latest_scan_id':
            'secret_latest_scan_id', 'docker_container_network_mode': 'docker_container_network_mode',
            'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id', 'kubernetes_namespace': 'kubernetes_namespace',
            'malware_scan_status': 'malware_scan_status', 'docker_container_ips': ['', ''], 'docker_labels': {'key': ''},
            'is_deepfence_system': True, 'image': None, 'processes': [{'cpu_max': 2.3021358869347655, 'node_name':
            'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'ppid': 7, 'memory_max': 9,
            'active_secrets': ['active_secrets', 'active_secrets'], 'cmdline': 'cmdline', 'active_cves': ['active_cves',
            'active_cves'], 'active_malwares': ['active_malwares', 'active_malwares'], 'short_name': 'short_name',
            'cpu_usage': 7.061401241503109, 'node_id': 'node_id'}, {'cpu_max': 2.3021358869347655, 'node_name': 'node_name',
            'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets':
            ['active_secrets', 'active_secrets'], 'cmdline': 'cmdline', 'active_cves': ['active_cves', 'active_cves'],
            'active_malwares': ['active_malwares', 'active_malwares'], 'short_name': 'short_name', 'cpu_usage':
            7.061401241503109, 'node_id': 'node_id'}], 'secret_scan_status': 'secret_scan_status', 'docker_container_name':
            'docker_container_name', 'docker_container_created': 'docker_container_created', 'malware_latest_scan_id':
            'malware_latest_scan_id', 'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name':
            'node_name', 'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'},
            {'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count':
            2, 'threads': 1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'],
            'cmdline': 'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'},
            {'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads':
            1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'], 'cmdline':
            'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}],
            'cpu_usage': 2.3021358869347655, 'instance_type': 'instance_type', 'local_networks': ['', ''],
            'vulnerabilities_count': 4, 'secrets_count': 7, 'cloud_region': 'cloud_region',
            'network_tracer_status_updated_at': 1, 'network_filter_status': 'network_filter_status', 'memory_usage': 1,
            'private_ip': ['', ''], 'exploitable_vulnerabilities_count': 3, 'cloud_account_id': 'cloud_account_id',
            'resource_group': 'resource_group', 'malware_scan_status': 'malware_scan_status', 'exploitable_malwares_count':
            7, 'agent_installer_tracer_status_updated_at': 0, 'filesystem_tracer_status_updated_at': 2,
            'filesystem_tracer_status': 'filesystem_tracer_status', 'inbound_connections': [{'count': 4, 'node_name':
            'node_name', 'ips': ['', ''], 'node_id': 'node_id'}, {'count': 4, 'node_name': 'node_name', 'ips': ['', ''],
            'node_id': 'node_id'}], 'availability_zone': 'availability_zone', 'is_console_vm': True, 'processes':
            [{'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads':
            1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'], 'cmdline':
            'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'},
            {'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads':
            1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'], 'cmdline':
            'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'}],
            'secret_scan_status': 'secret_scan_status', 'compliance_scan_status': 'compliance_scan_status',
            'outbound_connections': [{'count': 4, 'node_name': 'node_name', 'ips': ['', ''], 'node_id': 'node_id'},
            {'count': 4, 'node_name': 'node_name', 'ips': ['', ''], 'node_id': 'node_id'}], 'os': 'os', 'local_cidr': ['',
            ''], 'malwares_count': 7, 'node_name': 'node_name', 'cloud_provider': 'cloud_provider', 'process_tracer_status':
            'process_tracer_status', 'agent_running': True, 'cloud_warn_alarm_count': 1, 'exploitable_secrets_count': 9,
            'process_tracer_status_updated_at': 6, 'uptime': 1, 'memory_max': 1, 'account_id': 'account_id',
            'compliances_count': 5, 'kernel_version': 'kernel_version', 'warn_alarm_count': 5, 'pods':
            [{'is_deepfence_system': True, 'kubernetes_ip': 'kubernetes_ip', 'processes': [{'cpu_max': 2.3021358869347655,
            'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'ppid': 7,
            'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'], 'cmdline': 'cmdline', 'active_cves':
            ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares', 'active_malwares'], 'short_name':
            'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'}, {'cpu_max': 2.3021358869347655,
            'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'ppid': 7,
            'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'], 'cmdline': 'cmdline', 'active_cves':
            ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares', 'active_malwares'], 'short_name':
            'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'}], 'secret_scan_status':
            'secret_scan_status', 'kubernetes_cluster_id': 'kubernetes_cluster_id', 'kubernetes_cluster_name':
            'kubernetes_cluster_name', 'kubernetes_state': 'kubernetes_state', 'node_name': 'node_name',
            'kubernetes_created': 'kubernetes_created', 'pod_name': 'pod_name', 'kubernetes_namespace':
            'kubernetes_namespace', 'kubernetes_is_in_host_network': True, 'malware_scan_status': 'malware_scan_status',
            'kubernetes_labels': {'key': ''}, 'containers': [{'vulnerabilities_count': 6, 'secrets_count': 1,
            'kubernetes_cluster_name': 'kubernetes_cluster_name', 'docker_container_state': 'docker_container_state',
            'cpu_max': 0.8008281904610115, 'memory_usage': 5, 'secret_latest_scan_id': 'secret_latest_scan_id',
            'docker_container_network_mode': 'docker_container_network_mode', 'vulnerability_latest_scan_id':
            'vulnerability_latest_scan_id', 'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status':
            'malware_scan_status', 'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system':
            True, 'image': None, 'processes': [{'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3,
            'open_files_count': 2, 'threads': 1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets',
            'active_secrets'], 'cmdline': 'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares':
            ['active_malwares', 'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id':
            'node_id'}, {'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2,
            'threads': 1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'],
            'cmdline': 'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'},
            {'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count':
            2, 'threads': 1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'],
            'cmdline': 'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'},
            {'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads':
            1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'], 'cmdline':
            'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}],
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'},
            {'is_deepfence_system': True, 'kubernetes_ip': 'kubernetes_ip', 'processes': [{'cpu_max': 2.3021358869347655,
            'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'ppid': 7,
            'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'], 'cmdline': 'cmdline', 'active_cves':
            ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares', 'active_malwares'], 'short_name':
            'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'}, {'cpu_max': 2.3021358869347655,
            'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'ppid': 7,
            'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'], 'cmdline': 'cmdline', 'active_cves':
            ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares', 'active_malwares'], 'short_name':
            'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'}], 'secret_scan_status':
            'secret_scan_status', 'kubernetes_cluster_id': 'kubernetes_cluster_id', 'kubernetes_cluster_name':
            'kubernetes_cluster_name', 'kubernetes_state': 'kubernetes_state', 'node_name': 'node_name',
            'kubernetes_created': 'kubernetes_created', 'pod_name': 'pod_name', 'kubernetes_namespace':
            'kubernetes_namespace', 'kubernetes_is_in_host_network': True, 'malware_scan_status': 'malware_scan_status',
            'kubernetes_labels': {'key': ''}, 'containers': [{'vulnerabilities_count': 6, 'secrets_count': 1,
            'kubernetes_cluster_name': 'kubernetes_cluster_name', 'docker_container_state': 'docker_container_state',
            'cpu_max': 0.8008281904610115, 'memory_usage': 5, 'secret_latest_scan_id': 'secret_latest_scan_id',
            'docker_container_network_mode': 'docker_container_network_mode', 'vulnerability_latest_scan_id':
            'vulnerability_latest_scan_id', 'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status':
            'malware_scan_status', 'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system':
            True, 'image': None, 'processes': [{'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3,
            'open_files_count': 2, 'threads': 1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets',
            'active_secrets'], 'cmdline': 'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares':
            ['active_malwares', 'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id':
            'node_id'}, {'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2,
            'threads': 1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'],
            'cmdline': 'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'},
            {'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count':
            2, 'threads': 1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'],
            'cmdline': 'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'},
            {'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads':
            1, 'pid': 4, 'ppid': 7, 'memory_max': 9, 'active_secrets': ['active_secrets', 'active_secrets'], 'cmdline':
            'cmdline', 'active_cves': ['active_cves', 'active_cves'], 'active_malwares': ['active_malwares',
            'active_malwares'], 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id'}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}],
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}],
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}],
            'node_name': 'node_name', 'agent_running': True, 'node_id': 'node_id'}

    Attributes:
        agent_running (bool):
        hosts (Union[List['ModelHost'], None]):
        node_id (str):
        node_name (str):
    """

    agent_running: bool
    hosts: Union[List["ModelHost"], None]
    node_id: str
    node_name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        agent_running = self.agent_running

        hosts: Union[List[Dict[str, Any]], None]
        if isinstance(self.hosts, list):
            hosts = []
            for hosts_type_0_item_data in self.hosts:
                hosts_type_0_item = hosts_type_0_item_data.to_dict()
                hosts.append(hosts_type_0_item)

        else:
            hosts = self.hosts

        node_id = self.node_id

        node_name = self.node_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_running": agent_running,
                "hosts": hosts,
                "node_id": node_id,
                "node_name": node_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_host import ModelHost

        d = src_dict.copy()
        agent_running = d.pop("agent_running")

        def _parse_hosts(data: object) -> Union[List["ModelHost"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                hosts_type_0 = []
                _hosts_type_0 = data
                for hosts_type_0_item_data in _hosts_type_0:
                    hosts_type_0_item = ModelHost.from_dict(hosts_type_0_item_data)

                    hosts_type_0.append(hosts_type_0_item)

                return hosts_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelHost"], None], data)

        hosts = _parse_hosts(d.pop("hosts"))

        node_id = d.pop("node_id")

        node_name = d.pop("node_name")

        model_kubernetes_cluster = cls(
            agent_running=agent_running,
            hosts=hosts,
            node_id=node_id,
            node_name=node_name,
        )

        model_kubernetes_cluster.additional_properties = d
        return model_kubernetes_cluster

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
