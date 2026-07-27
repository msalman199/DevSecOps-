#!/bin/bash

REPORT_DIR="../reports"
DATE=$(date +%Y%m%d_%H%M%S)

echo "Starting automated security checks..."

# Create reports directory if it doesn't exist
mkdir -p $REPORT_DIR

# Run Bandit scan
echo "Running Bandit security scan..."
cd ../src
bandit -r . -f json -o $REPORT_DIR/bandit-$DATE.json
bandit -r . -f txt -o $REPORT_DIR/bandit-$DATE.txt

# Run dependency check
echo "Running dependency vulnerability scan..."
cd ..
dependency-check --project "DevSecOps Demo" --scan src/ --format JSON --out $REPORT_DIR/dependency-check-$DATE.json

# Scan Docker images
echo "Scanning Docker images..."
for image in $(docker images --format "{{.Repository}}:{{.Tag}}" | grep devsecops-demo); do
    echo "Scanning $image..."
    trivy image --format json --output $REPORT_DIR/trivy-$image-$DATE.json $image
done

echo "Security checks completed. Reports saved in $REPORT_DIR/"
ls -la $REPORT_DIR/
