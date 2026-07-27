<div align="center">

# 🚨 DevSecOps Culture and Activities — Incident Response Planning

### Building a Complete Incident Response Plan, Playbooks, and Management Tooling

![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu_22.04-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-CB171E?style=for-the-badge&logo=yaml&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![Incident Response](https://img.shields.io/badge/Incident_Response-b91c1c?style=for-the-badge)

</div>

---

## 📋 Table of Contents

- [🎯 Lab Objectives](#-lab-objectives)
- [📌 Prerequisites](#-prerequisites)
- [🖥️ Lab Environment Setup](#️-lab-environment-setup)
- [📘 Task 1: Create a Complete Incident Response Plan](#-task-1-create-a-complete-incident-response-plan)
- [📕 Task 2: Create a Complete Incident Response Playbook](#-task-2-create-a-complete-incident-response-playbook)
- [🗺️ MITRE ATT&CK Mapping](#️-mitre-attck-mapping)
- [🧯 Troubleshooting](#-troubleshooting)
- [✅ Conclusion](#-conclusion)

---

## 🎯 Lab Objectives

| # | Objective |
|---|-----------|
| 1 | Understand the fundamental principles of DevSecOps culture and incident response |
| 2 | Create a comprehensive incident response plan following industry best practices |
| 3 | Develop a detailed incident response playbook with actionable procedures |
| 4 | Implement security-first thinking in development and operations workflows |
| 5 | Establish communication protocols and escalation procedures for security incidents |
| 6 | Document and structure incident response processes for team collaboration |

## 📌 Prerequisites

| Requirement | Details |
|---|---|
| 🔄 SDLC | Basic understanding of software development lifecycle (SDLC) |
| 🐧 Linux CLI | Familiarity with Linux command line operations |
| 🛡️ Cybersecurity | General knowledge of cybersecurity concepts |
| 🤝 Collaboration | Understanding of team collaboration tools and processes |
| 📄 Documentation | Basic knowledge of documentation formats (Markdown, YAML) |

## 🖥️ Lab Environment Setup

> **☁️ Ready-to-Use Cloud Machines**
> Al Nafi provides pre-configured Linux-based cloud machines for this lab. Simply click **"Start Lab"** to access your environment — no need to build your own VM or install additional software.

**Your lab environment includes:**
- 🐧 Ubuntu 22.04 LTS with necessary tools pre-installed
- 📝 Text editors (nano, vim)
- 🌿 Git for version control
- 📄 YAML and Markdown processors
- 📁 Sample templates and documentation tools

---

## 📘 Task 1: Create a Complete Incident Response Plan

![Markdown](https://img.shields.io/badge/Markdown-000000?style=flat-square&logo=markdown&logoColor=white) ![YAML](https://img.shields.io/badge/YAML-CB171E?style=flat-square&logo=yaml&logoColor=white)

### Subtask 1.1: Understanding Incident Response Framework

#### 🪜 Step 1: Set Up the Project Structure

```bash
# 📁 Access your lab environment and open a terminal, then create the project directory structure
mkdir -p ~/devsecops-lab/incident-response
cd ~/devsecops-lab/incident-response
mkdir -p {plans,playbooks,templates,documentation}
```

#### 🪜 Step 2: Author the Main Incident Response Plan

```bash
# 📝 Create the main incident response plan document
nano plans/incident-response-plan.md
```

Add the following comprehensive incident response plan content:

```markdown
# DevSecOps Incident Response Plan

## 1. Executive Summary
This Incident Response Plan (IRP) establishes procedures for identifying, responding to,
and recovering from security incidents within our DevSecOps environment. This plan ensures
rapid response, minimal business impact, and continuous improvement of security postures.

## 2. Incident Response Team Structure

### 2.1 Core Team Roles
- Incident Commander (IC): overall incident coordination, decision-making authority,
  external communication lead
- Security Lead: technical security analysis, threat assessment, forensic coordination
- Development Lead: code analysis and remediation, application security assessment,
  development team coordination
- Operations Lead: infrastructure management, system recovery coordination,
  performance monitoring
- Communications Lead: internal stakeholder updates, customer communication,
  media relations (if required)
<!-- TODO: Fill in Primary/Secondary contact details for each role above -->
```

**Incident Severity Levels**

| Level | Criteria | Response Time | Resolution Target |
|---|---|---|---|
| 🔴 Critical (P1) | Complete system compromise, data breach with PII/PHI exposure, production system completely down | 15 minutes | 4 hours |
| 🟠 High (P2) | Partial system compromise, suspected data breach, major functionality impaired | 30 minutes | 8 hours |
| 🟡 Medium (P3) | Security policy violations, minor system vulnerabilities, limited functionality impact | 2 hours | 24 hours |
| 🟢 Low (P4) | Security awareness issues, non-critical vulnerabilities, minimal business impact | 8 hours | 72 hours |

**Incident Response Phases**

| Phase | Focus |
|---|---|
| 1️⃣ Preparation | Maintain IR tools/procedures, regular team training and simulations, communication channels, system baselines |
| 2️⃣ Identification | Monitor security alerts/logs, validate incident occurrence, initial impact assessment, classification |
| 3️⃣ Containment | Short-term containment, system isolation if necessary, evidence preservation, long-term containment strategy |
| 4️⃣ Eradication | Remove threat, identify and fix vulnerabilities, update security controls, system hardening |
| 5️⃣ Recovery | Restore systems to normal operation, additional monitoring, validate integrity, return to normal operations |
| 6️⃣ Lessons Learned | Post-incident review, document lessons learned, update procedures/tools, share knowledge with team |

**Communication Procedures**

| Type | Requirement |
|---|---|
| 📢 Internal | IC notifies executive team within 30 minutes; status updates every 2 hours during active incidents; all-clear notification on resolution |
| 📣 External | Customer notification within 4 hours for P1/P2; regulatory notification as required by law; media communication through designated spokesperson only |

**Tools, Legal, and Maintenance**

```markdown
## 6. Tools and Resources
- Communication: Slack #incident-response channel, conference bridge, mobile phone contact list
- Technical: SIEM, ELK Stack (Elasticsearch, Logstash, Kibana), SANS SIFT Workstation,
  incident tracking system

## 7. Legal and Regulatory Requirements
- GDPR: 72 hours to supervisory authority; state laws vary by jurisdiction;
  industry regulations as applicable
- Evidence handling: chain of custody procedures, legal hold requirements,
  forensic imaging standards

## 8. Training and Awareness
- Quarterly incident response drills, annual plan review, new team member onboarding
- Security awareness training, incident reporting procedures, escalation path communication

## 9. Plan Maintenance
- Monthly: contact information updates
- Quarterly: procedure review
- Annually: complete plan revision
- All changes tracked in version control; approval required for major changes

## 10. Appendices
- A: Contact Information
- B: System Inventory
- C: Network Diagrams
- D: Legal Contacts
<!-- TODO: Populate Appendices A-D with your organization's actual contacts, systems, and diagrams -->
```

```bash
# 💾 Save the file
# Ctrl+X, then Y, then Enter
```

### Subtask 1.2: Create Supporting Documentation Templates

#### 🪜 Step 3: Create the Incident Classification Template

```bash
# 📝 Create the classification template
nano templates/incident-classification-template.yaml
```

```yaml
# 🏷️ Incident Classification Template
incident_id: "INC-YYYY-MMDD-###"
date_reported: "YYYY-MM-DD HH:MM:SS UTC"
reported_by: ""
incident_commander: ""

# Classification
severity: "" # Critical, High, Medium, Low
category: "" # Security, Availability, Performance, Data
subcategory: ""
affected_systems: []
business_impact: ""

# Initial Assessment
description: ""
potential_causes: []
initial_containment_actions: []
estimated_resolution_time: ""

# Stakeholders
technical_lead: ""
business_owner: ""
external_parties_notified: []

# Status Tracking
current_status: "Open" # Open, In Progress, Resolved, Closed
next_update_due: "YYYY-MM-DD HH:MM:SS UTC"
resolution_summary: ""
lessons_learned: []

# Metrics
time_to_detection: ""
time_to_response: ""
time_to_containment: ""
time_to_resolution: ""
# TODO: Wire this template into your ticketing system so a new incident auto-populates incident_id and date_reported
```

#### 🪜 Step 4: Create the Communication Template

```bash
# 📝 Create the communication template
nano templates/communication-template.md
```

```markdown
# Incident Communication Template

## Initial Notification
**Subject**: [SEVERITY] Security Incident - [BRIEF DESCRIPTION]
**Incident ID**: INC-YYYY-MMDD-###
**Severity**: [Critical/High/Medium/Low]
**Status**: [Open/In Progress/Resolved]
**Incident Commander**: [Name]
**Next Update**: [Time]

### Summary
[Brief description of the incident]

### Impact
- **Systems Affected**: [List systems]
- **Business Impact**: [Description]
- **Customer Impact**: [Yes/No - Description]

### Current Actions
- [Action 1]
- [Action 2]
- [Action 3]

### Next Steps
- [Next step 1]
- [Next step 2]

---

## Status Update Template
**Subject**: [UPDATE] [SEVERITY] Security Incident - [BRIEF DESCRIPTION]
**Incident ID**: INC-YYYY-MMDD-###
**Status**: [Current Status]
**Time Since Last Update**: [Duration]
**Next Update**: [Time]

### Progress Since Last Update
- [Progress item 1]
- [Progress item 2]

### Current Status
[Detailed status description]

### Ongoing Actions
- [Action 1 - Owner - ETA]
- [Action 2 - Owner - ETA]

### Blockers/Issues
- [Issue 1 - Impact]
- [Issue 2 - Impact]

---

## Resolution Notification
**Subject**: [RESOLVED] Security Incident - [BRIEF DESCRIPTION]
**Incident ID**: INC-YYYY-MMDD-###
**Status**: Resolved
**Resolution Time**: [Total time]
**Post-Incident Review**: [Scheduled date/time]

### Resolution Summary
[Description of how the incident was resolved]

### Root Cause
[Root cause analysis]

### Preventive Measures
- [Measure 1]
- [Measure 2]

### Monitoring
[Ongoing monitoring measures]
```

<details>
<summary>🧯 Troubleshooting: YAML template fails validation</summary>

`incident_id`, `date_reported`, and `next_update_due` are quoted strings, not native YAML dates/numbers — keep the quotes so downstream parsers (and ticketing-system integrations) don't try to coerce them into a date type and reject the placeholder format.

</details>

---

## 📕 Task 2: Create a Complete Incident Response Playbook

![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white) ![ClamAV](https://img.shields.io/badge/ClamAV-000000?style=flat-square) ![iptables](https://img.shields.io/badge/iptables-4EAA25?style=flat-square)

### Subtask 2.1: Develop Specific Response Playbooks

#### 🪜 Step 5: Create the Playbook Directory Structure

```bash
# 📁 Create the main playbook directory structure
cd ~/devsecops-lab/incident-response/playbooks
mkdir -p {security-breach,ddos-attack,malware-infection,data-leak,insider-threat}
# 📌 data-leak and insider-threat are scaffolded here for future playbooks;
# this lab only develops content for security-breach, ddos-attack, and malware-infection
```

#### 🪜 Step 6: Author the Security Breach Response Playbook

```bash
# 📝 Create the comprehensive security breach playbook
nano security-breach/security-breach-playbook.md
```

**Playbook Overview**

| Field | Value |
|---|---|
| Purpose | Respond to confirmed or suspected security breaches |
| Scope | All systems and data within the organization |
| Trigger | Security alert, anomalous activity, or breach notification |
| Owner | Security Team Lead |

**Pre-Incident Preparation**
- [ ] Access to SIEM dashboard
- [ ] Forensic imaging tools ready
- [ ] Communication channels established
- [ ] Legal contacts available
- [ ] Backup systems verified
- [ ] Incident Commander assigned
- [ ] Security Lead notified
- [ ] Development Lead on standby
- [ ] Operations Lead available
- [ ] Communications Lead ready

**Phase 1: Initial Response (0–15 minutes)**

*Step 1 — Incident Verification*

```bash
# 🔎 Check system logs for suspicious activity
sudo tail -f /var/log/auth.log
sudo tail -f /var/log/syslog

# 🌐 Check network connections
netstat -tulpn | grep LISTEN
ss -tulpn | grep LISTEN

# 🖥️ Check running processes
ps aux | grep -v "^\[" | sort
```
- [ ] Confirm incident occurrence
- [ ] Document initial findings
- [ ] Assess immediate threat level
- [ ] Notify Incident Commander

*Step 2 — Initial Containment*

```bash
# 🚫 If system compromise suspected, isolate the system
# Block suspicious IP addresses
sudo iptables -A INPUT -s [SUSPICIOUS_IP] -j DROP
# TODO: Replace [SUSPICIOUS_IP] with the address identified during triage

# 🔒 Disable compromised user accounts
sudo usermod -L [USERNAME]

# 🛑 Stop suspicious processes
sudo kill -9 [PID]
```
- [ ] Isolate affected systems
- [ ] Preserve evidence
- [ ] Block malicious traffic
- [ ] Document all actions taken

**Phase 2: Investigation and Analysis (15 minutes – 2 hours)**

*Step 3 — Evidence Collection*

```bash
# 💿 Create forensic image of affected system
sudo dd if=/dev/sda of=/mnt/forensics/system-image.dd bs=4096

# 🧠 Collect memory dump
sudo dd if=/dev/mem of=/mnt/forensics/memory-dump.dd

# 📡 Collect network traffic
sudo tcpdump -i eth0 -w /mnt/forensics/network-capture.pcap

# 📋 Collect system information
sudo lshw > /mnt/forensics/hardware-info.txt
sudo ps aux > /mnt/forensics/process-list.txt
sudo netstat -tulpn > /mnt/forensics/network-connections.txt
```
- [ ] Create forensic images
- [ ] Collect volatile data
- [ ] Document system state
- [ ] Preserve log files
- [ ] Maintain chain of custody

*Step 4 — Threat Analysis*

```bash
# 🔍 Analyze log files for indicators of compromise
grep -i "failed\|error\|unauthorized" /var/log/auth.log
grep -i "attack\|intrusion\|malware" /var/log/syslog

# 📁 Check for unusual file modifications
find /etc -type f -mtime -1 -ls
find /var/www -type f -mtime -1 -ls

# 📡 Analyze network traffic
tcpdump -r network-capture.pcap | grep -i "suspicious_pattern"
```
- [ ] Identify attack vectors
- [ ] Determine scope of compromise
- [ ] Assess data exposure risk
- [ ] Identify affected systems
- [ ] Document findings

**Phase 3: Containment and Eradication (2–8 hours)**

*Step 5 — Extended Containment*

```bash
# 🔥 Update firewall rules
sudo iptables -A INPUT -s [MALICIOUS_NETWORK] -j DROP
sudo iptables-save > /etc/iptables/rules.v4

# 🩹 Patch vulnerable systems
sudo apt update && sudo apt upgrade -y

# 🔑 Reset compromised passwords
sudo passwd [USERNAME]

# 📜 Revoke and reissue certificates if needed
sudo openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout key.pem
```
- [ ] Implement additional security controls
- [ ] Patch vulnerabilities
- [ ] Reset credentials
- [ ] Update security configurations
- [ ] Monitor for persistence

*Step 6 — Eradication*

```bash
# 🧹 Remove malware/backdoors
sudo find / -name "*.suspicious" -delete
sudo crontab -l | grep -v "malicious_command" | crontab -

# 🦠 Clean infected files
sudo clamscan -r --remove /home/
sudo rkhunter --check --sk

# 🏗️ Rebuild compromised systems if necessary
# (This would involve system reinstallation procedures)
```
- [ ] Remove malicious code
- [ ] Clean infected files
- [ ] Rebuild systems if necessary
- [ ] Verify system integrity
- [ ] Update security tools

**Phase 4: Recovery (8–24 hours)**

*Step 7 — System Recovery*

```bash
# ♻️ Restore from clean backups
sudo rsync -av /backup/clean-data/ /var/www/html/

# ✅ Verify system integrity
sudo aide --check
sudo tripwire --check

# 🧪 Test system functionality
curl -I http://localhost
systemctl status apache2
```
- [ ] Restore systems from clean backups
- [ ] Verify data integrity
- [ ] Test system functionality
- [ ] Implement additional monitoring
- [ ] Gradual return to normal operations

*Step 8 — Enhanced Monitoring*

```bash
# 📊 Set up additional logging
echo "*.* /var/log/security-enhanced.log" >> /etc/rsyslog.conf
sudo systemctl restart rsyslog

# 👀 Configure real-time monitoring
sudo tail -f /var/log/security-enhanced.log | grep -i "suspicious"

# ⏰ Set up automated alerts
echo "*/5 * * * * root /usr/local/bin/security-check.sh" >> /etc/crontab
```
- [ ] Implement enhanced logging
- [ ] Set up real-time monitoring
- [ ] Configure automated alerts
- [ ] Establish baseline metrics
- [ ] Document new monitoring procedures

**Phase 5: Post-Incident Activities (24–72 hours)**

*Step 9 — Documentation and Reporting*

```bash
# 📝 Generate incident report
cat > incident-report.md << EOF
# Security Breach Incident Report

## Incident Summary
- **Incident ID**: INC-$(date +%Y%m%d)-001
- **Date/Time**: $(date)
- **Duration**: [DURATION]
- **Severity**: [SEVERITY]

## Timeline of Events
[Detailed timeline]

## Root Cause Analysis
[Analysis findings]

## Impact Assessment
[Business and technical impact]

## Response Actions
[Actions taken during response]

## Lessons Learned
[Key takeaways]

## Recommendations
[Preventive measures]
EOF
```
- [ ] Complete incident documentation
- [ ] Conduct post-incident review
- [ ] Update response procedures
- [ ] Share lessons learned
- [ ] Implement preventive measures

**Escalation Procedures**

| Path | Level | Timeframe |
|---|---|---|
| Internal | 1 — Security Team Lead | 0–15 minutes |
| Internal | 2 — IT Director | 15–30 minutes |
| Internal | 3 — CISO/CTO | 30–60 minutes |
| Internal | 4 — Executive Team | 1–2 hours |
| External | Law Enforcement | For criminal activity |
| External | Legal Counsel | For regulatory compliance |
| External | Customers | For data exposure |
| External | Regulators | As required by law |

**Success Criteria**
- [ ] Threat contained within target timeframe
- [ ] No additional systems compromised
- [ ] Data integrity maintained
- [ ] Business operations restored
- [ ] Lessons learned documented
- [ ] Preventive measures implemented

**Playbook Maintenance**: Reviewed quarterly; updated after each incident or technology change; approval required from Security Team Lead and IT Director; distributed to all incident response team members.

<details>
<summary>🧯 Troubleshooting: <code>dd</code> forensic imaging hangs or fills the disk</summary>

`dd if=/dev/sda of=/mnt/forensics/system-image.dd` writes a full raw copy of the source device — confirm `/mnt/forensics` is mounted on separate, sufficiently large storage before running it, and consider adding `status=progress` to monitor throughput on a live incident.

</details>

### Subtask 2.2: Create Additional Specialized Playbooks

#### 🪜 Step 7: Author the DDoS Attack Response Playbook

```bash
# 📝 Create the DDoS response playbook
nano ddos-attack/ddos-response-playbook.md
```

**Playbook Overview**

| Field | Value |
|---|---|
| Purpose | Respond to Distributed Denial of Service attacks |
| Scope | Network infrastructure and web services |
| Trigger | Service degradation, traffic anomalies, monitoring alerts |
| Owner | Operations Team Lead |

*Step 1 — Confirm DDoS Attack*

```bash
# 🔢 Check current connections
netstat -an | grep :80 | wc -l
ss -tuln | grep :80 | wc -l

# 📊 Monitor traffic patterns
sudo iftop -i eth0
sudo nethogs eth0

# ⚙️ Check system load
uptime
top -n 1 | head -5
```

*Step 2 — Immediate Mitigation*

```bash
# 🚦 Implement rate limiting
sudo iptables -A INPUT -p tcp --dport 80 -m limit --limit 25/minute --limit-burst 100 -j ACCEPT

# 🚫 Block suspicious source networks
sudo iptables -A INPUT -s [ATTACKING_NETWORK] -j DROP
# TODO: Replace [ATTACKING_NETWORK] with the CIDR range identified in Step 1

# 🌊 Enable SYN flood protection
echo 1 > /proc/sys/net/ipv4/tcp_syncookies
```

*Step 3 — Traffic Analysis*

```bash
# 📡 Analyze traffic patterns
sudo tcpdump -i eth0 -c 1000 -w ddos-traffic.pcap
sudo tshark -r ddos-traffic.pcap -q -z conv,ip

# 🕵️ Identify attack sources
sudo netstat -ntu | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -n
```

**Response Actions**

| Window | Actions |
|---|---|
| ⏱️ Immediate (0–30 min) | Confirm attack, implement basic rate limiting, contact ISP/CDN provider, notify IR team, begin traffic analysis |
| ⏳ Short-term (30 min – 2 hr) | Implement advanced filtering, scale infrastructure if possible, coordinate with upstream providers, monitor attack evolution, document attack characteristics |
| 🗓️ Long-term (2+ hr) | Implement permanent protections, review/update DDoS defenses, conduct post-attack analysis, update response procedures, plan capacity improvements |

#### 🪜 Step 8: Author the Malware Infection Response Playbook

```bash
# 📝 Create the malware response playbook
nano malware-infection/malware-response-playbook.md
```

**Playbook Overview**

| Field | Value |
|---|---|
| Purpose | Respond to malware infections and suspicious software |
| Scope | All systems and endpoints |
| Trigger | Antivirus alerts, suspicious behavior, performance issues |
| Owner | Security Team Lead |

*Step 1 — Isolate Infected System*

```bash
# 🔌 Disconnect from network (if safe to do so)
sudo ifconfig eth0 down

# 🛡️ Or implement network isolation
sudo iptables -A OUTPUT -j DROP
sudo iptables -A INPUT -j DROP
sudo iptables -I INPUT 1 -i lo -j ACCEPT
sudo iptables -I OUTPUT 1 -o lo -j ACCEPT
```

*Step 2 — Malware Analysis*

```bash
# 🦠 Scan for malware
sudo clamscan -r --infected --remove /home/
sudo rkhunter --check --sk
sudo chkrootkit

# 🖥️ Check running processes
ps aux | grep -v "^\[" | sort
sudo lsof -i -P -n | grep LISTEN

# 📁 Check for suspicious files
find /tmp -type f -executable
find /var/tmp -type f -executable
find /dev/shm -type f -executable
```

*Step 3 — Evidence Collection*

```bash
# 💿 Create system snapshot
sudo dd if=/dev/sda of=/mnt/forensics/infected-system.dd bs=4096

# 🧫 Collect malware samples
mkdir -p /mnt/forensics/malware-samples
cp [MALWARE_FILE] /mnt/forensics/malware-samples/

# 📋 Document system state
sudo ps aux > /mnt/forensics/process-list.txt
sudo lsof > /mnt/forensics/open-files.txt
sudo netstat -tulpn > /mnt/forensics/network-connections.txt
```

*Step 4 — Remove Malware*

```bash
# 🗑️ Remove identified malware
sudo rm -f [MALWARE_FILES]

# 🧽 Clean registry/configuration files
sudo sed -i '/malicious_entry/d' /etc/crontab
sudo systemctl disable malicious-service

# 🔄 Update and run security tools
sudo apt update
sudo apt install -y clamav rkhunter chkrootkit
sudo freshclam
sudo clamscan -r --remove /
```

*Step 5 — System Hardening*

```bash
# 🔄 Update all software
sudo apt update && sudo apt upgrade -y

# ⚙️ Configure automatic updates
sudo apt install -y unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades

# 🛡️ Implement additional security measures
sudo ufw enable
sudo fail2ban-client start
```

**Prevention Measures**
- [ ] Install and configure endpoint protection
- [ ] Implement application whitelisting
- [ ] Regular security updates
- [ ] User security training
- [ ] Email security controls
- [ ] Web filtering
- [ ] Backup and recovery procedures

<details>
<summary>🧯 Troubleshooting: <code>clamscan -r --remove /</code> deletes files you didn't expect</summary>

Running ClamAV with `--remove` across the entire filesystem (`/`) will delete anything it flags, including false positives. In a real incident, scan with reporting only first (drop `--remove`), review the results, then re-run against the specific infected paths.

</details>

### Subtask 2.3: Create the Playbook Management System

#### 🪜 Step 9: Build the Playbook Manager Script

```bash
# 📝 Create the playbook management script
nano ../playbook-manager.sh
```

```bash
#!/bin/bash

# 🗂️ DevSecOps Incident Response Playbook Manager
# This script helps manage and execute incident response playbooks

PLAYBOOK_DIR="$(dirname "$0")/playbooks"
LOG_DIR="$(dirname "$0")/logs"
INCIDENT_DIR="$(dirname "$0")/incidents"

# 📁 Create necessary directories
mkdir -p "$LOG_DIR" "$INCIDENT_DIR"

# 📋 Function to list available playbooks
list_playbooks() {
    echo "Available Incident Response Playbooks:"
    echo "======================================"
    find "$PLAYBOOK_DIR" -name "*.md" -type f | while read -r playbook; do
        playbook_name=$(basename "$playbook" .md)
        playbook_dir=$(basename "$(dirname "$playbook")")
        echo "- $playbook_dir: $playbook_name"
    done
}

# 📖 Function to display a playbook
show_playbook() {
    local playbook_type="$1"
    local playbook_file="$PLAYBOOK_DIR/$playbook_type"

    if [ -f "$playbook_file" ]; then
        less "$playbook_file"
    else
        echo "Playbook not found: $playbook_file"
        echo "Available playbooks:"
        list_playbooks
    fi
}

# ▶️ Function to start incident response
start_incident() {
    local incident_type="$1"
    local incident_id="INC-$(date +%Y%m%d)-$(printf "%03d" $(($(ls "$INCIDENT_DIR" | wc -l) + 1)))"
    local incident_dir="$INCIDENT_DIR/$incident_id"

    mkdir -p "$incident_dir"

    # 📝 Create incident log
    cat > "$incident_dir/incident-log.md" << EOF
# Incident Response Log

**Incident ID**: $incident_id
**Type**: $incident_type
**Start Time**: $(date)
**Status**: Active

## Timeline

$(date): Incident response initiated

## Actions Taken

- Incident response playbook activated
- Incident directory created: $incident_dir

## Next Steps

- Follow $incident_type playbook procedures
- Document all actions in this log
- Update status regularly

EOF

    echo "Incident $incident_id started"
    echo "Incident directory: $incident_dir"
    echo "Log file: $incident_dir/incident-log.md"

    # 📋 Copy relevant playbook to incident directory
    if [ -f "$PLAYBOOK_DIR/$incident_type/${incident_type}-playbook.md" ]; then
        cp "$PLAYBOOK_DIR/$incident_type/${incident_type}-playbook.md" "$incident_dir/"
        echo "Playbook copied to incident directory"
    fi
}

# 🔄 Function to update incident
update_incident() {
    local incident_id="$1"
    local update_message="$2"
    local incident_dir="$INCIDENT_DIR/$incident_id"

    if [ -d "$incident_dir" ]; then
        echo "" >> "$incident_dir/incident-log.md"
        echo "$(date): $update_message" >> "$incident_dir/incident-log.md"
        echo "Incident $incident_id updated"
    else
        echo "Incident not found: $incident_id"
    fi
}

# 🔒 Function to close incident
close_incident() {
    local incident_id="$1"
    local incident_dir="$INCIDENT_DIR/$incident_id"

    if [ -d "$incident_dir" ]; then
        echo "" >> "$incident_dir/incident-log.md"
        echo "$(date): Incident closed" >> "$incident_dir/incident-log.md"
        echo "**Status**: Closed" >> "$incident_dir/incident-log.md"
        echo "Incident $incident_id closed"
    else
        echo "Incident not found: $incident_id"
    fi
}

# 🎛️ Main script logic
case "$1" in
    "list")
        list_playbooks
        ;;
    "show")
        if [ -z "$2" ]; then
            echo "Usage: $0 show <playbook-type>"
            echo "Example: $0 show security-breach"
        else
            show_playbook "$2"
        fi
        ;;
    "start")
        if [ -z "$2" ]; then
            echo "Usage: $0 start <incident-type>"
            echo "Example: $0 start security-breach"
        else
            start_incident "$2"
        fi
        ;;
    "update")
        if [ -z "$2" ] || [ -z "$3" ]; then
            echo "Usage: $0 update <incident-id> \"<update-message>\""
            echo "Example: $0 update INC-20231201-001 \"Containment actions completed\""
        else
            update_incident "$2" "$3"
        fi
        ;;
    "close")
        if [ -z "$2" ]; then
            echo "Usage: $0 close <incident-id>"
            echo "Example: $0 close INC-20231201-001"
        else
            close_incident "$2"
        fi
        ;;
    *)
        echo "DevSecOps Incident Response Playbook Manager"
        echo "Usage: $0 {list|show|start|update|close}"
        echo ""
        echo "Commands:"
        echo "  list                           - List available playbooks"
        echo "  show <playbook-type>          - Display a specific playbook"
        echo "  start <incident-type>         - Start new incident response"
        echo "  update <incident-id> <message> - Update incident log"
        echo "  close <incident-id>           - Close incident"
        echo ""
        echo "Examples:"
        echo "  $0 list"
        echo "  $0 show security-breach"
        echo "  $0 start security-breach"
        echo "  $0 update INC-20231201-001 \"Malware removed\""
        echo "  $0 close INC-20231201-001"
        ;;
esac
```

```bash
# 🔑 Make the script executable
chmod +x ../playbook-manager.sh

# ▶️ Test the playbook manager
cd ~/devsecops-lab/incident-response
./playbook-manager.sh list
```

<details>
<summary>🧯 Troubleshooting: <code>playbook-manager.sh start</code> can't find a playbook to copy</summary>

`start_incident()` only copies a playbook when a file matching `$PLAYBOOK_DIR/$incident_type/${incident_type}-playbook.md` exists — the directory name and file prefix must match exactly (e.g. `security-breach/security-breach-playbook.md`). A typo in `<incident-type>` silently skips the copy step rather than erroring.

</details>

### Subtask 2.4: Create the Incident Response Checklist

#### 🪜 Step 10: Author the Comprehensive Checklist

```bash
# 📝 Create a comprehensive incident response checklist
nano documentation/incident-response-checklist.md
```

**Pre-Incident Preparation**
- [ ] Incident response team identified and trained
- [ ] Contact information up to date
- [ ] Tools and resources available
- [ ] Communication channels established
- [ ] Playbooks reviewed and updated
- [ ] Backup and recovery procedures tested

**Initial Response (0–15 minutes)**
- [ ] Incident detected and reported
- [ ] Incident Commander assigned
- [ ] Initial assessment completed
- [ ] Severity level determined
- [ ] Stakeholders notified
- [ ] Response team assembled

**Investigation Phase (15 minutes – 2 hours)**
- [ ] Evidence collection initiated
- [ ] Forensic procedures followed
- [ ] Chain of custody maintained
- [ ] Threat analysis conducted
- [ ] Scope of impact determined
- [ ] Timeline established

**Containment Phase (Immediate)**
- [ ] Immediate containment actions taken
- [ ] Affected systems isolated
- [ ] Malicious activity stopped
- [ ] Evidence preserved
- [ ] Additional monitoring implemented
- [ ] Containment effectiveness verified

**Eradication Phase**
- [ ] Root cause identified
- [ ] Vulnerabilities patched
- [ ] Malicious code removed
- [ ] System hardening implemented
- [ ] Security controls updated
- [ ] Eradication verified

**Recovery Phase**
- [ ] Systems restored from clean backups
- [ ] Functionality testing completed
- [ ] Enhanced monitoring deployed
- [ ] Gradual return to normal operations
- [ ] Performance monitoring active
- [ ] Recovery validation completed

**Post-Incident Activities**
- [ ] Incident documentation completed
- [ ] Post-incident review conducted
- [ ] Lessons learned documented
- [ ] Procedures updated
- [ ] Training needs identified
- [ ] Preventive measures implemented

**Communication Requirements**
- [ ] Internal stakeholders updated
- [ ] Executive team briefed
- [ ] Customers notified (if required)
- [ ] Regulatory reporting completed
- [ ] Media response coordinated
- [ ] Final incident report published

**Legal and Compliance**
- [ ] Legal requirements assessed
- [ ] Regulatory notifications made
- [ ] Evidence handling documented
- [ ] Privacy impact assessed
- [ ] Compliance obligations met

> ⚠️ **Source content ends here.** The original lab material is cut off mid-item in the Legal and Compliance checklist (the final line breaks off after "Legal counsel consul..."). No further checklist items, remaining subtasks, or a Lab Conclusion were provided in the source material, so nothing beyond this point has been fabricated for this README.

---

## 🗺️ MITRE ATT&CK Mapping

| Tactic | Technique ID | Technique Name | How This Lab Addresses It |
|---|---|---|---|
| Credential Access / Persistence | T1078 | Valid Accounts | The security breach playbook's containment phase disables (`usermod -L`) and resets credentials for compromised accounts before an attacker can reuse them |
| Impact | T1499 | Endpoint Denial of Service | The DDoS playbook detects volumetric attacks via connection/traffic monitoring and mitigates them with rate limiting and SYN flood protection |
| Persistence | T1053.003 | Scheduled Task/Job: Cron | The malware playbook's eradication step identifies and strips malicious `crontab` entries used to maintain persistence |
| Defense Evasion | T1070 | Indicator Removal | Forensic evidence collection (disk/memory imaging, chain-of-custody documentation) preserves artifacts before an attacker can destroy or alter them |
| Execution | T1059.004 | Command and Scripting Interpreter: Unix Shell | Malware eradication removes shell-installed backdoors and disables malicious services set up via scripting |

---

## 🧯 Troubleshooting

<details>
<summary>🧯 <code>iptables</code> rules disappear after a reboot</summary>

The rules added throughout these playbooks (`iptables -A INPUT ...`) are not persistent by default. Use `iptables-save > /etc/iptables/rules.v4` (as shown in Step 5 of the security breach playbook) and restore it on boot, or install `iptables-persistent`.

</details>

<details>
<summary>🧯 <code>usermod -L</code> doesn't fully stop an active session</summary>

Locking an account prevents new logins but doesn't terminate an existing session. Pair it with `pkill -KILL -u [USERNAME]` to end active sessions for a compromised account during containment.

</details>

---

## ✅ Conclusion

> ⚠️ Because the source lab material ends mid-checklist in Task 2.4 with no Lab Conclusion of its own, the summary below is drawn only from the lab's stated Objectives rather than a source-provided conclusion, which was not present in the material.

### 🏆 Key Accomplishments

By completing the tasks documented above, you have:
- Authored a comprehensive Incident Response Plan covering team roles, severity levels, response phases, and communication procedures
- Built reusable incident classification and communication templates in YAML and Markdown
- Developed detailed, phase-by-phase response playbooks for security breaches, DDoS attacks, and malware infections
- Automated playbook access and incident tracking with a custom Bash-based playbook manager
- Assembled a full incident response checklist spanning preparation through legal/compliance follow-up

### 🌍 Real-World Applications

- **Faster, calmer response**: pre-written playbooks remove decision-making friction in the middle of an active incident
- **Consistency across responders**: templates and checklists ensure every incident is documented and escalated the same way, regardless of who's on call
- **Audit-readiness**: chain-of-custody and communication templates give legal and compliance teams the evidence trail they need after the fact
- **Continuous improvement**: the "Lessons Learned" phase and quarterly playbook review turn every incident into an input for a stronger plan next time

---

<div align="center">

### 🎓 Provided by Al Nafi

![Al Nafi](https://img.shields.io/badge/Al_Nafi-Cybersecurity_Education-1e3a8a?style=for-the-badge)

</div>
