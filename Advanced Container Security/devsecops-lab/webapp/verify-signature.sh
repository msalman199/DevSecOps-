#!/bin/bash

IMAGE_NAME=$1

if [ -z "$IMAGE_NAME" ]; then
    echo "Usage: $0 <image-name>"
    exit 1
fi

echo "Verifying signature for image: $IMAGE_NAME"

# Check if image is signed
if docker trust inspect $IMAGE_NAME > /dev/null 2>&1; then
    echo "SUCCESS: Image signature verified!"
    docker trust inspect $IMAGE_NAME
    exit 0
else
    echo "ERROR: Image signature verification failed!"
    exit 1
fi
