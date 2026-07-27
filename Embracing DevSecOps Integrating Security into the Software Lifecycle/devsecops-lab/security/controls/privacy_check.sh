#!/bin/bash

echo "Running automated privacy compliance checks..."

# Run InSpec privacy profile
inspec exec inspec-profiles/privacy-compliance \
    --reporter=json:privacy-results.json \
    --reporter=html:privacy-report.html \
    --reporter=cli

# Check results
if [ $? -eq 0 ]; then
    echo "All privacy compliance checks passed!"
else
    echo "Some privacy compliance checks failed. Review the reports."
fi

echo "Privacy compliance report generated: privacy-report.html"
echo "JSON results available: privacy-results.json"
