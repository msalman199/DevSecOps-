#!/bin/bash

# Create scripts directory if it doesn't exist
mkdir -p scripts

# Download OWASP Dependency Check
DEPENDENCY_CHECK_VERSION="8.4.0"
wget -O dependency-check.zip "https://github.com/jeremylong/DependencyCheck/releases/download/v${DEPENDENCY_CHECK_VERSION}/dependency-check-${DEPENDENCY_CHECK_VERSION}-release.zip"

# Extract and setup
unzip dependency-check.zip
mv dependency-check dependency-check-tool

# Run dependency check
./dependency-check-tool/bin/dependency-check.sh \
    --project "DevSecOps Lab" \
    --scan . \
    --format HTML \
    --format JSON \
    --out reports/dependency-check

echo "Dependency check completed. Reports available in reports/dependency-check/"
