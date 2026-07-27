<div align="center">

# 🧭 Strategic Framework for DevSecOps

### Wardley Mapping & the Cynefin Framework for DevSecOps Decision-Making

![Ubuntu](https://img.shields.io/badge/Ubuntu_22.04-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Wardley Mapping](https://img.shields.io/badge/Wardley_Mapping-2E3440?style=for-the-badge)
![Cynefin Framework](https://img.shields.io/badge/Cynefin_Framework-4B0082?style=for-the-badge)
![Strategic Planning](https://img.shields.io/badge/Strategic_Planning-1e3a8a?style=for-the-badge)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)

</div>

---

## 📋 Table of Contents

- [🎯 Lab Objectives](#-lab-objectives)
- [📌 Prerequisites](#-prerequisites)
- [🖥️ Lab Environment Setup](#️-lab-environment-setup)
- [🗺️ Task 1: Wardley Mapping for DevSecOps](#️-task-1-wardley-mapping-for-devsecops)
- [🧩 Task 2: Cynefin Framework Application](#-task-2-cynefin-framework-application)
- [🔗 Task 3: Integration and Strategic Planning](#-task-3-integration-and-strategic-planning)
- [📊 Key Concepts: Wardley Evolution & Cynefin Domains](#-key-concepts-wardley-evolution--cynefin-domains)
- [🧯 Troubleshooting](#-troubleshooting)
- [✅ Conclusion](#-conclusion)

---

## 🎯 Lab Objectives

| # | Objective |
|---|-----------|
| 1 | Understand the fundamental concepts of DevSecOps strategic frameworks |
| 2 | Apply Wardley Mapping techniques to visualize DevSecOps value chains and dependencies |
| 3 | Utilize the Cynefin Framework to categorize and approach different types of DevSecOps challenges |
| 4 | Create strategic maps that inform decision-making in DevSecOps implementations |
| 5 | Analyze organizational readiness for DevSecOps adoption using strategic frameworks |
| 6 | Develop actionable insights for DevSecOps transformation initiatives |

## 📌 Prerequisites

| Requirement | Details |
|---|---|
| 🔄 SDLC Concepts | Basic understanding of software development lifecycle concepts |
| ⚙️ DevOps | Familiarity with DevOps principles and practices |
| 🛡️ Security Basics | Basic knowledge of security concepts in software development |
| 🐧 CLI | Ability to use command-line interfaces |
| 🏢 Change Management | Understanding of organizational change management concepts |

## 🖥️ Lab Environment Setup

> **☁️ Ready-to-Use Cloud Machines**
> Al Nafi provides pre-configured Linux-based cloud machines for this lab. Simply click **"Start Lab"** to access your environment — no need to build or configure your own virtual machine.

**Your cloud machine includes:**
- 🐧 Ubuntu 22.04 LTS with GUI desktop
- 🗺️ Pre-installed open-source tools for strategic mapping
- 🌐 Web browser with bookmarked resources
- 📝 Text editors and diagramming tools

**Lab Tasks Overview** — this lab consists of two main strategic framework exercises, brought together in a final integration task:
1. Wardley Mapping for DevSecOps
2. Cynefin Framework Application
3. Integration and Strategic Planning

---

## 🗺️ Task 1: Wardley Mapping for DevSecOps

![Wardley Mapping](https://img.shields.io/badge/OnlineWardleyMaps-2E3440?style=flat-square) ![Web Browser](https://img.shields.io/badge/Web_Browser-4285F4?style=flat-square&logo=googlechrome&logoColor=white)

### Subtask 1.1: Understanding Wardley Maps Fundamentals

#### 🪜 Step 1: Access the Wardley Mapping Tool

1. 🌐 Open your web browser in the cloud machine
2. 🔗 Navigate to the OnlineWardleyMaps tool at: **https://onlinewardleymaps.com**
3. ➕ Click **Create New Map** to start a new mapping session

#### 🪜 Step 2: Learn Wardley Map Components

Wardley Maps consist of four key elements:

| Element | Axis / Role | Description |
|---|---|---|
| 📈 Value Chain | Y-axis | Shows what users need, from visible user needs at the top to invisible components at the bottom |
| ⏩ Evolution | X-axis | Shows how components evolve from Genesis → Custom → Product → Commodity |
| 🧱 Components | — | The building blocks of your system |
| 🔗 Dependencies | — | Lines showing how components depend on each other |

#### 🪜 Step 3: Create Your First DevSecOps Value Chain

In the OnlineWardleyMaps interface, start by defining the user need, then enter the following basic value chain for a DevSecOps scenario:

```text
# 🗺️ Initial DevSecOps value chain — e-commerce platform
title DevSecOps Strategic Map - E-commerce Platform
anchor Business [0.95, 0.63]
component Customer [0.95, 0.9] label [19, -4]
component Secure Application [0.89, 0.8] label [2, 17]
component Development Team [0.82, 0.7]
component Security Testing [0.75, 0.65]
component CI/CD Pipeline [0.68, 0.6]
component Code Repository [0.61, 0.55]
component Infrastructure [0.54, 0.5]
component Monitoring [0.47, 0.45]
component Compliance [0.40, 0.4]

Business->Customer
Customer->Secure Application
Secure Application->Development Team
Secure Application->Security Testing
Development Team->CI/CD Pipeline
Security Testing->CI/CD Pipeline
CI/CD Pipeline->Code Repository
CI/CD Pipeline->Infrastructure
Infrastructure->Monitoring
Security Testing->Compliance
# TODO: Swap in your own organization's value chain components once you're comfortable with the syntax
```

4. 💾 Click **Save** to generate your map

### Subtask 1.2: Analyzing Component Evolution

#### 🪜 Step 4: Position Components on the Evolution Axis

Analyze each component's evolutionary stage:

| Stage | Range | Characteristics |
|---|---|---|
| 🌱 Genesis | 0.0 – 0.25 | Novel, uncertain, experimental |
| 🛠️ Custom | 0.25 – 0.50 | Emerging, developing, custom-built |
| 📦 Product | 0.50 – 0.75 | Mature, stable, product-based |
| 🔌 Commodity | 0.75 – 1.0 | Standardized, utility-like |

Update your map with proper evolution positioning:

```text
# 🗺️ Evolved DevSecOps value chain
title DevSecOps Strategic Map - E-commerce Platform (Evolved)
anchor Business [0.95, 0.63]
component Customer [0.95, 0.9] label [19, -4]
component Secure Application [0.89, 0.8] label [2, 17]
component Development Team [0.82, 0.7]
component Security Testing [0.35, 0.65]  // Custom-built security processes
component CI/CD Pipeline [0.65, 0.6]    // Product-based solutions
component Code Repository [0.85, 0.55]  // Commodity (Git)
component Infrastructure [0.75, 0.5]    // Moving toward commodity (Cloud)
component Monitoring [0.55, 0.45]       // Product-based tools
component Compliance [0.25, 0.4]        // Genesis/Custom (emerging practices)

Business->Customer
Customer->Secure Application
Secure Application->Development Team
Secure Application->Security Testing
Development Team->CI/CD Pipeline
Security Testing->CI/CD Pipeline
CI/CD Pipeline->Code Repository
CI/CD Pipeline->Infrastructure
Infrastructure->Monitoring
Security Testing->Compliance
```

#### 🪜 Step 5: Identify Strategic Opportunities

```bash
# 📝 Create a text file to document your analysis
nano devsecops_analysis.txt
```

Add the following analysis framework:

```text
DevSecOps Wardley Map Analysis
==============================

HIGH-LEVEL INSIGHTS:
1. Components in Genesis/Custom stages (high uncertainty):
   - Security Testing processes
   - Compliance frameworks
   - Custom security tooling

2. Components ready for productization:
   - Monitoring solutions
   - CI/CD pipeline components

3. Commodity opportunities:
   - Code repositories (already commoditized)
   - Infrastructure (cloud adoption)

STRATEGIC RECOMMENDATIONS:
1. Invest in custom security testing automation
2. Standardize compliance processes
3. Leverage commodity infrastructure
4. Build competitive advantage in security innovation
```

### Subtask 1.3: Creating Movement and Future State Maps

#### 🪜 Step 6: Map Future State Evolution

Create a second map showing expected evolution over 2–3 years:

```text
# 🗺️ Future-state DevSecOps value chain
title DevSecOps Future State Map (2-3 Years)
anchor Business [0.95, 0.63]
component Customer [0.95, 0.9]
component Secure Application [0.89, 0.8]
component Development Team [0.82, 0.7]
component Security Testing [0.55, 0.65]  // Evolved to Product
component CI/CD Pipeline [0.75, 0.6]     // More commoditized
component Code Repository [0.90, 0.55]   // Fully commodity
component Infrastructure [0.85, 0.5]     // Commodity cloud
component Monitoring [0.70, 0.45]        // Standardized products
component Compliance [0.45, 0.4]         // Custom to Product

Business->Customer
Customer->Secure Application
Secure Application->Development Team
Secure Application->Security Testing
Development Team->CI/CD Pipeline
Security Testing->CI/CD Pipeline
CI/CD Pipeline->Code Repository
CI/CD Pipeline->Infrastructure
Infrastructure->Monitoring
Security Testing->Compliance
```

#### 🪜 Step 7: Document Strategic Movements

```bash
# 📝 Update your analysis file
nano devsecops_analysis.txt
```

Add movement analysis:

```text
STRATEGIC MOVEMENTS (Current → Future):
========================================

1. Security Testing: Custom → Product
   - Action: Invest in security automation platforms
   - Timeline: 18-24 months
   - Investment: High

2. Compliance: Genesis → Product
   - Action: Develop standardized compliance frameworks
   - Timeline: 24-36 months
   - Investment: Medium

3. Infrastructure: Product → Commodity
   - Action: Complete cloud migration
   - Timeline: 12-18 months
   - Investment: Low (operational)

4. Monitoring: Product → Commodity
   - Action: Adopt standardized monitoring solutions
   - Timeline: 6-12 months
   - Investment: Low
```

<details>
<summary>🧯 Troubleshooting: OnlineWardleyMaps rejects your map syntax</summary>

The tool is whitespace- and syntax-sensitive. Common causes of a parse error:
- Coordinates outside the `[0.0, 1.0]` range for either axis
- A `component` referenced in a dependency line (`A->B`) before it's declared above it
- Mismatched or missing brackets around `label [x, y]` offsets

</details>

---

## 🧩 Task 2: Cynefin Framework Application

![Cynefin](https://img.shields.io/badge/Cynefin_Framework-4B0082?style=flat-square)

### Subtask 2.1: Understanding the Cynefin Framework

#### 🪜 Step 8: Create the Cynefin Framework Template

```bash
# 📝 Create a new text file for Cynefin analysis
nano cynefin_analysis.txt
```

Add the framework structure:

```text
CYNEFIN FRAMEWORK FOR DEVSECOPS CHALLENGES
==========================================

SIMPLE/OBVIOUS Domain:
- Characteristics: Best practices, clear cause-and-effect
- Approach: Sense → Categorize → Respond
- DevSecOps Examples:

COMPLICATED Domain:
- Characteristics: Good practices, analyzable cause-and-effect
- Approach: Sense → Analyze → Respond
- DevSecOps Examples:

COMPLEX Domain:
- Characteristics: Emergent practices, unpredictable cause-and-effect
- Approach: Probe → Sense → Respond
- DevSecOps Examples:

CHAOTIC Domain:
- Characteristics: Novel practices, no clear cause-and-effect
- Approach: Act → Sense → Respond
- DevSecOps Examples:

DISORDER Domain:
- Characteristics: Unclear which domain applies
- Approach: Break down and categorize
- DevSecOps Examples:
```

### Subtask 2.2: Categorizing DevSecOps Challenges

#### 🪜 Step 9: Populate Each Domain with DevSecOps Scenarios

```bash
# 📝 Update your Cynefin analysis with specific examples
nano cynefin_analysis.txt
```

Replace the content with:

```text
CYNEFIN FRAMEWORK FOR DEVSECOPS CHALLENGES
==========================================

SIMPLE/OBVIOUS Domain:
- Characteristics: Best practices, clear cause-and-effect
- Approach: Sense → Categorize → Respond
- DevSecOps Examples:
  * Implementing basic code scanning tools
  * Setting up standard firewall rules
  * Applying security patches for known vulnerabilities
  * Basic access control implementation
  * Standard SSL/TLS certificate installation

COMPLICATED Domain:
- Characteristics: Good practices, analyzable cause-and-effect
- Approach: Sense → Analyze → Respond
- DevSecOps Examples:
  * Designing secure microservices architecture
  * Implementing advanced threat detection systems
  * Creating custom security testing frameworks
  * Optimizing CI/CD pipeline security
  * Compliance framework implementation

COMPLEX Domain:
- Characteristics: Emergent practices, unpredictable cause-and-effect
- Approach: Probe → Sense → Respond
- DevSecOps Examples:
  * Cultural transformation to DevSecOps mindset
  * Balancing security and development velocity
  * Managing security in cloud-native environments
  * Implementing zero-trust architecture
  * Cross-team collaboration optimization

CHAOTIC Domain:
- Characteristics: Novel practices, no clear cause-and-effect
- Approach: Act → Sense → Respond
- DevSecOps Examples:
  * Responding to zero-day security exploits
  * Managing security during major system outages
  * Handling data breaches in real-time
  * Crisis management during security incidents
  * Emergency security patches deployment

DISORDER Domain:
- Characteristics: Unclear which domain applies
- Approach: Break down and categorize
- DevSecOps Examples:
  * Initial DevSecOps transformation planning
  * Unclear security requirements from stakeholders
  * Mixed feedback on security tool effectiveness
  * Conflicting priorities between teams
  * Ambiguous compliance requirements
```

### Subtask 2.3: Creating Decision-Making Strategies

#### 🪜 Step 10: Develop Response Strategies for Each Domain

```bash
# 📝 Create a strategy document
nano cynefin_strategies.txt
```

Add detailed response strategies:

```text
CYNEFIN-BASED DEVSECOPS DECISION STRATEGIES
===========================================

SIMPLE/OBVIOUS DOMAIN STRATEGIES:
- Use established security standards and frameworks
- Implement proven tools and practices
- Create checklists and standard operating procedures
- Focus on efficiency and consistency
- Automate routine security tasks

Example Implementation:
1. Deploy OWASP security scanning tools
2. Follow CIS security benchmarks
3. Implement standard patch management processes

COMPLICATED DOMAIN STRATEGIES:
- Engage security experts and specialists
- Conduct thorough analysis before implementation
- Use proven methodologies and frameworks
- Plan carefully with detailed requirements
- Leverage expert knowledge and experience

Example Implementation:
1. Hire security architects for system design
2. Conduct security risk assessments
3. Implement enterprise security frameworks

COMPLEX DOMAIN STRATEGIES:
- Run small experiments and pilots
- Encourage innovation and learning
- Create feedback loops and monitoring
- Build adaptive and flexible solutions
- Foster collaboration and knowledge sharing

Example Implementation:
1. Pilot DevSecOps practices with small teams
2. Implement continuous feedback mechanisms
3. Create communities of practice

CHAOTIC DOMAIN STRATEGIES:
- Take immediate action to stabilize
- Establish crisis management procedures
- Focus on rapid response and containment
- Communicate clearly and frequently
- Learn and adapt quickly

Example Implementation:
1. Activate incident response teams
2. Implement emergency communication protocols
3. Execute crisis management procedures

DISORDER DOMAIN STRATEGIES:
- Gather more information and context
- Break complex problems into smaller parts
- Consult with diverse stakeholders
- Use multiple perspectives and approaches
- Move issues to appropriate domains

Example Implementation:
1. Conduct stakeholder interviews
2. Perform situation analysis
3. Create problem decomposition frameworks
```

### Subtask 2.4: Practical Application Exercise

#### 🪜 Step 11: Apply Frameworks to Real Scenarios

```bash
# 📝 Create a practical exercise file
nano practical_exercise.txt
```

Work through this scenario:

> **PRACTICAL EXERCISE: E-COMMERCE PLATFORM SECURITY**
> Your organization is implementing DevSecOps for a new e-commerce platform. You face multiple challenges that need strategic approaches.
> <!-- TODO: Fill in Domain / Approach / Rationale for each challenge below before revealing the solution -->

| Challenge | Domain | Approach | Rationale |
|---|---|---|---|
| 1️⃣ Implementing container security scanning | ______ | ______ | ______ |
| 2️⃣ Building security culture across development teams | ______ | ______ | ______ |
| 3️⃣ Responding to a critical security vulnerability in production | ______ | ______ | ______ |
| 4️⃣ Designing a new authentication system | ______ | ______ | ______ |
| 5️⃣ Unclear security requirements from business stakeholders | ______ | ______ | ______ |

<details>
<summary>✅ Reveal Solution</summary>

| Challenge | Domain | Approach | Rationale |
|---|---|---|---|
| 1️⃣ Container security scanning | SIMPLE/OBVIOUS | Sense → Categorize → Respond | Container scanning tools are well-established with clear best practices |
| 2️⃣ Building security culture | COMPLEX | Probe → Sense → Respond | Cultural change involves human behavior and emergent practices |
| 3️⃣ Critical vulnerability in production | CHAOTIC | Act → Sense → Respond | Crisis situation requiring immediate action to prevent damage |
| 4️⃣ Designing a new authentication system | COMPLICATED | Sense → Analyze → Respond | Requires expert analysis and careful planning with known good practices |
| 5️⃣ Unclear security requirements | DISORDER | Break down and categorize | Need to gather information and clarify before determining the appropriate domain |

</details>

---

## 🔗 Task 3: Integration and Strategic Planning

![Strategy](https://img.shields.io/badge/Strategic_Integration-1e3a8a?style=flat-square)

### Subtask 3.1: Combining Wardley Maps with Cynefin Framework

#### 🪜 Step 12: Create an Integrated Strategic Analysis

```bash
# 📝 Create an integration document
nano integrated_strategy.txt
```

Combine insights from both frameworks:

```text
INTEGRATED DEVSECOPS STRATEGIC ANALYSIS
======================================

WARDLEY MAP INSIGHTS:
- Security Testing is in Custom stage (high uncertainty)
- Compliance is in Genesis stage (novel approaches needed)
- Infrastructure is moving toward Commodity
- CI/CD Pipeline is in Product stage

CYNEFIN FRAMEWORK INSIGHTS:
- Security Testing challenges are COMPLICATED (need expert analysis)
- Compliance challenges are COMPLEX (emergent practices needed)
- Infrastructure challenges are SIMPLE (best practices available)
- CI/CD Pipeline challenges are COMPLICATED (good practices exist)

STRATEGIC INTEGRATION:
1. Custom/Genesis + Complex = Innovation Focus
   - Security Testing automation
   - Compliance framework development
   - Approach: Probe → Sense → Respond

2. Product + Complicated = Optimization Focus
   - CI/CD Pipeline enhancement
   - Monitoring tool selection
   - Approach: Sense → Analyze → Respond

3. Commodity + Simple = Efficiency Focus
   - Infrastructure standardization
   - Code repository management
   - Approach: Sense → Categorize → Respond
```

### Subtask 3.2: Create Action Plan

#### 🪜 Step 13: Develop a Strategic Action Plan

```bash
# 📝 Update your integration document
nano integrated_strategy.txt
```

Add the action plan:

```text
STRATEGIC ACTION PLAN
====================

PHASE 1 (0-6 months): Stabilize and Standardize
- Focus: Simple/Obvious + Commodity components
- Actions:
  * Standardize infrastructure using cloud services
  * Implement basic security scanning tools
  * Establish standard code repository practices
- Investment: Low
- Risk: Low

PHASE 2 (6-18 months): Analyze and Optimize
- Focus: Complicated + Product components
- Actions:
  * Enhance CI/CD pipeline security
  * Implement advanced monitoring solutions
  * Develop security testing expertise
- Investment: Medium
- Risk: Medium

PHASE 3 (18-36 months): Innovate and Experiment
- Focus: Complex + Custom/Genesis components
- Actions:
  * Pilot innovative security testing approaches
  * Develop custom compliance frameworks
  * Build security culture and practices
- Investment: High
- Risk: High

CONTINUOUS: Crisis Management
- Focus: Chaotic + Disorder situations
- Actions:
  * Maintain incident response capabilities
  * Regular crisis simulation exercises
  * Continuous learning and adaptation
- Investment: Ongoing
- Risk: Variable
```

---

## 📊 Key Concepts: Wardley Evolution & Cynefin Domains

> This lab is strategic and organizational rather than a technical security control, so no MITRE ATT&CK mapping applies here — the tables below capture the core frameworks instead.

**Wardley Map Evolution Stages**

| Stage | Range | Characteristics |
|---|---|---|
| 🌱 Genesis | 0.0 – 0.25 | Novel, uncertain, experimental |
| 🛠️ Custom | 0.25 – 0.50 | Emerging, developing, custom-built |
| 📦 Product | 0.50 – 0.75 | Mature, stable, product-based |
| 🔌 Commodity | 0.75 – 1.0 | Standardized, utility-like |

**Cynefin Domains**

| Domain | Cause & Effect | Approach |
|---|---|---|
| 🟢 Simple/Obvious | Clear | Sense → Categorize → Respond |
| 🔵 Complicated | Analyzable | Sense → Analyze → Respond |
| 🟣 Complex | Unpredictable, emergent | Probe → Sense → Respond |
| 🔴 Chaotic | No clear cause-and-effect | Act → Sense → Respond |
| ⚪ Disorder | Unclear which domain applies | Break down and categorize |

---

## 🧯 Troubleshooting

<details>
<summary>🧯 Your Wardley Map components all cluster in the same spot</summary>

Coordinates in OnlineWardleyMaps are `[x, y]` with `x` = evolution (0 = Genesis, 1 = Commodity) and `y` = visibility (0 = invisible/back-end, 1 = user-visible). If components look bunched together, double-check you haven't transposed the two values.

</details>

<details>
<summary>🧯 <code>nano</code> won't save your file</summary>

Use `Ctrl+O` to write out the file, confirm the filename with `Enter`, then `Ctrl+X` to exit. If nano reports a permissions error, check you're saving inside your home directory rather than a system path.

</details>

---

## ✅ Conclusion

### 🏆 Key Accomplishments

By completing the tasks documented above, you have:
- **Mastered Wardley Mapping** — created strategic maps showing the evolution of DevSecOps components from Genesis to Commodity stages, identifying where to invest and where to leverage existing solutions
- **Applied the Cynefin Framework** — categorized different types of DevSecOps challenges into appropriate domains and developed context-appropriate response strategies
- **Integrated strategic frameworks** — combined insights from both frameworks into a comprehensive strategic analysis and an actionable, phased plan
- **Developed practical skills** — worked through real-world scenarios using open-source tools and frameworks that can be immediately applied in professional settings

### 🌍 Real-World Applications — Why This Matters

Strategic frameworks are essential for DevSecOps success because they:
- **Reduce risk** — help organizations make informed decisions about where to invest time and resources
- **Improve efficiency** — prevent over-engineering simple problems or under-analyzing complex ones
- **Enable innovation** — identify opportunities for competitive advantage through strategic positioning
- **Support decision-making** — provide structured approaches to handling uncertainty and complexity
- **Facilitate communication** — create a common language and understanding across teams and stakeholders

### 🚀 Next Steps

To continue building your DevSecOps strategic capabilities:
1. **Practice mapping** — apply Wardley Mapping to your current projects and organizational challenges
2. **Use Cynefin daily** — categorize problems you encounter using the Cynefin framework before deciding on an approach
3. **Share knowledge** — teach these frameworks to your team members and stakeholders
4. **Iterate and improve** — regularly update your strategic maps as situations evolve
5. **Combine with other tools** — integrate these frameworks with other strategic planning and risk management tools

The strategic thinking skills developed in this lab serve as the foundation for all subsequent DevSecOps implementation activities, ensuring that technical decisions stay aligned with business strategy and organizational context.

---

<div align="center">

### 🎓 Provided by Al Nafi

![Al Nafi](https://img.shields.io/badge/Al_Nafi-Cybersecurity_Education-1e3a8a?style=for-the-badge)

</div>
