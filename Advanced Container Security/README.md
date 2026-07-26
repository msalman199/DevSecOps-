<div align="center">

# 🛡️ Advanced Container Security
### DevSecOps Pipeline — Scanning, Signing & Runtime Hardening

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Trivy](https://img.shields.io/badge/Trivy-1904DA?style=for-the-badge&logo=aquasecurityapp&logoColor=white)
![Notary](https://img.shields.io/badge/Docker_Content_Trust-Notary-0DB7ED?style=for-the-badge&logo=docker&logoColor=white)
![Minikube](https://img.shields.io/badge/Minikube-FF6D00?style=for-the-badge&logo=kubernetes&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![SecComp](https://img.shields.io/badge/SecComp-Syscall_Filtering-C21325?style=for-the-badge&logo=linux&logoColor=white)
![AppArmor](https://img.shields.io/badge/AppArmor-MAC-2E2E2E?style=for-the-badge&logo=linux&logoColor=white)
![Linux](https://img.shields.io/badge/Ubuntu_20.04-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

</div>

---

## 📚 Table of Contents

- [📘 Overview](#-overview)
- [🎯 Learning Objectives](#-learning-objectives)
- [📋 Prerequisites](#-prerequisites)
- [💻 Lab Environment Setup](#-lab-environment-setup)
- [🧩 Task 1: Setting Up the DevSecOps Pipeline Foundation](#-task-1-setting-up-the-devsecops-pipeline-foundation)
- [🔍 Task 2: Implementing Container Image Scanning with Trivy](#-task-2-implementing-container-image-scanning-with-trivy)
- [🔏 Task 3: Digital Signing with Docker Content Trust (Notary)](#-task-3-digital-signing-with-docker-content-trust-notary)
- [☸️ Task 4: Creating a Kubernetes Cluster and Deploying Signed Images](#️-task-4-creating-a-kubernetes-cluster-and-deploying-signed-images)
- [🧱 Task 5: Implementing Runtime Security with SecComp and AppArmor](#-task-5-implementing-runtime-security-with-seccomp-and-apparmor)
- [✅ Task 6: Validation and Testing](#-task-6-validation-and-testing)
- [🧯 Troubleshooting Common Issues](#-troubleshooting-common-issues)
- [🧹 Cleanup](#-cleanup)
- [🗺️ MITRE ATT&CK Mapping](#️-mitre-attck-mapping)
- [🏁 Conclusion](#-conclusion)

---

## 📘 Overview

This lab builds a complete **DevSecOps pipeline** for containerized applications — scanning images for vulnerabilities, cryptographically signing them, deploying them to Kubernetes, and locking down their runtime behavior with SecComp and AppArmor. Every stage of the container lifecycle gets a security control attached to it, from build to runtime.

---

## 🎯 Learning Objectives

| # | Objective |
|---|-----------|
| 1️⃣ | Understand the fundamentals of DevSecOps pipeline implementation |
| 2️⃣ | Implement container image vulnerability scanning using **Trivy** |
| 3️⃣ | Digitally sign Docker images using **Notary** for enhanced security |
| 4️⃣ | Deploy signed container images to **DockerHub** registry |
| 5️⃣ | Create and configure a **Kubernetes** cluster for secure container orchestration |
| 6️⃣ | Implement runtime security controls using **SecComp** and **AppArmor** profiles |
| 7️⃣ | Integrate security best practices throughout the container lifecycle |

## 📋 Prerequisites

| Requirement | Details |
|---|---|
| 🐳 Docker basics | Understanding of containers and containerization concepts |
| 🐧 Linux CLI | Familiarity with Linux command-line operations |
| ☸️ Kubernetes basics | Working knowledge of pods, deployments, and services |
| 🔄 CI/CD fundamentals | Understanding of pipeline concepts |
| 🔑 DockerHub account | Required for image registry push/pull operations |

---

## 💻 Lab Environment Setup

> **☁️ Ready-to-Use Cloud Machines**
> Al Nafi provides pre-configured Linux-based cloud machines for this lab. Simply click **Start Lab** to access your dedicated environment — no need to build or configure your own virtual machine.

**Your environment includes:**

| Component | Detail |
|---|---|
| 🖥️ OS | Ubuntu 20.04 LTS with Docker pre-installed |
| ☸️ Tooling | `kubectl` and necessary Kubernetes tools |
| 🌐 Network | Internet connectivity for downloading required tools |
| ⚙️ Resources | Sufficient to run a local Kubernetes cluster |

---

## 🧩 Task 1: Setting Up the DevSecOps Pipeline Foundation

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)

### 🔧 Subtask 1.1: Environment Preparation

```bash
# 🔄 Update the system packages
sudo apt update && sudo apt upgrade -y

# 📁 Create a working directory for our lab
mkdir -p ~/devsecops-lab
cd ~/devsecops-lab

# 🐳 Verify Docker installation
docker --version
```

### 🔍 Subtask 1.2: Install Trivy for Container Scanning

```bash
# 📦 Install dependencies
sudo apt-get install wget apt-transport-https gnupg lsb-release -y

# 🔑 Add the Trivy repository key
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | sudo apt-key add -
echo "deb https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main" | sudo tee -a /etc/apt/sources.list.d/trivy.list

# ⬇️ Install Trivy
sudo apt-get update
sudo apt-get install trivy -y

# ✅ Verify Trivy installation
trivy --version
```

### 🐍 Subtask 1.3: Create a Sample Application

```bash
# 📁 Create application directory
mkdir -p ~/devsecops-lab/webapp
cd ~/devsecops-lab/webapp

# ✍️ Create a simple Python web application
cat > app.py << 'EOF'
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Secure Container Demo Application</h1><p>This application is running in a secured container!</p>'

@app.route('/health')
def health():
    return {'status': 'healthy', 'version': '1.0.0'}

# TODO: Add a /version endpoint that reads the app version from an environment variable

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
EOF

# 📋 Create requirements file
cat > requirements.txt << 'EOF'
Flask==2.3.3
Werkzeug==2.3.7
EOF
```

### 📄 Subtask 1.4: Create Dockerfile

```dockerfile
# 🐳 Use specific version instead of latest
FROM python:3.9-slim-bullseye

# 👤 Create non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

# 📁 Set working directory
WORKDIR /app

# 📋 Copy requirements first for better caching
COPY requirements.txt .

# 📦 Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 📄 Copy application code
COPY app.py .

# 🔒 Change ownership to non-root user
RUN chown -R appuser:appuser /app

# 👤 Switch to non-root user
USER appuser

# 🌐 Expose port
EXPOSE 5000

# ▶️ Run application
CMD ["python", "app.py"]
```

> **TODO:** Pin the base image to a digest (`python:3.9-slim-bullseye@sha256:...`) instead of a tag for full build reproducibility.

---

## 🔍 Task 2: Implementing Container Image Scanning with Trivy

![Trivy](https://img.shields.io/badge/Trivy-1904DA?style=flat-square&logo=aquasecurityapp&logoColor=white) ![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white)

### 🏗️ Subtask 2.1: Build and Scan Docker Image

```bash
# 🏗️ Build the Docker image
docker build -t secure-webapp:v1.0 .

# 🔍 Scan the image with Trivy for vulnerabilities
trivy image secure-webapp:v1.0

# 📊 Generate detailed report in JSON format
trivy image --format json --output scan-report.json secure-webapp:v1.0

# ⚠️ View critical and high severity vulnerabilities only
trivy image --severity CRITICAL,HIGH secure-webapp:v1.0
```

### 🤖 Subtask 2.2: Create Automated Scanning Script

```bash
# ✍️ Create scanning script
cat > scan-image.sh << 'EOF'
#!/bin/bash

IMAGE_NAME=$1
SEVERITY_THRESHOLD="CRITICAL,HIGH"

if [ -z "$IMAGE_NAME" ]; then
    echo "Usage: $0 <image-name>"
    exit 1
fi

echo "Scanning image: $IMAGE_NAME"
echo "Severity threshold: $SEVERITY_THRESHOLD"

# 🔍 Run Trivy scan
trivy image --severity $SEVERITY_THRESHOLD --format table $IMAGE_NAME

# 🚦 Check for critical vulnerabilities and exit with error if found
CRITICAL_COUNT=$(trivy image --severity CRITICAL --format json $IMAGE_NAME | jq '.Results[]?.Vulnerabilities[]? | select(.Severity=="CRITICAL") | .VulnerabilityID' | wc -l)

if [ $CRITICAL_COUNT -gt 0 ]; then
    echo "ERROR: Found $CRITICAL_COUNT critical vulnerabilities. Build failed!"
    exit 1
else
    echo "SUCCESS: No critical vulnerabilities found. Image is ready for signing."
    exit 0
fi
EOF

# ✅ Make script executable
chmod +x scan-image.sh

# ▶️ Run the scanning script
./scan-image.sh secure-webapp:v1.0
```

> **TODO:** Adjust `SEVERITY_THRESHOLD` to also gate on `MEDIUM` findings once the baseline image is clean.

---

## 🔏 Task 3: Digital Signing with Docker Content Trust (Notary)

![Notary](https://img.shields.io/badge/Docker_Content_Trust-Notary-0DB7ED?style=flat-square&logo=docker&logoColor=white) ![DockerHub](https://img.shields.io/badge/DockerHub-2496ED?style=flat-square&logo=docker&logoColor=white)

### 🔐 Subtask 3.1: Enable Docker Content Trust

```bash
# 🔐 Enable Docker Content Trust
export DOCKER_CONTENT_TRUST=1

# ✅ Verify the environment variable is set
echo "Docker Content Trust enabled: $DOCKER_CONTENT_TRUST"
```

### 🔑 Subtask 3.2: Configure DockerHub Authentication

```bash
# 🔑 Login to DockerHub (replace with your credentials)
echo "Please enter your DockerHub username:"
read DOCKERHUB_USERNAME

docker login -u $DOCKERHUB_USERNAME

# 🏷️ Tag image for DockerHub
docker tag secure-webapp:v1.0 $DOCKERHUB_USERNAME/secure-webapp:v1.0-signed
```

### 📤 Subtask 3.3: Push Signed Image to DockerHub

```bash
# 📤 Push the signed image to DockerHub
# This will automatically sign the image due to DOCKER_CONTENT_TRUST=1
docker push $DOCKERHUB_USERNAME/secure-webapp:v1.0-signed

# 🔍 Verify the signature
docker trust inspect $DOCKERHUB_USERNAME/secure-webapp:v1.0-signed
```

### 🧾 Subtask 3.4: Create Signing Verification Script

```bash
# ✍️ Create verification script
cat > verify-signature.sh << 'EOF'
#!/bin/bash

IMAGE_NAME=$1

if [ -z "$IMAGE_NAME" ]; then
    echo "Usage: $0 <image-name>"
    exit 1
fi

echo "Verifying signature for image: $IMAGE_NAME"

# 🔍 Check if image is signed
if docker trust inspect $IMAGE_NAME > /dev/null 2>&1; then
    echo "SUCCESS: Image signature verified!"
    docker trust inspect $IMAGE_NAME
    exit 0
else
    echo "ERROR: Image signature verification failed!"
    exit 1
fi
EOF

# ✅ Make script executable
chmod +x verify-signature.sh

# ▶️ Test signature verification
./verify-signature.sh $DOCKERHUB_USERNAME/secure-webapp:v1.0-signed
```

> **TODO:** Add a second signer via `docker trust signer add` to demonstrate multi-party signing approval.

---

## ☸️ Task 4: Creating a Kubernetes Cluster and Deploying Signed Images

![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white) ![Minikube](https://img.shields.io/badge/Minikube-FF6D00?style=flat-square&logo=kubernetes&logoColor=white)

### ⚙️ Subtask 4.1: Install and Setup Minikube

```bash
# ⬇️ Install Minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# ▶️ Start Minikube cluster
minikube start --driver=docker

# ✅ Verify cluster is running
kubectl cluster-info
kubectl get nodes
```

### 📜 Subtask 4.2: Configure Image Pull Policy for Signed Images

```bash
# 📁 Create namespace for our secure application
kubectl create namespace secure-apps
```

```yaml
# 📜 secure-deployment.yaml — signed-image deployment + service
apiVersion: apps/v1
kind: Deployment
metadata:
  name: secure-webapp
  namespace: secure-apps
  labels:
    app: secure-webapp
spec:
  replicas: 2
  selector:
    matchLabels:
      app: secure-webapp
  template:
    metadata:
      labels:
        app: secure-webapp
    spec:
      containers:
      - name: webapp
        image: $DOCKERHUB_USERNAME/secure-webapp:v1.0-signed
        ports:
        - containerPort: 5000
        resources:
          requests:
            memory: "64Mi"
            cpu: "250m"
          limits:
            memory: "128Mi"
            cpu: "500m"
        # 🔒 Pod-level hardening
        securityContext:
          runAsNonRoot: true
          runAsUser: 1000
          allowPrivilegeEscalation: false
          readOnlyRootFilesystem: false
          capabilities:
            drop:
            - ALL
---
apiVersion: v1
kind: Service
metadata:
  name: secure-webapp-service
  namespace: secure-apps
spec:
  selector:
    app: secure-webapp
  ports:
  - protocol: TCP
    port: 80
    targetPort: 5000
  type: ClusterIP
```

### 🚀 Subtask 4.3: Deploy Application to Kubernetes

```bash
# 🚀 Apply the deployment
kubectl apply -f secure-deployment.yaml

# 📊 Check deployment status
kubectl get deployments -n secure-apps
kubectl get pods -n secure-apps

# ⏳ Wait for pods to be ready
kubectl wait --for=condition=ready pod -l app=secure-webapp -n secure-apps --timeout=300s

# 🧪 Test the application
kubectl port-forward -n secure-apps service/secure-webapp-service 8080:80 &
sleep 5
curl http://localhost:8080
curl http://localhost:8080/health

# 🛑 Stop port forwarding
pkill -f "kubectl port-forward"
```

---

## 🧱 Task 5: Implementing Runtime Security with SecComp and AppArmor

![SecComp](https://img.shields.io/badge/SecComp-Syscall_Filtering-C21325?style=flat-square&logo=linux&logoColor=white) ![AppArmor](https://img.shields.io/badge/AppArmor-MAC-2E2E2E?style=flat-square&logo=linux&logoColor=white)

### 🧩 Subtask 5.1: Create SecComp Profile

```bash
# 📁 Create SecComp profile directory
mkdir -p ~/devsecops-lab/security-profiles
```

```json
// 🧩 webapp-seccomp.json — allow-list of required syscalls only
{
  "defaultAction": "SCMP_ACT_ERRNO",
  "architectures": [
    "SCMP_ARCH_X86_64",
    "SCMP_ARCH_X86",
    "SCMP_ARCH_X32"
  ],
  "syscalls": [
    {
      "names": [
        "accept", "accept4", "access", "arch_prctl", "bind", "brk",
        "clone", "close", "connect", "dup", "dup2", "epoll_create",
        "epoll_create1", "epoll_ctl", "epoll_wait", "execve", "exit",
        "exit_group", "fcntl", "fstat", "futex", "getcwd", "getdents",
        "getpid", "getppid", "getrlimit", "getsockname", "getsockopt",
        "ioctl", "listen", "lseek", "mmap", "mprotect", "munmap",
        "open", "openat", "pipe", "poll", "read", "readlink",
        "rt_sigaction", "rt_sigprocmask", "rt_sigreturn", "select",
        "set_robust_list", "set_tid_address", "setrlimit", "setsockopt",
        "socket", "stat", "write"
      ],
      "action": "SCMP_ACT_ALLOW"
    }
  ]
}
```

### 🛡️ Subtask 5.2: Create AppArmor Profile

```bash
# 🛡️ Create AppArmor profile
cat > ~/devsecops-lab/security-profiles/webapp-apparmor << 'EOF'
#include <tunables/global>

profile webapp-container flags=(attach_disconnected,mediate_deleted) {
  #include <abstractions/base>

  # 🌐 Allow network access
  network inet tcp,
  network inet udp,

  # 📁 Allow access to application files
  /app/** r,
  /usr/local/lib/python3.9/** r,
  /usr/lib/python3.9/** r,

  # ▶️ Allow execution of Python
  /usr/local/bin/python ix,
  /usr/bin/python3.9 ix,

  # 📄 Allow reading system files needed by Python
  /etc/ld.so.cache r,
  /etc/passwd r,
  /etc/group r,
  /proc/*/stat r,
  /sys/fs/cgroup/** r,

  # 🚫 Deny dangerous capabilities
  deny capability sys_admin,
  deny capability sys_module,
  deny capability sys_rawio,
  deny capability sys_ptrace,

  # 📁 Allow temporary file access
  /tmp/** rw,

  # 📝 Allow logging
  /dev/stdout w,
  /dev/stderr w,
}
EOF
```

### 🔗 Subtask 5.3: Apply Security Profiles to Kubernetes Deployment

```bash
# 📤 Copy SecComp profile to Minikube
minikube ssh "sudo mkdir -p /var/lib/kubelet/seccomp/profiles"
minikube cp ~/devsecops-lab/security-profiles/webapp-seccomp.json /var/lib/kubelet/seccomp/profiles/webapp-seccomp.json
```

```yaml
# 🧱 secure-deployment-with-profiles.yaml — hardened deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: secure-webapp-hardened
  namespace: secure-apps
  labels:
    app: secure-webapp-hardened
spec:
  replicas: 2
  selector:
    matchLabels:
      app: secure-webapp-hardened
  template:
    metadata:
      labels:
        app: secure-webapp-hardened
      annotations:
        container.apparmor.security.beta.kubernetes.io/webapp: localhost/webapp-container
    spec:
      # 🧩 SecComp profile applied at pod level
      securityContext:
        seccompProfile:
          type: Localhost
          localhostProfile: profiles/webapp-seccomp.json
      containers:
      - name: webapp
        image: $DOCKERHUB_USERNAME/secure-webapp:v1.0-signed
        ports:
        - containerPort: 5000
        resources:
          requests:
            memory: "64Mi"
            cpu: "250m"
          limits:
            memory: "128Mi"
            cpu: "500m"
        securityContext:
          runAsNonRoot: true
          runAsUser: 1000
          allowPrivilegeEscalation: false
          readOnlyRootFilesystem: false
          capabilities:
            drop:
            - ALL
            add:
            - NET_BIND_SERVICE
---
apiVersion: v1
kind: Service
metadata:
  name: secure-webapp-hardened-service
  namespace: secure-apps
spec:
  selector:
    app: secure-webapp-hardened
  ports:
  - protocol: TCP
    port: 80
    targetPort: 5000
  type: ClusterIP
```

### 🚀 Subtask 5.4: Deploy Hardened Application

```bash
# 🚀 Apply the hardened deployment
kubectl apply -f secure-deployment-with-profiles.yaml

# 📊 Check deployment status
kubectl get deployments -n secure-apps
kubectl get pods -n secure-apps

# ⏳ Wait for pods to be ready
kubectl wait --for=condition=ready pod -l app=secure-webapp-hardened -n secure-apps --timeout=300s

# 🧪 Test the hardened application
kubectl port-forward -n secure-apps service/secure-webapp-hardened-service 8081:80 &
sleep 5
curl http://localhost:8081
curl http://localhost:8081/health

# 🛑 Stop port forwarding
pkill -f "kubectl port-forward"
```

> **TODO:** Tighten the AppArmor profile further by removing the `/tmp/** rw` rule once you've confirmed the app doesn't need writable temp storage.

---

## ✅ Task 6: Validation and Testing

![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white) ![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)

### 🩺 Subtask 6.1: Security Validation Script

```bash
# ✍️ Create validation script
cat > validate-security.sh << 'EOF'
#!/bin/bash

echo "=== DevSecOps Security Validation ==="
echo

# 🔍 Check Trivy installation
echo "1. Checking Trivy installation..."
if command -v trivy &> /dev/null; then
    echo "✓ Trivy is installed: $(trivy --version)"
else
    echo "✗ Trivy is not installed"
fi
echo

# 🔐 Check Docker Content Trust
echo "2. Checking Docker Content Trust..."
if [ "$DOCKER_CONTENT_TRUST" = "1" ]; then
    echo "✓ Docker Content Trust is enabled"
else
    echo "✗ Docker Content Trust is not enabled"
fi
echo

# ☸️ Check Kubernetes cluster
echo "3. Checking Kubernetes cluster..."
if kubectl cluster-info &> /dev/null; then
    echo "✓ Kubernetes cluster is accessible"
    kubectl get nodes
else
    echo "✗ Kubernetes cluster is not accessible"
fi
echo

# 📊 Check deployed applications
echo "4. Checking deployed applications..."
kubectl get deployments -n secure-apps
echo

# 🔒 Check pod security contexts
echo "5. Checking pod security contexts..."
kubectl get pods -n secure-apps -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.securityContext}{"\n"}{end}'
echo

echo "=== Validation Complete ==="
EOF

# ✅ Make script executable and run it
chmod +x validate-security.sh
./validate-security.sh
```

### 🧪 Subtask 6.2: Performance and Security Testing

```bash
# ✍️ Create comprehensive testing script
cat > test-security-features.sh << 'EOF'
#!/bin/bash

echo "=== Security Features Testing ==="
echo

# 🔍 Test 1: Verify image scanning
echo "Test 1: Image Vulnerability Scanning"
echo "Scanning image for vulnerabilities..."
trivy image --severity HIGH,CRITICAL secure-webapp:v1.0 --format table
echo

# 🔏 Test 2: Verify image signature
echo "Test 2: Image Signature Verification"
if [ ! -z "$DOCKERHUB_USERNAME" ]; then
    docker trust inspect $DOCKERHUB_USERNAME/secure-webapp:v1.0-signed
else
    echo "DOCKERHUB_USERNAME not set, skipping signature verification"
fi
echo

# 🌐 Test 3: Test application functionality
echo "Test 3: Application Functionality Test"
kubectl port-forward -n secure-apps service/secure-webapp-hardened-service 8082:80 &
PF_PID=$!
sleep 5

if curl -s http://localhost:8082 | grep -q "Secure Container Demo"; then
    echo "✓ Application is responding correctly"
else
    echo "✗ Application is not responding correctly"
fi

kill $PF_PID 2>/dev/null
echo

# 🔒 Test 4: Security context verification
echo "Test 4: Security Context Verification"
POD_NAME=$(kubectl get pods -n secure-apps -l app=secure-webapp-hardened -o jsonpath='{.items[0].metadata.name}')
if [ ! -z "$POD_NAME" ]; then
    echo "Checking security context for pod: $POD_NAME"
    kubectl get pod $POD_NAME -n secure-apps -o jsonpath='{.spec.containers[0].securityContext}' | jq .
else
    echo "No pods found for security context verification"
fi
echo

echo "=== Testing Complete ==="
EOF

# ✅ Make script executable and run it
chmod +x test-security-features.sh
./test-security-features.sh
```

---

## 🧯 Troubleshooting Common Issues

<details>
<summary>🔍 Issue 1: Trivy Scan Failures</summary>

If Trivy scanning fails, try updating the vulnerability database:

```bash
trivy image --clear-cache
trivy image --download-db-only
```
</details>

<details>
<summary>🔐 Issue 2: Docker Content Trust Issues</summary>

If signing fails, ensure you're logged into DockerHub and have the correct permissions:

```bash
docker logout
docker login
export DOCKER_CONTENT_TRUST=1
```
</details>

<details>
<summary>☸️ Issue 3: Kubernetes Pod Startup Issues</summary>

If pods fail to start, check the events and logs:

```bash
kubectl describe pod <pod-name> -n secure-apps
kubectl logs <pod-name> -n secure-apps
```
</details>

<details>
<summary>🧱 Issue 4: SecComp Profile Issues</summary>

If SecComp profiles cause issues, verify the profile is correctly placed:

```bash
minikube ssh "ls -la /var/lib/kubelet/seccomp/profiles/"
```
</details>

---

## 🧹 Cleanup

```bash
# 🗑️ Delete Kubernetes resources
kubectl delete namespace secure-apps

# 🛑 Stop Minikube
minikube stop
minikube delete

# 🗑️ Remove Docker images
docker rmi secure-webapp:v1.0
docker rmi $DOCKERHUB_USERNAME/secure-webapp:v1.0-signed

# 📁 Clean up working directory
cd ~
rm -rf ~/devsecops-lab
```

---

## 🗺️ MITRE ATT&CK Mapping

This lab's controls map to mitigated ATT&CK techniques — security controls positioned to prevent or contain these techniques, rather than detect them after the fact:

| Technique | ID | Mitigating Control |
|---|---|---|
| Supply Chain Compromise | T1195 | Trivy vulnerability scanning gates images before they're pushed or deployed |
| Compromise Software Supply Chain | T1195.002 | Automated scan-and-fail pipeline blocks images with critical CVEs |
| Compromise Client Software Binary | T1554 | Docker Content Trust ensures only signed, untampered images are pulled |
| Subvert Trust Controls | T1553 | Notary-based signature verification rejects unsigned images |
| Deploy Container | T1610 | Kubernetes security contexts enforce non-root, no-privilege-escalation deployments |
| Escape to Host | T1611 | SecComp syscall filtering + AppArmor MAC profiles restrict container breakout paths |

---

## 🏁 Conclusion

Congratulations! You have successfully completed the **Advanced Container Security** lab. 🎉

### ✅ Key Accomplishments

- 🏗️ Built a complete DevSecOps pipeline that integrates security at every stage of the container lifecycle
- 🔍 Implemented vulnerability scanning using Trivy to identify and address security issues before deployment
- 🔏 Digitally signed container images using Docker Content Trust and Notary, ensuring image integrity and authenticity
- ☸️ Deployed signed images to a Kubernetes cluster with proper verification mechanisms
- 🧱 Applied runtime security controls using SecComp and AppArmor to restrict container capabilities and system access

### 🌍 Why This Matters

Container security is critical in modern application deployment. The techniques you've learned provide multiple layers of defense:

- **Vulnerability scanning** prevents deploying containers with known security flaws
- **Image signing** ensures you're running trusted, unmodified containers
- **Runtime security profiles** limit the attack surface by restricting system calls and file access
- **Security contexts** enforce the principle of least privilege

### 🚀 Real-World Applications

These practices are essential for maintaining secure, compliant, and resilient containerized applications in production environments. The DevSecOps approach implemented here ensures that security is not an afterthought but an integral part of your development and deployment process — you now have the practical skills to implement enterprise-grade container security measures on real-world infrastructure.

---

<div align="center">

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Training-blueviolet?style=for-the-badge)

</div>
