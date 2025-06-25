#!/usr/bin/env python3
"""
ThreatStryker CLI Tool
A comprehensive command-line interface for ThreatStryker operations.
"""

import argparse
import getpass
from typing import List, Dict, Any, Optional

# ThreatStryker imports
from threatstryker import AuthenticatedClient, Client
from threatstryker.api.authentication import auth_token
from threatstryker.api.malware_scan import start_malware_scan
from threatstryker.api.search import (
    search_hosts,
    search_containers,
    search_pods,
    search_alerts,
)
from threatstryker.api.secret_scan import start_secret_scan
from threatstryker.api.vulnerability import start_vulnerability_scan
from threatstryker.errors import UnexpectedStatus
from threatstryker.models import (
    SearchSearchNodeReq,
    ModelVulnerabilityScanTriggerReq,
    ModelSecretScanTriggerReq,
    ModelMalwareScanTriggerReq,
    ModelAPIAuthRequest,
)


class ThreatStrykerCLI:
    """Main CLI class for ThreatStryker operations."""

    def __init__(self):
        self.client: Optional[AuthenticatedClient] = None
        self.base_url = None
        self.api_key = None

    def authenticate(self, base_url: str, api_key: str, verify_ssl: bool = True):
        """Authenticate with ThreatStryker API."""
        try:
            self.base_url = base_url
            self.api_key = api_key

            body = ModelAPIAuthRequest(
                api_token=api_key
            )
            api_response = auth_token.sync(client=Client(base_url=base_url), body=body)

            if verify_ssl:
                self.client = AuthenticatedClient(base_url=base_url, token=api_response.access_token)
            else:
                self.client = AuthenticatedClient(
                    base_url=base_url, token=api_response.access_token, verify_ssl=False
                )

            print(f"✅ Successfully authenticated with {base_url}")
            return True
        except Exception as e:
            print(f"❌ Authentication failed: {e}")
            return False

    def create_search_payload(
            self, size: int = 100, offset: int = 0, active_only: bool = True
    ) -> Dict[str, Any]:
        """Create standard search payload for listing resources."""
        return {
            "node_filter": {
                "filters": {
                    "compare_filter": None,
                    "contains_filter": {
                        "filter_in": {"active": [active_only] if active_only else {}}
                    },
                    "match_filter": {"filter_in": None},
                    "not_contains_filter": {"filter_in": {}},
                    "order_filter": {"order_fields": []},
                },
                "in_field_filter": None,
                "window": {"offset": 0, "size": 0},
            },
            "window": {"offset": offset, "size": size},
        }

    def list_hosts(self) -> List[Dict[str, Any]]:
        """List all hosts in the environment."""
        if not self.client:
            print("❌ Client not authenticated")
            return []

        try:
            payload = {
                "node_filter": {
                    "filters": {
                        "compare_filter": None,
                        "contains_filter": {"filter_in": {"active": [True], "pseudo": [False]}},
                        "match_filter": {"filter_in": None},
                        "not_contains_filter": {"filter_in": {}},
                        "order_filter": {"order_fields": []},
                    },
                    "in_field_filter": None,
                    "window": {"offset": 0, "size": 0},
                },
                "window": {"offset": 0, "size": 100},
            }
            body = SearchSearchNodeReq.from_dict(payload)
            hosts = search_hosts.sync(client=self.client, body=body)

            if not hosts:
                return []

            host_list = []
            # API returns List[ModelHost] on success, error objects on failure
            if isinstance(hosts, list):
                for host in hosts:
                    host_info = {
                        "node_id": host.node_id,
                        "node_name": host.node_name,
                        "host_name": host.host_name,
                        "agent_running": host.agent_running,
                        "os": host.os,
                        "cloud_provider": host.cloud_provider,
                        "vulnerabilities_count": host.vulnerabilities_count,
                        "secrets_count": host.secrets_count,
                        "malwares_count": host.malwares_count,
                        "compliance_scan_status": host.compliance_scan_status,
                        "vulnerability_scan_status": host.vulnerability_scan_status,
                        "secret_scan_status": host.secret_scan_status,
                        "malware_scan_status": host.malware_scan_status,
                    }
                    host_list.append(host_info)
            else:
                # Handle error responses
                print(f"❌ API returned error response: {hosts}")
                return []

            return host_list
        except UnexpectedStatus as e:
            print(f"❌ Error listing hosts: {e}")
            return []
        except Exception as e:
            print(f"❌ Unexpected error listing hosts: {e}")
            return []

    def list_containers(self) -> List[Dict[str, Any]]:
        """List all containers in the environment."""
        if not self.client:
            print("❌ Client not authenticated")
            return []

        try:
            payload = {
                "node_filter": {
                    "filters": {
                        "compare_filter": None,
                        "contains_filter": {"filter_in": {"active": [True], "pseudo": [False]}},
                        "match_filter": {"filter_in": None},
                        "not_contains_filter": {"filter_in": {}},
                        "order_filter": {"order_fields": []},
                    },
                    "in_field_filter": None,
                    "window": {"offset": 0, "size": 0},
                },
                "window": {"offset": 0, "size": 100},
            }
            body = SearchSearchNodeReq.from_dict(payload)
            containers = search_containers.sync(client=self.client, body=body)

            if not containers:
                return []

            container_list = []
            # Check if containers is iterable (list) or handle single response
            if hasattr(containers, "__iter__") and not isinstance(containers, str):
                for container in containers:
                    container_info = {
                        "node_id": container.node_id,
                        "node_name": container.node_name,
                        "docker_container_name": container.docker_container_name,
                        "host_name": container.host_name,
                        "docker_container_state": container.docker_container_state,
                        "kubernetes_cluster_name": container.kubernetes_cluster_name,
                        "kubernetes_namespace": container.kubernetes_namespace,
                        "vulnerabilities_count": container.vulnerabilities_count,
                        "secrets_count": container.secrets_count,
                        "malwares_count": container.malwares_count,
                        "vulnerability_scan_status": container.vulnerability_scan_status,
                        "secret_scan_status": container.secret_scan_status,
                        "malware_scan_status": container.malware_scan_status,
                    }
                    container_list.append(container_info)
            else:
                # Handle single container response
                container_info = {
                    "node_id": containers.node_id,
                    "node_name": containers.node_name,
                    "docker_container_name": containers.docker_container_name,
                    "host_name": containers.host_name,
                    "docker_container_state": containers.docker_container_state,
                    "kubernetes_cluster_name": containers.kubernetes_cluster_name,
                    "kubernetes_namespace": containers.kubernetes_namespace,
                    "vulnerabilities_count": containers.vulnerabilities_count,
                    "secrets_count": containers.secrets_count,
                    "malwares_count": containers.malwares_count,
                    "vulnerability_scan_status": containers.vulnerability_scan_status,
                    "secret_scan_status": containers.secret_scan_status,
                    "malware_scan_status": containers.malware_scan_status,
                }
                container_list.append(container_info)

            return container_list
        except UnexpectedStatus as e:
            print(f"❌ Error listing containers: {e}")
            return []
        except Exception as e:
            print(f"❌ Unexpected error listing containers: {e}")
            return []

    def list_pods(self) -> List[Dict[str, Any]]:
        """List all pods in the environment."""
        if not self.client:
            print("❌ Client not authenticated")
            return []

        try:
            payload = self.create_search_payload()
            body = SearchSearchNodeReq.from_dict(payload)
            pods = search_pods.sync(client=self.client, body=body)

            if not pods:
                return []

            pod_list = []
            # Check if pods is iterable (list) or handle single response
            if hasattr(pods, "__iter__") and not isinstance(pods, str):
                for pod in pods:
                    pod_info = {
                        "node_id": pod.node_id,
                        "node_name": pod.node_name,
                        "pod_name": pod.pod_name,
                        "host_name": pod.host_name,
                        "kubernetes_cluster_name": pod.kubernetes_cluster_name,
                        "kubernetes_namespace": pod.kubernetes_namespace,
                        "kubernetes_state": pod.kubernetes_state,
                        "vulnerability_scan_status": pod.vulnerability_scan_status,
                        "secret_scan_status": pod.secret_scan_status,
                        "malware_scan_status": pod.malware_scan_status,
                    }
                    pod_list.append(pod_info)
            else:
                # Handle single pod response
                pod_info = {
                    "node_id": pods.node_id,
                    "node_name": pods.node_name,
                    "pod_name": pods.pod_name,
                    "host_name": pods.host_name,
                    "kubernetes_cluster_name": pods.kubernetes_cluster_name,
                    "kubernetes_namespace": pods.kubernetes_namespace,
                    "kubernetes_state": pods.kubernetes_state,
                    "vulnerability_scan_status": pods.vulnerability_scan_status,
                    "secret_scan_status": pods.secret_scan_status,
                    "malware_scan_status": pods.malware_scan_status,
                }
                pod_list.append(pod_info)

            return pod_list
        except UnexpectedStatus as e:
            print(f"❌ Error listing pods: {e}")
            return []
        except Exception as e:
            print(f"❌ Unexpected error listing pods: {e}")
            return []

    def list_runtime_incidents(self) -> List[Dict[str, Any]]:
        """List runtime incidents/alerts."""
        if not self.client:
            print("❌ Client not authenticated")
            return []

        try:
            payload = {
                "extended_node_filter": {
                    "filters": {
                        "compare_filter": None,
                        "contains_filter": {"filter_in": {}},
                        "contains_in_array_filter": {"filter_in": {}},
                        "match_filter": {"filter_in": {}},
                        "order_filter": {"order_fields": []},
                    },
                    "in_field_filter": None,
                    "window": {"offset": 0, "size": 0},
                },
                "node_filter": {
                    "filters": {
                        "compare_filter": None,
                        "contains_filter": {"filter_in": {}},
                        "match_filter": {"filter_in": {}},
                        "order_filter": {
                            "order_fields": [
                                {"descending": True, "field_name": "updated_at"}
                            ]
                        },
                    },
                    "in_field_filter": None,
                    "window": {"offset": 0, "size": 0},
                },
                "window": {"offset": 0, "size": 100},
            }

            body = SearchSearchNodeReq.from_dict(payload)
            alerts = search_alerts.sync(client=self.client, body=body)

            if not alerts:
                return []

            alert_list = []
            # Check if alerts is iterable (list) or handle single response
            if hasattr(alerts, "__iter__") and not isinstance(alerts, str):
                for alert in alerts:
                    alert_info = {
                        "node_id": getattr(alert, "node_id", "N/A"),
                        "node_name": getattr(alert, "node_name", "N/A"),
                        "alert_type": getattr(alert, "alert_type", "N/A"),
                        "description": getattr(alert, "description", "N/A"),
                        "severity": getattr(alert, "severity", "N/A"),
                        "updated_at": getattr(alert, "updated_at", "N/A"),
                        "created_at": getattr(alert, "created_at", "N/A"),
                    }
                    alert_list.append(alert_info)
            else:
                # Handle single alert response
                alert_info = {
                    "node_id": getattr(alerts, "node_id", "N/A"),
                    "node_name": getattr(alerts, "node_name", "N/A"),
                    "alert_type": getattr(alerts, "alert_type", "N/A"),
                    "description": getattr(alerts, "description", "N/A"),
                    "severity": getattr(alerts, "severity", "N/A"),
                    "updated_at": getattr(alerts, "updated_at", "N/A"),
                    "created_at": getattr(alerts, "created_at", "N/A"),
                }
                alert_list.append(alert_info)

            return alert_list
        except UnexpectedStatus as e:
            print(f"❌ Error listing runtime incidents: {e}")
            return []
        except Exception as e:
            print(f"❌ Unexpected error listing runtime incidents: {e}")
            return []

    def create_node_list(
            self, resources: List[Dict[str, Any]], resource_type: str
    ) -> List[Dict[str, str]]:
        """Create node list for scan operations."""
        node_list = []
        for resource in resources:
            node_list.append(
                {"node_id": resource["node_id"], "node_type": resource_type}
            )
        return node_list

    def start_vulnerability_scan(self, node_list: List[Dict[str, str]]) -> bool:
        """Start vulnerability scan on selected nodes."""
        if not self.client:
            print("❌ Client not authenticated")
            return False

        try:
            scan_config = [
                {"language": "base"},
                {"language": "java"},
                {"language": "javascript"},
                {"language": "rust"},
                {"language": "golang"},
                {"language": "ruby"},
                {"language": "python"},
                {"language": "php"},
                {"language": "dotnet"},
            ]

            payload = {
                "filters": {
                    "cloud_account_scan_filter": {"filter_in": None},
                    "container_scan_filter": {"filter_in": None},
                    "host_scan_filter": {"filter_in": None},
                    "image_scan_filter": {"filter_in": None},
                    "kubernetes_cluster_scan_filter": {"filter_in": None},
                },
                "node_ids": node_list,
                "scan_config": scan_config,
            }

            body = ModelVulnerabilityScanTriggerReq.from_dict(payload)
            response = start_vulnerability_scan.sync(client=self.client, body=body)

            if response:
                print(f"✅ Vulnerability scan started successfully!")
                print(f"   Scan IDs: {response.scan_ids}")
                if hasattr(response, "bulk_scan_id"):
                    print(f"   Bulk Scan ID: {response.bulk_scan_id}")
                return True
            return False
        except UnexpectedStatus as e:
            print(f"❌ Error starting vulnerability scan: {e}")
            return False
        except Exception as e:
            print(f"❌ Unexpected error starting vulnerability scan: {e}")
            return False

    def start_secret_scan(self, node_list: List[Dict[str, str]]) -> bool:
        """Start secret scan on selected nodes."""
        if not self.client:
            print("❌ Client not authenticated")
            return False

        try:
            payload = {
                "filters": {
                    "cloud_account_scan_filter": {"filter_in": None},
                    "container_scan_filter": {"filter_in": None},
                    "host_scan_filter": {"filter_in": None},
                    "image_scan_filter": {"filter_in": None},
                    "kubernetes_cluster_scan_filter": {"filter_in": None},
                },
                "node_ids": node_list,
            }

            body = ModelSecretScanTriggerReq.from_dict(payload)
            response = start_secret_scan.sync(client=self.client, body=body)

            if response:
                print(f"✅ Secret scan started successfully!")
                print(f"   Scan IDs: {response.scan_ids}")
                if hasattr(response, "bulk_scan_id"):
                    print(f"   Bulk Scan ID: {response.bulk_scan_id}")
                return True
            return False
        except UnexpectedStatus as e:
            print(f"❌ Error starting secret scan: {e}")
            return False
        except Exception as e:
            print(f"❌ Unexpected error starting secret scan: {e}")
            return False

    def start_malware_scan(self, node_list: List[Dict[str, str]]) -> bool:
        """Start malware scan on selected nodes."""
        if not self.client:
            print("❌ Client not authenticated")
            return False

        try:
            payload = {
                "filters": {
                    "cloud_account_scan_filter": {"filter_in": None},
                    "container_scan_filter": {"filter_in": None},
                    "host_scan_filter": {"filter_in": None},
                    "image_scan_filter": {"filter_in": None},
                    "kubernetes_cluster_scan_filter": {"filter_in": None},
                },
                "node_ids": node_list,
            }

            body = ModelMalwareScanTriggerReq.from_dict(payload)
            response = start_malware_scan.sync(client=self.client, body=body)

            if response:
                print(f"✅ Malware scan started successfully!")
                print(f"   Scan IDs: {response.scan_ids}")
                if hasattr(response, "bulk_scan_id"):
                    print(f"   Bulk Scan ID: {response.bulk_scan_id}")
                return True
            return False
        except UnexpectedStatus as e:
            print(f"❌ Error starting malware scan: {e}")
            return False
        except Exception as e:
            print(f"❌ Unexpected error starting malware scan: {e}")
            return False

    def display_table(self, data: List[Dict[str, Any]], title: str, max_rows: int = 50):
        """Display data in a formatted table."""
        if not data:
            print(f"\n📊 {title}: No data found")
            return

        print(f"\n📊 {title} ({len(data)} items):")
        print("=" * 100)

        # Limit display for readability
        display_data = data[:max_rows]
        if len(data) > max_rows:
            print(f"Showing first {max_rows} of {len(data)} items...\n")

        # Print headers
        if display_data:
            headers = list(display_data[0].keys())
            header_line = " | ".join(f"{h:20}" for h in headers)
            print(header_line)
            print("-" * len(header_line))

            # Print data rows
            for item in display_data:
                row = " | ".join(f"{str(item.get(h, 'N/A'))[:20]:20}" for h in headers)
                print(row)

        print("=" * 100)

    def select_resources(
            self, resources: List[Dict[str, Any]], resource_type: str
    ) -> List[Dict[str, Any]]:
        """Allow user to select specific resources from the list."""
        if not resources:
            print(f"No {resource_type} available for selection.")
            return []

        print(f"\n🎯 Select {resource_type} for operations:")
        print("0. Select All")

        for i, resource in enumerate(resources, 1):
            name = resource.get(
                "node_name",
                resource.get("host_name", resource.get("pod_name", "Unknown")),
            )
            print(f"{i}. {name} ({resource.get('node_id', 'Unknown ID')})")

        while True:
            try:
                selection = input(
                    f"\nEnter numbers (comma-separated) or 0 for all {resource_type}: "
                ).strip()

                if selection == "0":
                    return resources

                indices = [int(x.strip()) - 1 for x in selection.split(",")]
                selected = [resources[i] for i in indices if 0 <= i < len(resources)]

                if selected:
                    return selected
                else:
                    print("❌ Invalid selection. Please try again.")
            except (ValueError, IndexError):
                print("❌ Invalid input. Please enter valid numbers.")

    def interactive_mode(self):
        """Run the CLI in interactive mode."""
        print("🛡️  ThreatStryker CLI Tool")
        print("=" * 50)

        # Authentication
        if not self.client:
            base_url = input("Enter ThreatStryker Console URL: ").strip()
            api_key = getpass.getpass("Enter API Key: ").strip()

            ssl_verify = input("Verify SSL? (y/n) [y]: ").strip().lower()
            verify_ssl = ssl_verify != "n"

            if not self.authenticate(base_url, api_key, verify_ssl):
                return

        while True:
            print("\n🔍 Resource Discovery Options:")
            print("1. List Hosts")
            print("2. List Containers")
            print("3. List Pods")
            print("4. List Runtime Incidents (Alerts)")
            print("5. Exit")

            choice = input("\nSelect an option (1-5): ").strip()

            if choice == "1":
                self.handle_hosts()
            elif choice == "2":
                self.handle_containers()
            elif choice == "3":
                self.handle_pods()
            elif choice == "4":
                self.handle_runtime_incidents()
            elif choice == "5":
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please select 1-5.")

    def handle_hosts(self):
        """Handle host-related operations."""
        print("\n🖥️  Fetching hosts...")
        hosts = self.list_hosts()
        self.display_table(hosts, "Hosts")

        if not hosts:
            return

        while True:
            print("\n🔧 Host Operations:")
            print("1. Start Vulnerability Scan")
            print("2. Start Secret Scan")
            print("3. Start Malware Scan")
            print("4. List Runtime Incidents")
            print("5. Back to Main Menu")

            choice = input("\nSelect operation (1-5): ").strip()

            if choice in ["1", "2", "3"]:
                selected_hosts = self.select_resources(hosts, "hosts")
                if selected_hosts:
                    node_list = self.create_node_list(selected_hosts, "host")

                    if choice == "1":
                        self.start_vulnerability_scan(node_list)
                    elif choice == "2":
                        self.start_secret_scan(node_list)
                    elif choice == "3":
                        self.start_malware_scan(node_list)
            elif choice == "4":
                self.handle_runtime_incidents()
            elif choice == "5":
                break
            else:
                print("❌ Invalid choice. Please select 1-5.")

    def handle_containers(self):
        """Handle container-related operations."""
        print("\n🐳 Fetching containers...")
        containers = self.list_containers()
        self.display_table(containers, "Containers")

        if not containers:
            return

        while True:
            print("\n🔧 Container Operations:")
            print("1. Start Vulnerability Scan")
            print("2. Start Secret Scan")
            print("3. Start Malware Scan")
            print("4. Back to Main Menu")

            choice = input("\nSelect operation (1-4): ").strip()

            if choice in ["1", "2", "3"]:
                selected_containers = self.select_resources(containers, "containers")
                if selected_containers:
                    node_list = self.create_node_list(selected_containers, "container")

                    if choice == "1":
                        self.start_vulnerability_scan(node_list)
                    elif choice == "2":
                        self.start_secret_scan(node_list)
                    elif choice == "3":
                        self.start_malware_scan(node_list)
            elif choice == "4":
                break
            else:
                print("❌ Invalid choice. Please select 1-4.")

    def handle_pods(self):
        """Handle pod-related operations."""
        print("\n🎯 Fetching pods...")
        pods = self.list_pods()
        self.display_table(pods, "Pods")

        if not pods:
            return

        while True:
            print("\n🔧 Pod Operations:")
            print("1. Start Vulnerability Scan")
            print("2. Start Secret Scan")
            print("3. Start Malware Scan")
            print("4. Back to Main Menu")

            choice = input("\nSelect operation (1-4): ").strip()

            if choice in ["1", "2", "3"]:
                selected_pods = self.select_resources(pods, "pods")
                if selected_pods:
                    node_list = self.create_node_list(selected_pods, "pod")

                    if choice == "1":
                        self.start_vulnerability_scan(node_list)
                    elif choice == "2":
                        self.start_secret_scan(node_list)
                    elif choice == "3":
                        self.start_malware_scan(node_list)
            elif choice == "4":
                break
            else:
                print("❌ Invalid choice. Please select 1-4.")

    def handle_runtime_incidents(self):
        """Handle runtime incidents/alerts."""
        print("\n🚨 Fetching runtime incidents...")
        incidents = self.list_runtime_incidents()
        self.display_table(incidents, "Runtime Incidents/Alerts")

        input("\nPress Enter to continue...")


def main():
    """Main entry point for the CLI tool."""
    parser = argparse.ArgumentParser(
        description="ThreatStryker CLI Tool - Comprehensive security operations",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                           # Interactive mode
  %(prog)s --url https://console.example.com --api-key YOUR_KEY
        """,
    )

    parser.add_argument("--url", help="ThreatStryker console URL")
    parser.add_argument("--api-key", help="API key for authentication")
    parser.add_argument(
        "--no-ssl-verify",
        action="store_true",
        help="Disable SSL certificate verification",
    )
    parser.add_argument(
        "--version", action="version", version="ThreatStryker CLI v1.0.0"
    )

    args = parser.parse_args()

    cli = ThreatStrykerCLI()

    # If URL and API key provided via arguments, authenticate directly
    if args.url and args.api_key:
        verify_ssl = not args.no_ssl_verify
        if cli.authenticate(args.url, args.api_key, verify_ssl):
            cli.interactive_mode()
    else:
        # Run in interactive mode
        cli.interactive_mode()


if __name__ == "__main__":
    main()
