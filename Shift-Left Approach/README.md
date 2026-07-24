<div align="center">

# ⏪ Shift-Left Approach Implementation with CI/CD Pipeline
### Designing & Building a Security-Integrated Pipeline with Jenkins, SonarQube & OWASP ZAP

![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)
![SonarQube](https://img.shields.io/badge/SonarQube-4E9BCD?style=for-the-badge&logo=sonarqube&logoColor=white)
![OWASP ZAP](https://img.shields.io/badge/OWASP_ZAP-000000?style=for-the-badge&logo=owasp&logoColor=white)
![Draw.io](https://img.shields.io/badge/draw.io-F08705?style=for-the-badge&logo=diagramsdotnet&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

![Level](https://img.shields.io/badge/Level-Beginner-brightgreen?style=for-the-badge)
![Duration](https://img.shields.io/badge/Duration-2--3_Hours-blue?style=for-the-badge)
![Track](https://img.shields.io/badge/Track-DevSecOps-orange?style=for-the-badge)

</div>

---

## 📑 Table of Contents

- [🎯 Lab Objectives](#-lab-objectives)
- [📋 Prerequisites](#-prerequisites)
- [🖥️ Lab Environment Setup](#️-lab-environment-setup)
- [🔧 Task 1: Pipeline Visualization and Shift-Left Approach Design](#-task-1-pipeline-visualization-and-shift-left-approach-design)
- [🔍 Task 2: Tools Integration and Code Scanning Implementation](#-task-2-tools-integration-and-code-scanning-implementation)
- [🗺️ MITRE ATT&CK Mapping](#️-mitre-attck-mapping)
- [🛠️ Troubleshooting Common Issues](#️-troubleshooting-common-issues)
- [📚 Key Concepts Summary](#-key-concepts-summary)
- [🎓 Conclusion](#-conclusion)

---

## 🎯 Lab Objectives

By the end of this lab, students will be able to:

| # | Learning Objective |
|---|---|
| 1 | ⏪ Understand and implement the Shift-Left security approach in DevOps pipelines |
| 2 | 🗺️ Design and visualize a complete CI/CD pipeline with integrated security tools |
| 3 | 🔧 Configure Jenkins as a CI/CD server for automated builds and deployments |
| 4 | 🔍 Integrate SonarQube for Static Application Security Testing (SAST) |
| 5 | 🕷️ Implement ZAP (OWASP Zed Attack Proxy) for Dynamic Application Security Testing (DAST) |
| 6 | 🤖 Demonstrate automated security scanning throughout the development lifecycle |
| 7 | 📊 Analyze security scan results and understand their impact on code quality |

## 📋 Prerequisites

| # | Requirement |
|---|---|
| 1 | 🔄 Basic understanding of DevOps concepts and CI/CD pipelines |
| 2 | 🐧 Familiarity with Linux command line operations |
| 3 | 🌐 Basic knowledge of web application security concepts |
| 4 | 🌿 Understanding of version control systems (Git) |
| 5 | 📦 Basic knowledge of containerization concepts |

## 🖥️ Lab Environment Setup

> ☁️ **Ready-to-Use Cloud Machines** — Al Nafi provides pre-configured Linux-based cloud machines for this lab. Simply click **Start Lab** to access your environment. No need to build your own VM or install additional software — everything is ready to use!

**Your lab environment includes:**

![Ubuntu](https://img.shields.io/badge/Ubuntu_20.04_LTS-E95420?style=flat-square&logo=ubuntu&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Preinstalled-2496ED?style=flat-square&logo=docker&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-Ready-D24939?style=flat-square&logo=jenkins&logoColor=white)
![SonarQube](https://img.shields.io/badge/SonarQube-Ready-4E9BCD?style=flat-square&logo=sonarqube&logoColor=white)

- 🐧 Ubuntu 20.04 LTS with Docker pre-installed
- 🔧 Jenkins server ready for configuration
- 🔍 SonarQube server ready for setup
- 🕷️ OWASP ZAP proxy tool
- 🧪 Sample web application for testing
- 🗺️ Draw.io access for pipeline visualization

---

## 🔧 Task 1: Pipeline Visualization and Shift-Left Approach Design

![Draw.io](https://img.shields.io/badge/draw.io-F08705?style=flat-square&logo=diagramsdotnet&logoColor=white)

### 🔹 Subtask 1.1: Understanding Shift-Left Security

The Shift-Left approach means integrating security testing early in the development process rather than waiting until the end. This approach helps identify and fix security issues when they are less expensive and easier to resolve.

**Key benefits of Shift-Left security:**

- ⏱️ **Early Detection:** Find vulnerabilities during development
- 💰 **Cost Reduction:** Fix issues before they reach production
- 🚀 **Faster Delivery:** Reduce delays caused by late-stage security findings
- ✨ **Better Quality:** Improve overall code quality and security posture

### 🔹 Subtask 1.2: Creating Pipeline Visualization with Draw.io

① Access Draw.io:

```bash
# 🌐 Open your web browser and navigate to:
https://app.diagrams.net/
```

② Create a new diagram:

- ➕ Click **Create New Diagram**
- ⬜ Select **Blank Diagram**
- 🏷️ Name it `Shift-Left-Security-Pipeline`

③ Design the complete pipeline — create the following stages left to right:

> **🧩 Stage 1: Development Phase (Shift-Left Security)**
> - 🌿 Developer commits code to Git repository
> - 🪝 Pre-commit hooks run basic security checks
> - 👀 Code review with security focus

> **🏗️ Stage 2: Build Phase**
> - 🔧 Jenkins triggers automated build
> - ✅ Unit tests execution
> - 🔍 Static code analysis with SonarQube (SAST)

> **🧪 Stage 3: Testing Phase**
> - 🔗 Integration tests
> - 🛡️ Security unit tests
> - 📦 Container security scanning

> **🚀 Stage 4: Deployment Phase**
> - 🎭 Deploy to staging environment
> - 🕷️ Dynamic security testing with OWASP ZAP (DAST)
> - ⚡ Performance and load testing

> **🌍 Stage 5: Production Phase**
> - 🏭 Production deployment
> - 📡 Runtime security monitoring
> - 🔄 Continuous security assessment

④ Add security tools integration points:

- 🔍 Mark where SonarQube integrates (Build phase)
- 🕷️ Mark where OWASP ZAP integrates (Testing phase)
- 🔁 Show feedback loops back to developers

⑤ Save your diagram:

- 📤 **File → Export as → PNG**
- 💾 Save as `shift-left-pipeline.png`

```
# TODO: Attach your exported shift-left-pipeline.png alongside this README
# as visual evidence of the completed diagram.
```

---

## 🔍 Task 2: Tools Integration and Code Scanning Implementation

![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=flat-square&logo=jenkins&logoColor=white)
![SonarQube](https://img.shields.io/badge/SonarQube-4E9BCD?style=flat-square&logo=sonarqube&logoColor=white)
![OWASP ZAP](https://img.shields.io/badge/OWASP_ZAP-000000?style=flat-square&logo=owasp&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)

### 🔹 Subtask 2.1: Jenkins CI/CD Server Setup

① Start the Jenkins service:

```bash
# 🔍 Check if Jenkins is running
sudo systemctl status jenkins

# 🚀 If not running, start Jenkins
sudo systemctl start jenkins
sudo systemctl enable jenkins
```

② Access the Jenkins web interface:

```bash
# 🔑 Get the initial admin password
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

Open your browser and navigate to:

```
http://localhost:8080
# TODO: Replace 'localhost' with your cloud machine's public IP if accessing remotely
```

③ Complete Jenkins initial setup:

- 🔑 Enter the initial admin password
- 📦 Install suggested plugins
- 👤 Create admin user:

```
Username: admin
Password: admin123
Full name: Lab Administrator
Email: admin@lab.local
# TODO: Replace with your own credentials before sharing this environment
```

④ Install required plugins:

- ⚙️ Go to **Manage Jenkins → Manage Plugins**
- 📥 Install the following plugins:
  - 🔍 SonarQube Scanner
  - 🕷️ OWASP ZAP Official Jenkins Plugin
  - 🌿 Git Plugin
  - 🔄 Pipeline Plugin
  - 🐳 Docker Pipeline Plugin

### 🔹 Subtask 2.2: SonarQube SAST Tool Integration

① Start the SonarQube server:

```bash
# 📁 Navigate to the SonarQube directory
cd /opt/sonarqube/bin/linux-x86-64/

# 🚀 Start SonarQube
sudo ./sonar.sh start

# ✅ Check status
sudo ./sonar.sh status
```

② Access the SonarQube web interface:

```
http://localhost:9000
```

Default credentials:

```
Username: admin
Password: admin
```

- 🔐 Change password when prompted to: `admin123`

③ Create a SonarQube project:

- ➕ Click **Create Project → Manually**
- 🏷️ Project key: `secure-web-app`
- 📛 Display name: `Secure Web Application`
- ✅ Click **Set Up**

④ Generate a SonarQube token:

- ⚙️ Go to **My Account → Security**
- 🔑 Generate token named: `jenkins-integration`
- 💾 Copy and save the token: `squ_xxxxxxxxxxxxxxxxxxxxxxxxx`

⑤ Configure SonarQube in Jenkins:

- ⚙️ In Jenkins: **Manage Jenkins → Configure System**
- 🔍 Find the **SonarQube servers** section
- ➕ Add SonarQube server:

```
Name: SonarQube-Local
Server URL: http://localhost:9000
Server authentication token: (paste the token generated above)
```

### 🔹 Subtask 2.3: OWASP ZAP DAST Tool Integration

① Start OWASP ZAP:

```bash
# 🕷️ Start ZAP in daemon mode
/opt/zaproxy/zap.sh -daemon -host 0.0.0.0 -port 8090 -config api.addrs.addr.name=.* -config api.addrs.addr.regex=true
```

② Verify ZAP is running:

```bash
# 🔍 Check if ZAP is listening
netstat -tlnp | grep 8090

# 🧪 Test the ZAP API
curl http://localhost:8090/JSON/core/view/version/
```

③ Configure ZAP in Jenkins:

- ⚙️ In Jenkins: **Manage Jenkins → Configure System**
- 🔍 Find the **ZAP** section
- ➕ Add ZAP installation:

```
Name: ZAP-Local
Host: localhost
Port: 8090
```

### 🔹 Subtask 2.4: Sample Application Setup

① Create the sample web application:

```bash
# 📁 Create the project directory
mkdir -p /home/ubuntu/secure-web-app
cd /home/ubuntu/secure-web-app

# 📝 Create a simple vulnerable web application
cat > app.py << 'EOF'
from flask import Flask, request, render_template_string
import sqlite3
import os

app = Flask(__name__)

# 🚨 Vulnerable SQL query (for demonstration)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # 🚨 Vulnerable SQL injection point — intentionally left insecure for scanning
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

        return f"Query executed: {query}"

    return '''
    <form method="post">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
    '''

@app.route('/')
def home():
    return '<h1>Secure Web App Demo</h1><a href="/login">Login</a>'

# TODO: Replace debug=True with a production-safe config before any real deployment
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
EOF
```

② Create a requirements file:

```bash
# 📝 Pin dependency versions
cat > requirements.txt << 'EOF'
Flask==2.3.3
Werkzeug==2.3.7
EOF
```

③ Create a Dockerfile:

```bash
# 🐳 Containerize the sample app
cat > Dockerfile << 'EOF'
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]
EOF
```

④ Initialize a Git repository:

```bash
# 🌿 Version-control the sample app
git init
git add .
git commit -m "Initial commit - Sample web application"
```

### 🔹 Subtask 2.5: Create Jenkins Pipeline with Security Integration

① Create the Jenkins pipeline job:

- 🏠 In the Jenkins dashboard, click **New Item**
- 🏷️ Enter name: `Secure-Web-App-Pipeline`
- 🔄 Select **Pipeline** and click **OK**

② Configure the pipeline script — in the **Pipeline** section, add the following:

```groovy
// 🔄 Jenkins declarative pipeline implementing Shift-Left security gates
pipeline {
    agent any

    environment {
        SONAR_PROJECT_KEY = 'secure-web-app'
        ZAP_PORT = '8090'
        APP_PORT = '5000'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from repository...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building the application...'
                sh '''
                    cd /home/ubuntu/secure-web-app
                    docker build -t secure-web-app:latest .
                '''
            }
        }

        stage('SAST - SonarQube Analysis') {
            steps {
                echo 'Running Static Application Security Testing...'
                script {
                    def scannerHome = tool 'SonarQubeScanner'
                    withSonarQubeEnv('SonarQube-Local') {
                        sh """
                            cd /home/ubuntu/secure-web-app
                            ${scannerHome}/bin/sonar-scanner \
                                -Dsonar.projectKey=${SONAR_PROJECT_KEY} \
                                -Dsonar.sources=. \
                                -Dsonar.host.url=http://localhost:9000 \
                                -Dsonar.login=${SONAR_AUTH_TOKEN}
                        """
                    }
                }
            }
        }

        stage('Deploy to Staging') {
            steps {
                echo 'Deploying application to staging environment...'
                sh '''
                    # 🧹 Stop any existing container
                    docker stop secure-web-app || true
                    docker rm secure-web-app || true

                    # 🚀 Run the application
                    docker run -d --name secure-web-app -p 5000:5000 secure-web-app:latest

                    # ⏳ Wait for application to start
                    sleep 10
                '''
            }
        }

        stage('DAST - ZAP Security Scan') {
            steps {
                echo 'Running Dynamic Application Security Testing...'
                script {
                    sh '''
                        # 🕷️ Basic ZAP spider scan
                        curl "http://localhost:8090/JSON/spider/action/scan/?url=http://localhost:5000"

                        # ⏳ Wait for spider to complete
                        sleep 30

                        # 🎯 Run active scan
                        curl "http://localhost:8090/JSON/ascan/action/scan/?url=http://localhost:5000"

                        # ⏳ Wait for scan to complete
                        sleep 60

                        # 📄 Generate report
                        curl "http://localhost:8090/OTHER/core/other/htmlreport/" > zap-report.html
                    '''
                }
            }
        }

        stage('Security Report') {
            steps {
                echo 'Generating security reports...'
                sh '''
                    echo "=== SECURITY SCAN SUMMARY ==="
                    echo "SonarQube SAST scan completed"
                    echo "ZAP DAST scan completed"
                    echo "Reports available in Jenkins workspace"
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed'
            sh 'docker stop secure-web-app || true'
        }
        success {
            echo 'All security scans passed successfully!'
        }
        failure {
            echo 'Security scans detected issues. Please review the reports.'
        }
    }
}
```

③ Configure the SonarQube Scanner tool:

- ⚙️ Go to **Manage Jenkins → Global Tool Configuration**
- 🔍 Find the **SonarQube Scanner** section
- ➕ Add SonarQube Scanner:

```
Name: SonarQubeScanner
Install automatically: Check
Version: Latest
```

### 🔹 Subtask 2.6: Execute Pipeline and Analyze Results

① Run the pipeline:

- 🏠 Go to your pipeline job
- ▶️ Click **Build Now**
- 👀 Monitor the build progress in **Console Output**

② Analyze SonarQube results:

- 🔍 Navigate to SonarQube: `http://localhost:9000`
- 📂 Click on your project **Secure Web Application**
- 🔎 Review the security findings:
  - 🔥 **Security Hotspots:** Potential security issues
  - 🚨 **Vulnerabilities:** Confirmed security problems
  - 👃 **Code Smells:** Maintainability issues
  - 📈 **Coverage:** Test coverage metrics

③ Analyze ZAP DAST results:

- 📄 Check the ZAP report generated in the Jenkins workspace
- 🔎 Review findings such as:
  - 🔴 **High Risk:** Critical security vulnerabilities
  - 🟠 **Medium Risk:** Important security issues
  - 🟡 **Low Risk:** Minor security concerns
  - 🔵 **Informational:** General security information

**Common SonarQube findings:**

```
Security Hotspots Found:
- SQL Injection vulnerability in login function
- Hardcoded credentials
- Insecure random number generation
- Cross-site scripting (XSS) potential
```

**Common ZAP findings:**

```
DAST Scan Results:
- Missing security headers
- Unencrypted communications
- Session management issues
- Input validation problems
```

### 🔹 Subtask 2.7: Demonstrate Shift-Left Benefits

① Show early detection via the SonarQube quality gate:

```bash
# 🚦 View SonarQube quality gate status
curl -u admin:admin123 "http://localhost:9000/api/qualitygates/project_status?projectKey=secure-web-app"
```

② Create a security-fixed version of the application:

```bash
cd /home/ubuntu/secure-web-app

# ✅ Create an improved, security-hardened version of the app
cat > app_secure.py << 'EOF'
from flask import Flask, request, render_template_string
import sqlite3
import hashlib
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)   # ✅ Cryptographically secure key generation

# ✅ Secure SQL query using parameterized statements
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # ✅ Secure parameterized query — fixes the SQL injection found in app.py
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        result = cursor.fetchone()
        conn.close()

        if result:
            return "Login successful!"
        else:
            return "Invalid credentials"

    return '''
    <form method="post">
        Username: <input type="text" name="username" required><br>
        Password: <input type="password" name="password" required><br>
        <input type="submit" value="Login">
    </form>
    '''

@app.route('/')
def home():
    return '<h1>Secure Web App Demo</h1><a href="/login">Login</a>'

# TODO: Add password hashing (e.g. Werkzeug's generate_password_hash) before any real deployment
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
EOF
```

③ Run the pipeline again with the secure code:

- 🔁 Replace `app.py` with `app_secure.py`
- 🌿 Commit changes and trigger the pipeline
- 📊 Compare the security scan results before and after

---

## 🗺️ MITRE ATT&CK Mapping

The vulnerability classes this lab's SAST/DAST tools surface map to well-known adversary techniques — and to the pipeline controls that mitigate them, illustrating exactly what "shifting left" catches before production.

| Vulnerability Class | Detected By | ATT&CK Technique | Mitigated By |
|---|---|---|---|
| 💉 SQL Injection | SonarQube (SAST) + ZAP (DAST) | [T1190 – Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/) | Parameterized queries (see `app_secure.py`) |
| 🔑 Hardcoded Credentials | SonarQube (SAST) | [T1552.001 – Unsecured Credentials: Credentials In Files](https://attack.mitre.org/techniques/T1552/001/) | Secrets management + credential scanning |
| 🎲 Insecure Random Number Generation | SonarQube (SAST) | [T1552.001 – Unsecured Credentials](https://attack.mitre.org/techniques/T1552/001/) *(weak tokens/keys enable credential compromise)* | CSPRNG (`secrets.token_hex`) instead of weak randomness |
| 🎭 Cross-Site Scripting (XSS) | ZAP (DAST) | [T1190 – Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/) | Output encoding + input validation |
| 🛡️ Missing Security Headers | ZAP (DAST) | [T1595 – Active Scanning](https://attack.mitre.org/techniques/T1595/) *(reduces recon value for attackers)* | Security header hardening (CSP, HSTS, X-Frame-Options) |
| 📡 Unencrypted Communications | ZAP (DAST) | [T1040 – Network Sniffing](https://attack.mitre.org/techniques/T1040/) | Enforce TLS/HTTPS end-to-end |
| 🍪 Session Management Issues | ZAP (DAST) | [T1539 – Steal Web Session Cookie](https://attack.mitre.org/techniques/T1539/) | Secure/HttpOnly cookie flags + session rotation |

> 🎓 This mapping is framed defensively: it shows which adversary techniques the Shift-Left pipeline's SAST/DAST gates are positioned to catch **before** vulnerable code reaches production, not an offensive playbook.

---

## 🛠️ Troubleshooting Common Issues

<details>
<summary>🔴 Jenkins Issues</summary>

```bash
# 🔄 If Jenkins fails to start
sudo systemctl restart jenkins
sudo journalctl -u jenkins -f

# 🔐 If plugins fail to install
sudo chown -R jenkins:jenkins /var/lib/jenkins/
sudo systemctl restart jenkins
```

</details>

<details>
<summary>🟠 SonarQube Issues</summary>

```bash
# ⚙️ If SonarQube fails to start
sudo sysctl -w vm.max_map_count=262144
echo 'vm.max_map_count=262144' | sudo tee -a /etc/sysctl.conf

# 📜 Check SonarQube logs
tail -f /opt/sonarqube/logs/sonar.log
```

</details>

<details>
<summary>🟡 ZAP Issues</summary>

```bash
# 🔥 If ZAP API is not accessible
sudo ufw allow 8090
netstat -tlnp | grep 8090

# ♻️ Restart ZAP if needed
pkill -f zap
/opt/zaproxy/zap.sh -daemon -host 0.0.0.0 -port 8090 -config api.addrs.addr.name=.* -config api.addrs.addr.regex=true
```

</details>

---

## 📚 Key Concepts Summary

### ⏪ Shift-Left Security Benefits

| Benefit | Description |
|---|---|
| ⏱️ Early Detection | Security issues found during the development phase |
| 💰 Cost Efficiency | Cheaper to fix issues early in the lifecycle |
| 🚀 Faster Delivery | Reduced delays from late-stage security findings |
| ✨ Quality Improvement | Better overall code quality and security posture |

### 🔍 SAST vs DAST

| Approach | Description |
|---|---|
| 🔍 SAST (Static) | Analyzes source code without executing it |
| 🕷️ DAST (Dynamic) | Tests running applications for vulnerabilities |
| 🤝 Complementary | Both approaches needed for comprehensive security |

### 🧩 Tool Integration Points

| Tool | Role |
|---|---|
| 🔧 Jenkins | Orchestrates the entire CI/CD pipeline |
| 🔍 SonarQube | Provides static code analysis and security scanning |
| 🕷️ OWASP ZAP | Performs dynamic security testing of web applications |

---

## 🎓 Conclusion

In this lab, you have successfully:

- 🗺️ Designed and visualized a complete CI/CD pipeline implementing the Shift-Left security approach
- 🔧 Configured Jenkins as a central CI/CD server to orchestrate automated builds and deployments
- 🔍 Integrated SonarQube for Static Application Security Testing (SAST) to catch security issues in source code
- 🕷️ Implemented OWASP ZAP for Dynamic Application Security Testing (DAST) to find runtime vulnerabilities
- 🤖 Demonstrated automated security scanning throughout the development lifecycle
- 📊 Analyzed security scan results and understood their impact on application security

### 💡 Why This Matters

The Shift-Left approach you've implemented represents a fundamental shift in how organizations approach security. By integrating security testing early and continuously throughout the development process, teams can:

- ⏱️ Identify vulnerabilities when they're easier and cheaper to fix
- 🚀 Maintain faster development cycles without compromising security
- 🧠 Build security awareness and expertise within development teams
- 🛡️ Achieve better overall security posture for applications

### 🌍 Real-World Applications

This hands-on experience with Jenkins, SonarQube, and OWASP ZAP provides you with practical skills in implementing DevSecOps practices that are highly valued in modern software development environments. The pipeline you've created serves as a foundation that can be extended with additional security tools and practices as your security program matures.

> 🔄 Remember: security is not a one-time activity but an ongoing process that requires continuous monitoring, updating, and improvement of your security practices and tools.

---

<div align="center">

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Training-blueviolet?style=for-the-badge)

</div>
