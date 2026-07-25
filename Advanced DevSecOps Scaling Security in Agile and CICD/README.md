<div align="center">

# 🛡️ Advanced DevSecOps — Scaling Security in Agile and CI/CD

### Secure User Stories • Wiki.js • Jenkins • Prometheus • Grafana

![DevSecOps](https://img.shields.io/badge/DevSecOps-FF4B4B?style=for-the-badge&logo=OWASP&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)
![Wiki.js](https://img.shields.io/badge/Wiki.js-1976D2?style=for-the-badge&logo=wikidotjs&logoColor=white)
![NodeJS](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
![Agile](https://img.shields.io/badge/Agile-0052CC?style=for-the-badge&logo=trello&logoColor=white)

</div>

---

## 📚 Table of Contents

- [🎯 Learning Objectives](#-learning-objectives)
- [📋 Prerequisites](#-prerequisites)
- [🖥️ Lab Environment](#️-lab-environment)
- [🗂️ Lab Tasks Overview](#️-lab-tasks-overview)
- [🔐 Lab 1: Writing Secure User Stories for Login Feature](#-lab-1-writing-secure-user-stories-for-login-feature)
  - [📖 Task 1.1: Understanding Secure User Stories](#-task-11-understanding-secure-user-stories)
  - [✍️ Task 1.2: Create Secure User Stories for Login Feature](#️-task-12-create-secure-user-stories-for-login-feature)
- [📊 Lab 2: Setting up DevSecOps Monitoring Stack](#-lab-2-setting-up-devsecops-monitoring-stack)
  - [📘 Task 2.1: Install and Configure Wiki.js](#-task-21-install-and-configure-wikijs)
  - [⚙️ Task 2.2: Install and Configure Jenkins](#️-task-22-install-and-configure-jenkins)
  - [🔁 Task 2.3: Create a Jenkins Pipeline](#-task-23-create-a-jenkins-pipeline)
  - [📈 Task 2.4: Install and Configure Prometheus](#-task-24-install-and-configure-prometheus)
  - [🔗 Task 2.5: Configure Jenkins–Prometheus Integration](#-task-25-configure-jenkinsprometheus-integration)
  - [📉 Task 2.6: Configure Grafana Dashboards](#-task-26-configure-grafana-dashboards)
  - [🧪 Task 2.7: Test the Complete Pipeline](#-task-27-test-the-complete-pipeline)
  - [🚨 Task 2.8: Create Alerting Rules (Optional Advanced Task)](#-task-28-create-alerting-rules-optional-advanced-task)
- [✅ Verification Checklist](#-verification-checklist)
- [🗺️ MITRE ATT&CK Mapping](#️-mitre-attck-mapping)
- [🧩 Key Concepts Summary](#-key-concepts-summary)
- [🛠️ Troubleshooting](#️-troubleshooting)
- [🏁 Conclusion](#-conclusion)

---

## 🎯 Learning Objectives

| # | Objective |
|---|-----------|
| 1 | Understand the fundamentals of DevSecOps and its integration with Agile methodologies |
| 2 | Write secure user stories following security best practices |
| 3 | Install and configure Wiki.js for documentation management |
| 4 | Create and configure Jenkins CI/CD pipelines |
| 5 | Integrate Jenkins with Prometheus for monitoring |
| 6 | Visualize pipeline metrics and logs using Grafana |
| 7 | Implement a complete DevSecOps monitoring stack using open-source tools |

## 📋 Prerequisites

| Skill Area | Requirement |
|---|---|
| 🐧 Linux | Basic command line operations |
| 🌿 Git | Familiarity with version control concepts |
| 🌐 Web/APIs | Basic knowledge of web applications and APIs |
| 🐳 Containers | Understanding of Docker basics |
| 📄 YAML | Basic knowledge of YAML syntax |
| 🔁 CI/CD | Familiarity with CI/CD concepts |

## 🖥️ Lab Environment

> ☁️ **Ready-to-Use Cloud Machines** — Al Nafi provides a pre-configured Linux-based cloud machine for this lab. Just click **Start Lab** — no need to build or configure your own VM.

| Spec | Value |
|---|---|
| 🖥️ OS | Ubuntu 20.04 LTS with Docker pre-installed |
| 💾 RAM | 4GB |
| 💽 Storage | 20GB |
| 🔌 Ports | All necessary ports pre-configured |
| 🌐 Network | Internet access for downloading required packages |

## 🗂️ Lab Tasks Overview

- 🔐 **Lab-1:** Writing Secure User Stories for Login Feature
- 📊 **Lab-2:** Setting up Wiki.js, Jenkins Pipeline, Prometheus, and Grafana integration

---

## 🔐 Lab 1: Writing Secure User Stories for Login Feature

### 📖 Task 1.1: Understanding Secure User Stories

> 💡 A **secure user story** incorporates security requirements directly into the development process, ensuring security is considered from the beginning rather than as an afterthought.

### ✍️ Task 1.2: Create Secure User Stories for Login Feature

#### 1️⃣ Subtask 1.2.1: Basic Login User Story

📂 Create the working directory and file:

```bash
# 📁 Create the project folder for the DevSecOps lab
mkdir -p ~/devsecops-lab/user-stories
cd ~/devsecops-lab/user-stories

# 📝 Open the login user stories file for editing
nano login-user-stories.md
```

✏️ Add the following four secure user stories:

<details>
<summary>📜 <strong>Story 1 — Basic User Authentication</strong></summary>

```markdown
**As a** registered user
**I want to** log into the application securely
**So that** I can access my personal dashboard and data

### Acceptance Criteria:
- User must provide valid username/email and password
- System must validate credentials against secure database
- Failed login attempts must be logged for security monitoring
- User session must be established securely upon successful authentication

### Security Requirements:
- Passwords must be hashed using bcrypt or similar strong hashing algorithm
- Implement rate limiting to prevent brute force attacks (max 5 attempts per 15 minutes)
- Use HTTPS for all authentication requests
- Implement CSRF protection
- Session tokens must be cryptographically secure and expire after 30 minutes of inactivity
```
</details>

<details>
<summary>🔒 <strong>Story 2 — Account Lockout Protection</strong></summary>

```markdown
**As a** system administrator
**I want to** automatically lock user accounts after multiple failed login attempts
**So that** I can protect against brute force attacks

### Acceptance Criteria:
- Account locks after 5 consecutive failed login attempts
- Locked accounts require administrator intervention or time-based unlock (30 minutes)
- User receives clear notification about account lockout
- Legitimate users can request account unlock via secure process

### Security Requirements:
- Lockout mechanism must be resistant to bypass attempts
- Lockout status must be stored securely and persistently
- Account unlock process must include additional verification
- All lockout events must be logged and monitored
```
</details>

<details>
<summary>📲 <strong>Story 3 — Multi-Factor Authentication (MFA)</strong></summary>

```markdown
**As a** security-conscious user
**I want to** enable two-factor authentication on my account
**So that** my account remains secure even if my password is compromised

### Acceptance Criteria:
- Users can enable/disable MFA in their account settings
- Support for TOTP (Time-based One-Time Password) authentication
- Backup codes are provided for account recovery
- MFA is required for sensitive operations

### Security Requirements:
- TOTP secrets must be generated securely and stored encrypted
- Backup codes must be cryptographically random and single-use
- MFA setup process must be secure and user-friendly
- Failed MFA attempts must be logged and monitored
```
</details>

<details>
<summary>♻️ <strong>Story 4 — Secure Password Reset</strong></summary>

```markdown
**As a** user who forgot their password
**I want to** reset my password securely
**So that** I can regain access to my account without compromising security

### Acceptance Criteria:
- Password reset can be initiated with email address
- Reset link is sent to registered email address
- Reset link expires after 1 hour
- New password must meet complexity requirements

### Security Requirements:
- Reset tokens must be cryptographically secure and single-use
- Reset process must not reveal whether email address is registered
- Old password must be invalidated immediately upon reset
- All password reset activities must be logged
```
</details>

💾 Save the file: `Ctrl+X`, then `Y`, then `Enter`.

#### 2️⃣ Subtask 1.2.2: Create Security Requirements Checklist

```bash
# 📝 Open the security checklist file
nano security-checklist.md
```

✅ Add the checklist covering:

| Phase | Checklist Focus |
|---|---|
| 🧪 Pre-Development | Input validation, authentication security, communication security, monitoring & logging |
| 💻 Development | Code security (no hardcoded creds, dependency scanning), security testing (unit/integration/pentest) |
| 🚀 Deployment | Infrastructure security (encrypted DB connections, least privilege), operational security (incident response, backups) |

```markdown
# TODO: Extend this checklist with any org-specific compliance requirements (e.g. PCI-DSS, SOC 2)
```

💾 Save the file and continue to Lab-2.

---

## 📊 Lab 2: Setting up DevSecOps Monitoring Stack

### 📘 Task 2.1: Install and Configure Wiki.js

#### 🐳 Subtask 2.1.1: Install Docker and Docker Compose

```bash
# ✅ Check if Docker is running
sudo systemctl status docker

# ▶️ If not running, start and enable Docker
sudo systemctl start docker
sudo systemctl enable docker

# ⬇️ Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# 🔍 Verify installation
docker-compose --version
```

#### 📝 Subtask 2.1.2: Create Wiki.js Configuration

```bash
# 📁 Create the Wiki.js project directory
mkdir -p ~/devsecops-lab/wikijs
cd ~/devsecops-lab/wikijs
nano docker-compose.yml
```

```yaml
# 🐘 Wiki.js + PostgreSQL stack
version: '3.8'

services:
  wikijs-db:
    image: postgres:13
    environment:
      POSTGRES_DB: wiki
      POSTGRES_PASSWORD: wikijsrocks
      POSTGRES_USER: wikijs
    logging:
      driver: "none"
    restart: unless-stopped
    volumes:
      - wikijs-db-data:/var/lib/postgresql/data
    networks:
      - wikijs-network

  wikijs:
    image: ghcr.io/requarks/wiki:2
    depends_on:
      - wikijs-db
    environment:
      DB_TYPE: postgres
      DB_HOST: wikijs-db
      DB_PORT: 5432
      DB_USER: wikijs
      DB_PASS: wikijsrocks
      DB_NAME: wiki
    restart: unless-stopped
    ports:
      - "3000:3000"
    networks:
      - wikijs-network
    volumes:
      - wikijs-data:/wiki/data

volumes:
  wikijs-db-data:
  wikijs-data:

networks:
  wikijs-network:
    driver: bridge
# TODO: Move DB_PASS to a Docker secret or .env file before using this outside a lab
```

#### 🚀 Subtask 2.1.3: Deploy Wiki.js

```bash
# ▶️ Start Wiki.js services
docker-compose up -d

# 🔍 Check if services are running
docker-compose ps

# 📜 View logs
docker-compose logs wikijs
```

#### ⚙️ Subtask 2.1.4: Configure Wiki.js

🌐 Access Wiki.js at `http://localhost:3000` and complete setup:

1. 👤 Create an administrator account
2. 🎛️ Configure the site settings
3. 🔑 Choose authentication method (**Local** for this lab)

#### 📄 Subtask 2.1.5: Create Documentation in Wiki.js

| Page | Purpose |
|---|---|
| 🛡️ DevSecOps Best Practices | Document security integration in CI/CD |
| 📋 Security Policies | Password policies, access controls |
| 🚨 Incident Response Procedures | Step-by-step response documentation |

---

### ⚙️ Task 2.2: Install and Configure Jenkins

#### 📝 Subtask 2.2.1: Create Jenkins Configuration

```bash
# 📁 Create the Jenkins project directory
mkdir -p ~/devsecops-lab/jenkins
cd ~/devsecops-lab/jenkins
nano docker-compose.yml
```

```yaml
# 🤖 Jenkins CI/CD server
version: '3.8'

services:
  jenkins:
    image: jenkins/jenkins:lts
    container_name: jenkins
    restart: unless-stopped
    ports:
      - "8080:8080"
      - "50000:50000"
    volumes:
      - jenkins_home:/var/jenkins_home
      - /var/run/docker.sock:/var/run/docker.sock
    environment:
      - JAVA_OPTS=-Djenkins.install.runSetupWizard=false
    networks:
      - jenkins-network

volumes:
  jenkins_home:

networks:
  jenkins-network:
    driver: bridge
```

#### 🚀 Subtask 2.2.2: Deploy Jenkins

```bash
# ▶️ Start Jenkins
docker-compose up -d

# 🔍 Check if Jenkins is running
docker-compose ps

# 🔑 Get the initial admin password
docker-compose exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

#### 🛠️ Subtask 2.2.3: Configure Jenkins

1. 🌐 Access Jenkins at `http://localhost:8080`
2. 🔑 Use the initial admin password
3. 📦 Install suggested plugins
4. 👤 Create an admin user
5. 🔗 Configure Jenkins URL

#### 🧩 Subtask 2.2.4: Install Required Jenkins Plugins

| Plugin | Purpose |
|---|---|
| 📈 Prometheus metrics plugin | Exposes build metrics for scraping |
| 🔁 Pipeline plugin | Declarative/scripted pipeline support |
| 🌿 Git plugin | Source control integration |
| 🐳 Docker plugin | Docker build/run integration |
| 🌊 Blue Ocean *(optional)* | Improved pipeline visualization UI |

---

### 🔁 Task 2.3: Create a Jenkins Pipeline

#### 📦 Subtask 2.3.1: Create a Sample Application Repository

```bash
# 📁 Create and initialize the sample app
mkdir -p ~/devsecops-lab/sample-app
cd ~/devsecops-lab/sample-app
git init
nano package.json
```

```json
{
  "name": "devsecops-sample-app",
  "version": "1.0.0",
  "description": "Sample application for DevSecOps lab",
  "main": "app.js",
  "scripts": {
    "start": "node app.js",
    "test": "echo \"Running tests...\" && exit 0"
  },
  "dependencies": {
    "express": "^4.18.2"
  }
}
```

```javascript
// 🚀 app.js — minimal Express service with a health endpoint
const express = require('express');
const app = express();
const port = 3001;

app.get('/', (req, res) => {
  res.json({
    message: 'DevSecOps Sample Application',
    version: '1.0.0',
    timestamp: new Date().toISOString()
  });
});

// 💓 Health check endpoint used by monitoring/orchestration
app.get('/health', (req, res) => {
  res.json({
    status: 'healthy',
    uptime: process.uptime()
  });
});

app.listen(port, () => {
  console.log(`Sample app listening at http://localhost:${port}`);
});
```

```dockerfile
# 🐳 Dockerfile
FROM node:16-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 3001

CMD ["npm", "start"]
```

#### 📜 Subtask 2.3.2: Create Jenkinsfile

```groovy
// 🔁 Jenkinsfile — DevSecOps pipeline with security gates baked in
pipeline {
    agent any

    environment {
        APP_NAME = 'devsecops-sample-app'
        BUILD_NUMBER = "${env.BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') { // 📥 Pull source
            steps {
                echo 'Checking out source code...'
                sh 'echo "Source code checked out successfully"'
            }
        }

        stage('Security Scan - Dependencies') { // 🔎 SCA
            steps {
                echo 'Scanning dependencies for vulnerabilities...'
                sh '''
                    echo "Running dependency security scan..."
                    # npm audit / snyk test would run here
                    echo "No critical vulnerabilities found"
                '''
            }
        }

        stage('Build') { // 🏗️ Build
            steps {
                echo 'Building application...'
                sh 'echo "Build completed successfully"'
            }
        }

        stage('Test') { // 🧪 Test
            steps {
                echo 'Running tests...'
                sh '''
                    echo "Running unit tests..."
                    echo "Running security tests..."
                    echo "All tests passed"
                '''
            }
        }

        stage('Security Scan - Code') { // 🛡️ SAST
            steps {
                echo 'Running static code analysis...'
                sh 'echo "Code security scan completed"'
            }
        }

        stage('Build Docker Image') { // 🐳 Image build
            steps {
                echo 'Building Docker image...'
                sh 'echo "Docker image built successfully"'
            }
        }

        stage('Security Scan - Container') { // 🔬 Container scan
            steps {
                echo 'Scanning Docker image for vulnerabilities...'
                sh 'echo "Container security scan completed"'
            }
        }

        stage('Deploy to Staging') { // 🚀 Deploy
            steps {
                echo 'Deploying to staging environment...'
                sh 'echo "Application deployed successfully"'
            }
        }

        stage('DAST - Dynamic Security Testing') { // 🕷️ DAST
            steps {
                echo 'Running dynamic security tests...'
                sh 'echo "Dynamic security testing completed"'
            }
        }
    }

    post {
        always { echo 'Pipeline execution completed' }
        success { echo 'Pipeline executed successfully!' }
        failure { echo 'Pipeline failed. Check logs for details.' }
    }
}
// TODO: Wire real tool calls (npm audit, SonarQube, Trivy, OWASP ZAP) into each stage
```

```bash
# 💾 Commit the sample app and pipeline
git add .
git commit -m "Initial commit with sample application and Jenkinsfile"
```

#### 🏗️ Subtask 2.3.3: Create Jenkins Pipeline Job

1. ➕ In Jenkins, click **New Item**
2. 🏷️ Name it `DevSecOps-Sample-Pipeline`
3. 🔁 Select **Pipeline** → OK
4. 📋 Under **Pipeline**, choose **Pipeline script** and paste the Jenkinsfile
5. 💾 Save
6. ▶️ Click **Build Now**

---

### 📈 Task 2.4: Install and Configure Prometheus

#### 📝 Subtask 2.4.1: Create Prometheus Configuration

```bash
mkdir -p ~/devsecops-lab/monitoring
cd ~/devsecops-lab/monitoring
nano prometheus.yml
```

```yaml
# 📡 prometheus.yml — scrape configuration
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'jenkins'
    metrics_path: '/prometheus'
    static_configs:
      - targets: ['jenkins:8080']

  - job_name: 'node-exporter'
    static_configs:
      - targets: ['node-exporter:9100']
```

#### 🧱 Subtask 2.4.2: Create Docker Compose for Monitoring Stack

```bash
nano docker-compose.yml
```

```yaml
# 📊 Prometheus + Grafana + node-exporter monitoring stack
version: '3.8'

services:
  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus
    restart: unless-stopped
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--web.console.libraries=/etc/prometheus/console_libraries'
      - '--web.console.templates=/etc/prometheus/consoles'
      - '--storage.tsdb.retention.time=200h'
      - '--web.enable-lifecycle'
    networks:
      - monitoring

  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    restart: unless-stopped
    ports:
      - "3001:3000"
    environment:
      - GF_SECURITY_ADMIN_USER=admin
      - GF_SECURITY_ADMIN_PASSWORD=admin123
    volumes:
      - grafana_data:/var/lib/grafana
    networks:
      - monitoring

  node-exporter:
    image: prom/node-exporter:latest
    container_name: node-exporter
    restart: unless-stopped
    ports:
      - "9100:9100"
    volumes:
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
      - /:/rootfs:ro
    command:
      - '--path.procfs=/host/proc'
      - '--path.rootfs=/rootfs'
      - '--path.sysfs=/host/sys'
      - '--collector.filesystem.mount-points-exclude=^/(sys|proc|dev|host|etc)($$|/)'
    networks:
      - monitoring

volumes:
  prometheus_data:
  grafana_data:

networks:
  monitoring:
    driver: bridge
# TODO: Replace GF_SECURITY_ADMIN_PASSWORD with a secret before any non-lab use
```

#### 🚀 Subtask 2.4.3: Deploy Monitoring Stack

```bash
# ▶️ Start monitoring stack
docker-compose up -d

# 🔍 Check status
docker-compose ps

# 📜 View logs
docker-compose logs prometheus
docker-compose logs grafana
```

---

### 🔗 Task 2.5: Configure Jenkins–Prometheus Integration

#### 🧩 Subtask 2.5.1: Configure Jenkins Prometheus Plugin

1. ⚙️ In Jenkins: **Manage Jenkins → Configure System**
2. 📈 Find the **Prometheus** section
3. ✅ Check **Collect metrics for builds**
4. 🛣️ Set path to `/prometheus` (default)
5. 💾 Save

#### 🔄 Subtask 2.5.2: Update Prometheus Configuration

```bash
# ⏹️ Stop the monitoring stack
docker-compose down
nano prometheus.yml
```

```yaml
# 🌉 Jenkins target updated to reach the host from the Docker network
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'jenkins'
    metrics_path: '/prometheus'
    static_configs:
      - targets: ['host.docker.internal:8080']
    scrape_interval: 30s

  - job_name: 'node-exporter'
    static_configs:
      - targets: ['node-exporter:9100']
```

```bash
# ▶️ Restart the monitoring stack
docker-compose up -d
```

---

### 📉 Task 2.6: Configure Grafana Dashboards

#### 🔓 Subtask 2.6.1: Access Grafana

🌐 Navigate to `http://localhost:3001` and log in with `admin` / `admin123`.

#### 🔌 Subtask 2.6.2: Add Prometheus Data Source

1. ⚙️ Click the gear icon → **Data Sources**
2. ➕ **Add data source** → **Prometheus**
3. 🔗 URL: `http://prometheus:9090`
4. 💾 **Save & Test**

#### 📊 Subtask 2.6.3: Create Jenkins Dashboard

| Panel | PromQL Query |
|---|---|
| ⏱️ Jenkins Build Duration | `jenkins_builds_duration_milliseconds_summary` |
| ✅ Build Success Rate | `rate(jenkins_builds_success_build_count[5m])` |
| 🏃 Active Builds | `jenkins_builds_running_build_count` |
| 📋 Queue Length | `jenkins_queue_size_value` |

#### 🖥️ Subtask 2.6.4: Create System Monitoring Dashboard

| Panel | PromQL Query |
|---|---|
| 🔥 CPU Usage | `100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)` |
| 🧠 Memory Usage | `(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100` |
| 💽 Disk Usage | `100 - ((node_filesystem_avail_bytes * 100) / node_filesystem_size_bytes)` |

---

### 🧪 Task 2.7: Test the Complete Pipeline

#### ▶️ Subtask 2.7.1: Run Jenkins Pipeline

1. 🖥️ Go to the Jenkins dashboard
2. 🖱️ Click **DevSecOps-Sample-Pipeline**
3. ▶️ Click **Build Now**
4. 👀 Monitor the build progress

#### 📡 Subtask 2.7.2: Verify Metrics Collection

```text
🌐 Access Prometheus → http://localhost:9090
📍 Status → Targets → confirm Jenkins target is UP
🔍 Query: jenkins_builds_duration_milliseconds_summary
```

#### 📈 Subtask 2.7.3: View Metrics in Grafana

```text
🌐 Access Grafana → http://localhost:3001
📊 Open the Jenkins dashboard
✅ Confirm build metrics render
🔁 Run additional builds and watch metrics update live
```

---

### 🚨 Task 2.8: Create Alerting Rules (Optional Advanced Task)

#### 🔔 Subtask 2.8.1: Create Alerting Rules

```bash
cd ~/devsecops-lab/monitoring
nano alert_rules.yml
```

```yaml
# 🚨 alert_rules.yml
groups:
  - name: jenkins_alerts
    rules:
      - alert: JenkinsBuildFailure
        expr: increase(jenkins_builds_failed_build_count[5m]) > 0
        for: 1m
        labels:
          severity: warning
        annotations:
          summary: "Jenkins build failed"
          description: "A Jenkins build has failed in the last 5 minutes"

      - alert: JenkinsDown
        expr: up{job="jenkins"} == 0
        for: 2m
        labels:
          severity: critical
        annotations:
          summary: "Jenkins is down"
          description: "Jenkins has been down for more than 2 minutes"

  - name: system_alerts
    rules:
      - alert: HighCPUUsage
        expr: 100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100) > 80
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High CPU usage detected"
          description: "CPU usage is above 80% for more than 5 minutes"
# TODO: Add a MemoryHighUsage and DiskSpaceLow alert following the same pattern
```

```bash
# 📎 Wire the rule file into prometheus.yml
nano prometheus.yml
```

```yaml
rule_files:
  - "alert_rules.yml"
```

```bash
# 📂 Mount the rules file in docker-compose.yml, then restart Prometheus
docker-compose restart prometheus
```

---

## ✅ Verification Checklist

- [ ] 📘 Wiki.js is accessible and contains documentation
- [ ] ⚙️ Jenkins is running and the pipeline executes successfully
- [ ] 📈 Prometheus is collecting metrics from Jenkins and the system
- [ ] 📉 Grafana displays dashboards with Jenkins and system metrics
- [ ] 🔗 All services are properly networked and communicating
- [ ] 🔐 Secure user stories are documented with proper security requirements

---

## 🗺️ MITRE ATT&CK Mapping

> The security requirements baked into the Lab-1 user stories map to attacker techniques they are designed to mitigate:

| Technique ID | Technique | Mitigated By |
|---|---|---|
| T1110 | Brute Force | Rate limiting (5 attempts/15 min) + account lockout policy |
| T1078 | Valid Accounts | Automated account lockout after repeated failed logins |
| T1556 | Modify Authentication Process | MFA enforced for sensitive operations |
| T1621 | Multi-Factor Authentication Request Generation | TOTP-based MFA design with single-use backup codes |
| T1539 | Steal Web Session Cookie | Cryptographically secure session tokens, 30-min inactivity expiry |
| T1552.001 | Credentials In Files | bcrypt password hashing, plaintext passwords never stored or transmitted |

## 🧩 Key Concepts Summary

| Concept | Role in This Stack |
|---|---|
| 📘 Wiki.js | Centralized documentation for policies, procedures, and best practices |
| ⚙️ Jenkins | Automates the build → security scan → deploy pipeline |
| 📈 Prometheus | Scrapes and stores time-series metrics from Jenkins and the host |
| 📉 Grafana | Visualizes Prometheus data as build and system dashboards |
| 🧵 Jenkinsfile stages | Embed SAST, dependency, container, and DAST scans directly into CI/CD |
| 🖥️ node-exporter | Exposes host-level CPU, memory, and disk metrics to Prometheus |

---

## 🛠️ Troubleshooting

<details>
<summary>🔴 Issue 1: Jenkins Not Accessible</summary>

**Problem:** Cannot access Jenkins on port 8080

```bash
# 🔍 Check if Jenkins container is running
docker ps | grep jenkins

# 📜 Check Jenkins logs
docker logs jenkins

# 🔄 Restart Jenkins if needed
cd ~/devsecops-lab/jenkins
docker-compose restart jenkins
```
</details>

<details>
<summary>🟠 Issue 2: Prometheus Cannot Scrape Jenkins</summary>

**Problem:** Jenkins target shows as "DOWN" in Prometheus

```bash
# ✅ Verify the Jenkins Prometheus plugin is installed
# 🌉 Check reachability from inside the Prometheus container
docker exec -it prometheus wget -qO- http://host.docker.internal:8080/prometheus
```
</details>

<details>
<summary>🟡 Issue 3: Grafana Cannot Connect to Prometheus</summary>

**Problem:** Grafana shows "Bad Gateway" when testing the Prometheus data source

```bash
# 🔗 Verify both containers are on the same network
docker network ls
docker network inspect monitoring_monitoring

# ✅ Use the correct Prometheus URL: http://prometheus:9090
```
</details>

<details>
<summary>🔵 Issue 4: Wiki.js Database Connection Issues</summary>

**Problem:** Wiki.js cannot connect to PostgreSQL

```bash
# 🔍 Check if both containers are running
cd ~/devsecops-lab/wikijs
docker-compose ps

# 📜 Check database logs
docker-compose logs wikijs-db

# 🔄 Restart the entire stack
docker-compose down && docker-compose up -d
```
</details>

---

## 🏁 Conclusion

### 🎉 Key Accomplishments

- 🔐 Created secure user stories that integrate security requirements from the beginning of the development process
- 📘 Set up a complete documentation system using Wiki.js for DevSecOps policies and procedures
- ⚙️ Implemented a Jenkins CI/CD pipeline with security scanning stages integrated throughout the build process
- 📈 Configured Prometheus to collect metrics from Jenkins and system components
- 📉 Created Grafana dashboards to visualize pipeline performance and system health
- 🧩 Established a complete DevSecOps monitoring and observability stack using open-source tools

### 💡 Why This Matters

This lab demonstrates the practical implementation of DevSecOps principles, where security is integrated throughout the entire software development lifecycle rather than treated as an afterthought. The monitoring and observability stack built here provides real-time visibility into both security and operational metrics, enabling teams to quickly identify and respond to issues. The secure user stories establish a foundation for security-first development, ensuring requirements are considered from the initial planning stages.

### 🌍 Real-World Applications

The skills and tools covered in this lab are directly applicable to enterprise DevSecOps implementations. Organizations use similar stacks — documentation (Wiki.js), automation (Jenkins), and monitoring (Prometheus/Grafana) — to maintain security compliance, monitor application performance, and ensure rapid, secure software delivery. This foundation prepares learners for more advanced DevSecOps topics, including automated security testing, compliance as code, and advanced threat detection and response.

```markdown
# TODO: Extend this pipeline with a real SAST tool (SonarQube), SCA (OWASP Dependency-Check),
# and DAST (OWASP ZAP) to replace the placeholder echo statements in the Jenkinsfile
```

---

<div align="center">

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Training-1976D2?style=for-the-badge)

</div>
