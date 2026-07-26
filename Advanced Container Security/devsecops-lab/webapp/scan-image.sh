#!/bin/bash

IMAGE_NAME=$1
SEVERITY_THRESHOLD="CRITICAL,HIGH"

if [ -z "$IMAGE_NAME" ]; then
    echo "Usage: $0 <image-name>"
    exit 1
fi

echo "Scanning image: $IMAGE_NAME"
echo "Severity threshold: $SEVERITY_THRESHOLD"

# Run Trivy scan
trivy image --severity $SEVERITY_THRESHOLD --format table $IMAGE_NAME

# Check for critical vulnerabilities and exit with error if found
CRITICAL_COUNT=$(trivy image --severity CRITICAL --format json $IMAGE_NAME | jq '.Results[]?.Vulnerabilities[]? | select(.Severity=="CRITICAL") | .VulnerabilityID' | wc -l)

if [ $CRITICAL_COUNT -gt 0 ]; then
    echo "ERROR: Found $CRITICAL_COUNT critical vulnerabilities. Build failed!"
    exit 1
else
    echo "SUCCESS: No critical vulnerabilities found. Image is ready for signing."
    exit 0
fi
