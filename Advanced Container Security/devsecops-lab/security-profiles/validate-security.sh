#!/bin/bash

echo "=== DevSecOps Security Validation ==="
echo

# Check Trivy installation
echo "1. Checking Trivy installation..."
if command -v trivy &> /dev/null; then
    echo "✓ Trivy is installed: $(trivy --version)"
else
    echo "✗ Trivy is not installed"
fi
echo

# Check Docker Content Trust
echo "2. Checking Docker Content Trust..."
if [ "$DOCKER_CONTENT_TRUST" = "1" ]; then
    echo "✓ Docker Content Trust is enabled"
else
    echo "✗ Docker Content Trust is not enabled"
fi
echo

# Check Kubernetes cluster
echo "3. Checking Kubernetes cluster..."
if kubectl cluster-info &> /dev/null; then
    echo "✓ Kubernetes cluster is accessible"
    kubectl get nodes
else
    echo "✗ Kubernetes cluster is not accessible"
fi
echo

# Check deployed applications
echo "4. Checking deployed applications..."
kubectl get deployments -n secure-apps
echo

# Check pod security contexts
echo "5. Checking pod security contexts..."
kubectl get pods -n secure-apps -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.securityContext}{"\n"}{end}'
echo

echo "=== Validation Complete ==="
