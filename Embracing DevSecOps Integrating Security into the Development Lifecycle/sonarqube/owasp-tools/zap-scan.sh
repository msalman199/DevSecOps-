#!/bin/bash

# ZAP Baseline Scan Script
TARGET_URL=$1
REPORT_DIR=$2

if [ -z "$TARGET_URL" ] || [ -z "$REPORT_DIR" ]; then
    echo "Usage: $0 <target_url> <report_directory>"
    exit 1
fi

echo "Starting ZAP baseline scan for: $TARGET_URL"

# Run ZAP baseline scan
docker run -v $REPORT_DIR:/zap/wrk/:rw \
    -t owasp/zap2docker-stable \
    zap-baseline.py \
    -t $TARGET_URL \
    -J zap-report.json \
    -H zap-report.html \
    -r zap-report.md

echo "ZAP scan completed. Reports saved to: $REPORT_DIR"
