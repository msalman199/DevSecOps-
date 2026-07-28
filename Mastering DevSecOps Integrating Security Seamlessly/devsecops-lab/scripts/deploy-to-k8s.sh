#!/bin/bash

echo "Deploying application to Kubernetes..."

# Build and load image
echo "Building Docker image..."
docker build -t devsecops-demo:latest .

echo "Loading image to Minikube..."
minikube image load devsecops-demo:latest

# Deploy to Kubernetes
echo "Applying Kubernetes manifests..."
kubectl apply -f k8s-manifests/

# Wait for deployment
echo "Waiting for deployment to be ready..."
kubectl wait --for=condition=available --timeout=300s deployment/devsecops-demo-app -n devsecops-demo

# Display status
echo "Deployment status:"
kubectl get pods -n devsecops-demo
kubectl get services -n devsecops-demo

# Get application URL
echo "Application URL:"
minikube service devsecops-demo-service -n devsecops-demo --url

echo "Deployment completed!"
