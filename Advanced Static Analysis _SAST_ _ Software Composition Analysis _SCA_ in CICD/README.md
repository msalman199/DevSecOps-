<div align="center">

# 🔎 Advanced Static Analysis (SAST) & Software Composition Analysis (SCA) in CI/CD

### Catching Vulnerable Code and Vulnerable Dependencies Before They Ship

![DevSecOps](https://img.shields.io/badge/DevSecOps-FF4B4B?style=for-the-badge&logo=OWASP&logoColor=white)
![Semgrep](https://img.shields.io/badge/Semgrep-0B6E4F?style=for-the-badge&logo=semgrep&logoColor=white)
![OWASP](https://img.shields.io/badge/OWASP%20Dependency--Check-000000?style=for-the-badge&logo=owasp&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)
![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Maven](https://img.shields.io/badge/Maven-C71A36?style=for-the-badge&logo=apachemaven&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

</div>

---

## 📚 Table of Contents

- [🎯 Lab Objectives](#-lab-objectives)
- [📋 Prerequisites](#-prerequisites)
- [🖥️ Lab Environment](#️-lab-environment)
- [🧰 Task 1: Environment Preparation and Tool Installation](#-task-1-environment-preparation-and-tool-installation)
- [☕ Task 2: Create Sample Application for Testing](#-task-2-create-sample-application-for-testing)
- [⚙️ Task 3: Configure Jenkins CI/CD Pipeline](#️-task-3-configure-jenkins-cicd-pipeline)
- [🧪 Task 4: Execute and Analyze Security Scans](#-task-4-execute-and-analyze-security-scans)
- [📄 Task 5: Configure Advanced Reporting and Notifications](#-task-5-configure-advanced-reporting-and-notifications)
- [🗺️ MITRE ATT&CK Mapping](#️-mitre-attck-mapping)
- [🧩 Key Concepts Summary](#-key-concepts-summary)
- [🏁 Conclusion](#-conclusion)

---

## 🎯 Lab Objectives

| # | Objective |
|---|-----------|
| 1 | Understand the fundamentals of Static Application Security Testing (SAST) and Software Composition Analysis (SCA) |
| 2 | Integrate Semgrep (SAST tool) into a CI/CD pipeline for automated code security scanning |
| 3 | Implement OWASP Dependency Check (SCA tool) to identify vulnerable dependencies |
| 4 | Configure automated report generation and email notifications for security findings |
| 5 | Build a complete CI/CD pipeline using Jenkins with security scanning capabilities |
| 6 | Analyze and interpret security scan results to improve application security posture |

## 📋 Prerequisites

| Skill Area | Requirement |
|---|---|
| 🌿 Git | Basic understanding of Git version control |
| 🐧 Linux | Familiarity with command line operations |
| ⚙️ CI/CD | Basic knowledge of CI/CD concepts |
| 🔁 SDLC | Understanding of the software development lifecycle |
| 🤖 Jenkins | Basic familiarity with Jenkins or similar CI/CD tools |
| 📧 Email | Knowledge of email configuration concepts |

## 🖥️ Lab Environment

> ☁️ **Ready-to-Use Cloud Machine** — Al Nafi provides a pre-configured Linux-based cloud machine. Click **Start Lab** — no VM build or manual installs required.

| Component | Details |
|---|---|
| 🖥️ OS | Ubuntu 20.04 LTS |
| 🤖 CI/CD | Jenkins CI/CD server |
| 🌿 VCS | Git version control |
| ☕ Runtime | Java Development Kit (JDK) |
| 🐍 Scripting | Python 3 with pip |
| 🐳 Containers | Docker (for containerized scanning) |
| 📧 Mail | Email utilities (mailutils) |

---

## 🧰 Task 1: Environment Preparation and Tool Installation

### 🔍 Subtask 1.1: Verify System Requirements

```bash
# 🖥️ Check system information
uname -a
cat /etc/os-release

# ☕ Verify Java installation (required for Jenkins)
java -version

# 🤖 Check if Jenkins is running
sudo systemctl status jenkins

# 🌿 Verify Git installation
git --version

# 🐍 Check Python installation
python3 --version
pip3 --version
```

### 🛡️ Subtask 1.2: Install Semgrep (SAST Tool)

> 💡 Semgrep is a powerful static analysis tool that finds bugs, security issues, and anti-patterns in your code.

```bash
# 📦 Install Semgrep using pip
pip3 install semgrep

# 🔍 Verify Semgrep installation
semgrep --version

# 🧪 Test Semgrep with a simple scan
semgrep --config=auto --dry-run
```

### 📦 Subtask 1.3: Install OWASP Dependency Check (SCA Tool)

> 💡 OWASP Dependency Check identifies known vulnerabilities in project dependencies.

```bash
# 📁 Create directory for OWASP Dependency Check
sudo mkdir -p /opt/dependency-check
cd /opt/dependency-check

# ⬇️ Download OWASP Dependency Check
sudo wget https://github.com/jeremylong/DependencyCheck/releases/download/v8.4.0/dependency-check-8.4.0-release.zip

# 📂 Extract the downloaded file
sudo unzip dependency-check-8.4.0-release.zip

# 🔗 Create symbolic link for easy access
sudo ln -s /opt/dependency-check/dependency-check/bin/dependency-check.sh /usr/local/bin/dependency-check

# ✅ Verify installation
dependency-check --version
```

### 📧 Subtask 1.4: Configure Email Notifications

```bash
# 📦 Install mail utilities
sudo apt update
sudo apt install -y mailutils ssmtp

# ⚙️ Configure SSMTP for Gmail (example configuration)
sudo tee /etc/ssmtp/ssmtp.conf > /dev/null <<EOF
root=your-email@gmail.com
mailhub=smtp.gmail.com:587
rewriteDomain=gmail.com
AuthUser=your-email@gmail.com
AuthPass=your-app-password
FromLineOverride=YES
UseSTARTTLS=YES
EOF

# 🔐 Set proper permissions
sudo chmod 640 /etc/ssmtp/ssmtp.conf
```

> ⚠️ **Note:** Replace `your-email@gmail.com` and `your-app-password` with actual credentials. For Gmail, use an **App Password** instead of your regular password.

---

## ☕ Task 2: Create Sample Application for Testing

### 📁 Subtask 2.1: Set Up Sample Java Application

```bash
# 📁 Create project directory
mkdir -p ~/security-lab/sample-app
cd ~/security-lab/sample-app

# 🌿 Initialize Git repository
git init

# 🗂️ Create Maven project structure
mkdir -p src/main/java/com/example/app
mkdir -p src/test/java
```

### ⚠️ Subtask 2.2: Create Vulnerable Java Code

> 💡 A sample Java application with intentional security issues so the SAST tool has real findings to surface.

<details>
<summary>☕ <strong>src/main/java/com/example/app/VulnerableApp.java</strong> — click to expand</summary>

```java
package com.example.app;

import java.sql.*;
import java.io.*;
import javax.servlet.http.*;
import java.security.MessageDigest;

public class VulnerableApp {

    // 🚨 SQL Injection vulnerability
    public User getUserById(String userId, Connection conn) throws SQLException {
        String query = "SELECT * FROM users WHERE id = '" + userId + "'";
        Statement stmt = conn.createStatement();
        ResultSet rs = stmt.executeQuery(query);

        if (rs.next()) {
            return new User(rs.getString("username"), rs.getString("email"));
        }
        return null;
    }

    // 🚨 Weak cryptography (MD5)
    public String hashPassword(String password) {
        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] hash = md.digest(password.getBytes());
            return new String(hash);
        } catch (Exception e) {
            return password;
        }
    }

    // 🚨 Path traversal vulnerability
    public String readFile(String filename) {
        try {
            BufferedReader reader = new BufferedReader(new FileReader(filename));
            StringBuilder content = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                content.append(line);
            }
            reader.close();
            return content.toString();
        } catch (IOException e) {
            return "Error reading file";
        }
    }

    // 🚨 XSS vulnerability
    public void displayUserInput(HttpServletResponse response, String userInput) {
        try {
            PrintWriter out = response.getWriter();
            out.println("<html><body>");
            out.println("User input: " + userInput);
            out.println("</body></html>");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

class User {
    private String username;
    private String email;

    public User(String username, String email) {
        this.username = username;
        this.email = email;
    }

    public String getUsername() { return username; }
    public String getEmail() { return email; }
}
```
</details>

### 📦 Subtask 2.3: Create Maven Configuration with Vulnerable Dependencies

> 💡 Outdated dependencies with known CVEs, so OWASP Dependency Check has real findings to surface.

| Dependency | Version | Note |
|---|---|---|
| 🥊 org.apache.struts:struts2-core | 2.3.20 | Known CVEs in older Struts2 releases |
| 📚 commons-collections:commons-collections | 3.2.1 | Deserialization vulnerabilities |
| 🌱 org.springframework:spring-core | 4.3.0.RELEASE | Outdated Spring release |
| 🌐 javax.servlet:servlet-api | 2.5 | Legacy servlet API (provided scope) |
| 🐬 mysql:mysql-connector-java | 5.1.40 | Outdated JDBC driver |

<details>
<summary>📄 <strong>pom.xml</strong> — click to expand</summary>

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>vulnerable-app</artifactId>
    <version>1.0.0</version>
    <packaging>jar</packaging>

    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <!-- Vulnerable dependencies with known CVEs -->
        <dependency>
            <groupId>org.apache.struts</groupId>
            <artifactId>struts2-core</artifactId>
            <version>2.3.20</version>
        </dependency>

        <dependency>
            <groupId>commons-collections</groupId>
            <artifactId>commons-collections</artifactId>
            <version>3.2.1</version>
        </dependency>

        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-core</artifactId>
            <version>4.3.0.RELEASE</version>
        </dependency>

        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>servlet-api</artifactId>
            <version>2.5</version>
            <scope>provided</scope>
        </dependency>

        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>5.1.40</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.8.1</version>
                <configuration>
                    <source>11</source>
                    <target>11</target>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```
</details>

---

## ⚙️ Task 3: Configure Jenkins CI/CD Pipeline

### 🔐 Subtask 3.1: Access Jenkins and Create New Job

```bash
# ▶️ Start Jenkins if not already running
sudo systemctl start jenkins
sudo systemctl enable jenkins

# 🔑 Get Jenkins initial admin password
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

1. 🌐 Open your browser and navigate to `http://localhost:8080`
2. 🔑 Enter the initial admin password
3. 📦 Install suggested plugins
4. 👤 Create admin user
5. ➕ Click **New Item**
6. 🏷️ Enter job name: `security-scan-pipeline`
7. 🔁 Select **Pipeline** and click **OK**

### 📜 Subtask 3.2: Create Jenkins Pipeline Script

> 💡 A comprehensive pipeline integrating both the SAST (Semgrep) and SCA (OWASP Dependency Check) tools, plus summary reporting and email delivery.

<details>
<summary>🔁 <strong>Jenkinsfile — Pipeline script</strong> — click to expand</summary>

```groovy
pipeline {
    agent any

    environment {
        PROJECT_NAME = 'vulnerable-app'
        SEMGREP_CONFIG = 'auto'
        DEPENDENCY_CHECK_PATH = '/opt/dependency-check/dependency-check/bin/dependency-check.sh'
        REPORTS_DIR = 'security-reports'
        DEVELOPER_EMAIL = 'developer@example.com'
    }

    stages {
        stage('Checkout') { // 📥
            steps {
                script {
                    deleteDir()

                    sh '''
                        mkdir -p ${PROJECT_NAME}
                        cp -r /home/ubuntu/security-lab/sample-app/* ${PROJECT_NAME}/
                        cd ${PROJECT_NAME}
                        ls -la
                    '''
                }
            }
        }

        stage('Prepare Reports Directory') { // 🗂️
            steps {
                sh '''
                    mkdir -p ${REPORTS_DIR}
                    echo "Reports will be stored in: ${REPORTS_DIR}"
                '''
            }
        }

        stage('SAST - Semgrep Scan') { // 🛡️
            steps {
                script {
                    try {
                        sh '''
                            echo "Starting Semgrep SAST scan..."
                            cd ${PROJECT_NAME}

                            semgrep --config=auto \
                                    --config=p/security-audit \
                                    --config=p/owasp-top-ten \
                                    --json \
                                    --output=../${REPORTS_DIR}/semgrep-report.json \
                                    .

                            semgrep --config=auto \
                                    --config=p/security-audit \
                                    --config=p/owasp-top-ten \
                                    --output=../${REPORTS_DIR}/semgrep-report.txt \
                                    .

                            echo "Semgrep scan completed successfully"
                        '''
                    } catch (Exception e) {
                        echo "Semgrep scan encountered issues: ${e.getMessage()}"
                        currentBuild.result = 'UNSTABLE'
                    }
                }
            }
        }

        stage('SCA - OWASP Dependency Check') { // 📦
            steps {
                script {
                    try {
                        sh '''
                            echo "Starting OWASP Dependency Check scan..."
                            cd ${PROJECT_NAME}

                            ${DEPENDENCY_CHECK_PATH} \
                                --project "${PROJECT_NAME}" \
                                --scan . \
                                --format JSON \
                                --format HTML \
                                --out ../${REPORTS_DIR} \
                                --suppression suppression.xml || true

                            echo "OWASP Dependency Check completed"
                        '''
                    } catch (Exception e) {
                        echo "OWASP Dependency Check encountered issues: ${e.getMessage()}"
                        currentBuild.result = 'UNSTABLE'
                    }
                }
            }
        }

        stage('Generate Summary Report') { // 📄
            steps {
                sh '''
                    echo "Generating security summary report..."

                    cat > ${REPORTS_DIR}/security-summary.txt << EOF
Security Scan Summary Report
============================
Project: ${PROJECT_NAME}
Scan Date: $(date)
Jenkins Build: ${BUILD_NUMBER}

SAST (Static Application Security Testing) - Semgrep Results:
------------------------------------------------------------
EOF

                    if [ -f "${REPORTS_DIR}/semgrep-report.json" ]; then
                        echo "Semgrep scan completed successfully" >> ${REPORTS_DIR}/security-summary.txt

                        python3 -c "
import json
import sys
try:
    with open('${REPORTS_DIR}/semgrep-report.json', 'r') as f:
        data = json.load(f)

    findings = data.get('results', [])
    total = len(findings)

    severity_counts = {}
    for finding in findings:
        severity = finding.get('extra', {}).get('severity', 'UNKNOWN')
        severity_counts[severity] = severity_counts.get(severity, 0) + 1

    print(f'Total findings: {total}')
    for severity, count in severity_counts.items():
        print(f'{severity}: {count}')

except Exception as e:
    print(f'Error processing Semgrep report: {e}')
" >> ${REPORTS_DIR}/security-summary.txt
                    else
                        echo "Semgrep report not found" >> ${REPORTS_DIR}/security-summary.txt
                    fi

                    cat >> ${REPORTS_DIR}/security-summary.txt << EOF

SCA (Software Composition Analysis) - OWASP Dependency Check Results:
---------------------------------------------------------------------
EOF

                    if [ -f "${REPORTS_DIR}/dependency-check-report.json" ]; then
                        echo "OWASP Dependency Check completed successfully" >> ${REPORTS_DIR}/security-summary.txt

                        python3 -c "
import json
try:
    with open('${REPORTS_DIR}/dependency-check-report.json', 'r') as f:
        data = json.load(f)

    dependencies = data.get('dependencies', [])
    total_deps = len(dependencies)
    vulnerable_deps = 0
    total_vulns = 0

    severity_counts = {'HIGH': 0, 'MEDIUM': 0, 'LOW': 0}

    for dep in dependencies:
        vulnerabilities = dep.get('vulnerabilities', [])
        if vulnerabilities:
            vulnerable_deps += 1
            total_vulns += len(vulnerabilities)

            for vuln in vulnerabilities:
                severity = vuln.get('severity', 'UNKNOWN')
                if severity in severity_counts:
                    severity_counts[severity] += 1

    print(f'Total dependencies scanned: {total_deps}')
    print(f'Vulnerable dependencies: {vulnerable_deps}')
    print(f'Total vulnerabilities: {total_vulns}')
    print(f'High severity: {severity_counts[\"HIGH\"]}')
    print(f'Medium severity: {severity_counts[\"MEDIUM\"]}')
    print(f'Low severity: {severity_counts[\"LOW\"]}')

except Exception as e:
    print(f'Error processing Dependency Check report: {e}')
" >> ${REPORTS_DIR}/security-summary.txt
                    else
                        echo "OWASP Dependency Check report not found" >> ${REPORTS_DIR}/security-summary.txt
                    fi

                    echo "" >> ${REPORTS_DIR}/security-summary.txt
                    echo "Detailed reports are available in the attached files." >> ${REPORTS_DIR}/security-summary.txt
                    echo "Please review and address the identified security issues." >> ${REPORTS_DIR}/security-summary.txt

                    echo "Summary report generated successfully"
                '''
            }
        }

        stage('Send Email Report') { // 📧
            steps {
                script {
                    try {
                        sh '''
                            echo "Preparing to send email report..."

                            cat > email-body.txt << EOF
Subject: Security Scan Report - ${PROJECT_NAME} Build #${BUILD_NUMBER}

Dear Developer,

Please find attached the security scan report for project: ${PROJECT_NAME}
Build Number: ${BUILD_NUMBER}
Scan Date: $(date)

This report includes:
1. SAST (Static Application Security Testing) results from Semgrep
2. SCA (Software Composition Analysis) results from OWASP Dependency Check
3. Summary of all findings

Please review the attached reports and address any security issues identified.

Best regards,
DevSecOps Team
EOF

                            if [ -f "${REPORTS_DIR}/security-summary.txt" ]; then
                                echo "Sending email report to ${DEVELOPER_EMAIL}..."

                                cat > send_email.py << 'PYEOF'
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import glob

def send_email():
    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = os.environ.get('SENDER_EMAIL', 'your-email@gmail.com')
        sender_password = os.environ.get('SENDER_PASSWORD', 'your-app-password')
        recipient_email = os.environ.get('DEVELOPER_EMAIL', 'developer@example.com')

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = f"Security Scan Report - {os.environ.get('PROJECT_NAME', 'Project')} Build #{os.environ.get('BUILD_NUMBER', 'N/A')}"

        body = f"""
Dear Developer,

Please find attached the security scan report for project: {os.environ.get('PROJECT_NAME', 'Project')}
Build Number: {os.environ.get('BUILD_NUMBER', 'N/A')}

This report includes:
1. SAST (Static Application Security Testing) results from Semgrep
2. SCA (Software Composition Analysis) results from OWASP Dependency Check
3. Summary of all findings

Please review the attached reports and address any security issues identified.

Best regards,
DevSecOps Team
        """

        msg.attach(MIMEText(body, 'plain'))

        reports_dir = os.environ.get('REPORTS_DIR', 'security-reports')
        report_files = glob.glob(f"{reports_dir}/*")

        for file_path in report_files:
            if os.path.isfile(file_path):
                with open(file_path, "rb") as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())

                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename= {os.path.basename(file_path)}'
                )
                msg.attach(part)

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()

        print("Email sent successfully!")
        return True

    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

if __name__ == "__main__":
    send_email()
PYEOF

                                python3 send_email.py || echo "Email sending failed, but continuing pipeline"
                            else
                                echo "No summary report found to send"
                            fi
                        '''
                    } catch (Exception e) {
                        echo "Email sending failed: ${e.getMessage()}"
                        // Don't fail the build if email fails
                    }
                }
            }
        }
    }

    post {
        always { // 📦
            archiveArtifacts artifacts: 'security-reports/**/*', fingerprint: true, allowEmptyArchive: true
            echo "Pipeline completed. Reports archived."
        }

        success { // ✅
            echo "Security scan pipeline completed successfully!"
        }

        failure { // ❌
            echo "Security scan pipeline failed. Please check the logs."
        }

        unstable { // ⚠️
            echo "Security scan pipeline completed with warnings. Please review the reports."
        }
    }
}
```
</details>

```markdown
# TODO: Move SENDER_EMAIL / SENDER_PASSWORD into a Jenkins credentials store
# (e.g. withCredentials) instead of relying on plain environment variables
```

---

## 🧪 Task 4: Execute and Analyze Security Scans

### ▶️ Subtask 4.1: Run the Jenkins Pipeline

1. 💾 Save the pipeline configuration in Jenkins
2. ▶️ Click **Build Now** to execute the pipeline
3. 👀 Monitor the build progress in the **Console Output**
4. ⏳ Wait for the pipeline to complete all stages

### 🖐️ Subtask 4.2: Manual Testing of Individual Tools

```bash
# 📁 Navigate to the sample application
cd ~/security-lab/sample-app

# 🛡️ Run Semgrep manually with verbose output
echo "Running Semgrep SAST scan..."
semgrep --config=auto --config=p/security-audit --config=p/owasp-top-ten --verbose .

# 📦 Run OWASP Dependency Check manually
echo "Running OWASP Dependency Check..."
dependency-check --project "manual-test" --scan . --format HTML --format JSON --out ./manual-reports
```

### 📊 Subtask 4.3: Analyze SAST Results

```bash
# 📄 View Semgrep findings
cd ~/security-lab/sample-app
cat ../security-reports/semgrep-report.txt
```

```python
# 🔍 Analyzing SAST findings
import json
import os

report_path = '../security-reports/semgrep-report.json'
if os.path.exists(report_path):
    with open(report_path, 'r') as f:
        data = json.load(f)

    findings = data.get('results', [])
    print(f"Total SAST findings: {len(findings)}")

    # Group by rule ID
    rule_counts = {}
    for finding in findings:
        rule_id = finding.get('check_id', 'unknown')
        rule_counts[rule_id] = rule_counts.get(rule_id, 0) + 1

    print("\nFindings by rule:")
    for rule, count in sorted(rule_counts.items()):
        print(f"  {rule}: {count}")

    # Show first few findings with details
    print("\nSample findings:")
    for i, finding in enumerate(findings[:3]):
        print(f"\n{i+1}. Rule: {finding.get('check_id', 'N/A')}")
        print(f"   File: {finding.get('path', 'N/A')}")
        print(f"   Line: {finding.get('start', {}).get('line', 'N/A')}")
        print(f"   Message: {finding.get('message', 'N/A')}")
        print(f"   Severity: {finding.get('extra', {}).get('severity', 'N/A')}")
else:
    print("Semgrep report not found")
```

### 📈 Subtask 4.4: Analyze SCA Results

```python
# 🔍 Analyzing SCA findings
import json
import os

report_path = '../security-reports/dependency-check-report.json'
if os.path.exists(report_path):
    with open(report_path, 'r') as f:
        data = json.load(f)

    dependencies = data.get('dependencies', [])
    print(f"Total dependencies scanned: {len(dependencies)}")

    vulnerable_deps = []
    total_vulns = 0
    severity_counts = {'HIGH': 0, 'MEDIUM': 0, 'LOW': 0, 'CRITICAL': 0}

    for dep in dependencies:
        vulnerabilities = dep.get('vulnerabilities', [])
        if vulnerabilities:
            vulnerable_deps.append({
                'name': dep.get('fileName', 'Unknown'),
                'vulns': vulnerabilities
            })
            total_vulns += len(vulnerabilities)

            for vuln in vulnerabilities:
                severity = vuln.get('severity', 'UNKNOWN')
                if severity in severity_counts:
                    severity_counts[severity] += 1

    print(f"Vulnerable dependencies: {len(vulnerable_deps)}")
    print(f"Total vulnerabilities: {total_vulns}")
    print("\nVulnerabilities by severity:")
    for severity, count in severity_counts.items():
        if count > 0:
            print(f"  {severity}: {count}")

    print("\nTop vulnerable dependencies:")
    for i, dep in enumerate(vulnerable_deps[:5]):
        print(f"\n{i+1}. {dep['name']}")
        print(f"   Vulnerabilities: {len(dep['vulns'])}")
        for vuln in dep['vulns'][:2]:
            print(f"   - {vuln.get('name', 'N/A')} ({vuln.get('severity', 'N/A')})")
            print(f"     Description: {vuln.get('description', 'N/A')[:100]}...")
else:
    print("OWASP Dependency Check report not found")
```

---

## 📄 Task 5: Configure Advanced Reporting and Notifications

### 🎨 Subtask 5.1: Create Custom Report Templates

```bash
# 📁 Create reports template directory
mkdir -p ~/security-lab/templates
```

<details>
<summary>🖼️ <strong>templates/security-report-template.html</strong> — click to expand</summary>

```html
<!DOCTYPE html>
<html>
<head>
    <title>Security Scan Report</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .header { background-color: #f4f4f4; padding: 20px; border-radius: 5px; }
        .section { margin: 20px 0; }
        .critical { color: #d32f2f; font-weight: bold; }
        .high { color: #f57c00; font-weight: bold; }
        .medium { color: #fbc02d; font-weight: bold; }
        .low { color: #388e3c; font-weight: bold; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        .summary-box { background-color: #e3f2fd; padding: 15px; border-radius: 5px; margin: 10px 0; }
    </style>
</head>
<body>
    <div class="header">
        <h1>Security Scan Report</h1>
        <p><strong>Project:</strong> {{PROJECT_NAME}}</p>
        <p><strong>Build Number:</strong> {{BUILD_NUMBER}}</p>
        <p><strong>Scan Date:</strong> {{SCAN_DATE}}</p>
    </div>

    <div class="section">
        <h2>Executive Summary</h2>
        <div class="summary-box">
            <p>This report contains the results of automated security scanning performed on your application code and dependencies.</p>
            <ul>
                <li><strong>SAST (Static Application Security Testing):</strong> Identifies security vulnerabilities in source code</li>
                <li><strong>SCA (Software Composition Analysis):</strong> Identifies known vulnerabilities in third-party dependencies</li>
            </ul>
        </div>
    </div>

    <div class="section">
        <h2>SAST Results - Semgrep</h2>
        <p>{{SAST_SUMMARY}}</p>
        <table>
            <tr><th>Severity</th><th>Count</th></tr>
            {{SAST_TABLE_ROWS}}
        </table>
    </div>

    <div class="section">
        <h2>SCA Results - OWASP Dependency Check</h2>
        <p>{{SCA_SUMMARY}}</p>
        <table>
            <tr><th>Severity</th><th>Count</th></tr>
            {{SCA_TABLE_ROWS}}
        </table>
    </div>

    <div class="section">
        <h2>Recommendations</h2>
        <ul>
            <li>Review and fix all CRITICAL and HIGH severity issues immediately</li>
            <li>Update vulnerable dependencies to their latest secure versions</li>
            <li>Implement secure coding practices to prevent future vulnerabilities</li>
            <li>Consider adding security testing to your development workflow</li>
        </ul>
    </div>
</body>
</html>
```
</details>

### 🐍 Subtask 5.2: Create Advanced Report Generation Script

```bash
# 📝 generate-advanced-report.py — comprehensive report generator (in progress)
cat > ~/security-lab/generate-advanced-report.py << 'EOF'
#!/usr/bin/env python3
import json
import os
import sys
from datetime import datetime
import argparse

def load_json_report(file_path):
    """Load JSON report file safely"""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading {file_path}: {e}")
        return None

def analyze_semgrep_report(report_data):
    """
```

> ⚠️ **Note:** The provided lab material ends here — mid-docstring inside the `analyze_semgrep_report()` function of `generate-advanced-report.py`. The rest of this script, any remaining Task 5 subtasks, a verification checklist, troubleshooting section, and conclusion were not included in the source content.

```markdown
# TODO: Complete analyze_semgrep_report() and add its SCA counterpart,
# then wire both into an HTML report built from security-report-template.html
# once the rest of the source material is available.
```

---

## 🗺️ MITRE ATT&CK Mapping

> Maps the vulnerability classes this lab's SAST/SCA tooling is designed to catch to the techniques they mitigate:

| Technique ID | Technique | Mitigated By |
|---|---|---|
| T1190 | Exploit Public-Facing Application | Semgrep SAST catching the SQL injection, path traversal, and XSS flaws in `VulnerableApp.java` |
| T1195.001 | Compromise Software Supply Chain (Dependencies) | OWASP Dependency Check flagging the vulnerable Struts2/commons-collections/Spring versions pinned in `pom.xml` |
| T1110 | Brute Force | Semgrep flagging the MD5-based password hashing, guiding remediation toward a brute-force-resistant algorithm |
| T1552.001 | Credentials In Files | Semgrep's `p/security-audit` ruleset scanning source for hardcoded secrets |

## 🧩 Key Concepts Summary

| Concept | Role in This Pipeline |
|---|---|
| 🛡️ SAST (Semgrep) | Scans source code for security antipatterns using `auto` + `p/security-audit` + `p/owasp-top-ten` rulesets |
| 📦 SCA (OWASP Dependency Check) | Cross-references project dependencies against known CVE databases |
| 🤖 Jenkins Pipeline | Orchestrates Checkout → SAST → SCA → Summary Report → Email Report stages |
| 📧 Email Reporting | ssmtp + a Python `smtplib` script deliver scan reports as attachments to developers automatically |

---

## 🏁 Conclusion

### 🎉 Key Accomplishments

- 🔎 Understood the fundamentals of SAST and SCA and how they complement each other in a security pipeline
- 🛡️ Integrated Semgrep into a Jenkins pipeline for automated source code security scanning
- 📦 Implemented OWASP Dependency Check to identify vulnerable dependencies in a Maven project
- 📧 Configured automated report generation and email notifications for security findings
- ⚙️ Built a complete Jenkins CI/CD pipeline combining SAST, SCA, reporting, and notification stages
- 📊 Practiced analyzing and interpreting SAST and SCA scan results to guide remediation

### 💡 Why This Matters

Running SAST and SCA together closes two very different gaps: SAST catches insecure code the team wrote, while SCA catches insecure code the team merely depends on. Automating both inside a Jenkins pipeline — and routing the results straight to developers by email — keeps security findings visible at build time instead of surfacing only during an audit or after an incident.

```markdown
# TODO: Once the remaining Task 5 source material is available, extend this
# README with a Real-World Applications section and a verification checklist
# consistent with the rest of the Al Nafi lab series.
```

---

<div align="center">

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Training-1976D2?style=for-the-badge)

</div>
