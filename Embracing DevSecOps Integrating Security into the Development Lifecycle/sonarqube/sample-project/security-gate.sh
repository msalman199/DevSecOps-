#!/bin/bash

# Security Gate Script
# This script checks if the build meets security requirements

DEPENDENCY_CHECK_REPORT="dependency-check-report/dependency-check-report.json"
ZAP_REPORT="zap-reports/zap-report.json"

echo "=== DevSecOps Security Gate ==="

# Check if dependency check found high/critical vulnerabilities
if [ -f "$DEPENDENCY_CHECK_REPORT" ]; then
    HIGH_VULNS=$(jq '.dependencies[].vulnerabilities[]? | select(.severity == "HIGH" or .severity == "CRITICAL")' "$DEPENDENCY_CHECK_REPORT" | wc -l)
    
    if [ "$HIGH_VULNS" -gt 0 ]; then
        echo "❌ FAIL: Found $HIGH_VULNS high/critical vulnerabilities in dependencies"
        exit 1
    else
        echo "✅ PASS: No high/critical vulnerabilities found in dependencies"
    fi
else
    echo "⚠️  WARNING: Dependency check report not found"
fi

# Check ZAP scan results
if [ -f "$ZAP_REPORT" ]; then
    HIGH_ALERTS=$(jq '.site[].alerts[]? | select(.riskdesc | contains("High"))' "$ZAP_REPORT" | wc -l)
    
    if [ "$HIGH_ALERTS" -gt 0 ]; then
        echo "❌ FAIL: Found $HIGH_ALERTS high-risk security alerts"
        exit 1
    else
        echo "✅ PASS: No high-risk security alerts found"
    fi
else
    echo "⚠️  WARNING: ZAP scan report not found"
fi

echo "=== Security Gate: PASSED ==="
exit 0
