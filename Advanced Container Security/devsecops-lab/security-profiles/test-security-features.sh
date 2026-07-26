#!/bin/bash

echo "=== Security Features Testing ==="
echo

# Test 1: Verify image scanning
echo "Test 1: Image Vulnerability Scanning"
echo "Scanning image for vulnerabilities..."
trivy image --severity HIGH,CRITICAL secure-webapp:v1.0 --format table
echo

# Test 2: Verify image signature
echo "Test 2: Image Signature Verification"
if [ ! -z "$DOCKERHUB_USERNAME" ]; then
    docker trust inspect $DOCKERHUB_USERNAME/secure-webapp:v1.0-signed
else
    echo "DOCKERHUB_USERNAME not set, skipping signature verification"
fi
echo

# Test 3: Test application functionality
echo "Test 3: Application Functionality Test"
kubectl port-forward -n secure-apps service/secure-webapp-hardened-service 8082:80 &
PF_PID=$!
sleep 5

if curl -s http://localhost:8082 | grep -q "Secure Container Demo"; then
    echo "✓ Application is responding correctly"
else
    echo "✗ Application is not responding correctly"
fi

kill $PF_PID 2>/dev/null
echo

# Test 4: Security context verification
echo "Test 4: Security Context Verification"
POD_NAME=$(kubectl get pods -n secure-apps -l app=secure-webapp-hardened -o jsonpath='{.items[0].metadata.name}')
if [ ! -z "$POD_NAME" ]; then
    echo "Checking security context for pod: $POD_NAME"
    kubectl get pod $POD_NAME -n secure-apps -o jsonpath='{.spec.containers[0].securityContext}' | jq .
else
    echo "No pods found for security context verification"
fi
echo

echo "=== Testing Complete ==="
