<div align="center">

# 🛡️ Embracing the DevSecOps Paradigm

### Building a Comprehensive DevSecOps Pipeline from Scratch

![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)
![SonarQube](https://img.shields.io/badge/SonarQube-4E9BCD?style=for-the-badge&logo=sonarqube&logoColor=white)
![OWASP](https://img.shields.io/badge/OWASP-000000?style=for-the-badge&logo=owasp&logoColor=white)
![HashiCorp Vault](https://img.shields.io/badge/HashiCorp_Vault-000000?style=for-the-badge&logo=vault&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![Open Policy Agent](https://img.shields.io/badge/Open_Policy_Agent-7D9199?style=for-the-badge&logo=openpolicyagent&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu_20.04-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

</div>

---

## 📋 Table of Contents

- [🎯 Learning Objectives](#-learning-objectives)
- [📌 Prerequisites](#-prerequisites)
- [🖥️ Lab Environment Setup](#️-lab-environment-setup)
- [🧩 Part 1: Setting Up the DevSecOps Pipeline Foundation](#-part-1-setting-up-the-devsecops-pipeline-foundation)
- [🔍 Part 2: Integrating Security Scanning Tools](#-part-2-integrating-security-scanning-tools)
- [🔐 Part 3: Implementing Secret Management with HashiCorp Vault](#-part-3-implementing-secret-management-with-hashicorp-vault)
- [🏗️ Part 4: Infrastructure as Code with Terraform](#️-part-4-infrastructure-as-code-with-terraform)
- [⚖️ Part 5: Integrating Open Policy Agent (OPA)](#️-part-5-integrating-open-policy-agent-opa)
- [🔄 Part 6: Creating a CI/CD Pipeline](#-part-6-creating-a-cicd-pipeline)
- [🧠 Part 7: Application Architecture and Threat Modeling](#-part-7-application-architecture-and-threat-modeling)
- [🗺️ MITRE ATT&CK Mapping](#️-mitre-attck-mapping)
- [🧯 Troubleshooting](#-troubleshooting)
- [✅ Conclusion](#-conclusion)

---

## 🎯 Learning Objectives

| # | Objective |
|---|-----------|
| 1 | Understand the core principles of DevSecOps and its importance in modern software development |
| 2 | Integrate security scanning tools (SonarQube, Dependency Check, ZAP) into CI/CD pipelines |
| 3 | Implement secret management using HashiCorp Vault |
| 4 | Create and validate Infrastructure as Code (IaC) templates using Terraform |
| 5 | Integrate Open Policy Agent (OPA) for policy enforcement |
| 6 | Design application architecture and perform threat modeling using Microsoft Threat Modeling Tool |
| 7 | Build a comprehensive DevSecOps pipeline from scratch |

## 📌 Prerequisites

| Requirement | Details |
|---|---|
| 🐧 Linux CLI | Basic understanding of software development lifecycle and Linux command-line operations |
| 🌿 Git | Basic knowledge of Git version control |
| 🐳 Containers | Understanding of containerization concepts (Docker) |
| 🌐 Networking | Basic networking concepts |
| 📄 Data Formats | Familiarity with YAML and JSON formats |

## 🖥️ Lab Environment Setup

> **☁️ Ready-to-Use Cloud Machines**
> Al Nafi provides pre-configured Linux-based cloud machines for this lab. Simply click **"Start Lab"** to access your dedicated environment — no need to build your own VM or install additional software.

**Your lab environment includes:**
- 🐧 Ubuntu 20.04 LTS with Docker and Docker Compose
- 🔧 Jenkins for CI/CD pipeline
- 🌿 Git for version control
- 📦 All required tools pre-installed

---

## 🧩 Part 1: Setting Up the DevSecOps Pipeline Foundation

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white) ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)

### Task 1.1: Initialize Your Project Repository

#### 🪜 Step 1: Create the Project Structure

```bash
# 📁 Navigate to home directory
cd ~

# 📁 Create main project directory
mkdir devsecops-lab
cd devsecops-lab

# 🌿 Initialize Git repository
git init

# 🗂️ Create basic project structure
mkdir -p {src,tests,infrastructure,policies,configs}
mkdir -p .github/workflows
```

```python
# 🐍 src/app.py — intentionally vulnerable Flask app used as the scan target
cat > src/app.py << 'EOF'
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello DevSecOps World!"

@app.route('/api/data')
def get_data():
    # ⚠️ Intentional vulnerability for demonstration
    user_input = request.args.get('input', '')
    # TODO: Sanitize/escape user_input once the security scanners in Part 2 flag this line
    return f"You entered: {user_input}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
EOF
```

```text
# 📦 requirements.txt
cat > requirements.txt << 'EOF'
Flask==2.3.3
requests==2.31.0
EOF
```

```dockerfile
# 🐳 Dockerfile
cat > Dockerfile << 'EOF'
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ .

EXPOSE 5000

CMD ["python", "app.py"]
EOF
```

#### 🪜 Step 2: Create the Initial Git Commit

```bash
# ➕ Add all files to git
git add .

# 👤 Configure git (replace with your details)
git config user.name "DevSecOps Student"
git config user.email "student@example.com"
# TODO: Replace with your own name/email before committing

# ✅ Create initial commit
git commit -m "Initial project setup"
```

---

## 🔍 Part 2: Integrating Security Scanning Tools

![SonarQube](https://img.shields.io/badge/SonarQube-4E9BCD?style=flat-square&logo=sonarqube&logoColor=white) ![OWASP](https://img.shields.io/badge/OWASP_Dependency--Check-000000?style=flat-square&logo=owasp&logoColor=white) ![OWASP ZAP](https://img.shields.io/badge/OWASP_ZAP-000000?style=flat-square&logo=owasp&logoColor=white)

### Task 2.1: Setting Up SonarQube

#### 🪜 Step 1: Deploy SonarQube via Docker Compose

```yaml
# 🐳 docker-compose.sonarqube.yml
cat > docker-compose.sonarqube.yml << 'EOF'
version: '3.8'

services:
  sonarqube:
    image: sonarqube:9.9-community
    container_name: sonarqube
    ports:
      - "9000:9000"
    environment:
      - SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true
    volumes:
      - sonarqube_data:/opt/sonarqube/data
      - sonarqube_logs:/opt/sonarqube/logs
      - sonarqube_extensions:/opt/sonarqube/extensions

volumes:
  sonarqube_data:
  sonarqube_logs:
  sonarqube_extensions:
EOF

# ▶️ Start SonarQube
docker-compose -f docker-compose.sonarqube.yml up -d

# ⏳ Wait for SonarQube to start (this may take a few minutes)
echo "Waiting for SonarQube to start..."
sleep 60

# 🔎 Check if SonarQube is running
curl -f http://localhost:9000 && echo "SonarQube is running!" || echo "SonarQube is still starting..."
```

#### 🪜 Step 2: Configure the SonarQube Project

```ini
# ⚙️ sonar-project.properties
cat > sonar-project.properties << 'EOF'
sonar.projectKey=devsecops-lab
sonar.projectName=DevSecOps Lab Project
sonar.projectVersion=1.0
sonar.sources=src
sonar.language=py
sonar.sourceEncoding=UTF-8
sonar.python.coverage.reportPaths=coverage.xml
EOF
```

### Task 2.2: Setting Up OWASP Dependency-Check

#### 🪜 Step 1: Create the Dependency-Check Script

```bash
# 🛡️ scripts/dependency-check.sh
cat > scripts/dependency-check.sh << 'EOF'
#!/bin/bash

# 📁 Create scripts directory if it doesn't exist
mkdir -p scripts

# ⬇️ Download OWASP Dependency-Check
DEPENDENCY_CHECK_VERSION="8.4.0"
wget -O dependency-check.zip "https://github.com/jeremylong/DependencyCheck/releases/download/v${DEPENDENCY_CHECK_VERSION}/dependency-check-${DEPENDENCY_CHECK_VERSION}-release.zip"

# 📦 Extract and set up
unzip dependency-check.zip
mv dependency-check dependency-check-tool

# 🔎 Run dependency check
./dependency-check-tool/bin/dependency-check.sh \
    --project "DevSecOps Lab" \
    --scan . \
    --format HTML \
    --format JSON \
    --out reports/dependency-check

echo "Dependency check completed. Reports available in reports/dependency-check/"
EOF

# 🔑 Make script executable
chmod +x scripts/dependency-check.sh

# 📁 Create reports directory
mkdir -p reports/dependency-check
```

### Task 2.3: Setting Up OWASP ZAP

#### 🪜 Step 1: Create the ZAP Security Testing Script

```bash
# 🕷️ scripts/zap-scan.sh
cat > scripts/zap-scan.sh << 'EOF'
#!/bin/bash

# 📁 Create reports directory
mkdir -p reports/zap

# ▶️ Start the application in background for testing
echo "Starting application for security testing..."
python3 src/app.py &
APP_PID=$!

# ⏳ Wait for application to start
sleep 10

# 🔎 Run ZAP baseline scan using Docker
docker run -v $(pwd)/reports/zap:/zap/wrk/:rw \
    -t owasp/zap2docker-stable zap-baseline.py \
    -t http://host.docker.internal:5000 \
    -J zap-report.json \
    -r zap-report.html

# 🛑 Stop the application
kill $APP_PID

echo "ZAP security scan completed. Reports available in reports/zap/"
EOF

# 🔑 Make script executable
chmod +x scripts/zap-scan.sh
```

<details>
<summary>🧯 Troubleshooting: ZAP can't reach <code>host.docker.internal</code> on Linux</summary>

`host.docker.internal` resolves automatically on Docker Desktop (Mac/Windows) but not always on native Linux hosts. If the ZAP scan can't reach your Flask app:
- Add `--add-host=host.docker.internal:host-gateway` to the `docker run` command, or
- Replace the target URL with your host's Docker bridge IP (commonly `172.17.0.1`).

</details>

---

## 🔐 Part 3: Implementing Secret Management with HashiCorp Vault

![Vault](https://img.shields.io/badge/HashiCorp_Vault-000000?style=flat-square&logo=vault&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)

### Task 3.1: Setting Up Vault

#### 🪜 Step 1: Deploy Vault via Docker

```hcl
# 🔧 configs/vault-config.hcl
cat > configs/vault-config.hcl << 'EOF'
ui = true
disable_mlock = true

storage "file" {
  path = "/vault/data"
}

listener "tcp" {
  address = "0.0.0.0:8200"
  tls_disable = 1
}
EOF
```

```yaml
# 🐳 docker-compose.vault.yml
cat > docker-compose.vault.yml << 'EOF'
version: '3.8'

services:
  vault:
    image: vault:1.15.0
    container_name: vault
    ports:
      - "8200:8200"
    volumes:
      - ./configs/vault-config.hcl:/vault/config/vault-config.hcl
      - vault_data:/vault/data
    cap_add:
      - IPC_LOCK
    command: vault server -config=/vault/config/vault-config.hcl

volumes:
  vault_data:
EOF

# ▶️ Start Vault
docker-compose -f docker-compose.vault.yml up -d

# ⏳ Wait for Vault to start
sleep 10
```

#### 🪜 Step 2: Initialize and Configure Vault

```bash
# 🌐 Set Vault address
export VAULT_ADDR='http://localhost:8200'

# 🔑 Initialize Vault (save the output securely)
vault operator init -key-shares=1 -key-threshold=1 > vault-keys.txt
# ⚠️ Note: a single key-share/threshold is for lab convenience only — never use this in production

# 📤 Extract unseal key and root token
UNSEAL_KEY=$(grep 'Unseal Key 1:' vault-keys.txt | awk '{print $NF}')
ROOT_TOKEN=$(grep 'Initial Root Token:' vault-keys.txt | awk '{print $NF}')

# 🔓 Unseal Vault
vault operator unseal $UNSEAL_KEY

# 🔐 Log in to Vault
vault auth $ROOT_TOKEN

# ⚙️ Enable the KV secrets engine
vault secrets enable -path=secret kv-v2

# 💾 Store sample secrets
vault kv put secret/app/config \
    database_url="postgresql://user:pass@localhost:5432/mydb" \
    api_key="super-secret-api-key-12345" \
    jwt_secret="my-jwt-secret-key"
# TODO: Replace these placeholder secrets with values relevant to your own environment

echo "Vault setup completed!"
echo "Root Token: $ROOT_TOKEN"
echo "Unseal Key: $UNSEAL_KEY"
```

#### 🪜 Step 3: Create the Vault Integration Script

```python
# 🐍 scripts/vault-integration.py
cat > scripts/vault-integration.py << 'EOF'
#!/usr/bin/env python3

import hvac
import os
import sys

def get_secrets_from_vault():
    """Retrieve secrets from Vault"""

    # 🔌 Initialize Vault client
    client = hvac.Client(url='http://localhost:8200')

    # 🔑 Authenticate (in production, use proper auth methods)
    # TODO: Swap the static token below for AppRole or Kubernetes auth in production
    vault_token = os.getenv('VAULT_TOKEN')
    if not vault_token:
        print("Error: VAULT_TOKEN environment variable not set")
        sys.exit(1)

    client.token = vault_token

    try:
        # 📖 Read secrets
        secret_response = client.secrets.kv.v2.read_secret_version(
            path='app/config'
        )

        secrets = secret_response['data']['data']

        print("Successfully retrieved secrets from Vault:")
        for key in secrets.keys():
            print(f"- {key}: {'*' * len(secrets[key])}")

        return secrets

    except Exception as e:
        print(f"Error retrieving secrets: {e}")
        sys.exit(1)

if __name__ == "__main__":
    get_secrets_from_vault()
EOF

# 🔑 Make script executable
chmod +x scripts/vault-integration.py

# 📦 Install required Python package
pip3 install hvac
```

<details>
<summary>🧯 Troubleshooting: Vault stays "sealed" after a restart</summary>

Vault re-seals every time the container restarts (this is expected, secure-by-default behavior). Re-run `vault operator unseal $UNSEAL_KEY` after every restart, and keep `vault-keys.txt` out of version control.

</details>

---

## 🏗️ Part 4: Infrastructure as Code with Terraform

![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white) ![tfsec](https://img.shields.io/badge/tfsec-1F1F1F?style=flat-square&logo=aquasecurity&logoColor=white)

### Task 4.1: Creating Terraform Templates

#### 🪜 Step 1: Create the Basic Infrastructure Template

```bash
# 📁 Create Terraform directory structure
mkdir -p infrastructure/terraform/{modules,environments/dev}
```

```hcl
# 🏗️ infrastructure/terraform/main.tf
cat > infrastructure/terraform/main.tf << 'EOF'
terraform {
  required_version = ">= 1.0"
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {
  host = "unix:///var/run/docker.sock"
}

# 🌐 Create a network for our application
resource "docker_network" "app_network" {
  name = "devsecops-network"
}

# 🖼️ Create application container image
resource "docker_image" "app_image" {
  name = "devsecops-app:latest"
  build {
    context = "../../"
    dockerfile = "Dockerfile"
  }
}

resource "docker_container" "app_container" {
  name  = "devsecops-app"
  image = docker_image.app_image.image_id

  ports {
    internal = 5000
    external = 5000
  }

  networks_advanced {
    name = docker_network.app_network.name
  }

  env = [
    "ENVIRONMENT=development"
  ]
}

# 📤 Output the application URL
output "application_url" {
  value = "http://localhost:5000"
}
EOF
```

```hcl
# 🔧 infrastructure/terraform/variables.tf
cat > infrastructure/terraform/variables.tf << 'EOF'
variable "environment" {
  description = "Environment name"
  type        = string
  default     = "dev"
}

variable "app_port" {
  description = "Application port"
  type        = number
  default     = 5000
}

variable "app_name" {
  description = "Application name"
  type        = string
  default     = "devsecops-app"
}
EOF
```

#### 🪜 Step 2: Initialize and Plan Terraform

```bash
# 📂 Navigate to Terraform directory
cd infrastructure/terraform

# 🔧 Initialize Terraform
terraform init

# ✅ Validate configuration
terraform validate

# 📋 Plan the infrastructure
terraform plan -out=tfplan

# 👀 Show the plan
terraform show tfplan
```

### Task 4.2: Terraform Security Validation

#### 🪜 Step 1: Install and Configure tfsec

```bash
# ⬇️ Install tfsec (Terraform security scanner)
curl -s https://raw.githubusercontent.com/aquasecurity/tfsec/master/scripts/install_linux.sh | bash

# 📦 Move tfsec to PATH
sudo mv tfsec /usr/local/bin/
```

```yaml
# ⚙️ .tfsec.yml
cat > .tfsec.yml << 'EOF'
severity_overrides:
  HIGH: ERROR
  MEDIUM: WARNING
  LOW: INFO

exclude:
  - docker-port-exposed-to-internet
EOF

# 🔎 Run tfsec scan
tfsec . --format json --out tfsec-report.json
tfsec . --format lovely

echo "Terraform security scan completed!"
```

#### 🪜 Step 2: Create the Terraform Validation Script

```bash
# 🛡️ scripts/terraform-validate.sh
cat > ../../scripts/terraform-validate.sh << 'EOF'
#!/bin/bash

echo "=== Terraform Security Validation ==="

# 📂 Navigate to Terraform directory
cd infrastructure/terraform

# 1️⃣ Terraform format check
echo "1. Checking Terraform formatting..."
terraform fmt -check -recursive

# 2️⃣ Terraform validation
echo "2. Validating Terraform configuration..."
terraform validate

# 3️⃣ Security scanning with tfsec
echo "3. Running security scan with tfsec..."
tfsec . --format lovely

# 4️⃣ Plan validation
echo "4. Creating and validating Terraform plan..."
terraform plan -out=tfplan

# 5️⃣ Policy validation (if OPA policies exist)
if [ -f "../../policies/terraform.rego" ]; then
    echo "5. Validating against OPA policies..."
    terraform show -json tfplan > tfplan.json
    opa eval -d ../../policies -i tfplan.json "data.terraform.deny[x]"
fi

echo "=== Terraform validation completed ==="
EOF

# 🔑 Make script executable
chmod +x ../../scripts/terraform-validate.sh

# 🔙 Return to project root
cd ../../
```

<details>
<summary>🧯 Troubleshooting: <code>terraform init</code> fails to fetch the Docker provider</summary>

If `terraform init` can't download `kreuzwerker/docker`, confirm outbound internet access to `registry.terraform.io` and that the version constraint (`~> 3.0`) matches an available release. Corporate proxies often need `HTTPS_PROXY` set before `terraform init` runs.

</details>

---

## ⚖️ Part 5: Integrating Open Policy Agent (OPA)

![OPA](https://img.shields.io/badge/Open_Policy_Agent-7D9199?style=flat-square&logo=openpolicyagent&logoColor=white) ![Rego](https://img.shields.io/badge/Rego-7D9199?style=flat-square)

### Task 5.1: Setting Up OPA

#### 🪜 Step 1: Install OPA

```bash
# ⬇️ Download and install OPA
curl -L -o opa https://openpolicyagent.org/downloads/v0.57.0/opa_linux_amd64_static
chmod +x opa
sudo mv opa /usr/local/bin/

# ✅ Verify installation
opa version
```

#### 🪜 Step 2: Create OPA Policies

```bash
# 📁 Create policies directory structure
mkdir -p policies/{terraform,docker,kubernetes}
```

```rego
# ⚖️ policies/terraform.rego
cat > policies/terraform.rego << 'EOF'
package terraform

import rego.v1

# 🚫 Deny if containers expose ports to 0.0.0.0
deny contains msg if {
    resource := input.planned_values.root_module.resources[_]
    resource.type == "docker_container"
    port := resource.values.ports[_]
    port.external != null
    msg := sprintf("Container '%s' exposes port %d to all interfaces", [resource.name, port.external])
}

# 🚫 Deny if containers run as root
deny contains msg if {
    resource := input.planned_values.root_module.resources[_]
    resource.type == "docker_container"
    not resource.values.user
    msg := sprintf("Container '%s' runs as root user", [resource.name])
}

# ✅ Require environment specification
deny contains msg if {
    resource := input.planned_values.root_module.resources[_]
    resource.type == "docker_container"
    not has_environment_tag(resource)
    msg := sprintf("Container '%s' missing environment specification", [resource.name])
}

has_environment_tag(resource) if {
    env := resource.values.env[_]
    startswith(env, "ENVIRONMENT=")
}
EOF
```

```rego
# ⚖️ policies/docker.rego
cat > policies/docker.rego << 'EOF'
package docker

import rego.v1

# 🚫 Deny running containers as root
deny contains msg if {
    input.User == "root"
    msg := "Container should not run as root user"
}

# 🚫 Deny containers without health checks
deny contains msg if {
    not input.Config.Healthcheck
    msg := "Container should have health check configured"
}

# 🚫 Deny containers with privileged mode
deny contains msg if {
    input.HostConfig.Privileged == true
    msg := "Container should not run in privileged mode"
}
EOF
```

```rego
# ⚖️ policies/application.rego
cat > policies/application.rego << 'EOF'
package application

import rego.v1

# 🚫 Deny if debug mode is enabled in production
deny contains msg if {
    input.environment == "production"
    input.debug == true
    msg := "Debug mode should not be enabled in production"
}

# 🚫 Require HTTPS in production
deny contains msg if {
    input.environment == "production"
    input.protocol != "https"
    msg := "HTTPS must be used in production environment"
}
EOF
```

#### 🪜 Step 3: Create OPA Validation Scripts

```bash
# ⚖️ scripts/opa-validate.sh
cat > scripts/opa-validate.sh << 'EOF'
#!/bin/bash

echo "=== OPA Policy Validation ==="

# 1️⃣ Validate Terraform plan against policies
if [ -f "infrastructure/terraform/tfplan.json" ]; then
    echo "1. Validating Terraform plan against OPA policies..."
    opa eval -d policies -i infrastructure/terraform/tfplan.json "data.terraform.deny[x]"
else
    echo "1. No Terraform plan found, skipping validation"
fi

# 2️⃣ Validate Docker configuration
echo "2. Validating Docker configuration..."
docker inspect devsecops-app 2>/dev/null | opa eval -d policies -I "data.docker.deny[x]" || echo "Container not running"

# 3️⃣ Validate application configuration
echo "3. Validating application configuration..."
cat > temp-app-config.json << 'TEMP_EOF'
{
    "environment": "development",
    "debug": true,
    "protocol": "http"
}
TEMP_EOF

opa eval -d policies -i temp-app-config.json "data.application.deny[x]"
rm temp-app-config.json

echo "=== OPA validation completed ==="
EOF

# 🔑 Make script executable
chmod +x scripts/opa-validate.sh
```

<details>
<summary>🧯 Troubleshooting: <code>opa eval -d policies</code> returns no results</summary>

OPA resolves `-d policies` relative to your current working directory. If you run the validation script from a different folder than the project root, OPA silently loads zero policies. Always run `opa-validate.sh` from the project root, or pass an absolute path to `-d`.

</details>

---

## 🔄 Part 6: Creating a CI/CD Pipeline

![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=flat-square&logo=jenkins&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)

### Task 6.1: Jenkins Pipeline Configuration

#### 🪜 Step 1: Create the Jenkinsfile

```groovy
// 🔧 Jenkinsfile
cat > Jenkinsfile << 'EOF'
pipeline {
    agent any

    environment {
        VAULT_ADDR = 'http://localhost:8200'
        VAULT_TOKEN = credentials('vault-token')
        // TODO: Create the 'vault-token' credential in Jenkins before running this pipeline
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Security Scan - Secrets') {
            steps {
                script {
                    sh '''
                        echo "Scanning for secrets in code..."
                        # 🔎 Install truffleHog for secret scanning
                        pip3 install truffleHog3
                        trufflehog3 --format json --output secrets-report.json ./ || true
                    '''
                }
            }
        }

        stage('Static Code Analysis') {
            parallel {
                stage('SonarQube Analysis') {
                    steps {
                        script {
                            sh '''
                                # 📊 Run SonarQube analysis
                                docker run --rm \
                                    -v $(pwd):/usr/src \
                                    -w /usr/src \
                                    --network host \
                                    sonarsource/sonar-scanner-cli \
                                    -Dsonar.host.url=http://localhost:9000 \
                                    -Dsonar.login=admin \
                                    -Dsonar.password=admin
                                # TODO: Replace hardcoded admin/admin with a Jenkins credential binding
                            '''
                        }
                    }
                }

                stage('Dependency Check') {
                    steps {
                        script {
                            sh './scripts/dependency-check.sh'
                        }
                    }
                }
            }
        }

        stage('Build Application') {
            steps {
                script {
                    sh '''
                        echo "Building application..."
                        docker build -t devsecops-app:${BUILD_NUMBER} .
                        docker tag devsecops-app:${BUILD_NUMBER} devsecops-app:latest
                    '''
                }
            }
        }

        stage('Infrastructure Validation') {
            steps {
                script {
                    sh './scripts/terraform-validate.sh'
                }
            }
        }

        stage('Policy Validation') {
            steps {
                script {
                    sh './scripts/opa-validate.sh'
                }
            }
        }

        stage('Deploy to Test Environment') {
            steps {
                script {
                    sh '''
                        cd infrastructure/terraform
                        terraform apply -auto-approve tfplan
                    '''
                }
            }
        }

        stage('Dynamic Security Testing') {
            steps {
                script {
                    sh './scripts/zap-scan.sh'
                }
            }
        }

        stage('Security Report') {
            steps {
                script {
                    sh '''
                        echo "Generating security report..."
                        mkdir -p reports/consolidated

                        # 📝 Create consolidated security report
                        cat > reports/consolidated/security-summary.md << 'REPORT_EOF'
# DevSecOps Security Report

## Scan Results Summary

### 1. Secret Scanning
- Tool: TruffleHog
- Report: secrets-report.json

### 2. Static Code Analysis
- Tool: SonarQube
- Dashboard: http://localhost:9000

### 3. Dependency Scanning
- Tool: OWASP Dependency Check
- Report: reports/dependency-check/

### 4. Infrastructure Security
- Tool: tfsec
- Report: infrastructure/terraform/tfsec-report.json

### 5. Dynamic Security Testing
- Tool: OWASP ZAP
- Report: reports/zap/

### 6. Policy Compliance
- Tool: Open Policy Agent
- Policies: policies/

REPORT_EOF
                    '''
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/**/*', allowEmptyArchive: true
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: '**/*.html',
                reportName: 'Security Reports'
            ])
        }
    }
}
EOF
```

#### 🪜 Step 2: Create the GitHub Actions Workflow

```yaml
# 🔄 .github/workflows/devsecops.yml
cat > .github/workflows/devsecops.yml << 'EOF'
name: DevSecOps Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  security-scan:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install truffleHog3

    - name: Secret Scanning
      run: |
        trufflehog3 --format json --output secrets-report.json ./ || true

    - name: Static Code Analysis with SonarQube
      uses: sonarqube-quality-gate-action@master
      env:
        SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
        # TODO: Add SONAR_TOKEN to your repository's Actions secrets

    - name: Dependency Check
      run: |
        chmod +x scripts/dependency-check.sh
        ./scripts/dependency-check.sh

    - name: Build Docker Image
      run: |
        docker build -t devsecops-app:${{ github.sha }} .

    - name: Terraform Security Scan
      run: |
        # ⬇️ Install tfsec
        curl -s https://raw.githubusercontent.com/aquasecurity/tfsec/master/scripts/install_linux.sh | bash
        sudo mv tfsec /usr/local/bin/

        # 🔎 Run security scan
        chmod +x scripts/terraform-validate.sh
        ./scripts/terraform-validate.sh

    - name: OPA Policy Validation
      run: |
        # ⬇️ Install OPA
        curl -L -o opa https://openpolicyagent.org/downloads/v0.57.0/opa_linux_amd64_static
        chmod +x opa
        sudo mv opa /usr/local/bin/

        # ⚖️ Run policy validation
        chmod +x scripts/opa-validate.sh
        ./scripts/opa-validate.sh

    - name: Upload Security Reports
      uses: actions/upload-artifact@v3
      with:
        name: security-reports
        path: reports/
EOF
```

<details>
<summary>🧯 Troubleshooting: Jenkins pipeline fails at the <code>vault-token</code> credential step</summary>

The `VAULT_TOKEN = credentials('vault-token')` line requires a Jenkins **Secret text** credential named exactly `vault-token` to already exist under **Manage Jenkins → Credentials**. Create it using the root token generated in Part 3 before triggering the pipeline.

</details>

---

## 🧠 Part 7: Application Architecture and Threat Modeling

![Threat Modeling](https://img.shields.io/badge/Threat_Modeling-STRIDE-4B0082?style=flat-square) ![Microsoft TMT](https://img.shields.io/badge/Microsoft_Threat_Modeling_Tool-0078D4?style=flat-square&logo=microsoft&logoColor=white)

### Task 7.1: Design Application Architecture

#### 🪜 Step 1: Create Architecture Documentation

```markdown
# 📐 docs/architecture.md
cat > docs/architecture.md << 'EOF'
# DevSecOps Lab Application Architecture

## Overview
This document describes the architecture of our DevSecOps demonstration application.

## System Architecture

### Components

1. **Web Application Layer**
   - Flask-based Python web application
   - RESTful API endpoints
   - Static content serving

2. **Security Layer**
   - Authentication and authorization
   - Input validation
   - Security headers

3. **Data Layer**
   - Configuration management
   - Secret storage (Vault integration)

4. **Infrastructure Layer**
   - Containerized deployment (Docker)
   - Network security
   - Monitoring and logging

### Data Flow

1. User Request → Web Application
2. Application → Vault (for secrets)
3. Application → Data Processing
4. Response → User

### Security Boundaries

- Network boundary (firewall/security groups)
- Application boundary (authentication)
- Data boundary (encryption at rest/transit)

## Threat Model Scope

### Assets
- User data
- Application secrets
- Infrastructure configuration
- Source code

### Trust Boundaries
- Internet ↔ Application
- Application ↔ Vault
- Application ↔ Infrastructure

### Entry Points
- HTTP/HTTPS endpoints
- API endpoints
- Configuration files
- Environment variables
EOF
```

```text
# 🗺️ docs/architecture-diagram.txt (ASCII architecture diagram)
cat > docs/architecture-diagram.txt << 'EOF'
DevSecOps Application Architecture

┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│                 │    │                 │    │                 │
│   Internet      │    │   Load          │    │   Web           │
│   Users         │◄──►│   Balancer      │◄──►│   Application   │
│                 │    │   (nginx)       │    │   (Flask)       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                        │
                                                        ▼
                       ┌─────────────────┐    ┌─────────────────┐
                       │                 │    │                 │
                       │   HashiCorp     │◄──►│   Configuration │
                       │   Vault         │    │   Management    │
                       │                 │    │                 │
                       └─────────────────┘    └─────────────────┘
                                                        │
                                                        ▼
                       ┌─────────────────┐    ┌─────────────────┐
                       │                 │    │                 │
                       │   Monitoring    │◄──►│   Logging       │
                       │   (Prometheus)  │    │   (ELK Stack)   │
                       │                 │    │                 │
                       └─────────────────┘    └─────────────────┘

Security Controls:
- TLS/SSL encryption
- Authentication & Authorization
- Input validation
- Security headers
- Secret management
- Network segmentation
EOF
```

### Task 7.2: Threat Modeling with Microsoft Threat Modeling Tool

#### 🪜 Step 1: Prepare Threat Model Data

```bash
# 🧠 scripts/prepare-threat-model.sh
cat > scripts/prepare-threat-model.sh << 'EOF'
#!/bin/bash

echo "=== Preparing Threat Model Data ==="

# 📁 Create threat model directory
mkdir -p threat-model
EOF
```

**STRIDE Analysis** (`threat-model/stride-analysis.md`):

| STRIDE Category | Threat | Mitigation | Status |
|---|---|---|---|
| 🎭 Spoofing | Attacker impersonates legitimate user | Strong authentication, multi-factor authentication | ✅ Implemented |
| ✏️ Tampering | Unauthorized modification of data or code | Input validation, integrity checks, code signing | 🟡 Partially implemented |
| 🙅 Repudiation | Users deny performing actions | Comprehensive logging, digital signatures | ✅ Implemented |
| 🔓 Information Disclosure | Unauthorized access to sensitive information | Encryption, access controls, data classification | ✅ Implemented |
| 🚫 Denial of Service | Service unavailability | Rate limiting, resource monitoring, redundancy | 🟡 Partially implemented |
| 👑 Elevation of Privilege | Gaining unauthorized access levels | Principle of least privilege, regular access reviews | ✅ Implemented |

**Attack Surface Analysis** (`threat-model/attack-surface.md`):

| Surface | Entry Points | Attack Vectors | Risk Level |
|---|---|---|---|
| 🌐 Web Application (external) | HTTP/HTTPS endpoints | SQL injection, XSS, CSRF, authentication bypass | 🔴 High |
| 🔌 API Endpoints (external) | REST API | API abuse, injection attacks, broken authentication | 🔴 High |
| ⚙️ Configuration Management (internal) | Environment variables, config files | Configuration tampering, secret exposure | 🟠 Medium |
| 🏗️ Infrastructure (internal) | Container runtime, network | Container escape, network lateral movement | 🟠 Medium |

**Threat Scenarios** (`threat-model/threat-scenarios.md`):

> **Scenario 1: Malicious User Input**
> - **Description:** Attacker submits malicious input to exploit application vulnerabilities
> - **Impact:** Data breach, system compromise
> - **Likelihood:** High
> - **Mitigation:** Input validation, output encoding, WAF

> ⚠️ **Source content ends here.** The original lab material is cut off mid-way through the Threat Scenarios section, immediately after Scenario 1 and right as a second scenario heading begins. No further threat scenarios, remaining Part 7 steps, or a Part 8 were provided in the source material, so nothing beyond this point has been fabricated for this README.

---

## 🗺️ MITRE ATT&CK Mapping

| Tactic | Technique ID | Technique Name | How This Lab Addresses It |
|---|---|---|---|
| Initial Access | T1190 | Exploit Public-Facing Application | The intentionally vulnerable `/api/data` endpoint is scanned by SonarQube (Part 2.1) and OWASP ZAP (Part 2.3) to surface unsanitized-input flaws before they reach production |
| Credential Access | T1552.001 | Unsecured Credentials: Credentials In Files | HashiCorp Vault (Part 3) replaces hardcoded secrets (DB URLs, API keys, JWT secrets) with centrally managed, access-controlled storage |
| Resource Development | T1195.002 | Supply Chain Compromise: Compromise Software Supply Chain | OWASP Dependency-Check (Part 2.2) scans project dependencies for known-vulnerable versions before build |
| Execution | T1610 | Deploy Container | The `terraform.rego` and `docker.rego` OPA policies (Part 5.2) deny container deployments that expose ports to `0.0.0.0` or omit environment tagging |
| Privilege Escalation | T1611 | Escape to Host | The `docker.rego` policy denies containers running as root or in privileged mode, reducing the container-escape attack surface |

---

## 🧯 Troubleshooting

<details>
<summary>🧯 SonarQube container exits shortly after starting</summary>

SonarQube's Elasticsearch backend needs `vm.max_map_count` ≥ 262144 on the host. If the container restarts in a loop, run `sudo sysctl -w vm.max_map_count=262144` and restart the `docker-compose.sonarqube.yml` stack.

</details>

<details>
<summary>🧯 <code>vault operator init</code> reports "Vault is already initialized"</summary>

This happens if you re-run the setup against a Vault data volume from a previous session. Either reuse the existing `vault-keys.txt` to unseal, or remove the `vault_data` Docker volume for a clean re-initialization (lab environments only — never do this against real secrets).

</details>

<details>
<summary>🧯 <code>tfsec</code> reports findings that don't match the exclusions in <code>.tfsec.yml</code></summary>

Confirm `tfsec` is being run from the same directory as `.tfsec.yml` (`infrastructure/terraform`) — tfsec only auto-loads the config file from the current working directory, not from parent directories.

</details>

---

## ✅ Conclusion

> ⚠️ Because the source lab material ends mid-way through Part 7 (Task 7.2, Threat Scenarios), the summary below is drawn only from the lab's stated Learning Objectives rather than a source-provided conclusion, which was not present in the material.

### 🏆 Key Accomplishments

By completing the tasks documented above, you have:
- Built a Flask application and containerized it as the target for a full DevSecOps toolchain
- Integrated SonarQube, OWASP Dependency-Check, and OWASP ZAP into a security scanning workflow
- Implemented centralized secret management using HashiCorp Vault, removing hardcoded credentials from source
- Authored and validated Infrastructure as Code with Terraform, hardened by `tfsec` scanning
- Enforced policy-as-code guardrails with Open Policy Agent across Terraform plans, Docker configuration, and application settings
- Assembled the individual tools into unified Jenkins and GitHub Actions pipelines
- Began an application architecture and STRIDE-based threat model as the foundation for further threat modeling work

### 🌍 Real-World Applications

- **Shift-left security**: catching vulnerable code and dependencies before they reach production, rather than after
- **Secrets hygiene**: centralizing credential storage so secrets never live in source code or plaintext config
- **Policy-as-code**: codifying infrastructure guardrails so misconfigurations are blocked automatically instead of relying on manual review
- **Pipeline-driven compliance**: giving security and platform teams a single, auditable pipeline that ties scanning, secret management, IaC validation, and policy enforcement together

---

<div align="center">

### 🎓 Provided by Al Nafi

![Al Nafi](https://img.shields.io/badge/Al_Nafi-Cybersecurity_Education-1e3a8a?style=for-the-badge)

</div>
