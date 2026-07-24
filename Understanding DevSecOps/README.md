<div align="center">

# 🛡️ Understanding DevSecOps 
### Building a Secure CI/CD Pipeline with Jenkins, SonarQube & OWASP ZAP

![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)
![SonarQube](https://img.shields.io/badge/SonarQube-4E9BCD?style=for-the-badge&logo=sonarqube&logoColor=white)
![OWASP ZAP](https://img.shields.io/badge/OWASP_ZAP-000000?style=for-the-badge&logo=owasp&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Docker Compose](https://img.shields.io/badge/Docker_Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu_20.04-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=node.js&logoColor=white)

![Level](https://img.shields.io/badge/Level-Beginner-brightgreen?style=for-the-badge)
![Duration](https://img.shields.io/badge/Duration-2--3_Hours-blue?style=for-the-badge)
![Track](https://img.shields.io/badge/Track-DevSecOps-orange?style=for-the-badge)

</div>

---

## 📑 Table of Contents

- [🎯 Objectives](#-objectives)
- [📋 Prerequisites](#-prerequisites)
- [🖥️ Lab Environment Setup](#️-lab-environment-setup)
- [🔧 Task 1: Setting Up Jenkins as CI/CD Tool](#-task-1-setting-up-jenkins-as-cicd-tool)
- [🔍 Task 2: Setting Up SonarQube as SAST Tool](#-task-2-setting-up-sonarqube-as-sast-tool)
- [🕷️ Task 3: Setting Up OWASP ZAP as DAST Tool](#️-task-3-setting-up-owasp-zap-as-dast-tool)
- [🔄 Task 4: Creating an Integrated DevSecOps Pipeline](#-task-4-creating-an-integrated-devsecops-pipeline)
- [📊 Task 5: Understanding the Results](#-task-5-understanding-the-results)
- [🗺️ MITRE ATT&CK Mapping](#️-mitre-attck-mapping)
- [🛠️ Troubleshooting Common Issues](#️-troubleshooting-common-issues)
- [✅ Verification Steps](#-verification-steps)
- [🎓 Conclusion](#-conclusion)

---

## 🎯 Objectives

By the end of this lab, students will be able to:

| # | Learning Objective |
|---|---|
| 1 | 🧩 Understand the fundamental concepts of DevSecOps and its importance in modern software development |
| 2 | 🔧 Install and configure Jenkins as a CI/CD automation server |
| 3 | 🔍 Set up SonarQube for Static Application Security Testing (SAST) |
| 4 | 🕷️ Deploy and configure OWASP ZAP for Dynamic Application Security Testing (DAST) |
| 5 | 🔄 Create a basic CI/CD pipeline that integrates security testing tools |
| 6 | 🛡️ Demonstrate how security can be embedded into the development lifecycle |
| 7 | 🚨 Identify security vulnerabilities using automated scanning tools |

## 📋 Prerequisites

| # | Requirement |
|---|---|
| 1 | 🐧 Basic understanding of Linux command line operations |
| 2 | 💻 Familiarity with software development concepts |
| 3 | 🌐 Basic knowledge of web applications and HTTP protocols |
| 4 | 🔄 Understanding of what CI/CD means in software development |
| 5 | ✅ No prior experience with Jenkins, SonarQube, or ZAP is required |

## 🖥️ Lab Environment Setup

> ☁️ **Ready-to-Use Cloud Machines** — Al Nafi provides pre-configured Linux-based cloud machines for this lab. Simply click **Start Lab** to access your dedicated environment. No need to build your own virtual machine or install any software locally.

**Your cloud machine includes:**

![Ubuntu](https://img.shields.io/badge/Ubuntu_20.04_LTS-E95420?style=flat-square&logo=ubuntu&logoColor=white)
![RAM](https://img.shields.io/badge/RAM-4GB-informational?style=flat-square)
![Storage](https://img.shields.io/badge/Storage-20GB-informational?style=flat-square)
![Docker](https://img.shields.io/badge/Docker-Preinstalled-2496ED?style=flat-square&logo=docker&logoColor=white)

- 🐧 Ubuntu 20.04 LTS with 4GB RAM and 20GB storage
- 🐳 Docker and Docker Compose pre-installed
- 🔌 All necessary network ports configured
- 🌐 Internet access for downloading required tools

---

## 🔧 Task 1: Setting Up Jenkins as CI/CD Tool

![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=flat-square&logo=jenkins&logoColor=white)
![Docker Compose](https://img.shields.io/badge/Docker_Compose-2496ED?style=flat-square&logo=docker&logoColor=white)

### 🔹 Subtask 1.1: Install Jenkins

We'll install Jenkins using Docker to ensure a clean and consistent setup.

① Connect to your cloud machine and open a terminal

② Create a directory for our DevSecOps lab:

```bash
# 📁 Create and enter the lab working directory
mkdir ~/devsecops-lab
cd ~/devsecops-lab
```

③ Create a Docker Compose file for Jenkins:

```bash
# 📝 Open a new file for the Jenkins service definition
nano docker-compose-jenkins.yml
```

④ Add the following content to the file:

```yaml
# 🐳 Jenkins CI/CD server service definition
version: '3.8'
services:
  jenkins:
    image: jenkins/jenkins:lts       # 🏗️ Official LTS image
    container_name: jenkins-server
    restart: unless-stopped
    ports:
      - "8080:8080"                 # 🌐 Web UI
      - "50000:50000"               # 🔌 Agent connections
    volumes:
      - jenkins_home:/var/jenkins_home
      - /var/run/docker.sock:/var/run/docker.sock   # 🔧 Allows Jenkins to run Docker commands
    environment:
      - JAVA_OPTS=-Djenkins.install.runSetupWizard=false
    user: root

volumes:
  jenkins_home:
# TODO: Add memory limits (mem_limit/cpus) if running on a resource-constrained machine
```

⑤ Start Jenkins container:

```bash
# 🚀 Launch Jenkins in detached mode
docker-compose -f docker-compose-jenkins.yml up -d
```

⑥ Verify Jenkins is running:

```bash
# ✅ Confirm the container is up
docker ps
```

### 🔹 Subtask 1.2: Configure Jenkins Initial Setup

① Wait for Jenkins to start (approximately 2-3 minutes), then access the Jenkins web interface:

```
http://your-cloud-machine-ip:8080
```

② Get the initial admin password:

```bash
# 🔑 Retrieve the auto-generated admin password
docker exec jenkins-server cat /var/jenkins_home/secrets/initialAdminPassword
```

③ Complete Jenkins setup:

- 🔑 Enter the admin password when prompted
- 📦 Select **Install suggested plugins**
- 👤 Create your first admin user with these details:

```
Username: admin
Password: admin123
Full name: DevSecOps Admin
Email: admin@devsecops.local
# TODO: Replace with your own credentials before sharing this environment
```

- 🔗 Keep the default Jenkins URL

④ Install additional required plugins:

- ⚙️ Go to **Manage Jenkins → Manage Plugins**
- 📥 Click on the **Available** tab
- 🔍 Search and install these plugins:
  - 🔍 SonarQube Scanner
  - 🕷️ OWASP ZAP Official Jenkins Plugin
  - 🔄 Pipeline
  - 🌿 Git
- ♻️ Restart Jenkins when prompted

---

## 🔍 Task 2: Setting Up SonarQube as SAST Tool

![SonarQube](https://img.shields.io/badge/SonarQube-4E9BCD?style=flat-square&logo=sonarqube&logoColor=white)
![Docker Compose](https://img.shields.io/badge/Docker_Compose-2496ED?style=flat-square&logo=docker&logoColor=white)

### 🔹 Subtask 2.1: Install SonarQube

① Create a Docker Compose file for SonarQube:

```bash
# 📝 Open a new file for the SonarQube service definition
nano docker-compose-sonarqube.yml
```

② Add the following content:

```yaml
# 🔍 SonarQube SAST server service definition
version: '3.8'
services:
  sonarqube:
    image: sonarqube:community
    container_name: sonarqube-server
    restart: unless-stopped
    ports:
      - "9000:9000"                 # 🌐 Web UI / API
    environment:
      - SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true   # ⚙️ Relaxes Elasticsearch bootstrap checks for lab use
    volumes:
      - sonarqube_data:/opt/sonarqube/data
      - sonarqube_logs:/opt/sonarqube/logs
      - sonarqube_extensions:/opt/sonarqube/extensions

volumes:
  sonarqube_data:
  sonarqube_logs:
  sonarqube_extensions:
# TODO: In production, tune ES bootstrap (vm.max_map_count) instead of disabling checks
```

③ Start SonarQube container:

```bash
# 🚀 Launch SonarQube in detached mode
docker-compose -f docker-compose-sonarqube.yml up -d
```

④ Verify SonarQube is running:

```bash
# ✅ Confirm container status and boot logs
docker ps
docker logs sonarqube-server
```

### 🔹 Subtask 2.2: Configure SonarQube

① Access the SonarQube web interface (wait 3-4 minutes for startup):

```
http://your-cloud-machine-ip:9000
```

② Login with default credentials:

```
Username: admin
Password: admin
```

③ Change the default password:

- 🔐 You'll be prompted to change the password
- 🔑 Set new password: `admin123`
```
# TODO: Use a strong, unique password outside of a lab environment
```

④ Create a new project:

- ➕ Click **Create Project → Manually**
- 🏷️ Project key: `devsecops-demo`
- 📛 Display name: `DevSecOps Demo Project`
- ✅ Click **Set Up**

⑤ Generate an authentication token:

- 🔑 Select **Generate a token**
- 🏷️ Token name: `jenkins-integration`
- ✅ Click **Generate**
- ⚠️ **Important:** Copy and save this token for later use

### 🔹 Subtask 2.3: Integrate SonarQube with Jenkins

① Configure the SonarQube server in Jenkins:

- ⚙️ Go to **Manage Jenkins → Configure System**
- 📜 Scroll to the **SonarQube servers** section
- ➕ Click **Add SonarQube**
- 🏷️ Name: `SonarQube-Server`
- 🔗 Server URL: `http://your-cloud-machine-ip:9000`
- 🔑 Server authentication token: Click **Add → Jenkins**

```
Kind: Secret text
Secret: (paste the token you generated)
ID: sonarqube-token
Description: SonarQube Authentication Token
```

- ✅ Select the credential you just created
- 💾 Click **Save**

---

## 🕷️ Task 3: Setting Up OWASP ZAP as DAST Tool

![OWASP ZAP](https://img.shields.io/badge/OWASP_ZAP-000000?style=flat-square&logo=owasp&logoColor=white)
![Docker Compose](https://img.shields.io/badge/Docker_Compose-2496ED?style=flat-square&logo=docker&logoColor=white)

### 🔹 Subtask 3.1: Install OWASP ZAP

① Create a Docker Compose file for ZAP:

```bash
# 📝 Open a new file for the ZAP service definition
nano docker-compose-zap.yml
```

② Add the following content:

```yaml
# 🕷️ OWASP ZAP DAST scanner service definition
version: '3.8'
services:
  zap:
    image: owasp/zap2docker-stable
    container_name: zap-server
    restart: unless-stopped
    ports:
      - "8090:8080"                 # 🌐 Web-based ZAP desktop
      - "8091:8090"                 # 🔌 API access
    command: zap-webswing.sh
    volumes:
      - zap_data:/zap/wrk

volumes:
  zap_data:
```

③ Start ZAP container:

```bash
# 🚀 Launch OWASP ZAP in detached mode
docker-compose -f docker-compose-zap.yml up -d
```

④ Verify ZAP is running:

```bash
# ✅ Confirm the container is up
docker ps
```

### 🔹 Subtask 3.2: Configure OWASP ZAP

① Access the ZAP web interface (wait 2-3 minutes for startup):

```
http://your-cloud-machine-ip:8090
```

② Configure ZAP for API access:

- 🖥️ The web interface should load, showing the ZAP desktop
- ✅ ZAP is now ready to perform security scans

### 🔹 Subtask 3.3: Create a Test Web Application

> ⚠️ **Intentionally Vulnerable App** — DVWA is used purely to demonstrate DAST scanning in a safe, isolated lab environment. Never expose it outside this sandbox.

① Create a Docker Compose file for a test application:

```bash
# 📝 Open a new file for the vulnerable test app
nano docker-compose-webapp.yml
```

② Add the following content:

```yaml
# 🧪 DVWA vulnerable test application + database
version: '3.8'
services:
  dvwa:
    image: vulnerables/web-dvwa
    container_name: test-webapp
    restart: unless-stopped
    ports:
      - "8081:80"                   # 🌐 DVWA web UI
    environment:
      - MYSQL_HOSTNAME=db
      - MYSQL_DATABASE=dvwa
      - MYSQL_USERNAME=dvwa
      - MYSQL_PASSWORD=p@ssw0rd     # TODO: Move secrets to Docker secrets / .env before real use
    depends_on:
      - db

  db:
    image: mysql:5.7
    container_name: test-db
    restart: unless-stopped
    environment:
      - MYSQL_ROOT_PASSWORD=p@ssw0rd
      - MYSQL_DATABASE=dvwa
      - MYSQL_USER=dvwa
      - MYSQL_PASSWORD=p@ssw0rd
    volumes:
      - db_data:/var/lib/mysql

volumes:
  db_data:
```

③ Start the test application:

```bash
# 🚀 Launch the vulnerable test app and its database
docker-compose -f docker-compose-webapp.yml up -d
```

④ Verify the application is running:

```bash
# ✅ Confirm both containers are up
docker ps
```

⑤ Access the test application:

```
http://your-cloud-machine-ip:8081
```

---

## 🔄 Task 4: Creating an Integrated DevSecOps Pipeline

![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=flat-square&logo=jenkins&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=node.js&logoColor=white)
![SonarQube](https://img.shields.io/badge/SonarQube-4E9BCD?style=flat-square&logo=sonarqube&logoColor=white)
![OWASP ZAP](https://img.shields.io/badge/OWASP_ZAP-000000?style=flat-square&logo=owasp&logoColor=white)

### 🔹 Subtask 4.1: Create a Sample Application for Testing

① Create a simple web application directory:

```bash
# 📁 Create and enter the sample app directory
mkdir ~/devsecops-lab/sample-app
cd ~/devsecops-lab/sample-app
```

② Create a simple HTML file:

```bash
# 📝 Open a new HTML file
nano index.html
```

Add the following content:

```html
<!-- 🖼️ Simple demo login page -->
<!DOCTYPE html>
<html>
<head>
    <title>DevSecOps Demo App</title>
</head>
<body>
    <h1>Welcome to DevSecOps Demo</h1>
    <p>This is a sample application for security testing.</p>
    <form action="/login" method="post">
        <input type="text" name="username" placeholder="Username">
        <input type="password" name="password" placeholder="Password">
        <input type="submit" value="Login">
    </form>
</body>
</html>
```

③ Create a simple JavaScript file with potential security issues:

```bash
# 📝 Open a new JS file
nano app.js
```

Add the following content:

```javascript
// ⚠️ Sample application with intentional security issues for demonstration
const express = require('express');
const app = express();

// 🚨 Security issue: Missing input validation
app.post('/login', (req, res) => {
    const username = req.body.username;
    const password = req.body.password;

    // 🚨 Security issue: SQL injection vulnerability
    const query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'";

    // 🚨 Security issue: Hardcoded credentials
    if (username === 'admin' && password === 'password123') {
        res.send('Login successful');
    } else {
        res.send('Login failed');
    }
});

// TODO: Fix the issues above (parameterized queries, input validation, remove hardcoded creds)
// once SAST/DAST results confirm them — that remediation loop is the point of this lab.
app.listen(3000, () => {
    console.log('App running on port 3000');
});
```

④ Create a `package.json` file:

```bash
# 📝 Open a new package.json file
nano package.json
```

Add the following content:

```json
{
  "name": "devsecops-demo-app",
  "version": "1.0.0",
  "description": "Demo application for DevSecOps pipeline",
  "main": "app.js",
  "scripts": {
    "start": "node app.js",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "dependencies": {
    "express": "^4.18.0"
  }
}
```

⑤ Create a SonarQube configuration file:

```bash
# 📝 Open a new SonarQube properties file
nano sonar-project.properties
```

Add the following content:

```properties
# 🔍 SonarQube scanner configuration
sonar.projectKey=devsecops-demo
sonar.projectName=DevSecOps Demo Project
sonar.projectVersion=1.0
sonar.sources=.
sonar.language=js
sonar.sourceEncoding=UTF-8
```

### 🔹 Subtask 4.2: Create Jenkins Pipeline

① In Jenkins, create a new pipeline job:

- 🏠 Go to the Jenkins dashboard
- ➕ Click **New Item**
- 🏷️ Enter name: `DevSecOps-Pipeline`
- 🔄 Select **Pipeline**
- ✅ Click **OK**

② Configure the pipeline:

- 📜 Scroll to the **Pipeline** section
- 📋 Select **Pipeline script** from the **Definition** dropdown
- ➕ Add the following pipeline script:

```groovy
// 🔄 Jenkins declarative pipeline integrating SAST + DAST security gates
pipeline {
    agent any

    environment {
        SONAR_TOKEN = credentials('sonarqube-token')   // 🔑 Injected from Jenkins credentials store
        ZAP_PORT = '8090'
        TARGET_URL = 'http://your-cloud-machine-ip:8081'
        // TODO: Replace 'your-cloud-machine-ip' with your actual cloud machine IP address
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                // TODO: Replace with a real `git` checkout step for your repository
                sh 'echo "Source code checked out"'
            }
        }

        stage('Build') {
            steps {
                echo 'Building application...'
                sh 'echo "Application built successfully"'
            }
        }

        stage('SAST - SonarQube Analysis') {
            steps {
                echo 'Running Static Application Security Testing...'
                script {
                    def scannerHome = tool 'SonarScanner'
                    withSonarQubeEnv('SonarQube-Server') {
                        sh """
                            cd /home/ubuntu/devsecops-lab/sample-app
                            ${scannerHome}/bin/sonar-scanner \
                                -Dsonar.projectKey=devsecops-demo \
                                -Dsonar.sources=. \
                                -Dsonar.host.url=http://your-cloud-machine-ip:9000 \
                                -Dsonar.login=${SONAR_TOKEN}
                        """
                    }
                }
            }
        }

        stage('Deploy to Test') {
            steps {
                echo 'Deploying to test environment...'
                sh 'echo "Application deployed to test environment"'
            }
        }

        stage('DAST - ZAP Security Scan') {
            steps {
                echo 'Running Dynamic Application Security Testing...'
                script {
                    sh """
                        docker run --rm -v \$(pwd):/zap/wrk/:rw \
                        -t owasp/zap2docker-weekly zap-baseline.py \
                        -t ${TARGET_URL} -J zap-report.json || true
                    """
                }
            }
        }

        stage('Security Report') {
            steps {
                echo 'Generating security reports...'
                sh 'echo "Security scan completed. Check SonarQube dashboard for SAST results."'
                sh 'echo "ZAP scan completed. Check workspace for DAST results."'
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed!'
            // 📦 Archive security reports
            archiveArtifacts artifacts: '*.json', allowEmptyArchive: true
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed! Check security issues.'
        }
    }
}
```

> ⚠️ **Note:** Replace `your-cloud-machine-ip` with your actual cloud machine IP address in the pipeline script.

③ Install the SonarQube Scanner tool:

- ⚙️ Go to **Manage Jenkins → Global Tool Configuration**
- 📜 Scroll to **SonarQube Scanner**
- ➕ Click **Add SonarQube Scanner**
- 🏷️ Name: `SonarScanner`
- ☑️ Check **Install automatically**
- 📦 Select latest version
- 💾 Click **Save**

### 🔹 Subtask 4.3: Run the DevSecOps Pipeline

① Execute the pipeline:

- 🏠 Go to your `DevSecOps-Pipeline` job
- ▶️ Click **Build Now**
- 👀 Monitor the build progress in **Console Output**

② Review SAST results in SonarQube:

- 🔍 Go to the SonarQube dashboard: `http://your-cloud-machine-ip:9000`
- 📂 Click on your project `devsecops-demo`
- 🔎 Review security vulnerabilities, code smells, and bugs identified

③ Review DAST results:

- 📂 Check the Jenkins workspace for ZAP report files
- 🕷️ Review security vulnerabilities found in the web application

---

## 📊 Task 5: Understanding the Results

### 🔹 Subtask 5.1: Analyze SAST Results

In the SonarQube dashboard, examine:

- 🔥 **Security Hotspots:** Potential security vulnerabilities
- 🐛 **Bugs:** Code issues that could lead to security problems
- 👃 **Code Smells:** Maintainability issues that could indirectly affect security
- 📈 **Coverage:** How much of your code is tested

**Common SAST findings you might see:**

- 🔑 Hardcoded credentials
- 💉 SQL injection vulnerabilities
- 🎭 Cross-site scripting (XSS) potential
- ⚠️ Input validation issues

### 🔹 Subtask 5.2: Analyze DAST Results

Review ZAP scan results:

- 🌐 Look for common web application vulnerabilities
- 🔟 Check for OWASP Top 10 security risks
- 🚦 Review risk levels (High, Medium, Low, Informational)

**Common DAST findings include:**

- 🛡️ Missing security headers
- 🔓 Insecure HTTP methods
- 📁 Directory traversal vulnerabilities
- 🚪 Authentication bypass issues

---

## 🗺️ MITRE ATT&CK Mapping

The vulnerability classes this lab's SAST/DAST tools are designed to surface map to well-known adversary techniques — and to the pipeline controls that mitigate them.

| Vulnerability Class | Detected By | ATT&CK Technique | Mitigated By |
|---|---|---|---|
| 💉 SQL Injection | SonarQube (SAST) + ZAP (DAST) | [T1190 – Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/) | Parameterized queries + SAST gate before merge |
| 🔑 Hardcoded Credentials | SonarQube (SAST) | [T1552.001 – Unsecured Credentials: Credentials In Files](https://attack.mitre.org/techniques/T1552/001/) | Secrets management + credential scanning |
| 🚪 Weak/Default Authentication | ZAP (DAST) | [T1078 – Valid Accounts](https://attack.mitre.org/techniques/T1078/) | Strong credential policy + DAST auth testing |
| 🎭 Cross-Site Scripting (XSS) | ZAP (DAST) | [T1190 – Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/) | Output encoding + DAST regression scans |
| 🛡️ Missing Security Headers | ZAP (DAST) | [T1595 – Active Scanning](https://attack.mitre.org/techniques/T1595/) *(reduces attack-surface reconnaissance value)* | Security header hardening (CSP, HSTS, X-Frame-Options) |

> 🎓 This mapping is framed defensively: it shows which adversary techniques the DevSecOps pipeline's SAST/DAST gates are positioned to catch **before** vulnerable code reaches production, not an offensive playbook.

---

## 🛠️ Troubleshooting Common Issues

<details>
<summary>🔴 Issue 1: Jenkins Container Won't Start</summary>

**Solution:**

```bash
# 🔍 Check if port 8080 is already in use
sudo netstat -tlnp | grep 8080
# 🔄 If in use, stop the conflicting service or change the Jenkins port
```

</details>

<details>
<summary>🟠 Issue 2: SonarQube Takes Too Long to Start</summary>

**Solution:**

```bash
# 📜 Check SonarQube logs
docker logs sonarqube-server
# 💾 Increase memory if needed
docker-compose down
# ✏️ Edit docker-compose file to add memory limits
```

</details>

<details>
<summary>🟡 Issue 3: ZAP Scan Fails</summary>

**Solution:**

```bash
# 🌐 Ensure target application is accessible
curl http://your-cloud-machine-ip:8081
# 📜 Check ZAP container logs
docker logs zap-server
```

</details>

<details>
<summary>🟣 Issue 4: Pipeline Fails at SonarQube Stage</summary>

**Solution:**

```bash
# 🔑 Verify SonarQube token is correctly configured
# 🔌 Check SonarQube server connectivity from Jenkins
# 🧰 Ensure SonarQube Scanner tool is properly installed
```

</details>

---

## ✅ Verification Steps

To verify your lab setup is working correctly:

① Check all containers are running:

```bash
# ✅ List all running containers
docker ps
```

You should see containers for Jenkins, SonarQube, ZAP, and the test web application.

② Verify web interfaces are accessible:

| Service | URL |
|---|---|
| 🔧 Jenkins | `http://your-cloud-machine-ip:8080` |
| 🔍 SonarQube | `http://your-cloud-machine-ip:9000` |
| 🕷️ ZAP | `http://your-cloud-machine-ip:8090` |
| 🧪 Test App | `http://your-cloud-machine-ip:8081` |

③ Run a test pipeline build and ensure it completes successfully

④ Check that security reports are generated in both SonarQube and the Jenkins workspace

---

## 🎓 Conclusion

Congratulations! 🎉 You have successfully completed Lab 1 of Understanding DevSecOps.

### 🏆 Key Accomplishments

- 🔧 Implemented a complete DevSecOps toolchain using three essential open-source tools
- ⚙️ Set up Jenkins as your CI/CD automation server to orchestrate the entire pipeline
- 🔍 Configured SonarQube for Static Application Security Testing (SAST) to identify source-code vulnerabilities
- 🕷️ Deployed OWASP ZAP for Dynamic Application Security Testing (DAST) to find runtime security issues
- 🔄 Created an integrated pipeline that automatically runs security tests as part of the development process
- 📊 Learned to interpret security scan results from both static and dynamic analysis tools

### 💡 Why This Matters

This lab demonstrates the core principle of DevSecOps: shifting security left in the development lifecycle. Instead of treating security as an afterthought, you've learned to integrate security testing directly into your CI/CD pipeline. This approach helps teams:

- ⏱️ Identify security issues early, when they're cheaper and easier to fix
- 🤖 Automate security testing to ensure consistent coverage
- 📉 Reduce security debt by catching vulnerabilities before they reach production
- 🧠 Build security awareness among development teams through immediate feedback

### 🌍 Real-World Applications

The skills you've developed in this lab are directly applicable to enterprise environments where security is paramount. Organizations worldwide are adopting DevSecOps practices to build more secure software faster, and the tools you've learned to use are industry standards.

### 🚀 Next Steps

In future labs, you'll expand on this foundation by exploring advanced DevSecOps concepts such as:

- 📦 Container security scanning
- 🏗️ Infrastructure as Code (IaC) security
- 📋 Compliance automation
- 🎯 Advanced threat modeling
- 📊 Security metrics and reporting

You now have a solid foundation in DevSecOps tooling and can confidently explain how security integration improves software development practices. Keep practicing with different types of applications and security scenarios to deepen your expertise! 💪

---

<div align="center">

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Training-blueviolet?style=for-the-badge)

</div>
