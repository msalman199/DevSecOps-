#!/bin/bash

echo "=== Terraform Security Validation ==="

# Navigate to Terraform directory
cd infrastructure/terraform

# 1. Terraform format check
echo "1. Checking Terraform formatting..."
terraform fmt -check -recursive

# 2. Terraform validation
echo "2. Validating Terraform configuration..."
terraform validate

# 3. Security scanning with tfsec
echo "3. Running security scan with tfsec..."
tfsec . --format lovely

# 4. Plan validation
echo "4. Creating and validating Terraform plan..."
terraform plan -out=tfplan

# 5. Policy validation (if OPA policies exist)
if [ -f "../../policies/terraform.rego" ]; then
    echo "5. Validating against OPA policies..."
    terraform show -json tfplan > tfplan.json
    opa eval -d ../../policies -i tfplan.json "data.terraform.deny[x]"
fi

echo "=== Terraform validation completed ==="
