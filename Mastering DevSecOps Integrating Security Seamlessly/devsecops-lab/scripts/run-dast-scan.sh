#!/bin/bash

echo "Starting Dynamic Application Security Testing..."

# Create reports directory
mkdir -p dast-reports

# Start the application in background
echo "Starting application..."
docker run -d --name dast-test-app -p 3000:3000 devsecops-demo:latest

# Wait for application to start
sleep 15

# Check if application is running
if curl -f http://localhost:3000/health; then
    echo "Application is running, starting DAST scan..."
    
    # Run ZAP baseline scan
    docker run -v $(pwd)/dast-reports:/zap/wrk/:rw \
    -t owasp/zap2docker-stable zap-baseline.py \
    -t http://host.docker.internal:3000 \
    -J dast-report.json \
    -r dast-report.html
    
    echo "DAST scan completed."
else
    echo "Application failed to start. Skipping DAST scan."
fi

# Clean up
docker stop dast-test-app 2>/dev/null
docker rm dast-test-app 2>/dev/null

echo "DAST reports available in dast-reports/"
