#!/bin/bash

# Security Metrics Collection Script
METRICS_FILE="security-metrics.json"
DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

echo "Collecting security metrics..."

# Initialize metrics JSON
cat > "$METRICS_FILE" << EOL
{
  "timestamp": "$DATE",
  "sonarqube": {},
  "dependency_check": {},
  "zap": {}
}
EOL

# Collect SonarQube metrics (if available)
if command -v curl &> /dev/null; then
    SONAR_METRICS=$(curl -s "http://localhost:9000/api/measures/component?component=devsecops-demo&metricKeys=security_rating,reliability_rating,sqale_rating,coverage" || echo "{}")
    echo "$SONAR_METRICS" | jq '.component.measures' > temp_sonar.json 2>/dev/null || echo "[]" > temp_sonar.json
    jq --argjson sonar "$(cat temp_sonar.json)" '.sonarqube = $sonar' "$METRICS_FILE" > temp_metrics.json && mv temp_metrics.json "$METRICS_FILE"
    rm -f temp_sonar.json
fi

echo "Security metrics collected in $METRICS_FILE"
