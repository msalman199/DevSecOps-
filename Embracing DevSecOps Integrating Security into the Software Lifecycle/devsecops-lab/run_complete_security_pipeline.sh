#!/bin/bash

echo "========================================="
echo "DevSecOps Complete Security Pipeline"
echo "========================================="

# Step 1: Static Analysis
echo "Step 1: Running Static Application Security Testing..."
cd security
pip3 install bandit safety > /dev/null 2>&1
bandit -r ../src/ -f json -o
