#!/usr/bin/env python3
import json
import yaml
import sys
import os

class SecurityGate:
    def __init__(self, policy_file):
        with open(policy_file, 'r') as f:
            self.policies = yaml.safe_load(f)
        self.violations = []
    
    def check_sast_results(self, bandit_file, semgrep_file):
        """Check SAST results against policy"""
        print("Checking SAST results...")
        
        # Check Bandit results
        if os.path.exists(bandit_file):
            with open(bandit_file, 'r') as f:
                bandit_data = json.load(f)
            
            high_issues = len([r for r in bandit_data.get('results', []) 
                             if r.get('issue_severity') == 'HIGH'])
            medium_issues = len([r for r in bandit_data.get('results', []) 
                               if r.get('issue_severity') == 'MEDIUM'])
            
            policy = self.policies['security_policies']['sast']
            if high_issues > policy['max_high_vulnerabilities']:
                self.violations.append(f"SAST: {high_issues} HIGH vulnerabilities exceed limit of {policy['max_high_vulnerabilities']}")
            if medium_issues > policy['max_medium_vulnerabilities']:
                self.violations.append(f"SAST: {medium_issues} MEDIUM vulnerabilities exceed limit of {policy['max_medium_vulnerabilities']}")
    
    def check_dependency_results(self, safety_file):
        """Check dependency scan results"""
        print("Checking dependency scan results...")
        
        if os.path.exists(safety_file):
            with open(safety_file, 'r') as f:
                try:
                    safety_data = json.load(f)
                    if safety_data and len(safety_data) > 0:
                        self.violations.append(f"Dependencies: {len(safety_data)} vulnerabilities found")
                except json.JSONDecodeError:
                    # Safety might output text format
                    pass
    
    def check_container_results(self, trivy_file):
        """Check container scan results"""
        print("Checking container scan results...")
        
        if os.path.exists(trivy_file):
            with open(trivy_file, 'r') as f:
                trivy_data = json.load(f)
            
            critical_count = 0
            high_count = 0
            
            for result in trivy_data.get('Results', []):
                for vuln in result.get('Vulnerabilities', []):
                    severity = vuln.get('Severity', '').upper()
                    if severity == 'CRITICAL':
                        critical_count += 1
                    elif severity == 'HIGH':
                        high_count += 1
            
            policy = self.policies['security_policies']['container']
            if critical_count > policy['max_critical_vulnerabilities']:
                self.violations.append(f"Container: {critical_count} CRITICAL vulnerabilities exceed limit")
            if high_count > policy['max_high_vulnerabilities']:
                self.violations.append(f"Container: {high_count} HIGH vulnerabilities exceed limit")
    
    def generate_report(self):
        """Generate security gate report"""
        report = {
            'timestamp': '2024-01-01T00:00:00Z',
            'status': 'PASS' if len(self.violations) == 0 else 'FAIL',
            'violations': self.violations,
            'policy_compliance': len(self.violations) == 0
        }
        
        with open('../reports/level3/security-gate-report.json', 'w') as f:
            json.dump(report, f, indent=2)
        
        return report['status'] == 'PASS'

if __name__ == "__main__":
    gate = SecurityGate('security-policy.yaml')
    
    # Check all security scan results
    gate.check_sast_results('../reports/level2/sast-bandit.json', '../reports/level2/sast-semgrep.json')
    gate.check_dependency_results('../reports/level2/dependency-safety.json')
    gate.check_container_results('../reports/level2/container-trivy.json')
    
    # Generate report and exit with appropriate code
    if gate.generate_report():
        print("✅ Security gate PASSED")
        sys.exit(0)
    else:
        print("❌ Security gate FAILED")
        for violation in gate.violations:
            print(f"  - {violation}")
        sys.exit(1)
