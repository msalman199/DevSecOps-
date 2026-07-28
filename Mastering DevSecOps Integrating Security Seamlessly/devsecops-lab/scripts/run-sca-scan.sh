#!/bin/bash

echo "Starting Software Composition Analysis..."

# Create reports directory
mkdir -p sca-reports

# Run OWASP Dependency Check
dependency-check --project "DevSecOps Demo App" \
--scan . \
--format JSON \
--format HTML \
--format XML \
--out ./sca-reports/ \
--suppression suppression.xml

echo "SCA scan completed. Reports available in sca-reports/"

# Display summary
if [ -f "sca-reports/dependency-check-report.json" ]; then
    echo "Vulnerabilities found:"
    cat sca-reports/dependency-check-report.json | jq '.dependencies[].vulnerabilities | length' | awk '{sum+=$1} END {print "Total vulnerabilities: " sum}'
fi
