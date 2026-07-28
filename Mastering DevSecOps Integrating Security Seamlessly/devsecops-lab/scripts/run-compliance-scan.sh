#!/bin/bash

echo "Starting compliance validation with InSpec..."

# Create reports directory
mkdir -p compliance-reports

# Run InSpec compliance scan
inspec exec inspec-profiles/devsecops-compliance \
--reporter json:compliance-reports/inspec-report.json \
--reporter html:compliance-reports/inspec-report.html \
--reporter cli

echo "Compliance scan completed. Reports available in compliance-reports/"

# Display summary
if [ -f "compliance-reports/inspec-report.json" ]; then
    echo "Compliance summary:"
    cat compliance-reports/inspec-report.json | jq '.profiles[0].summary'
fi
