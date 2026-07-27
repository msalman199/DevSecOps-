#!/bin/bash

echo "=== DevSecOps Security Monitoring Report ==="
echo "Generated on: $(date)"
echo ""

# Check for running containers
echo "=== Running Containers ==="
docker ps --format "table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}"
echo ""

# Check for security updates
echo "=== System Security Updates ==="
apt list --upgradable 2>/dev/null | grep -i security | head -5
echo ""

# Check disk usage
echo "=== Disk Usage ==="
df -h / | tail -1
echo ""

# Check for failed login attempts
echo "=== Recent Failed Login Attempts ==="
grep "Failed password" /var/log/auth.log 2>/dev/null | tail -5 || echo "No failed login attempts found"
echo ""

# Generate summary
echo "=== Security Summary ==="
echo "- Containers running: $(docker ps -q | wc -l)"
echo "- Security updates available: $(apt list --upgradable 2>/dev/null | grep -i security | wc -l)"
echo "- System uptime: $(uptime -p)"
echo ""
echo "=== End of Report ==="
