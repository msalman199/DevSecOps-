#!/usr/bin/env python3
import subprocess
import json
import sys
import os
from datetime import datetime

class SecurityScanner:
    def __init__(self, project_path):
        self.project_path = project_path
        self.results = {
            'timestamp': datetime.now().isoformat(),
            'scans': {}
        }
    
    def run_bandit_scan(self):
        """Run Bandit security scan for Python code"""
        print("Running Bandit security scan...")
        try:
            result = subprocess.run([
                'bandit', '-r', self.project_path, '-f', 'json'
            ], capture_output=True, text=True)
            
            if result.stdout:
                bandit_results = json.loads(result.stdout)
                self.results['scans']['bandit'] = {
                    'status': 'completed',
                    'issues_found': len(bandit_results.get('results', [])),
                    'details': bandit_results
                }
            else:
                self.results['scans']['bandit'] = {
                    'status': 'no_issues',
                    'issues_found': 0
                }
        except Exception as e:
            self.results['scans']['bandit'] = {
                'status': 'error',
                'error': str(e)
            }
    
    def run_semgrep_scan(self):
        """Run Semgrep security scan"""
        print("Running Semgrep security scan...")
        try:
            result = subprocess.run([
                'semgrep', '--config=auto', '--json', self.project_path
            ], capture_output=True, text=True)
            
            if result.stdout:
                semgrep_results = json.loads(result.stdout)
                self.results['scans']['semgrep'] = {
                    'status': 'completed',
                    'issues_found': len(semgrep_results.get('results', [])),
                    'details': semgrep_results
                }
            else:
                self.results['scans']['semgrep'] = {
                    'status': 'no_issues',
                    'issues_found': 0
                }
        except Exception as e:
            self.results['scans']['semgrep'] = {
                'status': 'error',
                'error': str(e)
            }
    
    def run_gitleaks_scan(self):
        """Run GitLeaks secret detection"""
        print("Running GitLeaks secret detection...")
        try:
            result = subprocess.run([
                'gitleaks', 'detect', '--source', self.project_path, '--report-format', 'json'
            ], capture_output=True, text=True)
            
            if result.stdout:
                try:
                    gitleaks_results = json.loads(result.stdout)
                    self.results['scans']['gitleaks'] = {
                        'status': 'completed',
                        'secrets_found': len(gitleaks_results) if isinstance(gitleaks_results, list) else 0,
                        'details': gitleaks_results
                    }
                except json.JSONDecodeError:
                    self.results['scans']['gitleaks'] = {
                        'status': 'no_secrets',
                        'secrets_found': 0
                    }
            else:
                self.results['scans']['gitleaks'] = {
                    'status': 'no_secrets',
                    'secrets_found': 0
                }
        except Exception as e:
            self.results['scans']['gitleaks'] = {
                'status': 'error',
                'error': str(e)
            }
    
    def generate_report(self):
        """Generate comprehensive security report"""
        total_issues = 0
        for scan_name, scan_result in self.results['scans'].items():
            if scan_name == 'bandit' or scan_name == 'semgrep':
                total_issues += scan_result.get('issues_found', 0)
            elif scan_name == 'gitleaks':
                total_issues += scan_result.get('secrets_found', 0)
        
        self.results['summary'] = {
            'total_security_issues': total_issues,
            'risk_level': self.calculate_risk_level(total_issues)
        }
        
        # Save results to file
        with open('security/security_report.json', 'w') as f:
            json.dump(self.results, f, indent=2)
        
        return self.results
    
    def calculate_risk_level(self, total_issues):
        """Calculate risk level based on number of issues"""
        if total_issues == 0:
            return 'LOW'
        elif total_issues <= 5:
            return 'MEDIUM'
        else:
            return 'HIGH'
    
    def run_all_scans(self):
        """Run all security scans"""
        self.run_bandit_scan()
        self.run_semgrep_scan()
        self.run_gitleaks_scan()
        return self.generate_report()

if __name__ == '__main__':
    project_path = sys.argv[1] if len(sys.argv) > 1 else '.'
    scanner = SecurityScanner(project_path)
    results = scanner.run_all_scans()
    
    print("\n" + "="*50)
    print("SECURITY SCAN RESULTS")
    print("="*50)
    print(f"Total Issues Found: {results['summary']['total_security_issues']}")
    print(f"Risk Level: {results['summary']['risk_level']}")
    print(f"Report saved to: security/security_report.json")
