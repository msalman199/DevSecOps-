#!/usr/bin/env python3
import time
import subprocess
import sys

def run_zap_scan(target_url):
    """Run ZAP baseline scan"""
    cmd = [
        'zap-baseline.py',
        '-t', target_url,
        '-J', 'zap-report.json',
        '-r', 'zap-report.html'
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        print("ZAP scan completed")
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        print("ZAP scan timed out")
        return False
    except Exception as e:
        print(f"Error running ZAP scan: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 zap-automation.py <target_url>")
        sys.exit(1)
    
    target_url = sys.argv[1]
    success = run_zap_scan(target_url)
    sys.exit(0 if success else 1)
