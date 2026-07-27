#!/bin/bash

echo "=== OPA Policy Validation ==="

# 1. Validate Terraform plan against policies
if [ -f "infrastructure/terraform/tfplan.json" ]; then
    echo "1. Validating Terraform plan against OPA policies..."
    opa eval -d policies -i infrastructure/terraform/tfplan.json "data.terraform.deny[x]"
else
    echo "1. No Terraform plan found, skipping validation"
fi

# 2. Validate Docker configuration
echo "2. Validating Docker configuration..."
docker inspect devsecops-app 2>/dev/null | opa eval -d policies -I "data.docker.deny[x]" || echo "Container not running"

# 3. Validate application configuration
echo "3. Validating application configuration..."
cat > temp-app-config.json << 'TEMP_EOF'
{
    "environment": "development",
    "debug": true,
    "protocol": "http"
}
TEMP_EOF

opa eval -d policies -i temp-app-config.json "data.application.deny[x]"
rm temp-app-config.json

echo "=== OPA validation completed ==="
