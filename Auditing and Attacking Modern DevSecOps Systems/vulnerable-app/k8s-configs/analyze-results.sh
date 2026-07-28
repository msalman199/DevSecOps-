#!/bin/bash

echo "=== KubeLinter Security Analysis Summary ==="
echo

# Count total issues
TOTAL_ISSUES=$(kube-linter lint k8s-configs/ --format json | jq '.Reports | length')
echo "Total Security Issues Found: $TOTAL_ISSUES"
echo

# Group by severity
echo "Issues by Category:"
kube-linter lint k8s-configs/ --format json | jq -r '.Reports[] | .Check' | sort | uniq -c | sort -nr

echo
echo "=== Detailed Issues ==="
kube-linter lint k8s-configs/ --format json | jq -r '.Reports[] | "File: \(.Object.K8sObject.Name) | Check: \(.Check) | Message: \(.Message)"'
