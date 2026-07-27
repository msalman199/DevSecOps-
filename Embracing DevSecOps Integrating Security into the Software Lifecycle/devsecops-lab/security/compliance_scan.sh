#!/bin/bash

echo "Starting OpenSCAP compliance scan..."

# Create results directory
mkdir -p compliance-results

# Run SCAP scan for Ubuntu
oscap xccdf eval \
    --profile xccdf_org.ssgproject.content_profile_standard \
    --results compliance-results/scap-results.xml \
    --report compliance-results/scap-report.html \
    openscap-content/scap-security-guide-*/ssg-ubuntu2004-ds.xml

echo "Compliance scan completed. Results saved in compliance-results/"
echo "HTML report: compliance-results/scap-report.html"
echo "XML results: compliance-results/scap-results.xml"

# Generate summary
oscap xccdf generate report compliance-results/scap-results.xml > compliance-results/summary-report.html

echo "Summary report generated: compliance-results/summary-report.html"
