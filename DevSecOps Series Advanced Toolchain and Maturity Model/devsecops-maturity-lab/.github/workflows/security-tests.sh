#!/bin/bash

echo "Starting Level 2 Automated Security Testing..."

# Create reports directory
mkdir -p ../reports/level2

# Run SAST (Static Application Security Testing)
echo "Running Static Application Security Testing..."
bandit -r . -f json -o ../reports/level2/sast-bandit.json
semgrep --config=auto --json --output=../reports/level2/sast-semgrep.json .

# Run dependency scanning
echo "Running Dependency Vulnerability Scanning..."
safety check --json --output ../reports/level2/dependency-safety.json

# Run container scanning
echo "Running Container Security Scanning..."
trivy image --format json --output ../reports/level2/container-trivy.json sample-app:level2

# Run basic DAST (Dynamic Application Security Testing)
echo "Starting application for DAST..."
docker run -d -p 5000:5000 --name test-app sample-app:level2
sleep 5

# Install and run basic DAST with OWASP ZAP
docker run -t owasp/zap2docker-stable zap-baseline.py -t http://host.docker.internal:5000 -J ../reports/level2/dast-zap.json || true

# Cleanup
docker stop test-app
docker rm test-app

echo "Level 2 security testing completed!"
