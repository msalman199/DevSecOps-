#!/bin/bash

# Create reports directory
mkdir -p reports/zap

# Start the application in background for testing
echo "Starting application for security testing..."
python3 src/app.py &
APP_PID=$!

# Wait for application to start
sleep 10

# Run ZAP baseline scan using Docker
docker run -v $(pwd)/reports/zap:/zap/wrk/:rw \
    -t owasp/zap2docker-stable zap-baseline.py \
    -t http://host.docker.internal:5000 \
    -J zap-report.json \
    -r zap-report.html

# Stop the application
kill $APP_PID

echo "ZAP security scan completed. Reports available in reports/zap/"
