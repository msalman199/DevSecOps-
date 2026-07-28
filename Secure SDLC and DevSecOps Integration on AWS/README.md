<div align="center">

# ☁️ Secure SDLC and DevSecOps Integration on AWS

### Native AWS Security Services Meet Policy-as-Code: Security Hub • GuardDuty • Config • Checkov • TFLint

![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![Checkov](https://img.shields.io/badge/Checkov-4B32C3?style=for-the-badge&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GuardDuty](https://img.shields.io/badge/GuardDuty-C7131F?style=for-the-badge&logo=amazon-aws&logoColor=white)

</div>

---

## 📑 Table of Contents

- [🎯 Lab Objectives](#-lab-objectives)
- [📋 Prerequisites](#-prerequisites)
- [🖥️ Lab Environment Setup](#️-lab-environment-setup)
- [🧰 Task 1: Environment Preparation and Initial Setup](#-task-1-environment-preparation-and-initial-setup)
- [🏗️ Task 2: Setting Up AWS Security Services with Terraform](#️-task-2-setting-up-aws-security-services-with-terraform)
- [🔐 Task 3: Terraform Security Validation and Scanning](#-task-3-terraform-security-validation-and-scanning)
- [🚀 Task 4: Deploy and Test the DevSecOps Infrastructure](#-task-4-deploy-and-test-the-devsecops-infrastructure)
- [🔁 Task 5: Implement Automated Security Scanning Pipeline](#-task-5-implement-automated-security-scanning-pipeline)
- [📊 Task 6: Monitor and Analyze Security Findings](#-task-6-monitor-and-analyze-security-findings)
- [🧹 Task 7: Cleanup and Documentation](#-task-7-cleanup-and-documentation)
- [🗺️ MITRE ATT&CK Mapping](#️-mitre-attck-mapping)
- [🔧 Troubleshooting](#-troubleshooting)
- [🏁 Conclusion](#-conclusion)

---

## 🎯 Lab Objectives

| # | Objective |
|---|-----------|
| 1 | Understand the fundamentals of DevSecOps and its integration with AWS security services |
| 2 | Set up a complete DevSecOps pipeline using AWS native tools |
| 3 | Configure AWS Security Hub for centralized security findings management |
| 4 | Implement AWS CodeGuru Reviewer for automated code security analysis |
| 5 | Deploy Amazon GuardDuty for threat detection and monitoring |
| 6 | Utilize AWS Config for compliance monitoring and configuration management |
| 7 | Create Infrastructure as Code (IaC) templates using Terraform |
| 8 | Validate Terraform configurations using security scanning tools |
| 9 | Integrate Checkov for policy-as-code security scanning |
| 10 | Implement automated security testing throughout the software development lifecycle |

## 📋 Prerequisites

| Area | Requirement |
|------|-------------|
| ☁️ Cloud | Basic understanding of cloud computing concepts |
| 🔶 AWS | Familiarity with AWS services and console navigation |
| 🔀 Git | Basic knowledge of version control |
| 🔁 CI/CD | Understanding of pipeline concepts |
| ⌨️ CLI | Basic command-line interface experience |
| 📝 JSON/YAML | Fundamental knowledge of both formats |

## 🖥️ Lab Environment Setup

> ☁️ **Ready-to-Use Cloud Machines** — Al Nafi provides pre-configured Linux-based cloud machines with every tool below already installed. Click **Start Lab** — no VM building or manual configuration.

| Component | Purpose |
|---|---|
| 🔶 AWS CLI (pre-configured) | Authenticated access to AWS services |
| 🏗️ Terraform | Infrastructure as Code provisioning |
| 🔀 Git | Version control |
| 🐍 Python + pip | Scripting & additional security tools |
| 📝 nano / vim | In-terminal editing |
| 🛡️ Security scanning tools | Pre-installed for the lab |

---

## 🧰 Task 1: Environment Preparation and Initial Setup

![AWS CLI](https://img.shields.io/badge/AWS%20CLI-232F3E?style=flat-square&logo=amazon-aws&logoColor=white) ![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white)

### ✅ Subtask 1.1: Verify Lab Environment

```bash
# 🔎 confirm AWS CLI is configured and authenticated
aws --version
aws sts get-caller-identity
```

```bash
# 🔎 confirm Terraform is installed
terraform --version
```

```bash
# 🔎 confirm Python tooling is available
python3 --version
pip3 --version
```

### 🛠️ Subtask 1.2: Install Additional Security Tools

```bash
# 🔐 Checkov — policy-as-code scanning for Terraform
pip3 install checkov
checkov --version
```

```bash
# 📏 TFLint — Terraform linting
curl -s https://raw.githubusercontent.com/terraform-linters/tflint/master/install_linux.sh | bash
tflint --version
```

### 📁 Subtask 1.3: Create Project Directory Structure

```bash
# 📂 lay out the project workspace
mkdir -p ~/devsecops-lab
cd ~/devsecops-lab
mkdir -p {terraform,scripts,policies,docs}
```

---

## 🏗️ Task 2: Setting Up AWS Security Services with Terraform

![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazon-aws&logoColor=white) ![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white)

### 🛡️ Subtask 2.1: Create Terraform Configuration for AWS Security Hub

```bash
cd ~/devsecops-lab/terraform
nano main.tf
```

```hcl
# 🔶 main.tf — provider, variables, and Security Hub setup
terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# 🔧 Variables
variable "aws_region" {
  description = "AWS region for resources"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Name of the project"
  type        = string
  default     = "devsecops-lab"
}

# 🔎 Data sources
data "aws_caller_identity" "current" {}
data "aws_region" "current" {}

# 🛡️ Enable Security Hub
resource "aws_securityhub_account" "main" {
  enable_default_standards = true
}

# 📜 Subscribe to Security Hub standards
resource "aws_securityhub_standards_subscription" "aws_foundational" {
  standards_arn = "arn:aws:securityhub:::ruleset/finding-format/aws-foundational-security-standard/v/1.0.0"
  depends_on    = [aws_securityhub_account.main]
}

resource "aws_securityhub_standards_subscription" "cis" {
  standards_arn = "arn:aws:securityhub:::ruleset/finding-format/cis-aws-foundations-benchmark/v/1.2.0"
  depends_on    = [aws_securityhub_account.main]
}
```

### 🕵️ Subtask 2.2: Configure Amazon GuardDuty

```hcl
# 🕵️ append to main.tf — threat detection
resource "aws_guardduty_detector" "main" {
  enable                       = true
  finding_publishing_frequency = "FIFTEEN_MINUTES"

  datasources {
    s3_logs {
      enable = true
    }
    kubernetes {
      audit_logs {
        enable = true
      }
    }
    malware_protection {
      scan_ec2_instance_with_findings {
        ebs_volumes {
          enable = true
        }
      }
    }
  }

  tags = {
    Name        = "${var.project_name}-guardduty"
    Environment = "lab"
  }
}

# 🌐 optional GuardDuty threat intel set
resource "aws_guardduty_threatintelset" "main" {
  activate    = true
  detector_id = aws_guardduty_detector.main.id
  format      = "TXT"
  location    = "https://s3.amazonaws.com/your-bucket/threatintelset.txt"
  name        = "${var.project_name}-threat-intel"
}
```

> ✏️ **TODO:** Replace the placeholder `location` URL in `aws_guardduty_threatintelset` with your own vetted threat-intel feed before using this outside the lab.

### 📋 Subtask 2.3: Configure AWS Config

```hcl
# 🪣 S3 bucket for Config, encrypted and versioned
resource "aws_s3_bucket" "config" {
  bucket        = "${var.project_name}-config-${random_string.suffix.result}"
  force_destroy = true

  tags = {
    Name        = "${var.project_name}-config-bucket"
    Environment = "lab"
  }
}

resource "aws_s3_bucket_versioning" "config" {
  bucket = aws_s3_bucket.config.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "config" {
  bucket = aws_s3_bucket.config.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "random_string" "suffix" {
  length  = 8
  special = false
  upper   = false
}

# 🔑 IAM role for Config
resource "aws_iam_role" "config" {
  name = "${var.project_name}-config-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "config.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "config" {
  role       = aws_iam_role.config.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/ConfigRole"
}

# 📬 Config delivery channel
resource "aws_config_delivery_channel" "main" {
  name           = "${var.project_name}-delivery-channel"
  s3_bucket_name = aws_s3_bucket.config.bucket
  depends_on     = [aws_config_configuration_recorder.main]
}

# 🎙️ Config configuration recorder
resource "aws_config_configuration_recorder" "main" {
  name     = "${var.project_name}-recorder"
  role_arn = aws_iam_role.config.arn

  recording_group {
    all_supported                 = true
    include_global_resource_types = true
  }
}

# ▶️ enable the recorder
resource "aws_config_configuration_recorder_status" "main" {
  name       = aws_config_configuration_recorder.main.name
  is_enabled = true
  depends_on = [aws_config_delivery_channel.main]
}
```

### 🤖 Subtask 2.4: Add CodeGuru Reviewer Configuration

```hcl
# 📦 CodeCommit repository for demonstration
resource "aws_codecommit_repository" "main" {
  repository_name = "${var.project_name}-repo"
  description     = "Repository for DevSecOps lab"

  tags = {
    Name        = "${var.project_name}-repository"
    Environment = "lab"
  }
}

# 🤖 associate CodeGuru Reviewer for automated code analysis
resource "aws_codeguru_reviewer_repository_association" "main" {
  repository {
    codecommit {
      name = aws_codecommit_repository.main.repository_name
    }
  }

  type = "CodeCommit"
}
```

### 📤 Subtask 2.5: Create Outputs File

```bash
nano outputs.tf
```

```hcl
# 📤 outputs.tf
output "security_hub_arn" {
  description = "ARN of the Security Hub account"
  value       = aws_securityhub_account.main.arn
}

output "guardduty_detector_id" {
  description = "ID of the GuardDuty detector"
  value       = aws_guardduty_detector.main.id
}

output "config_recorder_name" {
  description = "Name of the Config recorder"
  value       = aws_config_configuration_recorder.main.name
}

output "codecommit_repository_url" {
  description = "URL of the CodeCommit repository"
  value       = aws_codecommit_repository.main.clone_url_http
}

output "config_s3_bucket" {
  description = "S3 bucket for Config"
  value       = aws_s3_bucket.config.bucket
}
```

---

## 🔐 Task 3: Terraform Security Validation and Scanning

![Checkov](https://img.shields.io/badge/Checkov-4B32C3?style=flat-square&logoColor=white) ![TFLint](https://img.shields.io/badge/TFLint-1A73E8?style=flat-square&logoColor=white)

### 🧪 Subtask 3.1: Initialize and Validate Terraform

```bash
# 🚀 initialize the working directory
cd ~/devsecops-lab/terraform
terraform init
```

```bash
# ✅ validate syntax
terraform validate
```

```bash
# 🧹 auto-format files
terraform fmt
```

### 🔍 Subtask 3.2: Run Checkov Security Scan

```bash
# 🔍 scan the whole Terraform configuration
checkov -d . --framework terraform
```

```bash
nano .checkov.yml
```

```yaml
# ⚙️ .checkov.yml — customize scan behavior
framework:
  - terraform
output: cli
quiet: false
compact: false
soft-fail: false
skip-check:
  - CKV_AWS_18  # Ensure S3 bucket has access logging configured
  - CKV_AWS_52  # Ensure S3 bucket has MFA delete enabled
```

```bash
# ▶️ run with the custom config
checkov -d . --config-file .checkov.yml
```

> ✏️ **TODO:** Revisit the `skip-check` list — skipping S3 access logging and MFA delete is a lab convenience, not a production-safe default.

### 📏 Subtask 3.3: Run TFLint for Additional Validation

```bash
nano .tflint.hcl
```

```hcl
# 📏 .tflint.hcl
plugin "aws" {
  enabled = true
  version = "0.24.1"
  source  = "github.com/terraform-linters/tflint-ruleset-aws"
}

rule "terraform_deprecated_interpolation" {
  enabled = true
}

rule "terraform_unused_declarations" {
  enabled = true
}

rule "terraform_comment_syntax" {
  enabled = true
}

rule "terraform_documented_outputs" {
  enabled = true
}

rule "terraform_documented_variables" {
  enabled = true
}
```

```bash
# ▶️ initialize plugins and lint
tflint --init
tflint
```

### 📝 Subtask 3.4: Create Security Policy as Code

```bash
mkdir -p ~/devsecops-lab/policies
cd ~/devsecops-lab/policies
nano custom_s3_policy.py
```

```python
# 📝 custom_s3_policy.py — enforce required tags on every S3 bucket
from checkov.common.models.enums import TRUE_VALUES
from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import ANY_VALUE


class S3BucketMustHaveTagging(BaseResourceCheck):
    def __init__(self):
        name = "Ensure S3 bucket has required tags"
        id = "CKV2_CUSTOM_1"
        supported_resources = ['aws_s3_bucket']
        categories = []
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        """
        Looks for required tags on S3 buckets
        """
        if 'tags' in conf:
            tags = conf['tags'][0]
            required_tags = ['Name', 'Environment']

            for required_tag in required_tags:
                if required_tag not in tags:
                    return CheckResult.FAILED
            return CheckResult.PASSED
        return CheckResult.FAILED


check = S3BucketMustHaveTagging()
```

```bash
# ▶️ run Checkov with the custom policy included
cd ~/devsecops-lab/terraform
checkov -d . --external-checks-dir ../policies
```

---

## 🚀 Task 4: Deploy and Test the DevSecOps Infrastructure

![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazon-aws&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

### ▶️ Subtask 4.1: Plan and Apply Terraform Configuration

```bash
# 📝 generate and review the execution plan
terraform plan -out=tfplan
```

```bash
# 🚀 apply the plan
terraform apply tfplan
```

### 🔎 Subtask 4.2: Verify AWS Security Services

```bash
# 🛡️ confirm Security Hub standards are enabled
aws securityhub get-enabled-standards --region us-east-1
```

```bash
# 🕵️ confirm GuardDuty detector exists
aws guardduty list-detectors --region us-east-1
```

```bash
# 📋 confirm Config recorder is active
aws configservice describe-configuration-recorders --region us-east-1
```

### 🐍 Subtask 4.3: Create Sample Application Code

```bash
cd ~/devsecops-lab
mkdir sample-app
cd sample-app
nano app.py
```

```python
#!/usr/bin/env python3
"""
Sample application for DevSecOps lab
"""
# ⚠️ intentionally vulnerable demo app — do not use these patterns in production
import os
import boto3
from flask import Flask, jsonify

app = Flask(__name__)

# 🚩 hard-coded credentials (intentional bad practice, for scanner demonstration)
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

@app.route('/')
def hello():
    return jsonify({"message": "Hello from DevSecOps Lab!"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/data')
def get_data():
    # 🚩 SQL injection vulnerability (intentional, for scanner demonstration)
    user_id = request.args.get('user_id')
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return jsonify({"query": query})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # 🚩 debug mode enabled (intentional bad practice)
```

```text
# 📦 requirements.txt
Flask==2.3.3
boto3==1.28.85
requests==2.31.0
```

```dockerfile
# 🐳 Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
```

> ✏️ **TODO:** Before shipping anything derived from this sample, remove the hard-coded AWS keys, fix the unparameterized SQL string, and disable Flask debug mode.

### 📤 Subtask 4.4: Commit Code to CodeCommit Repository

```bash
# 🔧 configure Git identity (skip if already set)
git config --global user.name "DevSecOps Student"
git config --global user.email "student@example.com"
```

```bash
# 📥 initialize and commit
cd ~/devsecops-lab/sample-app
git init
git add .
git commit -m "Initial commit of sample application"
```

```bash
# 🔗 fetch the CodeCommit URL from Terraform output
cd ~/devsecops-lab/terraform
terraform output codecommit_repository_url
```

```bash
# 📤 push to CodeCommit
cd ~/devsecops-lab/sample-app
git remote add origin $(cd ../terraform && terraform output -raw codecommit_repository_url)
git push -u origin master
```

---

## 🔁 Task 5: Implement Automated Security Scanning Pipeline

![AWS CodeBuild](https://img.shields.io/badge/CodeBuild-FF9900?style=flat-square&logo=amazon-aws&logoColor=white) ![Bandit](https://img.shields.io/badge/Bandit-yellow?style=flat-square&logoColor=black)

### ⚙️ Subtask 5.1: Create CI/CD Pipeline with Security Integration

```bash
cd ~/devsecops-lab/sample-app
nano buildspec.yml
```

```yaml
# ⚙️ buildspec.yml — CodeBuild phases with embedded security scanning
version: 0.2

phases:
  install:
    runtime-versions:
      python: 3.9
    commands:
      - echo Installing dependencies...
      - pip install --upgrade pip
      - pip install bandit safety checkov
      - pip install -r requirements.txt

  pre_build:
    commands:
      - echo Starting security scans...
      - echo Running Bandit security scan...
      - bandit -r . -f json -o bandit-report.json || true
      - echo Running Safety dependency scan...
      - safety check --json --output safety-report.json || true
      - echo Running Checkov infrastructure scan...
      - checkov -f Dockerfile --framework dockerfile -o json --output-file checkov-report.json || true

  build:
    commands:
      - echo Build started on `date`
      - echo Building the Docker image...
      - docker build -t $IMAGE_REPO_NAME:$IMAGE_TAG .
      - docker tag $IMAGE_REPO_NAME:$IMAGE_TAG $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$IMAGE_REPO_NAME:$IMAGE_TAG

  post_build:
    commands:
      - echo Build completed on `date`
      - echo Pushing the Docker image...
      - aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com
      - docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$IMAGE_REPO_NAME:$IMAGE_TAG
      - echo Generating security report summary...
      - python generate_security_report.py

artifacts:
  files:
    - '**/*'
  secondary-artifacts:
    security-reports:
      files:
        - '*-report.json'
        - security-summary.html
```

### 📊 Subtask 5.2: Create Security Report Generator

```bash
nano generate_security_report.py
```

```python
#!/usr/bin/env python3
"""
Security report generator for DevSecOps pipeline
"""
# 📊 aggregates Bandit, Safety, and Checkov output into one HTML report
import json
import os
from datetime import datetime

def load_json_report(filename):
    """Load JSON report if it exists"""
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except:
            return None
    return None

def generate_html_report():
    """Generate HTML security report"""

    # 📥 load results from every scanner
    bandit_report = load_json_report('bandit-report.json')
    safety_report = load_json_report('safety-report.json')
    checkov_report = load_json_report('checkov-report.json')

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevSecOps Security Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            .header {{ background-color: #f0f0f0; padding: 20px; border-radius: 5px; }}
            .section {{ margin: 20px 0; padding: 15px; border: 1px solid #ddd; border-radius: 5px; }}
            .critical {{ background-color: #ffebee; }}
            .warning {{ background-color: #fff3e0; }}
            .info {{ background-color: #e8f5e8; }}
            .summary {{ font-size: 18px; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>DevSecOps Security Scan Report</h1>
            <p>Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </div>

        <div class="section info">
            <h2>Scan Summary</h2>
            <div class="summary">
                <p>✓ Static Application Security Testing (SAST) - Bandit</p>
                <p>✓ Dependency Vulnerability Scanning - Safety</p>
                <p>✓ Infrastructure as Code Scanning - Checkov</p>
            </div>
        </div>
    """

    # 🐍 Bandit results
    if bandit_report:
        issues_count = len(bandit_report.get('results', []))
        html_content += f"""
        <div class="section {'critical' if issues_count > 0 else 'info'}">
            <h2>Static Code Analysis (Bandit)</h2>
            <p>Issues found: {issues_count}</p>
        """

        if issues_count > 0:
            html_content += "<ul>"
            for issue in bandit_report.get('results', [])[:5]:  # Show first 5 issues
                html_content += f"<li><strong>{issue.get('test_name', 'Unknown')}</strong>: {issue.get('issue_text', 'No description')}</li>"
            html_content += "</ul>"

        html_content += "</div>"

    # 📦 Safety results
    if safety_report:
        vulns = safety_report if isinstance(safety_report, list) else []
        html_content += f"""
        <div class="section {'warning' if len(vulns) > 0 else 'info'}">
            <h2>Dependency Vulnerability Scan (Safety)</h2>
            <p>Vulnerabilities found: {len(vulns)}</p>
        """

        if len(vulns) > 0:
            html_content += "<ul>"
            for vuln in vulns[:5]:  # Show first 5 vulnerabilities
                html_content += f"<li><strong>{vuln.get('package', 'Unknown package')}</strong>: {vuln.get('advisory', 'No advisory')}</li>"
            html_content += "</ul>"

        html_content += "</div>"

    # 🏗️ Checkov results
    if checkov_report:
        failed_checks = checkov_report.get('results', {}).get('failed_checks', [])
        html_content += f"""
        <div class="section {'warning' if len(failed_checks) > 0 else 'info'}">
            <h2>Infrastructure Scan (Checkov)</h2>
            <p>Failed checks: {len(failed_checks)}</p>
        """

        if len(failed_checks) > 0:
            html_content += "<ul>"
            for check in failed_checks[:5]:  # Show first 5 failed checks
                html_content += f"<li><strong>{check.get('check_id', 'Unknown')}</strong>: {check.get('check_name', 'No description')}</li>"
            html_content += "</ul>"

        html_content += "</div>"

    html_content += """
        <div class="section info">
            <h2>Recommendations</h2>
            <ul>
                <li>Review and fix all critical and high-severity security issues</li>
                <li>Update dependencies with known vulnerabilities</li>
                <li>Implement security best practices in infrastructure code</li>
                <li>Regular security scanning in CI/CD pipeline</li>
            </ul>
        </div>
    </body>
    </html>
    """

    with open('security-summary.html', 'w') as f:
        f.write(html_content)

    print("Security report generated: security-summary.html")

if __name__ == "__main__":
    generate_html_report()
```

### 🧪 Subtask 5.3: Test Security Scanning Locally

```bash
cd ~/devsecops-lab/sample-app

# 🛠️ install security scanning tools
pip3 install bandit safety

# 🐍 SAST — Bandit
bandit -r . -f json -o bandit-report.json

# 📦 SCA — Safety
safety check --json --output safety-report.json

# 🐳 IaC — Checkov on the Dockerfile
checkov -f Dockerfile --framework dockerfile -o json --output-file checkov-report.json

# 📊 build the combined HTML report
python3 generate_security_report.py
```

```bash
# 👀 review generated artifacts
ls -la *.json *.html
```

---

## 📊 Task 6: Monitor and Analyze Security Findings

![Security Hub](https://img.shields.io/badge/Security%20Hub-FF9900?style=flat-square&logo=amazon-aws&logoColor=white) ![GuardDuty](https://img.shields.io/badge/GuardDuty-C7131F?style=flat-square&logo=amazon-aws&logoColor=white)

### 🔎 Subtask 6.1: Check Security Hub Findings

```bash
# 🔍 list recent findings
aws securityhub get-findings --region us-east-1 --max-items 10
```

```bash
# 🔴 filter to HIGH severity only
aws securityhub get-findings \
    --filters '{"SeverityLabel":[{"Value":"HIGH","Comparison":"EQUALS"}]}' \
    --region us-east-1
```

### 🕵️ Subtask 6.2: Monitor GuardDuty Findings

```bash
# 🆔 grab the detector ID
DETECTOR_ID=$(aws guardduty list-detectors --query 'DetectorIds[0]' --output text --region us-east-1)
aws guardduty list-findings --detector-id $DETECTOR_ID --region us-east-1
```

```bash
# 🔬 pull full detail on the first finding
aws guardduty get-findings --detector-id $DETECTOR_ID --finding-ids $(aws guardduty list-findings --detector-id $DETECTOR_ID --query 'FindingIds[0]' --output text --region us-east-1) --region us-east-1
```

### 📋 Subtask 6.3: Review AWS Config Compliance

```bash
# ✅ check rule-by-rule compliance
aws configservice describe-compliance-by-config-rule --region us-east-1
```

```bash
# 🕰️ pull configuration history for the Config S3 bucket
aws configservice get-resource-config-history \
    --resource-type AWS::S3::Bucket \
    --resource-id $(cd ../terraform && terraform output -raw config_s3_bucket) \
    --region us-east-1
```

### 📈 Subtask 6.4: Create Security Dashboard Script

```bash
cd ~/devsecops-lab/scripts
nano security_dashboard.py
```

```python
#!/usr/bin/env python3
"""
Security Dashboard - Aggregate security findings from AWS services
"""
# 📈 pulls Security Hub + GuardDuty + Config into one CLI dashboard
import boto3
import json
from datetime import datetime, timedelta

def get_security_hub_findings():
    """Get Security Hub findings"""
    client = boto3.client('securityhub', region_name='us-east-1')

    try:
        response = client.get_findings(
            Filters={
                'RecordState': [{'Value': 'ACTIVE', 'Comparison': 'EQUALS'}]
            },
            MaxResults=50
        )
        return response.get('Findings', [])
    except Exception as e:
        print(f"Error getting Security Hub findings: {e}")
        return []

def get_guardduty_findings():
    """Get GuardDuty findings"""
    client = boto3.client('guardduty', region_name='us-east-1')

    try:
        detectors = client.list_detectors()
        if not detectors['DetectorIds']:
            return []

        detector_id = detectors['DetectorIds'][0]
        findings = client.list_findings(DetectorId=detector_id)

        if findings['FindingIds']:
            detailed_findings = client.get_findings(
                DetectorId=detector_id,
                FindingIds=findings['FindingIds'][:10]  # Get first 10
            )
            return detailed_findings.get('Findings', [])
        return []
    except Exception as e:
        print(f"Error getting GuardDuty findings: {e}")
        return []

def get_config_compliance():
    """Get Config compliance status"""
    client = boto3.client('config', region_name='us-east-1')

    try:
        response = client.describe_compliance_by_config_rule()
        return response.get('ComplianceByConfigRules', [])
    except Exception as e:
        print(f"Error getting Config compliance: {e}")
        return []

def generate_dashboard():
    """Generate security dashboard"""
    print("=" * 60)
    print("DEVSECOPS SECURITY DASHBOARD")
    print("=" * 60)
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # 🔍 Security Hub findings
    print("🔍 SECURITY HUB FINDINGS")
    print("-" * 30)
    sh_findings = get_security_hub_findings()

    if sh_findings:
        severity_counts = {}
        for finding in sh_findings:
            severity = finding.get('Severity', {}).get('Label', 'UNKNOWN')
            severity_counts[severity] = severity_counts.get(severity, 0) + 1

        for severity, count in severity_counts.items():
            print(f"{severity}: {count}")
    else:
        print("No active findings")
    print()

    # 🛡️ GuardDuty findings
    print("🛡️  GUARDDUTY FINDINGS")
    print("-" * 30)
    gd_findings = get_guardduty_findings()

    if gd_findings:
        for finding in gd_findings[:5]:  # Show first 5
            print(f"• {finding.get('Title', 'Unknown threat')}")
            print(f"  Severity: {finding.get('Severity', 'Unknown')}")
    else:
        print("No threats detected")
    print()

    # 📋 Config compliance
    print("📋 CONFIG COMPLIANCE")
    print("-" * 30)
    config_rules = get_config_compliance()

    if config_rules:
        compliant = sum(1 for rule in config_rules if rule.get('Compliance', {}).get('ComplianceType') == 'COMPLIANT')
        total = len(config_rules)
        print(f"Compliant rules: {compliant}/{total}")

        non_compliant = [rule for rule in config_rules if rule.get('Compliance', {}).get('ComplianceType') == 'NON_COMPLIANT']
        if non_compliant:
            print("Non-compliant rules:")
            for rule in non_compliant[:3]:  # Show first 3
                print(f"• {rule.get('ConfigRuleName', 'Unknown rule')}")
    else:
        print("No Config rules found")
    print()

    print("=" * 60)
    print("Dashboard generation complete!")

if __name__ == "__main__":
    generate_dashboard()
```

```bash
# ▶️ run the dashboard
python3 security_dashboard.py
```

---

## 🧹 Task 7: Cleanup and Documentation

> ⚠️ **Source content ends here.** The original lab document is truncated immediately at the "Subtask 7.1:" heading — no cleanup commands (e.g. `terraform destroy`), no documentation steps, and no source conclusion were provided. Nothing below this point has been fabricated to fill that gap; the Conclusion is synthesized strictly from the Lab Objectives stated at the top of the lab.

---

## 🗺️ MITRE ATT&CK Mapping

| Technique ID | Technique | How This Lab Addresses It |
|---|---|---|
| [T1190](https://attack.mitre.org/techniques/T1190/) | Exploit Public-Facing Application | The `/data` endpoint's intentional unparameterized SQL query is caught by Bandit SAST scanning in the CodeBuild pipeline |
| [T1552.001](https://attack.mitre.org/techniques/T1552/001/) | Unsecured Credentials: Credentials In Files | `app.py`'s hard-coded `AWS_ACCESS_KEY`/`AWS_SECRET_KEY` demonstrate exactly what Bandit and code review are meant to catch |
| [T1078.004](https://attack.mitre.org/techniques/T1078/004/) | Valid Accounts: Cloud Accounts | Leaked AWS credentials like the hard-coded pair would grant an attacker valid cloud account access — GuardDuty and Security Hub exist to detect resulting anomalous activity |
| [T1195.002](https://attack.mitre.org/techniques/T1195/002/) | Supply Chain Compromise: Compromise Software Dependencies | Safety dependency scanning in the pipeline flags known-vulnerable pinned packages in `requirements.txt` |
| [T1580](https://attack.mitre.org/techniques/T1580/) | Cloud Infrastructure Discovery | AWS Config continuously records resource configuration, surfacing unauthorized or drifted infrastructure changes that could precede or follow discovery activity |

---

## 🔧 Troubleshooting

<details>
<summary>🔴 <code>terraform apply</code> fails on Security Hub or GuardDuty resources</summary>

- Confirm the AWS account doesn't already have Security Hub/GuardDuty enabled in another region conflict — check with `aws securityhub describe-hub` and `aws guardduty list-detectors`
- IAM permissions for the lab's AWS CLI profile must include `securityhub:*` and `guardduty:*` actions

</details>

<details>
<summary>🔴 Checkov reports failures on resources you expected to skip</summary>

- Confirm you're running with `--config-file .checkov.yml`, not the bare `checkov -d .` command — the skip list only applies when the config file is passed explicitly
- Double check `.checkov.yml` is in the directory you're scanning from

</details>

<details>
<summary>🔴 <code>git push -u origin master</code> to CodeCommit fails with authentication errors</summary>

- CodeCommit requires either Git credentials generated in IAM or the `git-remote-codecommit` helper — plain AWS CLI credentials alone won't authenticate a `git push`
- Verify the remote URL matches exactly what `terraform output -raw codecommit_repository_url` returns

</details>

<details>
<summary>🔴 CodeBuild's <code>buildspec.yml</code> security scan steps fail silently</summary>

- Note the `|| true` on each scan command — scan failures won't fail the build, but they also won't be visible unless you check the `*-report.json` artifacts afterward
- Confirm `generate_security_report.py` is present in the same directory as `buildspec.yml` before the `post_build` phase runs

</details>

<details>
<summary>🔴 <code>security_dashboard.py</code> returns empty results for every section</summary>

- GuardDuty and Security Hub findings take time to populate after first enabling — an idle lab account may have nothing to report yet
- Confirm the script's hardcoded `region_name='us-east-1'` matches the region you actually deployed into

</details>

---

## 🏁 Conclusion

### ✅ Key Accomplishments

- ☁️ Enabled **AWS Security Hub** with the AWS Foundational and CIS benchmark standards
- 🕵️ Deployed **Amazon GuardDuty** with S3, Kubernetes audit log, and EBS malware protection data sources
- 📋 Configured **AWS Config** with an encrypted, versioned S3 delivery bucket and a full-resource recorder
- 🤖 Associated **CodeGuru Reviewer** with a CodeCommit repository for automated code analysis
- 🏗️ Authored all of the above as **Terraform** IaC, then validated it with `terraform validate`/`fmt`
- 🔐 Scanned that IaC with **Checkov** (including a custom policy-as-code check) and **TFLint**
- 🐍 Built a sample Flask app with intentional credential, injection, and debug-mode issues, then caught them with **Bandit**, **Safety**, and **Checkov** inside a CodeBuild `buildspec.yml`
- 📊 Aggregated Security Hub, GuardDuty, and Config findings into a single Python CLI dashboard

### 🌍 Real-World Applications

- Enabling Security Hub, GuardDuty, and Config together gives a baseline of continuous detection, threat intelligence, and compliance drift monitoring — the three pillars most AWS security teams stand up first
- Defining that entire security posture as Terraform means it's reviewable, versioned, and repeatable across accounts instead of being clicked together once in the console
- Running Checkov and TFLint in the same workflow as `terraform plan` catches misconfigurations before they're ever applied to a real account
- Embedding Bandit, Safety, and Checkov directly into a CodeBuild `buildspec.yml` keeps security feedback in the same pipeline developers already use, rather than a separate audit process
- A findings dashboard that spans multiple AWS security services gives responders one place to triage instead of switching between three consoles

</br>

<div align="center">

**📚 Provided by [Al Nafi](https://alnafi.com) — Cloud & Cybersecurity Training**

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Training-blue?style=for-the-badge)

</div>
