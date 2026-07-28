<div align="center">

# 🛡️ Mastering DevSecOps — Integrating Security Seamlessly

### Building a Full-Spectrum CI/CD Security Pipeline: SAST • SCA • DAST • IaC • Compliance • Runtime Defense

![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)
![SonarQube](https://img.shields.io/badge/SonarQube-4E9BCD?style=for-the-badge&logo=sonarqube&logoColor=white)
![OWASP](https://img.shields.io/badge/OWASP-000000?style=for-the-badge&logo=owasp&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=node.js&logoColor=white)
![Falco](https://img.shields.io/badge/Falco-00AEC7?style=for-the-badge&logo=falco&logoColor=white)
![InSpec](https://img.shields.io/badge/InSpec-red?style=for-the-badge&logo=chef&logoColor=white)
![DefectDojo](https://img.shields.io/badge/DefectDojo-FF6F00?style=for-the-badge&logoColor=white)

</div>

---

## 📑 Table of Contents

- [🎯 Learning Objectives](#-learning-objectives)
- [📋 Prerequisites](#-prerequisites)
- [🖥️ Lab Environment Setup](#️-lab-environment-setup)
- [🧩 Task 1: CI/CD Pipeline with SAST](#-task-1-setting-up-the-cicd-pipeline-with-sast)
- [🧪 Task 2: SCA and DAST Tools](#-task-2-implementing-sca-and-dast-tools)
- [🏗️ Task 3: IaC with Terraform and TFSec](#️-task-3-infrastructure-as-code-with-terraform-and-tfsec)
- [📊 Task 4: Vulnerability Management with DefectDojo](#-task-4-centralized-vulnerability-management-with-defectdojo)
- [✅ Task 5: Compliance Validation with InSpec](#-task-5-compliance-validation-using-inspec)
- [☸️ Task 6: Deploy Application in Kubernetes](#️-task-6-deploy-application-in-kubernetes)
- [🚨 Task 7: Incident Response Automation with Falco](#-task-7-incident-response-automation-using-falco)
- [🗺️ MITRE ATT&CK Mapping](#️-mitre-attck-mapping)
- [🔧 Troubleshooting](#-troubleshooting)
- [🏁 Conclusion](#-conclusion)

---

## 🎯 Learning Objectives

| # | Objective |
|---|-----------|
| 1 | Implement a complete CI/CD pipeline with integrated security scanning tools |
| 2 | Configure Static Application Security Testing (SAST) using SonarQube |
| 3 | Set up Software Composition Analysis (SCA) using OWASP Dependency-Check |
| 4 | Perform Dynamic Application Security Testing (DAST) using OWASP ZAP |
| 5 | Create and scan Infrastructure as Code (IaC) templates using Terraform and TFSec |
| 6 | Centralize vulnerability management using DefectDojo |
| 7 | Validate compliance using InSpec |
| 8 | Deploy applications securely in Kubernetes |
| 9 | Implement incident response automation using Falco |
| 10 | Understand the complete DevSecOps workflow and security integration points |

## 📋 Prerequisites

| Area | Requirement |
|------|-------------|
| 🐧 Linux | Basic understanding of command line operations |
| 🔀 Git | Familiarity with version control concepts |
| 🐳 Docker | Basic knowledge of containers |
| 🔁 CI/CD | Understanding of pipeline concepts |
| 📝 YAML | Basic familiarity with configuration files |
| 🌐 AppSec | Elementary knowledge of web application security concepts |

## 🖥️ Lab Environment Setup

> ☁️ **Ready-to-Use Cloud Machines** — Al Nafi provides pre-configured Linux-based cloud machines with every tool below already installed. Click **Start Lab** — no VM building, no manual installs.

| Component | Purpose |
|---|---|
| 🐧 Ubuntu 20.04 LTS + Docker/Compose | Base OS & container runtime |
| ⚙️ Jenkins | CI/CD pipeline orchestration |
| 🔍 SonarQube | SAST |
| 📦 OWASP Dependency-Check | SCA |
| 🕷️ OWASP ZAP | DAST |
| 🏗️ Terraform + TFSec | IaC provisioning & scanning |
| 📊 DefectDojo | Centralized vulnerability management |
| ✅ InSpec | Compliance validation |
| ☸️ Kubernetes (minikube) | Container orchestration |
| 🚨 Falco | Runtime security monitoring |

---

## 🧩 Task 1: Setting Up the CI/CD Pipeline with SAST

![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=node.js&logoColor=white) ![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=flat-square&logo=jenkins&logoColor=white) ![SonarQube](https://img.shields.io/badge/SonarQube-4E9BCD?style=flat-square&logo=sonarqube&logoColor=white)

### 🧱 Subtask 1.1: Initialize the Sample Application

Create the project directory:

```bash
# 📁 create and enter the project workspace
mkdir devsecops-lab
cd devsecops-lab
```

Create `package.json`:

```bash
# 📦 define the Node.js demo app manifest
cat > package.json << 'EOF'
{
  "name": "devsecops-demo-app",
  "version": "1.0.0",
  "description": "Demo application for DevSecOps lab",
  "main": "app.js",
  "scripts": {
    "start": "node app.js",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "dependencies": {
    "express": "4.17.1",
    "lodash": "4.17.20"
  }
}
EOF
```

Create `app.js` — includes an **intentional** SQL-injection-style vulnerability for scanner demonstration:

```javascript
// ⚠️ intentionally vulnerable demo endpoint — do not use in production
const express = require('express');
const _ = require('lodash');
const app = express();
const port = 3000;

app.get('/user/:id', (req, res) => {
    const userId = req.params.id;
    // 🚩 SQL injection vulnerability (simulated)
    const query = "SELECT * FROM users WHERE id = " + userId;
    res.json({ message: 'User data retrieved', query: query });
});

app.get('/health', (req, res) => {
    res.json({ status: 'healthy', timestamp: new Date().toISOString() });
});

app.listen(port, () => {
    console.log(`App listening at http://localhost:${port}`);
});
```

Create `Dockerfile`:

```dockerfile
# 🐳 containerize the demo app
FROM node:14-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
```

### 🔍 Subtask 1.2: Configure SonarQube for SAST

```yaml
# 🔍 spin up SonarQube via Compose
version: '3.8'
services:
  sonarqube:
    image: sonarqube:community
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
```

```bash
# ▶️ launch SonarQube
docker-compose -f docker-compose-sonar.yml up -d

# ⏳ give it time to boot, then verify
echo "Waiting for SonarQube to start..."
sleep 60
curl -f http://localhost:9000/api/system/status || echo "SonarQube is starting up..."
```

```properties
# 🗂️ sonar-project.properties
sonar.projectKey=devsecops-demo
sonar.projectName=DevSecOps Demo Application
sonar.projectVersion=1.0
sonar.sources=.
sonar.exclusions=node_modules/**
sonar.javascript.lcov.reportPaths=coverage/lcov.info
```

> ✏️ **TODO:** Point `sonar.sources` at additional service directories once your app grows past a single-file demo.

### ⚙️ Subtask 1.3: Create Jenkins Pipeline with SAST Integration

```groovy
// ⚙️ Jenkinsfile — SAST + SCA + build + DAST + DefectDojo upload
pipeline {
    agent any

    environment {
        SONAR_TOKEN = credentials('sonar-token')
        DEFECTDOJO_TOKEN = credentials('defectdojo-token')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'npm install'
            }
        }

        stage('SAST - SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarQubeScanner'
                    withSonarQubeEnv('SonarQube') {
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }

        stage('SCA - Dependency Check') {
            steps {
                sh '''
                    dependency-check --project "DevSecOps Demo" \
                    --scan . \
                    --format JSON \
                    --out dependency-check-report.json
                '''
                archiveArtifacts artifacts: 'dependency-check-report.json'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devsecops-demo:latest .'
            }
        }

        stage('DAST - ZAP Security Scan') {
            steps {
                sh '''
                    # 🚀 start the app under test
                    docker run -d --name test-app -p 3000:3000 devsecops-demo:latest
                    sleep 10

                    # 🕷️ run ZAP baseline scan
                    docker run -t owasp/zap2docker-stable zap-baseline.py \
                    -t http://host.docker.internal:3000 \
                    -J zap-report.json

                    docker stop test-app
                    docker rm test-app
                '''
            }
        }

        stage('Upload to DefectDojo') {
            steps {
                sh '''
                    # 📤 push SonarQube findings into DefectDojo
                    curl -X POST "http://localhost:8080/api/v2/import-scan/" \
                    -H "Authorization: Token $DEFECTDOJO_TOKEN" \
                    -F "scan_type=SonarQube Scan" \
                    -F "file=@sonar-report.json" \
                    -F "engagement=1"
                '''
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
```

> ✏️ **TODO:** Replace the hardcoded `engagement=1` with a parameterized engagement ID once you have multiple environments in DefectDojo.

---

## 🧪 Task 2: Implementing SCA and DAST Tools

![OWASP Dependency-Check](https://img.shields.io/badge/Dependency--Check-000000?style=flat-square&logo=owasp&logoColor=white) ![OWASP ZAP](https://img.shields.io/badge/OWASP%20ZAP-000000?style=flat-square&logo=owasp&logoColor=white)

### 📦 Subtask 2.1: Configure OWASP Dependency-Check for SCA

```bash
# ⬇️ install Dependency-Check
wget https://github.com/jeremylong/DependencyCheck/releases/download/v7.4.4/dependency-check-7.4.4-release.zip
unzip dependency-check-7.4.4-release.zip
sudo mv dependency-check /opt/
sudo ln -s /opt/dependency-check/bin/dependency-check.sh /usr/local/bin/dependency-check
```

```bash
# 🔎 run a manual SCA scan
dependency-check --project "DevSecOps Demo App" \
--scan . \
--format JSON \
--format HTML \
--out ./sca-reports/
```

```bash
#!/bin/bash
# 📦 scripts/run-sca-scan.sh
echo "Starting Software Composition Analysis..."

mkdir -p sca-reports

dependency-check --project "DevSecOps Demo App" \
--scan . \
--format JSON \
--format HTML \
--format XML \
--out ./sca-reports/ \
--suppression suppression.xml

echo "SCA scan completed. Reports available in sca-reports/"

# 📊 print a quick vulnerability count
if [ -f "sca-reports/dependency-check-report.json" ]; then
    echo "Vulnerabilities found:"
    cat sca-reports/dependency-check-report.json | jq '.dependencies[].vulnerabilities | length' | awk '{sum+=$1} END {print "Total vulnerabilities: " sum}'
fi
```

```bash
chmod +x scripts/run-sca-scan.sh
```

### 🕷️ Subtask 2.2: Configure OWASP ZAP for DAST

```bash
#!/bin/bash
# 🕷️ scripts/run-dast-scan.sh
echo "Starting Dynamic Application Security Testing..."

mkdir -p dast-reports

# 🚀 start the target app
echo "Starting application..."
docker run -d --name dast-test-app -p 3000:3000 devsecops-demo:latest
sleep 15

if curl -f http://localhost:3000/health; then
    echo "Application is running, starting DAST scan..."

    docker run -v $(pwd)/dast-reports:/zap/wrk/:rw \
    -t owasp/zap2docker-stable zap-baseline.py \
    -t http://host.docker.internal:3000 \
    -J dast-report.json \
    -r dast-report.html

    echo "DAST scan completed."
else
    echo "Application failed to start. Skipping DAST scan."
fi

# 🧹 clean up
docker stop dast-test-app 2>/dev/null
docker rm dast-test-app 2>/dev/null

echo "DAST reports available in dast-reports/"
```

```bash
chmod +x scripts/run-dast-scan.sh
./scripts/run-dast-scan.sh
```

---

## 🏗️ Task 3: Infrastructure as Code with Terraform and TFSec

![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white) ![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazon-aws&logoColor=white) ![TFSec](https://img.shields.io/badge/TFSec-1A73E8?style=flat-square&logoColor=white)

### 🏛️ Subtask 3.1: Create Terraform Templates

```hcl
# 🏗️ terraform/main.tf — VPC, IGW, subnet, SG, and S3 bucket
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# 🌐 VPC Configuration
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name        = "devsecops-vpc"
    Environment = var.environment
  }
}

# 🚪 Internet Gateway
resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "devsecops-igw"
  }
}

# 🌍 Public Subnet
resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = data.aws_availability_zones.available.names[0]
  map_public_ip_on_launch = true

  tags = {
    Name = "devsecops-public-subnet"
  }
}

# ⚠️ Security Group — intentionally over-permissive for TFSec demonstration
resource "aws_security_group" "web" {
  name_prefix = "devsecops-web-"
  vpc_id      = aws_vpc.main.id

  # 🚩 allows all inbound traffic (intentional misconfiguration)
  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "devsecops-web-sg"
  }
}

# 🪣 S3 Bucket — intentionally public for TFSec demonstration
resource "aws_s3_bucket" "app_data" {
  bucket = "devsecops-demo-bucket-${random_string.bucket_suffix.result}"

  tags = {
    Name        = "devsecops-app-data"
    Environment = var.environment
  }
}

# 🚩 intentionally insecure public-access configuration
resource "aws_s3_bucket_public_access_block" "app_data" {
  bucket = aws_s3_bucket.app_data.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

resource "random_string" "bucket_suffix" {
  length  = 8
  special = false
  upper   = false
}

data "aws_availability_zones" "available" {
  state = "available"
}
```

```hcl
# 🔧 terraform/variables.tf
variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-west-2"
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "dev"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}
```

```hcl
# 📤 terraform/outputs.tf
output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.main.id
}

output "public_subnet_id" {
  description = "ID of the public subnet"
  value       = aws_subnet.public.id
}

output "security_group_id" {
  description = "ID of the security group"
  value       = aws_security_group.web.id
}

output "s3_bucket_name" {
  description = "Name of the S3 bucket"
  value       = aws_s3_bucket.app_data.bucket
}
```

> ✏️ **TODO:** Before running against a real AWS account, fix the intentional `0.0.0.0/0` ingress rule and re-enable the S3 public-access block.

### 🔐 Subtask 3.2: Install and Configure TFSec

```bash
# ⬇️ install TFSec
curl -s https://raw.githubusercontent.com/aquasecurity/tfsec/master/scripts/install_linux.sh | bash
sudo mv tfsec /usr/local/bin/
```

```bash
#!/bin/bash
# 🔐 scripts/run-tfsec-scan.sh
echo "Starting Terraform security scanning with TFSec..."

mkdir -p iac-reports

tfsec terraform/ --format json --out iac-reports/tfsec-report.json
tfsec terraform/ --format html --out iac-reports/tfsec-report.html
tfsec terraform/ --format sarif --out iac-reports/tfsec-report.sarif

echo "TFSec scan completed. Reports available in iac-reports/"

# 📊 print issue count
if [ -f "iac-reports/tfsec-report.json" ]; then
    echo "Security issues found:"
    cat iac-reports/tfsec-report.json | jq '.results | length'
fi
```

```bash
chmod +x scripts/run-tfsec-scan.sh
./scripts/run-tfsec-scan.sh
```

---

## 📊 Task 4: Centralized Vulnerability Management with DefectDojo

![DefectDojo](https://img.shields.io/badge/DefectDojo-FF6F00?style=flat-square&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)

### 🐳 Subtask 4.1: Setup DefectDojo

```yaml
# 📊 docker-compose-defectdojo.yml
version: '3.8'
services:
  defectdojo:
    image: defectdojo/defectdojo-django:latest
    container_name: defectdojo
    ports:
      - "8080:8080"
    environment:
      - DD_DATABASE_URL=postgresql://defectdojo:defectdojo@postgres:5432/defectdojo
      - DD_SECRET_KEY=your-secret-key-here
      - DD_DEBUG=True
      - DD_ALLOWED_HOSTS=*
    depends_on:
      - postgres
    volumes:
      - defectdojo_media:/app/media

  postgres:
    image: postgres:13
    container_name: defectdojo-postgres
    environment:
      - POSTGRES_DB=defectdojo
      - POSTGRES_USER=defectdojo
      - POSTGRES_PASSWORD=defectdojo
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  defectdojo_media:
  postgres_data:
```

```bash
# ▶️ launch DefectDojo + Postgres
docker-compose -f docker-compose-defectdojo.yml up -d

# ⏳ wait for initialization
echo "Waiting for DefectDojo to start..."
sleep 120
curl -f http://localhost:8080 || echo "DefectDojo is still starting up..."
```

> ✏️ **TODO:** Replace `DD_SECRET_KEY=your-secret-key-here` with a securely generated secret before anything beyond local lab use.

### 🔗 Subtask 4.2: Configure DefectDojo Integration

```bash
#!/bin/bash
# 📤 scripts/upload-to-defectdojo.sh
DEFECTDOJO_URL="http://localhost:8080"
API_TOKEN="your-api-token-here"  # ✏️ TODO: replace with actual token after setup

echo "Uploading scan results to DefectDojo..."

upload_scan() {
    local scan_type=$1
    local file_path=$2
    local engagement_id=$3

    if [ -f "$file_path" ]; then
        echo "Uploading $scan_type results..."
        curl -X POST "$DEFECTDOJO_URL/api/v2/import-scan/" \
        -H "Authorization: Token $API_TOKEN" \
        -F "scan_type=$scan_type" \
        -F "file=@$file_path" \
        -F "engagement=$engagement_id" \
        -F "active=true" \
        -F "verified=false"
    else
        echo "File $file_path not found, skipping $scan_type upload"
    fi
}

# 📥 upload every scanner's findings into one place
upload_scan "SonarQube Scan" "sonar-report.json" "1"
upload_scan "Dependency Check Scan" "sca-reports/dependency-check-report.json" "1"
upload_scan "ZAP Scan" "dast-reports/dast-report.json" "1"
upload_scan "Terrascan Scan" "iac-reports/tfsec-report.json" "1"

echo "Upload completed!"
```

```bash
chmod +x scripts/upload-to-defectdojo.sh
```

---

## ✅ Task 5: Compliance Validation using InSpec

![Chef InSpec](https://img.shields.io/badge/InSpec-red?style=flat-square&logo=chef&logoColor=white)

### 📥 Subtask 5.1: Install and Configure InSpec

```bash
# ⬇️ install InSpec via Chef Omnitruck
curl https://omnitruck.chef.io/install.sh | sudo bash -s -- -P inspec
```

```bash
# 🗂️ scaffold a compliance profile
mkdir -p inspec-profiles/devsecops-compliance
cd inspec-profiles/devsecops-compliance
inspec init profile . --overwrite
```

```ruby
# ✅ controls/security_controls.rb — Security Controls for DevSecOps Demo

control 'docker-security-1' do
  title 'Docker daemon configuration'
  desc 'Ensure Docker daemon is configured securely'
  impact 0.7

  describe file('/etc/docker/daemon.json') do
    it { should exist }
  end

  describe json('/etc/docker/daemon.json') do
    its(['log-driver']) { should eq 'json-file' }
  end
end

control 'system-security-1' do
  title 'System security configuration'
  desc 'Ensure system is configured with security best practices'
  impact 0.8

  describe file('/etc/passwd') do
    its('mode') { should cmp '0644' }
  end

  describe file('/etc/shadow') do
    its('mode') { should cmp '0640' }
  end
end

control 'network-security-1' do
  title 'Network security configuration'
  desc 'Ensure network is configured securely'
  impact 0.6

  describe port(22) do
    it { should be_listening }
  end

  describe iptables do
    it { should have_rule('-P INPUT DROP') }
  end
end

control 'application-security-1' do
  title 'Application security checks'
  desc 'Ensure application follows security best practices'
  impact 0.9

  describe file('/app/package.json') do
    it { should exist }
  end

  # 🔎 flag known-vulnerable packages
  describe command('npm audit --json') do
    its('exit_status') { should eq 0 }
  end
end
```

```bash
#!/bin/bash
# ✅ scripts/run-compliance-scan.sh
echo "Starting compliance validation with InSpec..."

mkdir -p compliance-reports

inspec exec inspec-profiles/devsecops-compliance \
--reporter json:compliance-reports/inspec-report.json \
--reporter html:compliance-reports/inspec-report.html \
--reporter cli

echo "Compliance scan completed. Reports available in compliance-reports/"

if [ -f "compliance-reports/inspec-report.json" ]; then
    echo "Compliance summary:"
    cat compliance-reports/inspec-report.json | jq '.profiles[0].summary'
fi
```

```bash
chmod +x scripts/run-compliance-scan.sh
./scripts/run-compliance-scan.sh
```

---

## ☸️ Task 6: Deploy Application in Kubernetes

![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white) ![Minikube](https://img.shields.io/badge/Minikube-2496ED?style=flat-square&logo=kubernetes&logoColor=white)

### 🚀 Subtask 6.1: Setup Kubernetes Environment

```bash
# ☸️ start the local cluster and enable addons
minikube start --driver=docker
minikube addons enable ingress
minikube addons enable metrics-server
```

```yaml
# 🏷️ k8s-manifests/namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: devsecops-demo
  labels:
    name: devsecops-demo
```

```yaml
# 📦 k8s-manifests/deployment.yaml — hardened pod security context
apiVersion: apps/v1
kind: Deployment
metadata:
  name: devsecops-demo-app
  namespace: devsecops-demo
  labels:
    app: devsecops-demo
spec:
  replicas: 2
  selector:
    matchLabels:
      app: devsecops-demo
  template:
    metadata:
      labels:
        app: devsecops-demo
    spec:
      containers:
      - name: devsecops-demo
        image: devsecops-demo:latest
        imagePullPolicy: Never
        ports:
        - containerPort: 3000
        env:
        - name: NODE_ENV
          value: "production"
        resources:
          requests:
            memory: "64Mi"
            cpu: "50m"
          limits:
            memory: "128Mi"
            cpu: "100m"
        securityContext:
          runAsNonRoot: true
          runAsUser: 1000
          allowPrivilegeEscalation: false
          readOnlyRootFilesystem: false
        livenessProbe:
          httpGet:
            path: /health
            port: 3000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /health
            port: 3000
          initialDelaySeconds: 5
          periodSeconds: 5
```

```yaml
# 🔌 k8s-manifests/service.yaml
apiVersion: v1
kind: Service
metadata:
  name: devsecops-demo-service
  namespace: devsecops-demo
spec:
  selector:
    app: devsecops-demo
  ports:
  - protocol: TCP
    port: 80
    targetPort: 3000
  type: ClusterIP
```

```yaml
# 🧱 k8s-manifests/network-policy.yaml — restrict ingress to nginx namespace
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: devsecops-demo-netpol
  namespace: devsecops-demo
spec:
  podSelector:
    matchLabels:
      app: devsecops-demo
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: ingress-nginx
    ports:
    - protocol: TCP
      port: 3000
  egress:
  - {}
```

> ✏️ **TODO:** Tighten the empty `egress: - {}` rule to only the destinations the app actually needs (DNS, DefectDojo API, etc.).

### 📤 Subtask 6.2: Deploy Application to Kubernetes

```bash
# 🐳 build and load the image into Minikube
docker build -t devsecops-demo:latest .
minikube image load devsecops-demo:latest
```

```bash
# ☸️ apply manifests and verify rollout
kubectl apply -f k8s-manifests/
kubectl wait --for=condition=available --timeout=300s deployment/devsecops-demo-app -n devsecops-demo
kubectl get pods -n devsecops-demo
kubectl get services -n devsecops-demo
```

```bash
#!/bin/bash
# 🚀 scripts/deploy-to-k8s.sh
echo "Deploying application to Kubernetes..."

echo "Building Docker image..."
docker build -t devsecops-demo:latest .

echo "Loading image to Minikube..."
minikube image load devsecops-demo:latest

echo "Applying Kubernetes manifests..."
kubectl apply -f k8s-manifests/

echo "Waiting for deployment to be ready..."
kubectl wait --for=condition=available --timeout=300s deployment/devsecops-demo-app -n devsecops-demo

echo "Deployment status:"
kubectl get pods -n devsecops-demo
kubectl get services -n devsecops-demo

echo "Application URL:"
minikube service devsecops-demo-service -n devsecops-demo --url

echo "Deployment completed!"
```

```bash
chmod +x scripts/deploy-to-k8s.sh
```

---

## 🚨 Task 7: Incident Response Automation using Falco

![Falco](https://img.shields.io/badge/Falco-00AEC7?style=flat-square&logo=falco&logoColor=white)

### 📥 Subtask 7.1: Install and Configure Falco

```bash
# ⬇️ add the Falco repo and install
curl -s https://falco.org/repo/falcosecurity-3672BA8F.asc | sudo apt-key add -
echo "deb https://download.falco.org/packages/deb stable main" | sudo tee -a /etc/apt/sources.list.d/falcosecurity.list
sudo apt-get update -y
sudo apt-get install -y falco
```

```yaml
# 🚨 /etc/falco/rules.d/devsecops_rules.yaml — custom detection rules

- rule: Suspicious Network Activity in Container
  desc: Detect suspicious network activity in containers
  condition: >
    spawned_process and container and
    (proc.name in (nc, ncat, netcat, wget, curl) and
     proc.args contains "http")
  output: >
    Suspicious network activity detected in container
    (user=%user.name command=%proc.cmdline container=%container.name
     image=%container.image.repository)
  priority: WARNING
  tags: [network, container]

- rule: Unauthorized File Access in Container
  desc: Detect unauthorized file access in containers
  condition: >
    open_read and container and
    fd.name startswith /etc and
    not proc.name in (cat, less, more, tail, head, grep)
  output: >
    Unauthorized file access detected
    (user=%user.name file=%fd.name command=%proc.cmdline
     container=%container.name)
  priority: WARNING
  tags: [filesystem, container]

# 🚩 privilege escalation detection
- rule: Container Privilege Escalation
  desc: Detect privilege escalation attempts in containers
  condition: >
    spawned_process and container and
    proc.name in (sudo, su, passwd, chsh, chfn) and
    not user.name=root
  output: >
    Privilege escalation attempt detected
    (user=%user.name command=%proc.cmdline container=%container.name
     image=%container.image.repository)
  priority: CRITICAL
  tags: [privilege_escalation, container]

- rule: Suspicious Process in DevSecOps Namespace
  desc: Detect suspicious processes in DevSecOps namespace
  condition: >
    spawned_process and k8s_ns=devsecops-demo and
    proc.name in (sh, bash, zsh, csh, ksh, tcsh, dash)
  output: >
    Suspicious shell process in DevSecOps namespace
    (user=%user.name command=%proc.cmdline pod=%k8s.pod.name
     namespace=%k8s.ns.name)
  priority: WARNING
  tags: [shell, kubernetes]
```

```yaml
# ⚙️ /etc/falco/falco.yaml — begins Kubernetes-aware configuration
rules_file:
  - /etc/falco/falco_rules.yaml
```

> ⚠️ **Source content ends here.** The original lab document is truncated mid-configuration at the start of the `falco.yaml` `rules_file` block in Subtask 7.1 — no completion of the Falco config, no Falco deployment/testing steps, and no source conclusion were provided. Nothing below this point has been fabricated to fill that gap; the Conclusion is synthesized strictly from the Learning Objectives stated at the top of the lab.

---

## 🗺️ MITRE ATT&CK Mapping

| Technique ID | Technique | How This Lab Addresses It |
|---|---|---|
| [T1190](https://attack.mitre.org/techniques/T1190/) | Exploit Public-Facing Application | The demo app's intentional SQL-injection endpoint is caught by SAST (SonarQube) and DAST (ZAP) scanning |
| [T1552.001](https://attack.mitre.org/techniques/T1552/001/) | Unsecured Credentials: Credentials In Files | Jenkins pipeline credentials binding and the DefectDojo `API_TOKEN` placeholder highlight the risk of hardcoded tokens in scripts |
| [T1195.002](https://attack.mitre.org/techniques/T1195/002/) | Supply Chain Compromise: Compromise Software Dependencies | OWASP Dependency-Check (SCA) flags known-vulnerable pinned packages (`express 4.17.1`, `lodash 4.17.20`) |
| [T1610](https://attack.mitre.org/techniques/T1610/) | Deploy Container | Kubernetes deployment manifests and hardened `securityContext` settings govern how containers are launched |
| [T1611](https://attack.mitre.org/techniques/T1611/) | Escape to Host | Falco's privilege-escalation and unauthorized-file-access rules detect container breakout attempts at runtime |

---

## 🔧 Troubleshooting

<details>
<summary>🔴 SonarQube fails to start / stays unhealthy</summary>

- Confirm `vm.max_map_count` is at least `262144` on the host (Elasticsearch bootstrap check inside SonarQube requires it)
- Check container logs: `docker logs sonarqube`
- Give it the full 60+ seconds before hitting the API — first boot is slow

</details>

<details>
<summary>🔴 DAST scan can't reach the target app</summary>

- Verify `test-app` / `dast-test-app` is actually running: `docker ps`
- On Linux hosts, `host.docker.internal` may need `--add-host=host.docker.internal:host-gateway` added to the `docker run` command
- Check `/health` responds locally first: `curl http://localhost:3000/health`

</details>

<details>
<summary>🔴 DefectDojo import-scan returns 401/403</summary>

- The placeholder `API_TOKEN`/`DEFECTDOJO_TOKEN` values must be replaced with a real token generated from the DefectDojo UI (**API v2 Key** under user settings)
- Confirm the `engagement` ID exists in DefectDojo before uploading

</details>

<details>
<summary>🔴 TFSec reports unexpected findings</summary>

- Remember Task 3's Terraform is intentionally insecure (open security group, public S3 bucket) — those findings are expected teaching material, not scan errors
- Run `tfsec terraform/ --format json | jq '.results[].rule_id'` to see exactly which rules fired

</details>

<details>
<summary>🔴 Kubernetes deployment stuck in ImagePullBackOff</summary>

- `imagePullPolicy: Never` requires the image to already exist inside Minikube's Docker daemon — confirm with `minikube image load devsecops-demo:latest` before applying manifests
- Check `kubectl describe pod <pod-name> -n devsecops-demo` for the exact pull error

</details>

---

## 🏁 Conclusion

### ✅ Key Accomplishments

- 🔍 Built a Node.js demo application with an intentional vulnerability and wired it into a **SonarQube SAST** scan
- 📦 Implemented **OWASP Dependency-Check SCA** to catch known-vulnerable dependencies
- 🕷️ Performed **OWASP ZAP DAST** scanning against the running application
- 🏗️ Authored **Terraform** infrastructure and scanned it for misconfigurations with **TFSec**
- 📊 Centralized every scanner's output into **DefectDojo** for unified vulnerability tracking
- ✅ Validated system and application compliance with **InSpec** controls
- ☸️ Deployed the application securely to **Kubernetes**, including a restrictive `NetworkPolicy` and hardened pod `securityContext`
- 🚨 Began configuring **Falco** for container runtime threat detection

### 🌍 Real-World Applications

- Integrating SAST/SCA/DAST into a single Jenkins pipeline mirrors how mature engineering organizations "shift security left" instead of bolting it on at release time
- Scanning IaC before it's ever applied catches cloud misconfigurations — a leading cause of real-world breaches — before infrastructure exists
- Centralizing findings in a platform like DefectDojo gives security teams one place to triage, deduplicate, and track remediation across every scanner
- Compliance-as-code with InSpec lets teams continuously prove adherence to internal or regulatory security baselines
- Runtime detection with Falco closes the loop: even a fully scanned, fully compliant deployment still needs live monitoring for the threats that only appear once containers are running

</br>

<div align="center">

**📚 Provided by [Al Nafi](https://alnafi.com) — Cloud & Cybersecurity Training**

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Training-blue?style=for-the-badge)

</div>
