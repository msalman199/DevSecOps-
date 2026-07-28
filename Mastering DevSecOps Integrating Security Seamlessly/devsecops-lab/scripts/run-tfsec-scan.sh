#!/bin/bash

echo "Starting Terraform security scanning with TFSec..."

# Create reports directory
mkdir -p iac-reports

# Run TFSec scan
tfsec terraform/ \
--format json \
--out iac-reports/tfsec-report.json

tfsec terraform/ \
--format html \
--out iac-reports/tfsec-report.html

tfsec terraform/ \
--format sarif \
--out iac-reports/tfsec-report.sarif

echo "TFSec scan completed. Reports available in iac-reports/"

# Display summary
if [ -f "iac-reports/tfsec-report.json" ]; then
    echo "Security issues found:"
    cat iac-reports/tfsec-report.json | jq '.results | length'
fi
