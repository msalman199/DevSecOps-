<div align="center">

# 🔐 Advanced Identity and Access Management (IAM) in DevSecOps

### AWS IAM Privilege Escalation • Policy-as-Code with OPA Gatekeeper • Kubernetes Least Privilege

![AWS IAM](https://img.shields.io/badge/AWS%20IAM-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![OPA](https://img.shields.io/badge/Open%20Policy%20Agent-7D9199?style=for-the-badge&logo=openpolicyagent&logoColor=white)
![Rego](https://img.shields.io/badge/Rego-7D9199?style=for-the-badge&logoColor=white)
![RBAC](https://img.shields.io/badge/RBAC-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)

</div>

> ⚠️ **Authorized use only.** Task 1 deliberately provisions an over-permissive IAM trust policy and exploits it within your dedicated Al Nafi lab account. Only perform these steps in environments you own or are explicitly authorized to test — clean up the resources afterward using the steps provided.

---

## 📑 Table of Contents

- [🎯 Learning Objectives](#-learning-objectives)
- [📋 Prerequisites](#-prerequisites)
- [🖥️ Lab Environment Setup](#️-lab-environment-setup)
- [🔓 Task 1: AWS IAM Privilege Escalation](#-task-1-aws-iam-privilege-escalation)
- [🛡️ Task 2: OPA Policy-as-Code for Kubernetes](#️-task-2-opa-policy-as-code-for-kubernetes)
- [🗺️ MITRE ATT&CK Mapping](#️-mitre-attck-mapping)
- [🔧 Troubleshooting Tips](#-troubleshooting-tips)
- [🧹 Lab Cleanup](#-lab-cleanup)
- [🏁 Conclusion](#-conclusion)

---

## 🎯 Learning Objectives

| # | Objective |
|---|-----------|
| 1 | Understand the fundamentals of Identity and Access Management (IAM) in cloud environments |
| 2 | Identify and exploit privilege escalation vulnerabilities in AWS IAM trust policies |
| 3 | Implement Policy-as-Code using Open Policy Agent (OPA) for Kubernetes security |
| 4 | Configure least-privilege ServiceAccount bindings in Kubernetes |
| 5 | Apply security best practices for IAM in DevSecOps pipelines |
| 6 | Recognize common IAM misconfigurations and their security implications |

## 📋 Prerequisites

| Area | Requirement |
|------|-------------|
| ☁️ Cloud | Basic understanding of cloud computing concepts |
| 🐧 Linux | Familiarity with command line operations |
| 🔶 AWS | Basic knowledge of services and concepts |
| ☸️ Kubernetes | Understanding of fundamentals |
| 📝 YAML | Basic knowledge of file structure |
| 🗂️ JSON | Familiarity with the format |

## 🖥️ Lab Environment Setup

> ☁️ **Ready-to-Use Cloud Machines** — Al Nafi provides a pre-configured Linux-based cloud environment for this lab. Click **Start Lab** — no VM building or configuration required.

| Component | Purpose |
|---|---|
| 🐧 Ubuntu 20.04 LTS | Base OS, tools pre-installed |
| 🔶 AWS CLI (pre-configured) | Authenticated access to AWS IAM/STS/S3/EC2 |
| ☸️ kubectl | Kubernetes cluster access |
| 🛡️ Open Policy Agent (OPA) | Policy-as-Code engine, pre-installed |
| ☸️ Sample Kubernetes cluster | Target for Gatekeeper policies and RBAC |

---

## 🔓 Task 1: AWS IAM Privilege Escalation

![AWS IAM](https://img.shields.io/badge/AWS%20IAM-232F3E?style=flat-square&logo=amazon-aws&logoColor=white) ![AWS STS](https://img.shields.io/badge/AWS%20STS-232F3E?style=flat-square&logo=amazon-aws&logoColor=white)

> 📖 **Overview:** Identify and exploit an overly permissive IAM trust policy to demonstrate how common misconfigurations lead to privilege escalation.

### 📜 Subtask 1.1: Understanding IAM Trust Policies

```bash
# ✅ Step 1 — verify AWS CLI and current identity
aws --version
aws sts get-caller-identity
```

```bash
# 📝 Step 2 — trust policy that lets ANY AWS principal assume the role (intentional flaw)
cat > trust-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "*"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:RequestedRegion": "us-east-1"
        }
      }
    }
  ]
}
EOF
```

```bash
# 🚩 Step 3 — create the vulnerable role
aws iam create-role \
    --role-name VulnerableRole \
    --assume-role-policy-document file://trust-policy.json \
    --description "Demonstration role with overly permissive trust policy"
```

### 🔗 Subtask 1.2: Attaching Permissions to the Role

```bash
# 📝 Step 4 — permissions policy granting read access to S3/EC2
cat > permissions-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListAllMyBuckets",
        "s3:GetBucketLocation",
        "ec2:DescribeInstances"
      ],
      "Resource": "*"
    }
  ]
}
EOF
```

```bash
# 🔗 Step 5 — create and attach the policy
aws iam create-policy \
    --policy-name VulnerableRolePolicy \
    --policy-document file://permissions-policy.json \
    --description "Policy for vulnerable role demonstration"

# 🔎 look up the policy ARN
POLICY_ARN=$(aws iam list-policies --query 'Policies[?PolicyName==`VulnerableRolePolicy`].Arn' --output text)

# 📎 attach it to the role
aws iam attach-role-policy \
    --role-name VulnerableRole \
    --policy-arn $POLICY_ARN
```

### 🚨 Subtask 1.3: Exploiting the Privilege Escalation

```bash
# 🆔 Step 6 — get the role ARN
ROLE_ARN=$(aws iam get-role --role-name VulnerableRole --query 'Role.Arn' --output text)
echo "Role ARN: $ROLE_ARN"
```

```bash
# 🎭 Step 7 — assume the role via STS
aws sts assume-role \
    --role-arn $ROLE_ARN \
    --role-session-name "PrivilegeEscalationDemo" \
    --region us-east-1
```

```bash
# 🔑 Step 8 — extract and export the temporary credentials
ASSUME_ROLE_OUTPUT=$(aws sts assume-role \
    --role-arn $ROLE_ARN \
    --role-session-name "PrivilegeEscalationDemo" \
    --region us-east-1)

export AWS_ACCESS_KEY_ID=$(echo $ASSUME_ROLE_OUTPUT | jq -r '.Credentials.AccessKeyId')
export AWS_SECRET_ACCESS_KEY=$(echo $ASSUME_ROLE_OUTPUT | jq -r '.Credentials.SecretAccessKey')
export AWS_SESSION_TOKEN=$(echo $ASSUME_ROLE_OUTPUT | jq -r '.Credentials.SessionToken')

# ✅ confirm the new identity
aws sts get-caller-identity
```

```bash
# 🕵️ Step 9 — exercise the escalated privileges
aws s3 ls
aws ec2 describe-instances --query 'Reservations[].Instances[].{ID:InstanceId,State:State.Name}' --output table
```

### 🛡️ Subtask 1.4: Implementing Secure Trust Policies

```bash
# ✅ Step 10 — a properly scoped trust policy: specific principal + MFA + source IP
cat > secure-trust-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::ACCOUNT-ID:user/specific-user"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:RequestedRegion": "us-east-1"
        },
        "IpAddress": {
          "aws:SourceIp": "203.0.113.0/24"
        },
        "Bool": {
          "aws:MultiFactorAuthPresent": "true"
        }
      }
    }
  ]
}
EOF
```

```bash
# 🔄 Step 11 — replace the vulnerable trust policy with the secure one
aws iam update-assume-role-policy \
    --role-name VulnerableRole \
    --policy-document file://secure-trust-policy.json
```

---

## 🛡️ Task 2: OPA Policy-as-Code for Kubernetes

![OPA](https://img.shields.io/badge/Open%20Policy%20Agent-7D9199?style=flat-square&logo=openpolicyagent&logoColor=white) ![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)

> 📖 **Overview:** Enforce least-privilege ServiceAccount bindings in Kubernetes with OPA Gatekeeper, demonstrating Policy-as-Code principles.

### ⚙️ Subtask 2.1: Setting Up OPA Gatekeeper

```bash
# ✅ Step 1 — confirm cluster access
kubectl cluster-info
kubectl get nodes
```

```bash
# 🚀 Step 2 — install Gatekeeper
kubectl apply -f https://raw.githubusercontent.com/open-policy-agent/gatekeeper/release-3.14/deploy/gatekeeper.yaml
```

```bash
# ✅ Step 3 — verify the installation
kubectl get pods -n gatekeeper-system
kubectl wait --for=condition=Ready pod -l control-plane=controller-manager -n gatekeeper-system --timeout=300s
```

### 📐 Subtask 2.2: Creating Constraint Templates

```yaml
# 📐 Step 4 — serviceaccount-constraint-template.yaml
apiVersion: templates.gatekeeper.sh/v1beta1
kind: ConstraintTemplate
metadata:
  name: k8srequiredserviceaccount
spec:
  crd:
    spec:
      names:
        kind: K8sRequiredServiceAccount
      validation:
        type: object
        properties:
          allowedServiceAccounts:
            type: array
            items:
              type: string
          exemptNamespaces:
            type: array
            items:
              type: string
  targets:
    - target: admission.k8s.gatekeeper.sh
      rego: |
        package k8srequiredserviceaccount

        violation[{"msg": msg}] {
          input.review.kind.kind == "Pod"
          not exempt_namespace
          service_account := input.review.object.spec.serviceAccountName
          not allowed_service_account(service_account)
          msg := sprintf("Pod uses disallowed ServiceAccount '%v'. Allowed ServiceAccounts: %v", [service_account, input.parameters.allowedServiceAccounts])
        }

        violation[{"msg": msg}] {
          input.review.kind.kind == "Pod"
          not exempt_namespace
          not input.review.object.spec.serviceAccountName
          msg := "Pod must specify a ServiceAccount"
        }

        exempt_namespace {
          input.review.object.metadata.namespace == input.parameters.exemptNamespaces[_]
        }

        allowed_service_account(sa) {
          sa == input.parameters.allowedServiceAccounts[_]
        }
```

```bash
kubectl apply -f serviceaccount-constraint-template.yaml
```

```bash
# ✅ Step 5 — verify the template
kubectl get constrainttemplates
kubectl describe constrainttemplate k8srequiredserviceaccount
```

### 📏 Subtask 2.3: Creating and Applying Constraints

```yaml
# 📏 Step 6 — serviceaccount-constraint.yaml
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: K8sRequiredServiceAccount
metadata:
  name: must-use-approved-sa
spec:
  match:
    kinds:
      - apiGroups: [""]
        kinds: ["Pod"]
    excludedNamespaces: ["kube-system", "gatekeeper-system"]
  parameters:
    allowedServiceAccounts:
      - "default"
      - "app-service-account"
      - "monitoring-sa"
    exemptNamespaces:
      - "kube-system"
      - "gatekeeper-system"
```

```bash
kubectl apply -f serviceaccount-constraint.yaml
```

```bash
# ✅ Step 7 — verify the constraint is active
kubectl get k8srequiredserviceaccount
kubectl describe k8srequiredserviceaccount must-use-approved-sa
```

### 🧪 Subtask 2.4: Testing the OPA Policy

```bash
# 📁 Step 8 — test namespace
kubectl create namespace policy-test
```

```bash
# 👤 Step 9 — one approved, one unapproved ServiceAccount
kubectl create serviceaccount app-service-account -n policy-test
kubectl create serviceaccount unauthorized-sa -n policy-test
```

```yaml
# ✅ Step 10 — approved-pod.yaml (should be admitted)
apiVersion: v1
kind: Pod
metadata:
  name: approved-pod
  namespace: policy-test
spec:
  serviceAccountName: app-service-account
  containers:
  - name: nginx
    image: nginx:1.20
    ports:
    - containerPort: 80
```

```bash
kubectl apply -f approved-pod.yaml
```

```yaml
# 🚫 Step 11 — unapproved-pod.yaml (should be denied)
apiVersion: v1
kind: Pod
metadata:
  name: unapproved-pod
  namespace: policy-test
spec:
  serviceAccountName: unauthorized-sa
  containers:
  - name: nginx
    image: nginx:1.20
    ports:
    - containerPort: 80
```

```bash
kubectl apply -f unapproved-pod.yaml
```

```yaml
# 🚫 Step 12 — no-sa-pod.yaml (should be denied — no ServiceAccount specified)
apiVersion: v1
kind: Pod
metadata:
  name: no-sa-pod
  namespace: policy-test
spec:
  containers:
  - name: nginx
    image: nginx:1.20
    ports:
    - containerPort: 80
```

```bash
kubectl apply -f no-sa-pod.yaml
```

### 🔑 Subtask 2.5: Implementing RBAC with Least Privilege

```yaml
# 🔑 Step 13 — least-privilege-role.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: policy-test
  name: pod-reader
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list"]
- apiGroups: [""]
  resources: ["configmaps"]
  verbs: ["get"]
  resourceNames: ["app-config"]
```

```bash
kubectl apply -f least-privilege-role.yaml
```

```yaml
# 🔗 Step 14 — least-privilege-rolebinding.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: pod-reader-binding
  namespace: policy-test
subjects:
- kind: ServiceAccount
  name: app-service-account
  namespace: policy-test
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

```bash
kubectl apply -f least-privilege-rolebinding.yaml
```

```bash
# ✅ Step 15 — test the RBAC configuration
kubectl auth can-i get pods --as=system:serviceaccount:policy-test:app-service-account -n policy-test
kubectl auth can-i create pods --as=system:serviceaccount:policy-test:app-service-account -n policy-test
kubectl auth can-i delete pods --as=system:serviceaccount:policy-test:app-service-account -n policy-test
```

### 📦 Subtask 2.6: Advanced OPA Policy for Resource Limits

```yaml
# 📦 Step 16 — resource-limits-template.yaml
apiVersion: templates.gatekeeper.sh/v1beta1
kind: ConstraintTemplate
metadata:
  name: k8srequiredresources
spec:
  crd:
    spec:
      names:
        kind: K8sRequiredResources
      validation:
        type: object
        properties:
          limits:
            type: object
            properties:
              cpu:
                type: string
              memory:
                type: string
          requests:
            type: object
            properties:
              cpu:
                type: string
              memory:
                type: string
  targets:
    - target: admission.k8s.gatekeeper.sh
      rego: |
        package k8srequiredresources

        violation[{"msg": msg}] {
          input.review.kind.kind == "Pod"
          container := input.review.object.spec.containers[_]
          not container.resources.limits
          msg := sprintf("Container '%v' must specify resource limits", [container.name])
        }

        violation[{"msg": msg}] {
          input.review.kind.kind == "Pod"
          container := input.review.object.spec.containers[_]
          not container.resources.requests
          msg := sprintf("Container '%v' must specify resource requests", [container.name])
        }
```

```bash
kubectl apply -f resource-limits-template.yaml
```

```yaml
# 📦 Step 17 — resource-limits-constraint.yaml
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: K8sRequiredResources
metadata:
  name: must-have-resources
spec:
  match:
    kinds:
      - apiGroups: [""]
        kinds: ["Pod"]
    excludedNamespaces: ["kube-system", "gatekeeper-system"]
  parameters:
    limits:
      cpu: "500m"
      memory: "512Mi"
    requests:
      cpu: "100m"
      memory: "128Mi"
```

```bash
kubectl apply -f resource-limits-constraint.yaml
```

---

## 🗺️ MITRE ATT&CK Mapping

| Technique ID | Technique | How This Lab Addresses It |
|---|---|---|
| [T1548.005](https://attack.mitre.org/techniques/T1548/005/) | Abuse Elevation Control Mechanism: Temporary Elevated Cloud Access | Task 1's `sts assume-role` call against `VulnerableRole` obtains temporary elevated credentials through an overly permissive trust policy |
| [T1098.003](https://attack.mitre.org/techniques/T1098/003/) | Account Manipulation: Additional Cloud Roles | Attaching `VulnerableRolePolicy` and a wildcard-principal trust policy mirrors how an attacker grants themselves an additional assumable role |
| [T1078.004](https://attack.mitre.org/techniques/T1078/004/) | Valid Accounts: Cloud Accounts | Once assumed, the role's temporary credentials function as a valid — and over-privileged — cloud identity |
| [T1526](https://attack.mitre.org/techniques/T1526/) | Cloud Service Discovery | `aws s3 ls` and `aws ec2 describe-instances` enumerate account resources using the escalated credentials |
| [T1552.007](https://attack.mitre.org/techniques/T1552/007/) | Unsecured Credentials: Container API | Task 2's ServiceAccount and RBAC controls directly mitigate abuse of Kubernetes ServiceAccount tokens for lateral movement within a cluster |

---

## 🔧 Troubleshooting Tips

<details>
<summary>🔴 Issue 1: AWS CLI authentication errors</summary>

**Solution:** Verify your AWS credentials are properly configured
**Command:** `aws configure list`

</details>

<details>
<summary>🔴 Issue 2: Kubernetes cluster connection issues</summary>

**Solution:** Check your kubeconfig file and cluster status
**Command:** `kubectl config current-context`

</details>

<details>
<summary>🔴 Issue 3: OPA Gatekeeper pods not starting</summary>

**Solution:** Check cluster resources and node capacity
**Command:** `kubectl describe pods -n gatekeeper-system`

</details>

<details>
<summary>🔴 Issue 4: Constraint violations not working</summary>

**Solution:** Verify constraint template syntax and wait for propagation
**Command:** `kubectl get constrainttemplates -o yaml`

</details>

<details>
<summary>🔴 Issue 5: RBAC permission denied errors</summary>

**Solution:** Check ServiceAccount permissions and RoleBindings
**Command:** `kubectl describe rolebinding -n policy-test`

</details>

---

## 🧹 Lab Cleanup

```bash
# ☸️ Step 1 — clean up Kubernetes resources
kubectl delete namespace policy-test
kubectl delete constrainttemplates k8srequiredserviceaccount k8srequiredresources
kubectl delete -f https://raw.githubusercontent.com/open-policy-agent/gatekeeper/release-3.14/deploy/gatekeeper.yaml
```

```bash
# 🔶 Step 2 — clean up AWS resources
# 🔓 unset temporary credentials
unset AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_SESSION_TOKEN

# 🗑️ detach and delete the policy
aws iam detach-role-policy --role-name VulnerableRole --policy-arn $POLICY_ARN
aws iam delete-policy --policy-arn $POLICY_ARN

# 🗑️ delete the role
aws iam delete-role --role-name VulnerableRole

# 🧹 remove local files
rm -f trust-policy.json permissions-policy.json secure-trust-policy.json
rm -f *.yaml
```

---

## 🏁 Conclusion

In this comprehensive lab, you have successfully:

- 🔓 Identified and exploited AWS IAM privilege escalation vulnerabilities through overly permissive trust policies
- 🛡️ Implemented secure IAM practices by creating restrictive trust policies with proper conditions
- ⚙️ Deployed Open Policy Agent (OPA) Gatekeeper to enforce Policy-as-Code in Kubernetes
- 📐 Created and tested constraint templates to enforce least-privilege ServiceAccount bindings
- 🔑 Implemented RBAC configurations following the principle of least privilege
- 📦 Developed advanced OPA policies for resource management and security enforcement

### 🔑 Key Takeaways

**🛡️ Security Best Practices**
Always follow the principle of least privilege when configuring IAM roles and Kubernetes ServiceAccounts. Overly permissive policies can lead to serious security vulnerabilities.

**⚙️ Policy-as-Code Benefits**
Using OPA and Gatekeeper allows you to codify security policies, making them version-controlled, testable, and consistently enforceable across your Kubernetes clusters.

**🔁 DevSecOps Integration**
These IAM and policy management techniques are essential components of a mature DevSecOps pipeline, helping to shift security left and automate compliance checks.

**📊 Continuous Monitoring**
Regular auditing of IAM policies and Kubernetes RBAC configurations is crucial for maintaining a secure environment as your infrastructure evolves.

This lab provides a foundation for implementing advanced identity and access management practices in modern cloud-native environments, preparing you for real-world DevSecOps challenges.

</br>

<div align="center">

**📚 Provided by [Al Nafi](https://alnafi.com) — Cloud & Cybersecurity Training**

![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Training-blue?style=for-the-badge)

</div>
