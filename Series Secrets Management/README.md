<div align="center">

# 🔐 Series Secrets Management
### GitLeaks Detection + HashiCorp Vault Runtime Secret Injection on Kubernetes

![GitLeaks](https://img.shields.io/badge/GitLeaks-Secret_Scanning-FBB040?style=for-the-badge&logo=git&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![HashiCorp Vault](https://img.shields.io/badge/HashiCorp_Vault-FFEC6E?style=for-the-badge&logo=vault&logoColor=black)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Helm](https://img.shields.io/badge/Helm-0F1689?style=for-the-badge&logo=helm&logoColor=white)
![Minikube](https://img.shields.io/badge/Minikube-FF6D00?style=for-the-badge&logo=kubernetes&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![Linux](https://img.shields.io/badge/Ubuntu_20.04-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

</div>

---

## 📚 Table of Contents

- [📘 Overview](#-overview)
- [🎯 Lab Objectives](#-lab-objectives)
- [📋 Prerequisites](#-prerequisites)
- [💻 Lab Environment Setup](#-lab-environment-setup)
- [🕵️ Task 1: Setting Up GitLeaks for Sensitive Information Detection](#️-task-1-setting-up-gitleaks-for-sensitive-information-detection)
- [🔒 Task 2: Setting Up HashiCorp Vault with Kubernetes](#-task-2-setting-up-hashicorp-vault-with-kubernetes)
- [💉 Task 3: Implementing Runtime Secret Injection](#-task-3-implementing-runtime-secret-injection)
- [✅ Task 4: Testing and Validation](#-task-4-testing-and-validation)
- [🧯 Troubleshooting Common Issues](#-troubleshooting-common-issues)
- [🧹 Lab Cleanup](#-lab-cleanup)
- [🗺️ MITRE ATT&CK Mapping](#️-mitre-attck-mapping)
- [🏁 Conclusion](#-conclusion)

---

## 📘 Overview

This lab builds a complete **secrets management workflow** for DevOps pipelines — catching hardcoded credentials before they ever reach a remote repository with **GitLeaks**, and eliminating hardcoded secrets from running applications entirely with **HashiCorp Vault**'s runtime injection into Kubernetes pods.

---

## 🎯 Lab Objectives

| # | Objective |
|---|-----------|
| 1️⃣ | Understand the importance of secrets management in DevOps pipelines |
| 2️⃣ | Set up **GitLeaks** to detect sensitive information in Git commits |
| 3️⃣ | Create a DevOps pipeline with integrated security scanning |
| 4️⃣ | Deploy and configure **HashiCorp Vault** on a Kubernetes cluster |
| 5️⃣ | Implement runtime secret injection using Vault with Kubernetes |
| 6️⃣ | Secure application secrets using industry-standard practices |
| 7️⃣ | Troubleshoot common secrets management issues |

## 📋 Prerequisites

| Requirement | Details |
|---|---|
| 🌿 Git basics | Understanding of Git version control |
| 🐧 Linux CLI | Familiarity with Linux command-line operations |
| ☸️ Kubernetes basics | Working knowledge of pods, services, and deployments |
| 📄 YAML structure | Understanding of YAML file syntax |
| 🐳 Docker basics | Basic Docker concepts |

---

## 💻 Lab Environment Setup

> **☁️ Ready-to-Use Cloud Machines**
> Al Nafi provides pre-configured Linux-based cloud machines with all necessary tools installed. Simply click **Start Lab** to access your environment — no need to build your own VM or install additional software.

**Your environment includes:**

| Component | Detail |
|---|---|
| 🖥️ OS | Ubuntu 20.04 LTS with Docker installed |
| ☸️ Cluster | Kubernetes cluster (Minikube) pre-configured |
| 🌿 Tooling | Git and necessary development tools |
| 🌐 Network | Internet connectivity for downloading required packages |

---

## 🕵️ Task 1: Setting Up GitLeaks for Sensitive Information Detection

![GitLeaks](https://img.shields.io/badge/GitLeaks-FBB040?style=flat-square&logo=git&logoColor=white) ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)

### 📥 Subtask 1.1: Install GitLeaks

```bash
# 🔄 Update system packages
sudo apt update

# ⬇️ Download and install GitLeaks
wget https://github.com/gitleaks/gitleaks/releases/download/v8.18.0/gitleaks_8.18.0_linux_x64.tar.gz

# 📦 Extract the downloaded file
tar -xzf gitleaks_8.18.0_linux_x64.tar.gz

# 🚚 Move gitleaks to system path
sudo mv gitleaks /usr/local/bin/

# ✅ Verify installation
gitleaks version
```

### 🧪 Subtask 1.2: Create a Sample Repository with Secrets

```bash
# 📁 Create a new directory for our project
mkdir secrets-demo
cd secrets-demo

# 🌱 Initialize Git repository
git init

# ✍️ Create a sample application file with secrets
cat > app.py << 'EOF'
import os
import requests

# Bad practice - hardcoded secrets
API_KEY = "sk-1234567890abcdef"
DATABASE_PASSWORD = "super_secret_password123"
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"

def connect_to_database():
    connection_string = f"postgresql://user:{DATABASE_PASSWORD}@localhost:5432/mydb"
    return connection_string

def call_api():
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get("https://api.example.com/data", headers=headers)
    return response.json()

if __name__ == "__main__":
    print("Application started")
EOF

# 📄 Create a configuration file with more secrets
cat > config.yaml << 'EOF'
database:
  host: localhost
  port: 5432
  username: admin
  password: "MySecretPassword2023!"

api:
  key: "abc123def456ghi789"
  secret: "zyxwvu987654321"

aws:
  access_key_id: "AKIAI44QH8DHBEXAMPLE"
  secret_access_key: "je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY"
EOF

# ➕ Add files to Git
git add .
git commit -m "Initial commit with application code"
```

> ⚠️ **Note:** These secrets are intentionally hardcoded for demonstration purposes only — the whole point of Task 1 is to catch exactly this pattern before it ships.

### ⚙️ Subtask 1.3: Configure GitLeaks

```toml
# ⚙️ .gitleaks.toml — custom detection rules
title = "Gitleaks Configuration"

[extend]
useDefault = true

[[rules]]
description = "Custom API Key Detection"
id = "custom-api-key"
regex = '''(?i)(api[_-]?key|apikey)\s*[:=]\s*["\']?([a-zA-Z0-9_-]{20,})["\']?'''
keywords = ["api_key", "apikey", "api-key"]

[[rules]]
description = "Database Password Detection"
id = "database-password"
regex = '''(?i)(password|passwd|pwd)\s*[:=]\s*["\']([^"'\s]{8,})["\']'''
keywords = ["password", "passwd", "pwd"]

[allowlist]
description = "Allowlist for test files"
files = ['''test_.*\.py$''']
```

> **TODO:** Add an organization-specific regex rule (e.g. an internal token prefix) to `.gitleaks.toml` for your own environment.

### 🔍 Subtask 1.4: Run GitLeaks Scan

```bash
# 🔍 Scan the current repository
gitleaks detect --source . --verbose

# 📊 Generate a detailed report
gitleaks detect --source . --report-format json --report-path gitleaks-report.json

# 👀 View the report
cat gitleaks-report.json | jq '.'
```

### 🔄 Subtask 1.5: Integrate GitLeaks into CI/CD Pipeline

```bash
# 📁 Create GitHub Actions directory
mkdir -p .github/workflows
```

```yaml
# 🔄 .github/workflows/security-scan.yml
name: Security Scan

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  gitleaks:
    name: GitLeaks Secret Scanning
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
        with:
          fetch-depth: 0

      - name: Run GitLeaks
        uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          GITLEAKS_LICENSE: ${{ secrets.GITLEAKS_LICENSE }}

      - name: Upload GitLeaks report
        uses: actions/upload-artifact@v3
        if: failure()
        with:
          name: gitleaks-report
          path: results.sarif
```

---

## 🔒 Task 2: Setting Up HashiCorp Vault with Kubernetes

![Vault](https://img.shields.io/badge/HashiCorp_Vault-FFEC6E?style=flat-square&logo=vault&logoColor=black) ![Helm](https://img.shields.io/badge/Helm-0F1689?style=flat-square&logo=helm&logoColor=white) ![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)

### ▶️ Subtask 2.1: Start Kubernetes Cluster

```bash
# ▶️ Start minikube
minikube start --driver=docker --memory=4096 --cpus=2

# ✅ Verify cluster is running
kubectl cluster-info

# 📊 Check nodes
kubectl get nodes
```

### ⛵ Subtask 2.2: Install Helm

```bash
# ⬇️ Download and install Helm
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# ✅ Verify Helm installation
helm version

# 📚 Add HashiCorp Helm repository
helm repo add hashicorp https://helm.releases.hashicorp.com

# 🔄 Update Helm repositories
helm repo update
```

### 🚀 Subtask 2.3: Deploy Vault on Kubernetes

```bash
# 📁 Create namespace for Vault
kubectl create namespace vault
```

```yaml
# ⚙️ vault-values.yaml — Helm chart overrides
global:
  enabled: true
  tlsDisable: true

injector:
  enabled: true
  image:
    repository: "hashicorp/vault-k8s"
    tag: "1.3.1"

server:
  image:
    repository: "hashicorp/vault"
    tag: "1.15.2"

  resources:
    requests:
      memory: 256Mi
      cpu: 250m
    limits:
      memory: 256Mi
      cpu: 250m

  readinessProbe:
    enabled: true
    path: "/v1/sys/health?standbyok=true&sealedcode=204&uninitcode=204"
  livenessProbe:
    enabled: true
    path: "/v1/sys/health?standbyok=true"
    initialDelaySeconds: 60

  dataStorage:
    enabled: true
    size: 10Gi
    mountPath: "/vault/data"
    storageClass: null

  standalone:
    enabled: true
    config: |
      ui = true

      listener "tcp" {
        tls_disable = 1
        address = "[::]:8200"
        cluster_address = "[::]:8201"
      }

      storage "file" {
        path = "/vault/data"
      }

  service:
    enabled: true
    type: "ClusterIP"
    port: 8200
    targetPort: 8200

ui:
  enabled: true
  serviceType: "ClusterIP"
```

```bash
# 🚀 Install Vault using Helm
helm install vault hashicorp/vault --namespace vault -f vault-values.yaml

# ⏳ Wait for Vault to be ready
kubectl wait --for=condition=ready pod -l app.kubernetes.io/name=vault --namespace vault --timeout=300s
```

> ⚠️ **Note:** `tlsDisable: true` is used here for lab simplicity only. In production, always terminate TLS on the Vault listener.

### 🔓 Subtask 2.4: Initialize and Unseal Vault

```bash
# 📊 Check Vault pod status
kubectl get pods -n vault

# 🔑 Initialize Vault
kubectl exec -n vault vault-0 -- vault operator init -key-shares=1 -key-threshold=1 -format=json > vault-keys.json

# 🗝️ Extract unseal key and root token
VAULT_UNSEAL_KEY=$(cat vault-keys.json | jq -r ".unseal_keys_b64[]")
VAULT_ROOT_TOKEN=$(cat vault-keys.json | jq -r ".root_token")

echo "Unseal Key: $VAULT_UNSEAL_KEY"
echo "Root Token: $VAULT_ROOT_TOKEN"

# 🔓 Unseal Vault
kubectl exec -n vault vault-0 -- vault operator unseal $VAULT_UNSEAL_KEY

# ✅ Verify Vault status
kubectl exec -n vault vault-0 -- vault status
```

> **TODO:** This lab uses `-key-shares=1 -key-threshold=1` for simplicity. In production, use Shamir's Secret Sharing with multiple key holders (e.g. 5 shares, 3 threshold).

### 🔑 Subtask 2.5: Configure Vault for Kubernetes Authentication

```bash
# 🌐 Port forward to access Vault UI (run in background)
kubectl port-forward -n vault svc/vault 8200:8200 &

# 🌐 Set Vault environment variables
export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN=$VAULT_ROOT_TOKEN

# 🔑 Login to Vault
vault auth $VAULT_ROOT_TOKEN

# ☸️ Enable Kubernetes authentication
vault auth enable kubernetes

# ⚙️ Configure Kubernetes authentication
vault write auth/kubernetes/config \
    token_reviewer_jwt="$(kubectl get secret -n vault $(kubectl get serviceaccount -n vault vault -o jsonpath='{.secrets[0].name}') -o jsonpath='{.data.token}' | base64 --decode)" \
    kubernetes_host="https://$(kubectl get endpoints kubernetes -o jsonpath='{.subsets[0].addresses[0].ip}'):443" \
    kubernetes_ca_cert="$(kubectl config view --raw --minify --flatten -o jsonpath='{.clusters[].cluster.certificate-authority-data}' | base64 --decode)"
```

---

## 💉 Task 3: Implementing Runtime Secret Injection

![Vault](https://img.shields.io/badge/HashiCorp_Vault-FFEC6E?style=flat-square&logo=vault&logoColor=black) ![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)

### 📜 Subtask 3.1: Create Vault Policies and Secrets

```bash
# 📜 Create a policy for our application
vault policy write myapp-policy - <<EOF
path "secret/data/myapp/*" {
  capabilities = ["read"]
}
EOF

# 🔗 Create a Kubernetes role
vault write auth/kubernetes/role/myapp \
    bound_service_account_names=myapp \
    bound_service_account_namespaces=default \
    policies=myapp-policy \
    ttl=24h

# 🗄️ Enable KV secrets engine
vault secrets enable -path=secret kv-v2

# 💾 Store application secrets
vault kv put secret/myapp/config \
    database_password="VaultManagedPassword123!" \
    api_key="vault-managed-api-key-xyz789" \
    database_url="postgresql://user:password@db:5432/myapp"
```

### 👤 Subtask 3.2: Create Service Account and Application

```bash
# 👤 Create service account for our application
kubectl create serviceaccount myapp
```

```yaml
# 💉 myapp-deployment.yaml — Vault Agent sidecar injection
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
  labels:
    app: myapp
spec:
  replicas: 1
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
      annotations:
        vault.hashicorp.com/agent-inject: 'true'
        vault.hashicorp.com/role: 'myapp'
        vault.hashicorp.com/agent-inject-secret-database-config.txt: 'secret/data/myapp/config'
        vault.hashicorp.com/agent-inject-template-database-config.txt: |
          {{- with secret "secret/data/myapp/config" -}}
          DATABASE_PASSWORD="{{ .Data.data.database_password }}"
          API_KEY="{{ .Data.data.api_key }}"
          DATABASE_URL="{{ .Data.data.database_url }}"
          {{- end -}}
    spec:
      serviceAccountName: myapp
      containers:
      - name: myapp
        image: nginx:1.21
        ports:
        - containerPort: 80
        command: ["/bin/sh"]
        args:
          - -c
          - |
            echo "Starting application..."
            echo "Checking for injected secrets..."
            if [ -f /vault/secrets/database-config.txt ]; then
              echo "Secrets found! Content:"
              cat /vault/secrets/database-config.txt
            else
              echo "No secrets found"
            fi
            echo "Starting nginx..."
            nginx -g 'daemon off;'
        volumeMounts:
        - name: secrets
          mountPath: /vault/secrets
          readOnly: true
      volumes:
      - name: secrets
        emptyDir: {}
```

```bash
# 🚀 Deploy the application
kubectl apply -f myapp-deployment.yaml

# ⏳ Wait for deployment to be ready
kubectl wait --for=condition=available --timeout=300s deployment/myapp
```

### 🔍 Subtask 3.3: Verify Secret Injection

```bash
# 📊 Check pod status
kubectl get pods -l app=myapp

# 🏷️ Get pod name
POD_NAME=$(kubectl get pods -l app=myapp -o jsonpath='{.items[0].metadata.name}')

# 🔍 Check if secrets are injected
kubectl exec $POD_NAME -c myapp -- cat /vault/secrets/database-config.txt

# 📝 Check Vault agent logs
kubectl logs $POD_NAME -c vault-agent

# 📝 Verify the application logs
kubectl logs $POD_NAME -c myapp
```

### 🐍 Subtask 3.4: Create a More Complex Application Example

```yaml
# 🐍 python-app-configmap.yaml — Python app code as a ConfigMap
apiVersion: v1
kind: ConfigMap
metadata:
  name: python-app-code
data:
  app.py: |
    import os
    import time
    import json

    def load_secrets():
        secrets_file = '/vault/secrets/database-config.txt'
        if os.path.exists(secrets_file):
            print("Loading secrets from Vault...")
            with open(secrets_file, 'r') as f:
                content = f.read()
                print("Secrets loaded successfully!")
                print("Secret file content (first 50 chars):", content[:50] + "...")
                return True
        else:
            print("Secrets file not found!")
            return False

    def main():
        print("Python Application Starting...")

        while True:
            if load_secrets():
                print("Application running with secure secrets...")
            else:
                print("Application running without secrets (not secure)...")

            time.sleep(30)

    if __name__ == "__main__":
        main()
```

```bash
# 🚀 Apply the ConfigMap
kubectl apply -f python-app-configmap.yaml
```

```yaml
# 🐍 python-app-deployment.yaml — Vault-injected Python deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: python-myapp
  labels:
    app: python-myapp
spec:
  replicas: 1
  selector:
    matchLabels:
      app: python-myapp
  template:
    metadata:
      labels:
        app: python-myapp
      annotations:
        vault.hashicorp.com/agent-inject: 'true'
        vault.hashicorp.com/role: 'myapp'
        vault.hashicorp.com/agent-inject-secret-database-config.txt: 'secret/data/myapp/config'
        vault.hashicorp.com/agent-inject-template-database-config.txt: |
          {{- with secret "secret/data/myapp/config" -}}
          {
            "database_password": "{{ .Data.data.database_password }}",
            "api_key": "{{ .Data.data.api_key }}",
            "database_url": "{{ .Data.data.database_url }}"
          }
          {{- end -}}
    spec:
      serviceAccountName: myapp
      containers:
      - name: python-app
        image: python:3.9-slim
        command: ["python", "/app/app.py"]
        volumeMounts:
        - name: app-code
          mountPath: /app
        - name: secrets
          mountPath: /vault/secrets
          readOnly: true
      volumes:
      - name: app-code
        configMap:
          name: python-app-code
      - name: secrets
        emptyDir: {}
```

```bash
# 🚀 Deploy Python application
kubectl apply -f python-app-deployment.yaml

# ⏳ Wait for deployment
kubectl wait --for=condition=available --timeout=300s deployment/python-myapp
```

> **TODO:** Replace the `emptyDir` secrets volume with a `Memory` medium (`emptyDir: {medium: "Memory"}`) so injected secrets never touch disk.

### 📡 Subtask 3.5: Monitor and Verify the Complete Setup

```bash
# 📊 Check all pods
kubectl get pods

# 🏷️ Get Python app pod name
PYTHON_POD=$(kubectl get pods -l app=python-myapp -o jsonpath='{.items[0].metadata.name}')

# 📝 Check Python application logs
kubectl logs $PYTHON_POD -c python-app --tail=20

# 📝 Check Vault agent logs for Python app
kubectl logs $PYTHON_POD -c vault-agent --tail=20

# 🔍 Verify secrets are properly injected
kubectl exec $PYTHON_POD -c python-app -- cat /vault/secrets/database-config.txt

# ✅ Check Vault status
kubectl exec -n vault vault-0 -- vault status

# 📋 List active leases (should show Kubernetes auth tokens)
vault list auth/kubernetes/role
```

---

## ✅ Task 4: Testing and Validation

![Vault](https://img.shields.io/badge/HashiCorp_Vault-FFEC6E?style=flat-square&logo=vault&logoColor=black) ![GitLeaks](https://img.shields.io/badge/GitLeaks-FBB040?style=flat-square&logo=git&logoColor=white)

### 🔄 Subtask 4.1: Test Secret Rotation

```bash
# 🔄 Update secrets in Vault
vault kv put secret/myapp/config \
    database_password="NewRotatedPassword456!" \
    api_key="new-rotated-api-key-abc123" \
    database_url="postgresql://user:newpassword@db:5432/myapp"

# 🔁 Restart the application to pick up new secrets
kubectl rollout restart deployment/python-myapp

# ⏳ Wait for rollout to complete
kubectl rollout status deployment/python-myapp

# ✅ Verify new secrets are loaded
PYTHON_POD=$(kubectl get pods -l app=python-myapp -o jsonpath='{.items[0].metadata.name}')
kubectl logs $PYTHON_POD -c python-app --tail=10
kubectl exec $PYTHON_POD -c python-app -- cat /vault/secrets/database-config.txt
```

### 🕵️ Subtask 4.2: Test GitLeaks Integration

```bash
# 📁 Go back to our demo repository
cd ~/secrets-demo

# ✍️ Create a commit with a new secret
echo 'GITHUB_TOKEN="ghp_1234567890abcdefghijklmnopqrstuvwxyz"' >> config.yaml
git add config.yaml
git commit -m "Add GitHub token configuration"

# 🔍 Run GitLeaks scan on the latest commit
gitleaks detect --source . --log-level debug

# 🎯 Scan specific commit
LATEST_COMMIT=$(git rev-parse HEAD)
gitleaks detect --source . --log-opts="$LATEST_COMMIT^..$LATEST_COMMIT"
```

---

## 🧯 Troubleshooting Common Issues

<details>
<summary>🔒 Issue 1: Vault Pod Not Starting</summary>

```bash
# 📊 Check pod events
kubectl describe pod -n vault vault-0

# 📝 Check logs
kubectl logs -n vault vault-0

# 🔧 Common fix: Increase memory limits
kubectl patch deployment -n vault vault -p '{"spec":{"template":{"spec":{"containers":[{"name":"vault","resources":{"limits":{"memory":"512Mi"}}}]}}}}'
```
</details>

<details>
<summary>💉 Issue 2: Secret Injection Not Working</summary>

```bash
# 👤 Check service account permissions
kubectl describe serviceaccount myapp

# 📝 Verify Vault agent annotations
kubectl describe pod $POD_NAME

# 📝 Check Vault agent logs
kubectl logs $POD_NAME -c vault-agent

# 🌐 Test Vault connectivity from pod
kubectl exec $POD_NAME -c vault-agent -- wget -qO- http://vault.vault.svc.cluster.local:8200/v1/sys/health
```
</details>

<details>
<summary>🕵️ Issue 3: GitLeaks False Positives</summary>

```bash
# ⚙️ Update .gitleaks.toml to add allowlist
cat >> .gitleaks.toml << 'EOF'

[allowlist]
description = "Allowlist for example tokens"
regexes = ['''example''', '''EXAMPLE''']
paths = ['''.*test.*''', '''.*demo.*''']
EOF

# 🔍 Re-run scan
gitleaks detect --source . --config .gitleaks.toml
```
</details>

---

## 🧹 Lab Cleanup

```bash
# 🗑️ Clean up Kubernetes resources
kubectl delete deployment myapp python-myapp
kubectl delete configmap python-app-code
kubectl delete serviceaccount myapp

# 🗑️ Uninstall Vault
helm uninstall vault -n vault
kubectl delete namespace vault

# 🛑 Stop minikube
minikube stop

# 📁 Clean up demo repository
cd ~
rm -rf secrets-demo
```

---

## 🗺️ MITRE ATT&CK Mapping

This lab's controls map to mitigated ATT&CK techniques — security controls positioned to prevent or contain these techniques, rather than detect them after the fact:

| Technique | ID | Mitigating Control |
|---|---|---|
| Unsecured Credentials | T1552 | HashiCorp Vault centralizes secrets; runtime injection removes hardcoded credentials from application code |
| Unsecured Credentials: Credentials In Files | T1552.001 | GitLeaks scans Git commits and configuration files for hardcoded secrets before merge |
| Steal Application Access Token | T1528 | Vault issues short-TTL, policy-scoped tokens instead of static long-lived API keys |
| Valid Accounts: Cloud Accounts | T1078.004 | Vault's Kubernetes auth method binds secret access to a specific service account and namespace, scoping the blast radius |

---

## 🏁 Conclusion

In this comprehensive lab, you have successfully built a complete secrets management workflow. 🎉

### ✅ Key Accomplishments

- 🕵️ Implemented GitLeaks for automated secret detection in your DevOps pipeline, preventing sensitive information from being committed to version control
- 🔒 Deployed HashiCorp Vault on a Kubernetes cluster, creating a centralized and secure secrets management solution
- 💉 Configured runtime secret injection using Vault's Kubernetes integration, eliminating hardcoded secrets in application code
- 🔄 Created a complete DevOps security workflow that combines secret scanning and secure secret delivery

### 🌍 Why This Matters

This lab demonstrates critical security practices essential in modern DevOps environments. GitLeaks forms a first line of defense against accidental secret exposure, while the HashiCorp Vault integration provides enterprise-grade secret management with features like automatic rotation, audit logging, and fine-grained access control.

### 🚀 Real-World Impact

The techniques you've learned are used by major organizations to:

- 🛡️ Prevent data breaches caused by exposed credentials
- 📋 Maintain compliance with security regulations
- 🔐 Implement zero-trust security models
- 🔄 Automate secret lifecycle management

### 🔭 Next Steps

Consider exploring advanced Vault features like dynamic secrets, secret engines for different databases, and integration with cloud provider secret management services. You can also enhance your GitLeaks configuration to detect organization-specific secret patterns and integrate it with additional CI/CD tools.

This foundation in secrets management serves as a cornerstone for building secure, scalable applications in production environments.

---

<div align="center">

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Training-blueviolet?style=for-the-badge)

</div>
