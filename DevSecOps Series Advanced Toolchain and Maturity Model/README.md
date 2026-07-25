<div align="center">

# 📊 DevSecOps Series — Advanced Toolchain and Maturity Model

### Assessing and Advancing DevSecOps Practice from Basic to Optimized

![DevSecOps](https://img.shields.io/badge/DevSecOps-FF4B4B?style=for-the-badge&logo=OWASP&logoColor=white)
![OWASP](https://img.shields.io/badge/OWASP-000000?style=for-the-badge&logo=owasp&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![GitLab CI](https://img.shields.io/badge/GitLab_CI-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white)
![Trivy](https://img.shields.io/badge/Trivy-1904DA?style=for-the-badge&logo=aquasecurity&logoColor=white)

</div>

---

## 📚 Table of Contents

- [🎯 Learning Objectives](#-learning-objectives)
- [📋 Prerequisites](#-prerequisites)
- [🖥️ Lab Environment](#️-lab-environment)
- [🧭 Task 1: Understanding DevSecOps Maturity Model Framework](#-task-1-understanding-devsecops-maturity-model-framework)
- [🔧 Task 2: Installing DevSecOps Maturity Model Assessment Tool](#-task-2-installing-devsecops-maturity-model-assessment-tool)
- [🟢 Task 3: Implementing Level 1 Maturity Model (Basic)](#-task-3-implementing-level-1-maturity-model-basic)
- [🔵 Task 4: Implementing Level 2 Maturity Model (Managed)](#-task-4-implementing-level-2-maturity-model-managed)
- [🟣 Task 5: Implementing Level 3 Maturity Model (Defined)](#-task-5-implementing-level-3-maturity-model-defined)
- [🟠 Task 6: Implementing Level 4 Maturity Model (Optimized)](#-task-6-implementing-level-4-maturity-model-optimized)
- [🗺️ MITRE ATT&CK Mapping](#️-mitre-attck-mapping)
- [🧩 Key Concepts Summary](#-key-concepts-summary)
- [🏁 Conclusion](#-conclusion)

---

## 🎯 Learning Objectives

| # | Objective |
|---|-----------|
| 1 | Understand the DevSecOps Maturity Model framework and its importance in modern software development |
| 2 | Install and configure the DevSecOps Maturity Model assessment tool |
| 3 | Implement and evaluate maturity levels 1–4 in a practical environment |
| 4 | Assess current DevSecOps practices using standardized metrics |
| 5 | Create actionable improvement plans based on maturity assessment results |
| 6 | Configure automated security scanning tools integrated with CI/CD pipelines |
| 7 | Demonstrate practical implementation of security controls at different maturity levels |

## 📋 Prerequisites

| Skill Area | Requirement |
|---|---|
| 🔁 DevOps | Basic understanding of DevOps concepts and practices |
| 🐧 Linux | Familiarity with command line operations |
| 🌿 Git | Basic knowledge of Git version control |
| ⚙️ CI/CD | Understanding of CI/CD pipeline concepts |
| 🐳 Containers | Basic knowledge of Docker |
| 📄 YAML | Familiarity with YAML configuration files |

## 🖥️ Lab Environment

> ☁️ **Ready-to-Use Cloud Machine** — Al Nafi provides a pre-configured Linux-based cloud machine. Click **Start Lab** — no VM setup or extra installs required.

| Component | Details |
|---|---|
| 🖥️ OS | Ubuntu 20.04 LTS with administrative privileges |
| 🐳 Containers | Docker and Docker Compose pre-installed |
| 🌿 Dev Tools | Git and essential development tools |
| 🐍 Python | Python 3.8+ with pip |
| 🟩 Node.js | Node.js and npm for web-based tools |

---

## 🧭 Task 1: Understanding DevSecOps Maturity Model Framework

### 📖 Subtask 1.1: Introduction to DevSecOps Maturity Model

> 💡 The DevSecOps Maturity Model provides a structured approach to assess and improve security integration within DevOps practices.

| Level | Name | Description |
|---|---|---|
| 🟢 1 | Basic | Initial security awareness with manual processes |
| 🔵 2 | Managed | Defined security processes with some automation |
| 🟣 3 | Defined | Standardized security practices across teams |
| 🟠 4 | Optimized | Continuous improvement with advanced automation |

### 📁 Subtask 1.2: Setting Up the Working Directory

```bash
# 📁 Create the lab workspace
mkdir -p ~/devsecops-maturity-lab
cd ~/devsecops-maturity-lab

# 🗂️ Create subdirectories for each maturity component
mkdir -p {assessment,tools,configs,reports}

# 🔍 Verify the directory structure
tree . || ls -la
```

---

## 🔧 Task 2: Installing DevSecOps Maturity Model Assessment Tool

### 🌐 Subtask 2.1: Installing OWASP DevSecOps Maturity Model

```bash
# ⬇️ Clone the OWASP DevSecOps Maturity Model repository
git clone https://github.com/OWASP/DevSecOps-MaturityModel.git
cd DevSecOps-MaturityModel

# 📦 Install system dependencies
sudo apt update
sudo apt install -y nodejs npm python3-pip

# 📦 Install Node.js dependencies
npm install

# 🐍 Install Python dependencies if present
if [ -f requirements.txt ]; then
    pip3 install -r requirements.txt
fi
```

### ⚙️ Subtask 2.2: Setting Up the Assessment Environment

```bash
# 📝 Create the local assessment configuration
cat > config/local-config.yaml << 'EOF'
assessment:
  organization: "Lab Environment"
  assessor: "Student"
  date: "$(date +%Y-%m-%d)"
  scope: "Full DevSecOps Pipeline"

maturity_levels:
  level1:
    name: "Basic"
    description: "Initial security awareness"
  level2:
    name: "Managed"
    description: "Defined security processes"
  level3:
    name: "Defined"
    description: "Standardized practices"
  level4:
    name: "Optimized"
    description: "Continuous improvement"
EOF

# 🔐 Make the configuration file executable
chmod +x config/local-config.yaml
```

### ▶️ Subtask 2.3: Starting the Assessment Tool

```bash
# 🚀 Start the DevSecOps Maturity Model web interface
npm start &

# ⏳ Wait for the service to start
sleep 10

# ✅ Check if the service is running
curl -s http://localhost:3000 > /dev/null && echo "Service is running" || echo "Service failed to start"
```

---

## 🟢 Task 3: Implementing Level 1 Maturity Model (Basic)

> 🎯 Level 1 focuses on introducing basic security practices with minimal automation.

### 🧪 Subtask 3.1: Setting Up Basic Security Scanning

```bash
# 📁 Create a sample application for testing
cd ~/devsecops-maturity-lab
mkdir -p level1-basic/sample-app
cd level1-basic/sample-app
```

```python
# ⚠️ app.py — intentionally vulnerable Flask app used to demonstrate Level 1 scanning
from flask import Flask, request, render_template_string
import sqlite3
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Sample Application - Level 1</h1><a href="/search">Search Users</a>'

@app.route('/search')
def search():
    query = request.args.get('q', '')
    # 🚨 SQL Injection vulnerability (intentional for demo)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE name LIKE '%{query}%'")
    results = cursor.fetchall()
    conn.close()
    return f"Results: {results}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

```text
# requirements.txt
Flask==2.3.3
sqlite3
```

```bash
# 📦 Install dependencies
pip3 install -r requirements.txt
```

### 🔎 Subtask 3.2: Manual Security Assessment (Level 1)

```bash
# 🛡️ Install basic security scanning tools
sudo apt install -y bandit safety

# 🔍 Run static code analysis with Bandit
echo "Running Bandit security scan..."
bandit -r . -f json -o ../reports/bandit-level1.json
bandit -r . -f txt -o ../reports/bandit-level1.txt

# 🔍 Check dependencies for known vulnerabilities
echo "Checking dependencies for known vulnerabilities..."
safety check --json --output ../reports/safety-level1.json
safety check --output ../reports/safety-level1.txt
```

☑️ Manual Level 1 checklist:

```markdown
## Security Awareness
- [ ] Basic security training completed
- [ ] Security tools installed (Bandit, Safety)
- [ ] Manual security scans performed
- [ ] Vulnerability reports generated

## Basic Controls
- [ ] Static code analysis tool configured
- [ ] Dependency vulnerability scanning
- [ ] Manual code review process
- [ ] Basic incident response plan

## Documentation
- [ ] Security policies documented
- [ ] Tool usage guidelines created
- [ ] Vulnerability remediation process defined
```

### 📄 Subtask 3.3: Level 1 Assessment Results

| Category | Notes |
|---|---|
| ✅ Current State | Manual security processes, basic scanning tools, ad-hoc reviews, limited automation |
| 💪 Strengths | Security awareness established, basic tooling in place, documentation started |
| 🚧 Areas for Improvement | Automate scans, integrate with CI/CD, standardize processes, add continuous monitoring |
| ➡️ Next Steps | Move to Level 2 by automating scanning and integrating tools with the dev workflow |

```bash
echo "Level 1 implementation completed. Check reports in ../reports/"
```

---

## 🔵 Task 4: Implementing Level 2 Maturity Model (Managed)

> 🎯 Level 2 introduces automation and CI/CD integration.

### ⚙️ Subtask 4.1: Setting Up Automated Security Pipeline

```bash
cd ~/devsecops-maturity-lab
mkdir -p level2-managed
cd level2-managed
```

```yaml
# 🤖 .github/workflows/security-scan.yml — Level 2 automated security pipeline
name: DevSecOps Security Pipeline - Level 2

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
        python-version: '3.8'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install bandit safety semgrep
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

    # 🛡️ SAST
    - name: Run Bandit Security Scan
      run: |
        bandit -r . -f json -o bandit-report.json
        bandit -r . -f txt

    # 📦 Dependency scan
    - name: Run Safety Check
      run: |
        safety check --json --output safety-report.json
        safety check

    # 🕵️ SAST (broader ruleset)
    - name: Run Semgrep SAST
      run: |
        semgrep --config=auto --json --output=semgrep-report.json .
        semgrep --config=auto .

    # 📤 Publish results
    - name: Upload Security Reports
      uses: actions/upload-artifact@v3
      with:
        name: security-reports
        path: |
          bandit-report.json
          safety-report.json
          semgrep-report.json
```

### 🐳 Subtask 4.2: Implementing Container Security Scanning

```dockerfile
# 🐳 Dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

```bash
# ♻️ Reuse the Level 1 sample application
cp ../level1-basic/sample-app/app.py .
cp ../level1-basic/sample-app/requirements.txt .

# 🐳 Install Docker
sudo apt install -y docker.io
sudo systemctl start docker
sudo usermod -aG docker $USER

# 🔬 Install Trivy for container vulnerability scanning
sudo apt install -y wget apt-transport-https gnupg lsb-release
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo apt-key add -
echo "deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main" | sudo tee -a /etc/apt/sources.list.d/trivy.list
sudo apt update
sudo apt install -y trivy

# 🏗️ Build and scan the container image
docker build -t sample-app:level2 .
trivy image --format json --output ../reports/trivy-level2.json sample-app:level2
trivy image sample-app:level2
```

### 🧪 Subtask 4.3: Setting Up Automated Security Testing

```bash
# 🧪 security-tests.sh — runs the full Level 2 scan suite
cat > security-tests.sh << 'EOF'
#!/bin/bash

echo "Starting Level 2 Automated Security Testing..."

mkdir -p ../reports/level2

# 🛡️ SAST
echo "Running Static Application Security Testing..."
bandit -r . -f json -o ../reports/level2/sast-bandit.json
semgrep --config=auto --json --output=../reports/level2/sast-semgrep.json .

# 📦 Dependency scanning
echo "Running Dependency Vulnerability Scanning..."
safety check --json --output ../reports/level2/dependency-safety.json

# 🔬 Container scanning
echo "Running Container Security Scanning..."
trivy image --format json --output ../reports/level2/container-trivy.json sample-app:level2

# 🕷️ Basic DAST
echo "Starting application for DAST..."
docker run -d -p 5000:5000 --name test-app sample-app:level2
sleep 5

docker run -t owasp/zap2docker-stable zap-baseline.py -t http://host.docker.internal:5000 -J ../reports/level2/dast-zap.json || true

# 🧹 Cleanup
docker stop test-app
docker rm test-app

echo "Level 2 security testing completed!"
EOF

chmod +x security-tests.sh
./security-tests.sh
```

### 📊 Subtask 4.4: Level 2 Assessment and Reporting

| Category | Notes |
|---|---|
| ✅ Current State | Automated scanning, CI/CD integration, container scanning, basic DAST |
| 🧰 Implemented Controls | SAST (Bandit, Semgrep) · Dependency scan (Safety) · Container scan (Trivy) · DAST (OWASP ZAP baseline) · Automated reporting |
| 📈 Metrics | Scan automation ~80% · Pipeline integration complete · Detection & reporting automated |
| 💪 Strengths | Consistent scanning, early detection, automated reports, CI/CD integration |
| 🚧 Areas for Improvement | Security gates, compliance checking, deeper DAST coverage, metrics dashboard |
| ➡️ Next Steps to Level 3 | Standardize policies, add pipeline security gates, automate compliance, build a metrics dashboard |

```bash
echo "Level 2 implementation completed successfully!"
```

---

## 🟣 Task 5: Implementing Level 3 Maturity Model (Defined)

> 🎯 Level 3 focuses on standardized processes and security gates that block vulnerable code from reaching production.

### 🚧 Subtask 5.1: Implementing Security Gates and Policies

```bash
cd ~/devsecops-maturity-lab
mkdir -p level3-defined
cd level3-defined
```

```yaml
# 📜 security-policy.yaml — thresholds enforced by the security gate
security_policies:
  sast:
    fail_threshold: "HIGH"
    max_high_vulnerabilities: 0
    max_medium_vulnerabilities: 5
    max_low_vulnerabilities: 20

  dependency:
    fail_on_vulnerability: true
    allowed_licenses:
      - "MIT"
      - "Apache-2.0"
      - "BSD-3-Clause"
      - "ISC"

  container:
    fail_threshold: "HIGH"
    max_critical_vulnerabilities: 0
    max_high_vulnerabilities: 2
    base_image_policy: "approved_only"

  dast:
    fail_threshold: "MEDIUM"
    required_tests:
      - "sql_injection"
      - "xss"
      - "authentication"

  compliance:
    required_standards:
      - "OWASP_TOP_10"
      - "CWE_TOP_25"
    documentation_required: true
```

```python
#!/usr/bin/env python3
# 🚦 security-gate.py — evaluates scan results against security-policy.yaml
import json
import yaml
import sys
import os

class SecurityGate:
    def __init__(self, policy_file):
        with open(policy_file, 'r') as f:
            self.policies = yaml.safe_load(f)
        self.violations = []

    def check_sast_results(self, bandit_file, semgrep_file):
        """🛡️ Check SAST results against policy"""
        print("Checking SAST results...")

        if os.path.exists(bandit_file):
            with open(bandit_file, 'r') as f:
                bandit_data = json.load(f)

            high_issues = len([r for r in bandit_data.get('results', [])
                             if r.get('issue_severity') == 'HIGH'])
            medium_issues = len([r for r in bandit_data.get('results', [])
                               if r.get('issue_severity') == 'MEDIUM'])

            policy = self.policies['security_policies']['sast']
            if high_issues > policy['max_high_vulnerabilities']:
                self.violations.append(f"SAST: {high_issues} HIGH vulnerabilities exceed limit of {policy['max_high_vulnerabilities']}")
            if medium_issues > policy['max_medium_vulnerabilities']:
                self.violations.append(f"SAST: {medium_issues} MEDIUM vulnerabilities exceed limit of {policy['max_medium_vulnerabilities']}")

    def check_dependency_results(self, safety_file):
        """📦 Check dependency scan results"""
        print("Checking dependency scan results...")

        if os.path.exists(safety_file):
            with open(safety_file, 'r') as f:
                try:
                    safety_data = json.load(f)
                    if safety_data and len(safety_data) > 0:
                        self.violations.append(f"Dependencies: {len(safety_data)} vulnerabilities found")
                except json.JSONDecodeError:
                    pass

    def check_container_results(self, trivy_file):
        """🔬 Check container scan results"""
        print("Checking container scan results...")

        if os.path.exists(trivy_file):
            with open(trivy_file, 'r') as f:
                trivy_data = json.load(f)

            critical_count = 0
            high_count = 0

            for result in trivy_data.get('Results', []):
                for vuln in result.get('Vulnerabilities', []):
                    severity = vuln.get('Severity', '').upper()
                    if severity == 'CRITICAL':
                        critical_count += 1
                    elif severity == 'HIGH':
                        high_count += 1

            policy = self.policies['security_policies']['container']
            if critical_count > policy['max_critical_vulnerabilities']:
                self.violations.append(f"Container: {critical_count} CRITICAL vulnerabilities exceed limit")
            if high_count > policy['max_high_vulnerabilities']:
                self.violations.append(f"Container: {high_count} HIGH vulnerabilities exceed limit")

    def generate_report(self):
        """📄 Generate security gate report"""
        report = {
            'timestamp': '2024-01-01T00:00:00Z',
            'status': 'PASS' if len(self.violations) == 0 else 'FAIL',
            'violations': self.violations,
            'policy_compliance': len(self.violations) == 0
        }

        with open('../reports/level3/security-gate-report.json', 'w') as f:
            json.dump(report, f, indent=2)

        return report['status'] == 'PASS'

if __name__ == "__main__":
    gate = SecurityGate('security-policy.yaml')

    gate.check_sast_results('../reports/level2/sast-bandit.json', '../reports/level2/sast-semgrep.json')
    gate.check_dependency_results('../reports/level2/dependency-safety.json')
    gate.check_container_results('../reports/level2/container-trivy.json')

    if gate.generate_report():
        print("✅ Security gate PASSED")
        sys.exit(0)
    else:
        print("❌ Security gate FAILED")
        for violation in gate.violations:
            print(f"  - {violation}")
        sys.exit(1)
```

```bash
chmod +x security-gate.py
```

### 📑 Subtask 5.2: Implementing Compliance Automation

```python
#!/usr/bin/env python3
# 📋 compliance-check.py — checks OWASP Top 10 exposure and documentation compliance
import json
import yaml
import os
from datetime import datetime

class ComplianceChecker:
    def __init__(self):
        self.compliance_results = {
            'owasp_top_10': {},
            'cwe_top_25': {},
            'documentation': {},
            'timestamp': datetime.now().isoformat()
        }

    def check_owasp_top_10(self, scan_results_dir):
        """🔟 Check compliance with OWASP Top 10"""
        print("Checking OWASP Top 10 compliance...")

        owasp_categories = {
            'A01_Broken_Access_Control': False,
            'A02_Cryptographic_Failures': False,
            'A03_Injection': False,
            'A04_Insecure_Design': False,
            'A05_Security_Misconfiguration': False,
            'A06_Vulnerable_Components': False,
            'A07_Authentication_Failures': False,
            'A08_Software_Integrity_Failures': False,
            'A09_Logging_Monitoring_Failures': False,
            'A10_SSRF': False
        }

        bandit_file = os.path.join(scan_results_dir, 'sast-bandit.json')
        if os.path.exists(bandit_file):
            with open(bandit_file, 'r') as f:
                bandit_data = json.load(f)

            for result in bandit_data.get('results', []):
                test_id = result.get('test_id', '')
                if 'sql' in test_id.lower() or 'injection' in result.get('test_name', '').lower():
                    owasp_categories['A03_Injection'] = True

        safety_file = os.path.join(scan_results_dir, 'dependency-safety.json')
        if os.path.exists(safety_file):
            try:
                with open(safety_file, 'r') as f:
                    safety_data = json.load(f)
                if safety_data:
                    owasp_categories['A06_Vulnerable_Components'] = True
            except:
                pass

        self.compliance_results['owasp_top_10'] = owasp_categories

    def check_documentation_compliance(self):
        """📚 Check documentation compliance"""
        print("Checking documentation compliance...")

        required_docs = {
            'security_policy': os.path.exists('security-policy.yaml'),
            'incident_response': os.path.exists('incident-response.md'),
            'security_training': os.path.exists('security-training.md'),
            'vulnerability_management': os.path.exists('vulnerability-management.md')
        }

        self.compliance_results['documentation'] = required_docs

    def generate_compliance_report(self):
        """📄 Generate compliance report"""
        os.makedirs('../reports/level3', exist_ok=True)

        with open('../reports/level3/compliance-report.json', 'w') as f:
            json.dump(self.compliance_results, f, indent=2)

        with open('../reports/level3/compliance-report.md', 'w') as f:
            f.write("# Level 3 Compliance Report\n\n")
            f.write(f"Generated: {self.compliance_results['timestamp']}\n\n")

            f.write("## OWASP Top 10 Compliance\n")
            for category, detected in self.compliance_results['owasp_top_10'].items():
                status = "⚠️ DETECTED" if detected else "✅ CLEAN"
                f.write(f"- {category}: {status}\n")

            f.write("\n## Documentation Compliance\n")
            for doc, exists in self.compliance_results['documentation'].items():
                status = "✅ EXISTS" if exists else "❌ MISSING"
                f.write(f"- {doc}: {status}\n")

if __name__ == "__main__":
    checker = ComplianceChecker()
    checker.check_owasp_top_10('../reports/level2')
    checker.check_documentation_compliance()
    checker.generate_compliance_report()
    print("Compliance check completed!")
```

```bash
chmod +x compliance-check.py
```

📚 Required documentation templates:

<details>
<summary>🚨 <strong>incident-response.md</strong></summary>

```markdown
## Incident Classification
- **Critical**: System compromise, data breach
- **High**: Vulnerability exploitation attempt
- **Medium**: Policy violation, suspicious activity
- **Low**: Minor security event

## Response Team
- Incident Commander: Security Team Lead
- Technical Lead: DevOps Engineer
- Communications: Product Manager

## Response Procedures
1. Detection and Analysis
2. Containment and Eradication
3. Recovery and Post-Incident Analysis
4. Documentation and Lessons Learned
```
</details>

<details>
<summary>🎓 <strong>security-training.md</strong></summary>

```markdown
## Mandatory Training
- Secure Coding Practices
- OWASP Top 10 Awareness
- Incident Response Procedures
- Data Protection and Privacy

## Role-Based Training
- Developers: Secure coding, SAST tools
- DevOps: Infrastructure security, container security
- QA: Security testing, DAST tools

## Training Schedule
- Initial training: Within 30 days of joining
- Refresher training: Annually
- Specialized training: As needed
```
</details>

<details>
<summary>🩹 <strong>vulnerability-management.md</strong></summary>

```markdown
## Vulnerability Discovery
- Automated scanning (SAST, DAST, SCA)
- Manual security testing
- External security assessments
- Bug bounty programs

## Remediation Timeline
- Critical: 24 hours
- High: 7 days
- Medium: 30 days
- Low: 90 days

## Tracking and Reporting
- Vulnerability database maintenance
- Regular status reporting
- Metrics and KPIs
```
</details>

### 🔁 Subtask 5.3: Advanced Pipeline Integration

```yaml
# 🦊 .gitlab-ci.yml — pipeline with enforced security gates ahead of deploy
stages:
  - build
  - security-scan
  - security-gate
  - compliance-check
  - deploy

variables:
  DOCKER_IMAGE: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA

build: # 🏗️
  stage: build
  script:
    - docker build -t $DOCKER_IMAGE .
    - docker push $DOCKER_IMAGE

sast-scan: # 🛡️
  stage: security-scan
  script:
    - bandit -r . -f json -o bandit-results.json
    - semgrep --config=auto --json --output=semgrep-results.json .
  artifacts:
    reports:
      sast: [bandit-results.json, semgrep-results.json]
    paths:
      - bandit-results.json
      - semgrep-results.json

dependency-scan: # 📦
  stage: security-scan
  script:
    - safety check --json --output safety-results.json
  artifacts:
    reports:
      dependency_scanning: safety-results.json
    paths:
      - safety-results.json

container-scan: # 🔬
  stage: security-scan
  script:
    - trivy image --format json --output trivy-results.json $DOCKER_IMAGE
  artifacts:
    reports:
      container_scanning: trivy-results.json
    paths:
      - trivy-results.json

security-gate: # 🚦
  stage: security-gate
  script:
    - python3 security-gate.py
  dependencies:
    - sast-scan
    - dependency-scan
    - container-scan
  artifacts:
    paths:
      - reports/level3/security-gate-report.json

compliance-check: # 📋
  stage: compliance-check
  script:
    - python3 compliance-check.py
  artifacts:
    paths:
      - reports/level3/compliance-report.json
      - reports/level3/compliance-report.md

deploy-staging: # 🚀
  stage: deploy
  script:
    - echo "Deploying to staging environment"
    - docker run -d -p 5001:5000 --name staging-app $DOCKER_IMAGE
  dependencies:
    - security-gate
    - compliance-check
  only:
    - develop

deploy-production: # 🏁
  stage: deploy
  script:
    - echo "Deploying to production environment"
    - docker run -d -p 5002:5000 --name production-app $DOCKER_IMAGE
  dependencies:
    - security-gate
    - compliance-check
  only:
    - main
  when: manual
```

### 📈 Subtask 5.4: Level 3 Assessment and Metrics

```bash
# ▶️ Run the Level 3 gate and compliance checks
mkdir -p ../reports/level3
python3 security-gate.py
python3 compliance-check.py
```

| Category | Notes |
|---|---|
| ✅ Current State | Security gates in CI/CD, automated compliance checking, standardized policies, advanced reporting |
| 🧰 Implemented Controls | Policy-based gates · OWASP Top 10 compliance · Automated documentation compliance · Risk-based vuln management |
| 📊 Key Metrics | Gate pass rate 95% · Policy compliance 100% · MTTR: Critical <24h, High <7d, Medium <30d · Doc compliance 100% |
| 💪 Strengths | Consistent policy enforcement, automated compliance verification, standardized cross-team processes |
| 🚧 Areas for Improvement | Advanced threat modeling, runtime security monitoring, metrics dashboard, continuous compliance monitoring |
| ➡️ Next Steps to Level 4 | AI/ML-based threat detection, RASP, continuous compliance monitoring, advanced security analytics |

```bash
echo "Level 3 implementation completed successfully!"
```

---

## 🟠 Task 6: Implementing Level 4 Maturity Model (Optimized)

> 🎯 Level 4 represents the highest maturity level — continuous improvement, advanced analytics, and AI-driven security.

### 📊 Subtask 6.1: Implementing Advanced Security Analytics

```bash
cd ~/devsecops-maturity-lab
mkdir -p level4-optimized
cd level4-optimized

# 📦 Install advanced analytics tools
pip3 install pandas numpy matplotlib seaborn scikit-learn
```

```python
#!/usr/bin/env python3
# 📈 security-analytics.py — trend analysis engine for maturity metrics
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import os

class SecurityAnalytics:
    def __init__(self):
        self.metrics = {
            'vulnerability_trends': [],
            'security_gate_performance': [],
            'compliance_scores': [],
            'threat_intelligence': []
        }

    def analyze_vulnerability_trends(self, scan_results_dir):
        """📉 Analyze vulnerability trends over time"""
        print("Analyzing vulnerability trends...")

        # Simulate historical data for demonstration
        dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='W')

        vulnerability_data = []
        for date in dates:
            # Simulate decreasing vulnerability trend (improvement over time)
            base_vulns = max(50 - (date.dayofyear // 7), 5)
            critical = max(np.random.poisson(base_vulns * 0.1), 0)
            high = max(np.random.poisson(base_vulns * 0.3), 0)
            medium = max(np.random.poisson(base_vulns * 0.4), 0)
            low = max(np.random.poisson(base_vulns * 0.2), 0)

            vulnerability_data
```

> ⚠️ **Note:** The provided lab material ends mid-script at this point in the `analyze_vulnerability_trends` method — the `vulnerability_data` list append and the remainder of the Level 4 analytics engine (plus any subsequent Level 4 subtasks, verification checklist, and conclusion) were not included in the source content.

```markdown
# TODO: Complete the vulnerability_data.append(...) call and the rest of the
# SecurityAnalytics class, then continue with any remaining Level 4 subtasks
# (e.g. ML-based anomaly detection, RASP integration, continuous compliance
# monitoring) once that content is available.
```

---

## 🗺️ MITRE ATT&CK Mapping

> Maps the vulnerability classes this maturity model's tooling is positioned to catch at each level to the techniques they mitigate:

| Technique ID | Technique | Mitigated By |
|---|---|---|
| T1190 | Exploit Public-Facing Application | Bandit SAST + OWASP ZAP DAST catching the demo app's SQL injection flaw |
| T1195.001 | Compromise Software Supply Chain (Dependencies) | Safety dependency vulnerability scanning gate (Level 2–3) |
| T1610 | Deploy Container | Trivy container image scanning with enforced critical/high vulnerability thresholds |
| T1611 | Escape to Host | `base_image_policy: approved_only` control in the Level 3 security policy |

## 🧩 Key Concepts Summary

| Maturity Level | Focus | Core Tooling |
|---|---|---|
| 🟢 Level 1 — Basic | Manual security awareness | Bandit (SAST), Safety (dependency check) |
| 🔵 Level 2 — Managed | CI/CD automation | + Semgrep, Trivy (container), OWASP ZAP (DAST) |
| 🟣 Level 3 — Defined | Standardized policy enforcement | + Policy-driven security gates, OWASP Top 10 / CWE Top 25 compliance automation |
| 🟠 Level 4 — Optimized | Continuous, data-driven improvement | + pandas/scikit-learn based security analytics, trend & anomaly analysis |

---

## 🏁 Conclusion

### 🎉 Key Accomplishments

- 📊 Understood the DevSecOps Maturity Model framework and its role in modern software development
- 🔧 Installed and configured the OWASP DevSecOps Maturity Model assessment tool
- 🟢🔵🟣 Implemented and evaluated maturity Levels 1 through 3 in a practical environment, moving from manual scanning to automated, policy-gated pipelines
- 📈 Assessed DevSecOps practices using standardized metrics at each level
- ⚙️ Configured automated security scanning (SAST, dependency, container, DAST) integrated with CI/CD pipelines
- 🟠 Began implementing Level 4 advanced security analytics tooling

### 💡 Why This Matters

Progressing through the maturity model — from ad-hoc manual scans at Level 1 to policy-enforced security gates at Level 3 and analytics-driven continuous improvement at Level 4 — mirrors how real organizations mature their DevSecOps posture over time rather than adopting every control at once. Each level builds concrete, verifiable controls (scanning tools, CI/CD gates, compliance automation) on top of the last, giving teams a measurable path to follow.

```markdown
# TODO: Once the remaining Level 4 source material is available, extend this
# README's conclusion with Real-World Applications and Next Steps sections
# consistent with the rest of the Al Nafi lab series.
```

---

<div align="center">

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Training-1976D2?style=for-the-badge)

</div>
