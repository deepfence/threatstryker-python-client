# ThreatStryker CLI Tool

A comprehensive command-line interface for ThreatStryker security operations, enabling users to authenticate, discover resources, and perform various security scans across their infrastructure.

## Features

### 🔐 Authentication
- API key-based authentication  
- SSL verification support (optional)
- Interactive and command-line authentication modes

### 🔍 Resource Discovery
- **List Hosts**: Discover all host systems in your environment
- **List Containers**: Find all running containers  
- **List Pods**: Discover Kubernetes pods
- **List Runtime Incidents**: View security alerts and runtime incidents

### 🛡️ Security Scanning
- **Vulnerability Scanning**: Multi-language vulnerability detection
- **Secret Scanning**: Detect exposed secrets and credentials
- **Malware Scanning**: Identify malicious files and threats

### 📊 Interactive Interface
- User-friendly menu system
- Resource selection (individual or bulk)
- Formatted table output with scan status information

## Installation

First, install the ThreatStryker Python client:

```bash
pip install git+https://github.com/deepfence/threatstryker-python-client.git
```

## Usage

### Interactive Mode (Recommended)

Run the CLI tool in interactive mode:

```bash
python threatstryker_cli.py
```

The tool will prompt you for:
- ThreatStryker Console URL
- API Key (hidden input)
- SSL verification preference

### Command Line Arguments

You can also provide authentication details via command line:

```bash
python threatstryker_cli.py --url https://your-console.example.com --api-key YOUR_API_KEY
```

#### Command Line Options

- `--url`: ThreatStryker console URL
- `--api-key`: API key for authentication
- `--no-ssl-verify`: Disable SSL certificate verification
- `--version`: Show version information
- `--help`: Display help message

### Example Usage Flow

1. **Start the CLI**:
   ```bash
   python threatstryker_cli.py
   ```

2. **Authenticate** with your ThreatStryker console

3. **Discover Resources**:
   - Choose option 1 to list hosts
   - Choose option 2 to list containers  
   - Choose option 3 to list pods
   - Choose option 4 to view runtime incidents

4. **Perform Security Operations**:
   - Select specific resources or all resources
   - Choose from vulnerability, secret, or malware scanning
   - View scan initiation confirmation and IDs

## Workflow Examples

### Host Security Scanning

```
🔍 Resource Discovery Options:
1. List Hosts
2. List Containers
3. List Pods
4. List Runtime Incidents (Alerts)
5. Exit

Select an option (1-5): 1

🖥️  Fetching hosts...

📊 Hosts (5 items):
========================================
node_id              | host_name            | agent_running        | os                   | vulnerabilities_count| secrets_count        | malwares_count       
host-001             | prod-server-01       | True                 | ubuntu               | 23                   | 5                    | 0                    
host-002             | prod-server-02       | True                 | centos               | 15                   | 2                    | 1                    

🔧 Host Operations:
1. Start Vulnerability Scan
2. Start Secret Scan  
3. Start Malware Scan
4. List Runtime Incidents
5. Back to Main Menu

Select operation (1-5): 1

🎯 Select hosts for operations:
0. Select All
1. prod-server-01 (host-001)
2. prod-server-02 (host-002)

Enter numbers (comma-separated) or 0 for all hosts: 1,2

✅ Vulnerability scan started successfully!
   Scan IDs: ['scan-12345', 'scan-12346']  
   Bulk Scan ID: bulk-scan-789
```

### Container Discovery and Scanning

```
Select option: 2

🐳 Fetching containers...

📊 Containers (12 items):
========================================
node_id              | docker_container_name| kubernetes_namespace | vulnerabilities_count| secrets_count        | malwares_count       
container-001        | web-frontend         | production           | 8                    | 1                    | 0                    
container-002        | api-backend          | production           | 12                   | 3                    | 0                    

🔧 Container Operations:
1. Start Vulnerability Scan
2. Start Secret Scan
3. Start Malware Scan  
4. Back to Main Menu

Select operation (1-4): 2

✅ Secret scan started successfully!
   Scan IDs: ['secret-scan-456', 'secret-scan-457']
```

## Supported Scan Types

### Vulnerability Scanning
Supports multiple programming languages:
- Base system vulnerabilities
- Java applications
- JavaScript/Node.js
- Rust applications  
- Go applications
- Ruby applications
- Python applications
- PHP applications
- .NET applications

### Secret Scanning
Detects exposed:
- API keys
- Database credentials
- SSH keys
- OAuth tokens
- Other sensitive data

### Malware Scanning
Identifies:
- Known malware signatures
- Suspicious file patterns
- Potentially unwanted programs (PUPs)

## Output Information

### Host Information
- Node ID and hostname
- Agent status
- Operating system
- Vulnerability, secret, and malware counts
- Scan status for each type

### Container Information  
- Container name and node ID
- Host system information
- Kubernetes cluster and namespace
- Security findings counts
- Current scan statuses

### Pod Information
- Pod name and namespace
- Kubernetes cluster details
- Host information
- Security scan statuses

### Runtime Incidents
- Alert types and severity
- Affected nodes
- Timestamps
- Descriptions

## Error Handling

The CLI includes comprehensive error handling:
- Authentication failures
- Network connectivity issues
- API response errors
- Invalid user input
- Resource not found scenarios

## Requirements

- Python 3.7+
- ThreatStryker Python client library
- Valid ThreatStryker console access
- API key with appropriate permissions

## API Key Generation

To generate an API key:
1. Log into your ThreatStryker console
2. Navigate to Settings → User Management  
3. Click "Api key"
4. Generate and copy your new API key

## Security Notes

- API keys are entered securely (hidden input)
- SSL verification is enabled by default
- No credentials are stored or logged
- All communications use HTTPS

## Troubleshooting

### Common Issues

**Authentication Failed**
- Verify console URL is correct and accessible
- Check API key validity and permissions
- Ensure SSL certificates are valid (or use `--no-ssl-verify`)

**No Resources Found**
- Verify agents are deployed and running
- Check user permissions for resource access
- Confirm resources exist in the environment

**Scan Failures**
- Ensure selected resources are online
- Verify sufficient system resources
- Check scan permissions and policies

### Debug Information

For additional debugging, the CLI provides detailed error messages including:
- HTTP status codes
- API response details
- Network connectivity information

## Contributing

This CLI tool is part of the ThreatStryker Python client project. For contributions or issues:

1. Check existing issues in the GitHub repository
2. Submit bug reports with detailed information
3. Contribute improvements via pull requests

## License

This tool is distributed under the same license as the ThreatStryker Python client. 