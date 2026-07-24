<div align="center">

# 🛡️ Embracing DevSecOps
### Integrating Security into the Development Lifecycle

![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)
![SonarQube](https://img.shields.io/badge/SonarQube-4E9BCD?style=for-the-badge&logo=sonarqube&logoColor=white)
![OWASP ZAP](https://img.shields.io/badge/OWASP_ZAP-000000?style=for-the-badge&logo=owasp&logoColor=white)
![OWASP Dependency Check](https://img.shields.io/badge/OWASP_Dependency--Check-000000?style=for-the-badge&logo=owasp&logoColor=white)
![Maven](https://img.shields.io/badge/Maven-C71A36?style=for-the-badge&logo=apachemaven&logoColor=white)
![Java](https://img.shields.io/badge/Java_11-007396?style=for-the-badge&logo=openjdk&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

![Level](https://img.shields.io/badge/Level-Intermediate-yellow?style=for-the-badge)
![Duration](https://img.shields.io/badge/Duration-4--5_Hours-blue?style=for-the-badge)
![Track](https://img.shields.io/badge/Track-DevSecOps-orange?style=for-the-badge)

</div>

---

## 📑 Table of Contents

- [🎯 Lab Objectives](#-lab-objectives)
- [📋 Prerequisites](#-prerequisites)
- [🖥️ Lab Environment Setup](#️-lab-environment-setup)
- [🧠 Task 1: Understanding DevSecOps Fundamentals](#-task-1-understanding-devsecops-fundamentals)
- [🔧 Task 2: Setting Up Jenkins for DevSecOps](#-task-2-setting-up-jenkins-for-devsecops)
- [🔍 Task 3: Setting Up SonarQube for Code Quality and Security Analysis](#-task-3-setting-up-sonarqube-for-code-quality-and-security-analysis)
- [📦 Task 4: Setting Up OWASP Dependency Check](#-task-4-setting-up-owasp-dependency-check)
- [🕷️ Task 5: Setting Up OWASP ZAP for Dynamic Security Testing](#️-task-5-setting-up-owasp-zap-for-dynamic-security-testing)
- [🧪 Task 6: Creating a Sample Application for Testing](#-task-6-creating-a-sample-application-for-testing)
- [🔄 Task 7: Creating a DevSecOps Pipeline](#-task-7-creating-a-devsecops-pipeline)
- [🚨 Task 8: Running Security Scans and Analysis](#-task-8-running-security-scans-and-analysis)
- [📊 Task 9: Analyzing Security Reports and Remediation](#-task-9-analyzing-security-reports-and-remediation)
- [🚦 Task 10: Implementing Security Gates and Policies](#-task-10-implementing-security-gates-and-policies)
- [📈 Task 11: Monitoring and Continuous Improvement](#-task-11-monitoring-and-continuous-improvement)
- [▶️ Task 12: Running the Complete DevSecOps Pipeline](#️-task-12-running-the-complete-devsecops-pipeline)
- [🗺️ MITRE ATT&CK Mapping](#️-mitre-attck-mapping)
- [🎓 Conclusion](#-conclusion)

---

## 🎯 Lab Objectives

By the end of this lab, students will be able to:

| # | Learning Objective |
|---|---|
| 1 | 🧠 Understand the core principles of DevSecOps and its importance in modern software development |
| 2 | 🔧 Set up and configure Jenkins for continuous integration with security integration |
| 3 | 🔍 Install and configure SonarQube for static code analysis and security vulnerability detection |
| 4 | 📦 Implement OWASP Dependency Check to identify vulnerable dependencies in projects |
| 5 | 🕷️ Configure OWASP ZAP for automated security testing |
| 6 | 🔄 Create a complete DevSecOps pipeline that integrates security at every stage of development |
| 7 | 📊 Analyze security reports and understand how to remediate common vulnerabilities |
| 8 | 🚦 Implement security gates in CI/CD pipelines to prevent insecure code deployment |

## 📋 Prerequisites

| # | Requirement |
|---|---|
| 1 | 🔄 Basic understanding of software development lifecycle (SDLC) |
| 2 | 🐧 Familiarity with Linux command line operations |
| 3 | 🌿 Basic knowledge of version control systems (Git) |
| 4 | 🌐 Understanding of web applications and common security vulnerabilities |
| 5 | 🔁 Basic knowledge of continuous integration concepts |

> ☁️ **Ready-to-Use Cloud Machines** — Al Nafi provides ready-to-use Linux-based cloud machines for this lab. Simply click **Start Lab** to access your pre-configured environment — no need to build your own VM.

## 🖥️ Lab Environment Setup

**Your cloud machine comes pre-installed with:**

![Ubuntu](https://img.shields.io/badge/Ubuntu_20.04_LTS-E95420?style=flat-square&logo=ubuntu&logoColor=white)
![Docker](https://img.shields.io/badge/Docker_%26_Compose-2496ED?style=flat-square&logo=docker&logoColor=white)
![Java](https://img.shields.io/badge/Java_11-007396?style=flat-square&logo=openjdk&logoColor=white)
![Maven](https://img.shields.io/badge/Maven-C71A36?style=flat-square&logo=apachemaven&logoColor=white)

- 🐧 Ubuntu 20.04 LTS
- 🐳 Docker and Docker Compose
- ☕ Java 11
- 🌿 Git
- 📦 Maven
- 🧰 Basic development tools

---

## 🧠 Task 1: Understanding DevSecOps Fundamentals

### 🔹 Subtask 1.1: DevSecOps Overview

DevSecOps integrates security practices within the DevOps process. Instead of treating security as a separate phase, it embeds security throughout the entire development lifecycle.

**Key Principles:**

- ⏪ **Shift Left Security:** Implement security early in the development process
- 🤖 **Automation:** Automate security testing and compliance checks
- 📡 **Continuous Monitoring:** Monitor applications and infrastructure continuously
- 🤝 **Collaboration:** Foster collaboration between development, operations, and security teams

### 🔹 Subtask 1.2: Security Integration Points

In a DevSecOps pipeline, security is integrated at multiple stages:

| Stage | Security Activities |
|---|---|
| 💻 Code Development | Static code analysis, secure coding practices |
| 🏗️ Build Phase | Dependency scanning, container security |
| 🧪 Testing Phase | Dynamic application security testing (DAST) |
| 🚀 Deployment | Infrastructure security, configuration management |
| 🏭 Runtime | Continuous monitoring, incident response |

---

## 🔧 Task 2: Setting Up Jenkins for DevSecOps

![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=flat-square&logo=jenkins&logoColor=white)

### 🔹 Subtask 2.1: Installing Jenkins

① Update system packages:

```bash
# 🔄 Refresh package lists
sudo apt update
```

② Install Java 11 (required for Jenkins):

```bash
# ☕ Install the JDK
sudo apt install openjdk-11-jdk -y
```

③ Add the Jenkins repository key:

```bash
# 🔑 Trust the Jenkins signing key
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
```

④ Add the Jenkins repository:

```bash
# 📦 Register the Jenkins apt repository
sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
```

⑤ Update the package list:

```bash
# 🔄 Refresh again with the new repo
sudo apt update
```

⑥ Install Jenkins:

```bash
# 🚀 Install the Jenkins package
sudo apt install jenkins -y
```

⑦ Start the Jenkins service:

```bash
# ▶️ Start and enable Jenkins on boot
sudo systemctl start jenkins
sudo systemctl enable jenkins
```

⑧ Check Jenkins status:

```bash
# ✅ Confirm Jenkins is active
sudo systemctl status jenkins
```

### 🔹 Subtask 2.2: Initial Jenkins Configuration

① Get the initial admin password:

```bash
# 🔑 Retrieve the auto-generated admin password
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

② Open your web browser and navigate to:

```
http://your-server-ip:8080
# TODO: Replace 'your-server-ip' with your actual cloud machine IP address
```

③ Enter the initial admin password

④ Click **Install suggested plugins**

⑤ Create your first admin user

⑥ Configure the Jenkins URL (use your server IP)

### 🔹 Subtask 2.3: Installing Required Jenkins Plugins

Navigate to **Manage Jenkins → Manage Plugins → Available** and install:

- 🔍 SonarQube Scanner
- 📦 OWASP Dependency-Check Plugin
- 🔄 Pipeline
- 🌿 Git Plugin
- 📐 Maven Integration Plugin
- 🏗️ Build Pipeline Plugin

---

## 🔍 Task 3: Setting Up SonarQube for Code Quality and Security Analysis

![SonarQube](https://img.shields.io/badge/SonarQube-4E9BCD?style=flat-square&logo=sonarqube&logoColor=white)
![Docker](https://img.shields.io/badge/Docker_Compose-2496ED?style=flat-square&logo=docker&logoColor=white)

### 🔹 Subtask 3.1: Installing SonarQube with Docker

① Create a directory for SonarQube:

```bash
# 📁 Create and enter the SonarQube working directory
mkdir ~/sonarqube
cd ~/sonarqube
```

② Create the `docker-compose.yml` file:

```bash
# 🐳 Define the SonarQube service
cat > docker-compose.yml << 'EOF'
version: '3.7'

services:
  sonarqube:
    image: sonarqube:9.9-community
    container_name: sonarqube
    ports:
      - "9000:9000"                 # 🌐 Web UI / API
    environment:
      - SONAR_ES_BOOTSTRAP_CHECKS_DISABLE=true   # ⚙️ Relaxes ES bootstrap checks for lab use
    volumes:
      - sonarqube_data:/opt/sonarqube/data
      - sonarqube_extensions:/opt/sonarqube/extensions
      - sonarqube_logs:/opt/sonarqube/logs

volumes:
  sonarqube_data:
  sonarqube_extensions:
  sonarqube_logs:
EOF
```

③ Start SonarQube:

```bash
# 🚀 Launch SonarQube in detached mode
docker-compose up -d
```

④ Check if SonarQube is running:

```bash
# ✅ Confirm container status
docker-compose ps
```

### 🔹 Subtask 3.2: Configuring SonarQube

① Wait for SonarQube to start (it may take 2-3 minutes)

② Access SonarQube at:

```
http://your-server-ip:9000
```

③ Login with default credentials:

```
Username: admin
Password: admin
```

④ Change the default password when prompted

```
# TODO: Set a strong, unique password outside of a lab environment
```

⑤ Generate a token for Jenkins integration:

- ⚙️ Go to **User → My Account → Security**
- 🔑 Generate a new token named `jenkins-integration`
- 💾 Save this token — you'll need it for Jenkins configuration

### 🔹 Subtask 3.3: Integrating SonarQube with Jenkins

① In Jenkins, go to **Manage Jenkins → Configure System**

② Find the **SonarQube servers** section

③ Add the SonarQube server:

```
Name: SonarQube
Server URL: http://localhost:9000
Server authentication token: (add the token you generated)
```

---

## 📦 Task 4: Setting Up OWASP Dependency Check

![OWASP Dependency Check](https://img.shields.io/badge/OWASP_Dependency--Check-000000?style=flat-square&logo=owasp&logoColor=white)

### 🔹 Subtask 4.1: Installing OWASP Dependency Check

① Create a directory for OWASP tools:

```bash
# 📁 Create and enter the OWASP tools directory
mkdir ~/owasp-tools
cd ~/owasp-tools
```

② Download OWASP Dependency Check:

```bash
# ⬇️ Fetch the release archive
wget https://github.com/jeremylong/DependencyCheck/releases/download/v8.4.0/dependency-check-8.4.0-release.zip
```

③ Extract the archive:

```bash
# 📦 Unzip the tool
unzip dependency-check-8.4.0-release.zip
```

④ Make the script executable:

```bash
# 🔓 Grant execute permission
chmod +x dependency-check/bin/dependency-check.sh
```

⑤ Add to PATH (optional):

```bash
# 🛣️ Make the tool available anywhere in the shell
echo 'export PATH=$PATH:~/owasp-tools/dependency-check/bin' >> ~/.bashrc
source ~/.bashrc
```

### 🔹 Subtask 4.2: Configuring OWASP Dependency Check in Jenkins

① Go to **Manage Jenkins → Global Tool Configuration**

② Find **OWASP Dependency-Check installations**

③ Add installation:

```
Name: OWASP-Dependency-Check
Install automatically: Uncheck
DEPENDENCY_CHECK_HOME: /home/ubuntu/owasp-tools/dependency-check
```

---

## 🕷️ Task 5: Setting Up OWASP ZAP for Dynamic Security Testing

![OWASP ZAP](https://img.shields.io/badge/OWASP_ZAP-000000?style=flat-square&logo=owasp&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)

### 🔹 Subtask 5.1: Installing OWASP ZAP

① Install ZAP using Docker:

```bash
# 🐳 Pull the ZAP baseline scan image
docker pull owasp/zap2docker-stable
```

② Create a directory for ZAP reports:

```bash
# 📁 Create the reports directory
mkdir ~/zap-reports
```

③ Test the ZAP installation:

```bash
# 🧪 Confirm the baseline scan script works
docker run -t owasp/zap2docker-stable zap-baseline.py --help
```

### 🔹 Subtask 5.2: Creating a ZAP Scanning Script

① Create the ZAP scanning script:

```bash
# 📝 Reusable baseline-scan wrapper script
cat > ~/owasp-tools/zap-scan.sh << 'EOF'
#!/bin/bash

# 🕷️ ZAP Baseline Scan Script
TARGET_URL=$1
REPORT_DIR=$2

if [ -z "$TARGET_URL" ] || [ -z "$REPORT_DIR" ]; then
    echo "Usage: $0 <target_url> <report_directory>"
    exit 1
fi

echo "Starting ZAP baseline scan for: $TARGET_URL"

# 🚀 Run ZAP baseline scan
docker run -v $REPORT_DIR:/zap/wrk/:rw \
    -t owasp/zap2docker-stable \
    zap-baseline.py \
    -t $TARGET_URL \
    -J zap-report.json \
    -H zap-report.html \
    -r zap-report.md

echo "ZAP scan completed. Reports saved to: $REPORT_DIR"
EOF
```

② Make the script executable:

```bash
# 🔓 Grant execute permission
chmod +x ~/owasp-tools/zap-scan.sh
```

---

## 🧪 Task 6: Creating a Sample Application for Testing

![Java](https://img.shields.io/badge/Java_11-007396?style=flat-square&logo=openjdk&logoColor=white)
![Maven](https://img.shields.io/badge/Maven-C71A36?style=flat-square&logo=apachemaven&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)

### 🔹 Subtask 6.1: Setting Up a Vulnerable Web Application

① Clone a sample vulnerable application:

```bash
# 🌿 Clone WebGoat, OWASP's intentionally-vulnerable training app
cd ~
git clone https://github.com/WebGoat/WebGoat.git
cd WebGoat
```

② Build the application using Maven:

```bash
# 🏗️ Compile and package (tests skipped for speed)
mvn clean install -DskipTests
```

③ Create a simple Dockerfile for the application:

```bash
# 🐳 Containerize WebGoat
cat > Dockerfile << 'EOF'
FROM openjdk:11-jre-slim

COPY webgoat-server/target/webgoat-server-*.jar app.jar

EXPOSE 8080

ENTRYPOINT ["java", "-jar", "/app.jar"]
EOF
```

### 🔹 Subtask 6.2: Creating a Sample Java Project for Analysis

① Create a simple Java project structure:

```bash
# 📁 Create the sample project directory tree
mkdir -p ~/sample-project/src/main/java/com/example
cd ~/sample-project
```

② Create `pom.xml` with some vulnerable dependencies:

```bash
# 📝 Maven project descriptor — intentionally pinned to older, vulnerable versions
cat > pom.xml << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>devsecops-demo</artifactId>
    <version>1.0.0</version>
    <packaging>jar</packaging>

    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
        <sonar.projectKey>devsecops-demo</sonar.projectKey>
        <sonar.projectName>DevSecOps Demo</sonar.projectName>
    </properties>

    <dependencies>
        <!-- 🚨 Intentionally using older versions with known vulnerabilities -->
        <dependency>
            <groupId>org.apache.commons</groupId>
            <artifactId>commons-collections4</artifactId>
            <version>4.0</version>
        </dependency>

        <dependency>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-databind</artifactId>
            <version>2.9.8</version>
        </dependency>

        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.13.1</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.sonarsource.scanner.maven</groupId>
                <artifactId>sonar-maven-plugin</artifactId>
                <version>3.9.1.2184</version>
            </plugin>
        </plugins>
    </build>
</project>
EOF
```

③ Create a sample Java class with security issues:

```bash
# 📝 Vulnerable demo class for the scanners to catch
cat > src/main/java/com/example/VulnerableApp.java << 'EOF'
package com.example;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Scanner;

public class VulnerableApp {

    // 🚨 Hard-coded credentials (security vulnerability)
    private static final String DB_URL = "jdbc:mysql://localhost:3306/testdb";
    private static final String USERNAME = "admin";
    private static final String PASSWORD = "password123";

    public static void main(String[] args) {
        VulnerableApp app = new VulnerableApp();
        app.demonstrateVulnerabilities();
    }

    public void demonstrateVulnerabilities() {
        // 🚨 SQL Injection vulnerability
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter user ID: ");
        String userId = scanner.nextLine();

        try {
            Connection conn = DriverManager.getConnection(DB_URL, USERNAME, PASSWORD);
            Statement stmt = conn.createStatement();

            // 🚨 Vulnerable SQL query - direct string concatenation
            String query = "SELECT * FROM users WHERE id = '" + userId + "'";
            ResultSet rs = stmt.executeQuery(query);

            while (rs.next()) {
                System.out.println("User: " + rs.getString("username"));
            }

            conn.close();
        } catch (Exception e) {
            e.printStackTrace();
        }

        scanner.close();
    }

    // 🚨 Method with potential null pointer exception
    public String processUserInput(String input) {
        return input.toUpperCase(); // No null check
    }

    // 👃 Unused private method (code smell)
    private void unusedMethod() {
        System.out.println("This method is never called");
    }
}
EOF
```

④ Initialize a Git repository:

```bash
# 🌿 Version-control the sample project
git init
git add .
git commit -m "Initial commit with vulnerable code"
```

---

## 🔄 Task 7: Creating a DevSecOps Pipeline

![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=flat-square&logo=jenkins&logoColor=white)
![Maven](https://img.shields.io/badge/Maven-C71A36?style=flat-square&logo=apachemaven&logoColor=white)

### 🔹 Subtask 7.1: Creating a Jenkins Pipeline Script

① Create the `Jenkinsfile` in the sample project:

```bash
# 📁 Move into the sample project
cd ~/sample-project
```

```groovy
// 🔄 Full DevSecOps pipeline: build → test → SAST → gate → dependency check → package → deploy → DAST
cat > Jenkinsfile << 'EOF'
pipeline {
    agent any

    tools {
        maven 'Maven'
        jdk 'Java-11'
    }

    environment {
        SONAR_TOKEN = credentials('sonar-token')
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building the application...'
                sh 'mvn clean compile'
            }
        }

        stage('Unit Tests') {
            steps {
                echo 'Running unit tests...'
                sh 'mvn test'
            }
            post {
                always {
                    junit 'target/surefire-reports/*.xml'
                }
            }
        }

        stage('Static Code Analysis') {
            steps {
                echo 'Running SonarQube analysis...'
                withSonarQubeEnv('SonarQube') {
                    sh 'mvn sonar:sonar'
                }
            }
        }

        stage('Quality Gate') {
            steps {
                echo 'Checking SonarQube Quality Gate...'
                timeout(time: 1, unit: 'HOURS') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        stage('Dependency Check') {
            steps {
                echo 'Running OWASP Dependency Check...'
                dependencyCheck additionalArguments: '''
                    -o "./dependency-check-report"
                    -s "."
                    -f "ALL"
                    --prettyPrint
                ''', odcInstallation: 'OWASP-Dependency-Check'

                dependencyCheckPublisher pattern: 'dependency-check-report/dependency-check-report.xml'
            }
        }

        stage('Package') {
            steps {
                echo 'Packaging the application...'
                sh 'mvn package -DskipTests'
            }
        }

        stage('Deploy to Test Environment') {
            steps {
                echo 'Deploying to test environment...'
                // Simulate deployment
                sh 'echo "Application deployed to test environment"'
            }
        }

        stage('Dynamic Security Testing') {
            steps {
                echo 'Running OWASP ZAP security scan...'
                script {
                    // Run ZAP scan against deployed application
                    sh '''
                        mkdir -p zap-reports
                        docker run -v $(pwd)/zap-reports:/zap/wrk/:rw \
                            -t owasp/zap2docker-stable \
                            zap-baseline.py \
                            -t http://example.com \
                            -J zap-report.json \
                            -H zap-report.html \
                            -r zap-report.md || true
                    '''
                }
            }
            post {
                always {
                    publishHTML([
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'zap-reports',
                        reportFiles: 'zap-report.html',
                        reportName: 'ZAP Security Report'
                    ])
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed!'
            cleanWs()
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
EOF
```

> ⚠️ **Note:** Replace `http://example.com` in the DAST stage with your actual deployed test-environment URL.

② Commit the Jenkinsfile:

```bash
# 🌿 Version-control the pipeline definition
git add Jenkinsfile
git commit -m "Add DevSecOps pipeline configuration"
```

### 🔹 Subtask 7.2: Setting Up the Jenkins Job

① In Jenkins, click **New Item**

② Enter job name: `DevSecOps-Pipeline`

③ Select **Pipeline** and click **OK**

④ In the configuration:

```
Pipeline Definition: Pipeline script from SCM
SCM: Git
Repository URL: /home/ubuntu/sample-project (local path)
Branch: */master
Script Path: Jenkinsfile
```

⑤ Click **Save**

---

## 🚨 Task 8: Running Security Scans and Analysis

![OWASP Dependency Check](https://img.shields.io/badge/OWASP_Dependency--Check-000000?style=flat-square&logo=owasp&logoColor=white)
![SonarQube](https://img.shields.io/badge/SonarQube-4E9BCD?style=flat-square&logo=sonarqube&logoColor=white)
![OWASP ZAP](https://img.shields.io/badge/OWASP_ZAP-000000?style=flat-square&logo=owasp&logoColor=white)

### 🔹 Subtask 8.1: Manual OWASP Dependency Check

① Run dependency check manually on the sample project:

```bash
# 📁 Move into the sample project
cd ~/sample-project

# 🔍 Scan all dependencies and generate a full report
~/owasp-tools/dependency-check/bin/dependency-check.sh \
    --project "DevSecOps Demo" \
    --scan . \
    --format ALL \
    --out ./dependency-check-report
```

② View the HTML report:

```bash
# 📄 Print the report location
echo "Dependency check report generated at: $(pwd)/dependency-check-report/dependency-check-report.html"
```

### 🔹 Subtask 8.2: Manual SonarQube Analysis

① Run SonarQube analysis manually:

```bash
# 📁 Move into the sample project
cd ~/sample-project

# 🔍 Trigger a Maven-driven SonarQube scan
mvn sonar:sonar \
    -Dsonar.projectKey=devsecops-demo \
    -Dsonar.host.url=http://localhost:9000 \
    -Dsonar.login=your-sonar-token
# TODO: Replace 'your-sonar-token' with the token generated in Subtask 3.2
```

### 🔹 Subtask 8.3: Manual ZAP Security Scan

① Create a simple web server for testing:

```bash
# 📁 Move into the sample project
cd ~/sample-project

# 🌐 Start a simple HTTP server
python3 -m http.server 8000 &
SERVER_PID=$!

# ⏳ Wait for server to start
sleep 2
```

② Run the ZAP scan:

```bash
# 🕷️ Run a baseline scan against the local test server
mkdir -p zap-reports
docker run -v $(pwd)/zap-reports:/zap/wrk/:rw \
    -t owasp/zap2docker-stable \
    zap-baseline.py \
    -t http://host.docker.internal:8000 \
    -J zap-report.json \
    -H zap-report.html \
    -r zap-report.md
```

③ Stop the test server:

```bash
# 🛑 Kill the background HTTP server
kill $SERVER_PID

echo "ZAP scan completed. Report available at: $(pwd)/zap-reports/zap-report.html"
```

---

## 📊 Task 9: Analyzing Security Reports and Remediation

### 🔹 Subtask 9.1: Understanding SonarQube Security Reports

① Access SonarQube at `http://your-server-ip:9000`

② Navigate to your project: `devsecops-demo`

③ Review the **Security** tab to see:

- 🔥 **Security Hotspots:** Potential security vulnerabilities
- 🚨 **Vulnerabilities:** Confirmed security issues
- 📊 **Security Rating:** Overall security score

**Common Issues Found:**

- 🔑 Hard-coded credentials
- 💉 SQL injection vulnerabilities
- ⚠️ Potential null pointer exceptions

### 🔹 Subtask 9.2: Understanding OWASP Dependency Check Reports

Open the dependency check HTML report and review:

- 📋 **Summary:** Overview of vulnerabilities found
- 📦 **Dependencies:** List of all dependencies analyzed
- 🚨 **Vulnerabilities:** Detailed information about each vulnerability including:
  - 🆔 CVE numbers
  - 📊 CVSS scores
  - 🚦 Severity levels
  - 🩹 Remediation suggestions

### 🔹 Subtask 9.3: Remediation Examples

① Create a secure version of the vulnerable code:

```bash
# 📝 Hardened class fixing the issues found by SonarQube
cat > src/main/java/com/example/SecureApp.java << 'EOF'
package com.example;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.Properties;
import java.util.Scanner;

public class SecureApp {

    // ✅ Use configuration file / env vars instead of hard-coded credentials
    private Properties config;

    public SecureApp() {
        loadConfiguration();
    }

    private void loadConfiguration() {
        config = new Properties();
        // In a real application, load from secure configuration
        config.setProperty("db.url", "jdbc:mysql://localhost:3306/testdb");
        config.setProperty("db.username", System.getenv("DB_USERNAME"));
        config.setProperty("db.password", System.getenv("DB_PASSWORD"));
    }

    public static void main(String[] args) {
        SecureApp app = new SecureApp();
        app.demonstrateSecurePractices();
    }

    public void demonstrateSecurePractices() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter user ID: ");
        String userId = scanner.nextLine();

        try {
            Connection conn = DriverManager.getConnection(
                config.getProperty("db.url"),
                config.getProperty("db.username"),
                config.getProperty("db.password")
            );

            // ✅ Use prepared statement to prevent SQL injection
            String query = "SELECT * FROM users WHERE id = ?";
            PreparedStatement pstmt = conn.prepareStatement(query);
            pstmt.setString(1, userId);

            ResultSet rs = pstmt.executeQuery();

            while (rs.next()) {
                System.out.println("User: " + rs.getString("username"));
            }

            conn.close();
        } catch (Exception e) {
            // ✅ Log error securely without exposing sensitive information
            System.err.println("Database error occurred");
        }

        scanner.close();
    }

    // ✅ Method with proper null checking
    public String processUserInput(String input) {
        if (input == null) {
            throw new IllegalArgumentException("Input cannot be null");
        }
        return input.toUpperCase();
    }
}
EOF
```

② Update `pom.xml` to use secure dependency versions:

```bash
# 📝 Bump vulnerable dependencies to patched versions
cat > pom.xml << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>devsecops-demo</artifactId>
    <version>1.0.0</version>
    <packaging>jar</packaging>

    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
        <sonar.projectKey>devsecops-demo</sonar.projectKey>
        <sonar.projectName>DevSecOps Demo</sonar.projectName>
    </properties>

    <dependencies>
        <!-- ✅ Updated to secure versions -->
        <dependency>
            <groupId>org.apache.commons</groupId>
            <artifactId>commons-collections4</artifactId>
            <version>4.4</version>
        </dependency>

        <dependency>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-databind</artifactId>
            <version>2.15.2</version>
        </dependency>

        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.13.2</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.sonarsource.scanner.maven</groupId>
                <artifactId>sonar-maven-plugin</artifactId>
                <version>3.9.1.2184</version>
            </plugin>
        </plugins>
    </build>
</project>
EOF
```

③ Commit the secure version:

```bash
# 🌿 Commit the remediated code
git add .
git commit -m "Fix security vulnerabilities and update dependencies"
```

---

## 🚦 Task 10: Implementing Security Gates and Policies

![SonarQube](https://img.shields.io/badge/SonarQube-4E9BCD?style=flat-square&logo=sonarqube&logoColor=white)

### 🔹 Subtask 10.1: Configuring SonarQube Quality Gates

① In SonarQube, go to **Quality Gates**

② Create a new quality gate: `DevSecOps-Security-Gate`

③ Add conditions:

| Metric | Condition |
|---|---|
| 🛡️ Security Rating | is worse than A |
| 🔧 Reliability Rating | is worse than A |
| 📈 Coverage | is less than 80% |
| 🪞 Duplicated Lines (%) | is greater than 3% |

### 🔹 Subtask 10.2: Creating Security Policy Scripts

① Create a security policy checker script:

```bash
# 📝 Automated pass/fail gate based on scan results
cat > ~/owasp-tools/security-gate.sh << 'EOF'
#!/bin/bash

# 🚦 Security Gate Script
# This script checks if the build meets security requirements

DEPENDENCY_CHECK_REPORT="dependency-check-report/dependency-check-report.json"
ZAP_REPORT="zap-reports/zap-report.json"

echo "=== DevSecOps Security Gate ==="

# 📦 Check if dependency check found high/critical vulnerabilities
if [ -f "$DEPENDENCY_CHECK_REPORT" ]; then
    HIGH_VULNS=$(jq '.dependencies[].vulnerabilities[]? | select(.severity == "HIGH" or .severity == "CRITICAL")' "$DEPENDENCY_CHECK_REPORT" | wc -l)

    if [ "$HIGH_VULNS" -gt 0 ]; then
        echo "❌ FAIL: Found $HIGH_VULNS high/critical vulnerabilities in dependencies"
        exit 1
    else
        echo "✅ PASS: No high/critical vulnerabilities found in dependencies"
    fi
else
    echo "⚠️  WARNING: Dependency check report not found"
fi

# 🕷️ Check ZAP scan results
if [ -f "$ZAP_REPORT" ]; then
    HIGH_ALERTS=$(jq '.site[].alerts[]? | select(.riskdesc | contains("High"))' "$ZAP_REPORT" | wc -l)

    if [ "$HIGH_ALERTS" -gt 0 ]; then
        echo "❌ FAIL: Found $HIGH_ALERTS high-risk security alerts"
        exit 1
    else
        echo "✅ PASS: No high-risk security alerts found"
    fi
else
    echo "⚠️  WARNING: ZAP scan report not found"
fi

echo "=== Security Gate: PASSED ==="
exit 0
EOF
```

② Make the script executable:

```bash
# 🔓 Grant execute permission
chmod +x ~/owasp-tools/security-gate.sh
```

---

## 📈 Task 11: Monitoring and Continuous Improvement

### 🔹 Subtask 11.1: Setting Up a Security Metrics Dashboard

① Create a metrics collection script:

```bash
# 📝 Pulls SonarQube ratings into a timestamped JSON snapshot
cat > ~/owasp-tools/collect-metrics.sh << 'EOF'
#!/bin/bash

# 📊 Security Metrics Collection Script
METRICS_FILE="security-metrics.json"
DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

echo "Collecting security metrics..."

# 🗂️ Initialize metrics JSON
cat > "$METRICS_FILE" << EOL
{
  "timestamp": "$DATE",
  "sonarqube": {},
  "dependency_check": {},
  "zap": {}
}
EOL

# 🔍 Collect SonarQube metrics (if available)
if command -v curl &> /dev/null; then
    SONAR_METRICS=$(curl -s "http://localhost:9000/api/measures/component?component=devsecops-demo&metricKeys=security_rating,reliability_rating,sqale_rating,coverage" || echo "{}")
    echo "$SONAR_METRICS" | jq '.component.measures' > temp_sonar.json 2>/dev/null || echo "[]" > temp_sonar.json
    jq --argjson sonar "$(cat temp_sonar.json)" '.sonarqube = $sonar' "$METRICS_FILE" > temp_metrics.json && mv temp_metrics.json "$METRICS_FILE"
    rm -f temp_sonar.json
fi

echo "Security metrics collected in $METRICS_FILE"
EOF
```

② Make the script executable:

```bash
# 🔓 Grant execute permission
chmod +x ~/owasp-tools/collect-metrics.sh
```

### 🔹 Subtask 11.2: Creating a Security Incident Response Plan

① Create the incident response template:

```bash
# 📝 Save the response plan as a reference document
cat > ~/security-incident-response.md << 'EOF'
# Security Incident Response Plan

## Immediate Actions (0-1 hour)
1. **Identify and Isolate**
   - Determine the scope of the security issue
   - Isolate affected systems if necessary
   - Document initial findings

2. **Assess Impact**
   - Evaluate potential data exposure
   - Determine business impact
   - Identify affected users/systems

3. **Notify Stakeholders**
   - Security team
   - Development team
   - Management (if high severity)

## Short-term Actions (1-24 hours)
1. **Contain the Issue**
   - Apply temporary fixes
   - Block malicious traffic
   - Revoke compromised credentials

2. **Investigate**
   - Analyze logs and security reports
   - Determine root cause
   - Document timeline of events

3. **Communicate**
   - Update stakeholders
   - Prepare customer communication (if needed)

## Long-term Actions (1-7 days)
1. **Remediate**
   - Implement permanent fixes
   - Update security policies
   - Enhance monitoring

2. **Review and Improve**
   - Conduct post-incident review
   - Update security procedures
   - Provide additional training

## Prevention Measures
- Regular security assessments
- Automated security testing
- Security awareness training
- Incident response drills
EOF
```

---

## ▶️ Task 12: Running the Complete DevSecOps Pipeline

![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=flat-square&logo=jenkins&logoColor=white)

### 🔹 Subtask 12.1: Execute the Jenkins Pipeline

① Go to the Jenkins dashboard

② Click on your `DevSecOps-Pipeline` job

③ Click **Build Now**

④ Monitor the pipeline execution in **Console Output**

### 🔹 Subtask 12.2: Review Pipeline Results

After the pipeline completes, review:

- 🚦 **Build Status:** Check if all stages passed
- 🔍 **SonarQube Report:** Review code quality and security issues
- 📦 **Dependency Check Report:** Check for vulnerable dependencies
- 🕷️ **ZAP Security Report:** Review dynamic security testing results

### 🔹 Subtask 12.3: Troubleshooting Common Issues

<details>
<summary>🔴 Issue: SonarQube Connection Failed</summary>

**Solution:**

```bash
# 🔍 Check SonarQube status
docker-compose -f ~/sonarqube/docker-compose.yml ps

# ♻️ Restart SonarQube if needed
docker-compose -f ~/sonarqube/docker-compose.yml restart
```

</details>

---

## 🗺️ MITRE ATT&CK Mapping

This lab's tool stack — SonarQube (SAST), OWASP Dependency-Check (SCA), and OWASP ZAP (DAST) — each target a distinct class of adversary technique. The security gate in Task 10 is what turns detection into an enforced control.

| Vulnerability Class | Detected By | ATT&CK Technique | Mitigated By |
|---|---|---|---|
| 💉 SQL Injection (string concatenation) | SonarQube (SAST) | [T1190 – Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/) | Prepared statements (see `SecureApp.java`) |
| 🔑 Hardcoded Credentials | SonarQube (SAST) | [T1552.001 – Unsecured Credentials: Credentials In Files](https://attack.mitre.org/techniques/T1552/001/) | Environment-variable based config (see `SecureApp.java`) |
| 📦 Vulnerable/Outdated Dependencies (`commons-collections4` 4.0, `jackson-databind` 2.9.8) | OWASP Dependency-Check | [T1195.001 – Supply Chain Compromise: Compromise Software Dependencies and Development Tools](https://attack.mitre.org/techniques/T1195/001/) | Dependency version upgrades + `security-gate.sh` blocking HIGH/CRITICAL CVEs |
| 🕷️ Runtime Web Vulnerabilities (injection, misconfiguration, exposure) | OWASP ZAP (DAST) | [T1190 – Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/) | Gated `Dynamic Security Testing` pipeline stage |

> 🎓 This mapping is framed defensively: it shows which adversary techniques the pipeline's SAST, SCA, and DAST gates are positioned to catch **before** vulnerable code or dependencies reach production, not an offensive playbook.

---

## 🎓 Conclusion

Congratulations! 🎉 You have completed the Embracing DevSecOps lab and built a full security-integrated CI/CD pipeline from the ground up.

### 🏆 Key Accomplishments

- 🧠 Understood the core principles of DevSecOps and its importance in modern software development
- 🔧 Set up and configured Jenkins for continuous integration with security integration
- 🔍 Installed and configured SonarQube for static code analysis and security vulnerability detection
- 📦 Implemented OWASP Dependency Check to identify vulnerable dependencies in projects
- 🕷️ Configured OWASP ZAP for automated dynamic security testing
- 🔄 Created a complete DevSecOps pipeline that integrates security at every stage of development
- 📊 Analyzed security reports and remediated common vulnerabilities
- 🚦 Implemented security gates in CI/CD pipelines to prevent insecure code deployment

### 💡 Why This Matters

Layering SAST, SCA, and DAST into a single gated pipeline — rather than running any one of them in isolation — is what makes a DevSecOps program effective. Each tool covers a blind spot the others miss: source-code flaws, vulnerable third-party dependencies, and runtime behavior of the deployed application.

### 🌍 Real-World Applications

The Jenkins + SonarQube + OWASP Dependency-Check + OWASP ZAP toolchain you configured mirrors what enterprise security and platform teams run in production, and the security-gate and incident-response patterns you built are directly reusable in real engineering organizations.

### 🚀 Next Steps

- 📦 Extend dependency scanning to container images
- 🏗️ Add Infrastructure as Code (IaC) security scanning
- 📈 Build out the metrics dashboard into a persistent monitoring solution
- 🎯 Run tabletop exercises against your incident response plan

You now have hands-on experience building a complete, gated DevSecOps pipeline — a foundation you can extend with additional tools and policies as your security program matures. 💪

---

<div align="center">

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Training-blueviolet?style=for-the-badge)

</div>
