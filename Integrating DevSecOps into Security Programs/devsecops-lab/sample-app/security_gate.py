#!/usr/bin/env python3
import json
import sys
import os

def check_bandit_results(report_file='bandit-report.json'):
    """Check Bandit scan results against security gates"""
    
    if not os.path.exists(report_file):
        print("Bandit report not found!")
        return False
    
    with open(report_file, 'r') as f:
        report = json.load(f)
    
    high_severity_issues = 0
    medium_severity_issues = 0
    
    for result in report.get('results', []):
        if result['issue_severity'] == 'HIGH':
            high_severity_issues += 1
        elif result['issue_severity'] == 'MEDIUM':
            medium_severity_issues += 1
    
    print(f"Security Gate Check - Bandit Results:")
    print(f"  High severity issues: {high_severity_issues}")
    print(f"  Medium severity issues: {medium_severity_issues}")
    
    # Define security gates
    if high_severity_issues > 0:
        print("❌ SECURITY GATE FAILED: High severity issues found!")
        return False
    
    if medium_severity_issues > 5:
        print("❌ SECURITY GATE FAILED: Too many medium severity issues!")
        return False
    
    print("✅ SECURITY GATE PASSED: Bandit scan")
    return True

def check_dependency_results(report_file='safety-report.json'):
    """Check dependency scan results"""
    
    if not os.path.exists(report_file):
        print("Safety report not found!")
        return False
    
    try:
        with open(report_file, 'r') as f:
            report = json.load(f)
        
        vulnerabilities = len(report)
        print(f"Security Gate Check - Dependencies:")
        print(f"  Vulnerable dependencies: {vulnerabilities}")
        
        if vulnerabilities > 0:
            print("❌ SECURITY GATE FAILED: Vulnerable dependencies found!")
            return False
        
        print("✅ SECURITY GATE PASSED: Dependency scan")
        return True
    except json.JSONDecodeError:
        print("✅ SECURITY GATE PASSED: No vulnerabilities in dependencies")
        return True

def main():
    """Main security gate check"""
    print("Running Security Quality Gates...")
    
    bandit_passed = check_bandit_results()
    safety_passed = check_dependency_results()
    
    if bandit_passed and safety_passed:
        print("\n🎉 ALL SECURITY GATES PASSED! Deployment approved.")
        sys.exit(0)
    else:
        print("\n🚫 SECURITY GATES FAILED! Deployment blocked.")
        sys.exit(1)

if __name__ == '__main__':
    main()
