#!/bin/bash

DEFECTDOJO_URL="http://localhost:8080"
API_TOKEN="your-api-token-here"  # Replace with actual token after setup

echo "Uploading scan results to DefectDojo..."

# Function to upload scan results
upload_scan() {
    local scan_type=$1
    local file_path=$2
    local engagement_id=$3
    
    if [ -f "$file_path" ]; then
        echo "Uploading $scan_type results..."
        curl -X POST "$DEFECTDOJO_URL/api/v2/import-scan/" \
        -H "Authorization: Token $API_TOKEN" \
        -F "scan_type=$scan_type" \
        -F "file=@$file_path" \
        -F "engagement=$engagement_id" \
        -F "active=true" \
        -F "verified=false"
    else
        echo "File $file_path not found, skipping $scan_type upload"
    fi
}

# Upload different scan results
upload_scan "SonarQube Scan" "sonar-report.json" "1"
upload_scan "Dependency Check Scan" "sca-reports/dependency-check-report.json" "1"
upload_scan "ZAP Scan" "dast-reports/dast-report.json" "1"
upload_scan "Terrascan Scan" "iac-reports/tfsec-report.json" "1"

echo "Upload completed!"
