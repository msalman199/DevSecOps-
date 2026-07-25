#!/usr/bin/env python3
import json
import yaml
import os
from datetime import datetime

class ComplianceChecker:
    def __init__(self):
        self.compliance_results = {
            'owasp_top_10': {},
            'cwe_top_25': {},
            'documentation': {},
            'timestamp': datetime.now().isoformat()
        }
    
    def check_owasp_top_10(self, scan_results_dir):
        """Check compliance with OWASP Top 10"""
        print("Checking OWASP Top 10 compliance...")
        
        owasp_categories = {
            'A01_Broken_Access_Control': False,
            'A02_Cryptographic_Failures': False,
            'A03_Injection': False,
            'A04_Insecure_Design': False,
            'A05_Security_Misconfiguration': False,
            'A06_Vulnerable_Components': False,
            'A07_Authentication_Failures': False,
            'A08_Software_Integrity_Failures': False,
            'A09_Logging_Monitoring_Failures': False,
            'A10_SSRF': False
        }
        
        # Check for injection vulnerabilities
        bandit_file = os.path.join(scan_results_dir, 'sast-bandit.json')
        if os.path.exists(bandit_file):
            with open(bandit_file, 'r') as f:
                bandit_data = json.load(f)
            
            for result in bandit_data.get('results', []):
                test_id = result.get('test_id', '')
                if 'sql' in test_id.lower() or 'injection' in result.get('test_name', '').lower():
                    owasp_categories['A03_Injection'] = True
        
        # Check for vulnerable components
        safety_file = os.path.join(scan_results_dir, 'dependency-safety.json')
        if os.path.exists(safety_file):
            try:
                with open(safety_file, 'r') as f:
                    safety_data = json.load(f)
                if safety_data:
                    owasp_categories['A06_Vulnerable_Components'] = True
            except:
                pass
        
        self.compliance_results['owasp_top_10'] = owasp_categories
    
    def check_documentation_compliance(self):
        """Check documentation compliance"""
        print("Checking documentation compliance...")
        
        required_docs = {
            'security_policy': os.path.exists('security-policy.yaml'),
            'incident_response': os.path.exists('incident-response.md'),
            'security_training': os.path.exists('security-training.md'),
            'vulnerability_management': os.path.exists('vulnerability-management.md')
        }
        
        self.compliance_results['documentation'] = required_docs
    
    def generate_compliance_report(self):
        """Generate compliance report"""
        os.makedirs('../reports/level3', exist_ok=True)
        
        with open('../reports/level3/compliance-report.json', 'w') as f:
            json.dump(self.compliance_results, f, indent=2)
        
        # Generate human-readable report
        with open('../reports/level3/compliance-report.md', 'w') as f:
            f.write("# Level 3 Compliance Report\n\n")
            f.write(f"Generated: {self.compliance_results['timestamp']}\n\n")
            
            f.write("## OWASP Top 10 Compliance\n")
            for category, detected in self.compliance_results['owasp_top_10'].items():
                status = "⚠️ DETECTED" if detected else "✅ CLEAN"
                f.write(f"- {category}: {status}\n")
            
            f.write("\n## Documentation Compliance\n")
            for doc, exists in self.compliance_results['documentation'].items():
                status = "✅ EXISTS" if exists else "❌ MISSING"
                f.write(f"- {doc}: {status}\n")

if __name__ == "__main__":
    checker = ComplianceChecker()
    checker.check_owasp_top_10('../reports/level2')
    checker.check_documentation_compliance()
    checker.generate_compliance_report()
    print("Compliance check completed!")
