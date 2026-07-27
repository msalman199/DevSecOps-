#!/usr/bin/env python3
import json
import os
from datetime import datetime

def generate_security_report():
    """Generate comprehensive security report"""
    
    report = {
        'timestamp': datetime.now().isoformat(),
        'project': 'DevSecOps Sample Application',
        'scans_performed': [],
        'summary': {
            'total_issues': 0,
            'high_severity': 0,
            'medium_severity': 0,
            'low_severity': 0
        },
        'recommendations': []
    }
    
    # Analyze Bandit results
    if os.path.exists('bandit-report.json'):
        with open('bandit-report.json', 'r') as f:
            bandit_data = json.load(f)
        
        bandit_summary = {
            'tool': 'Bandit',
            'type': 'Static Code Analysis',
            'issues_found': len(bandit_data.get('results', [])),
            'details': bandit_data.get('results', [])
        }
        
        report['scans_performed'].append(bandit_summary)
        
        for result in bandit_data.get('results', []):
            report['summary']['total_issues'] += 1
            if result['issue_severity'] == 'HIGH':
                report['summary']['high_severity'] += 1
            elif result['issue_severity'] == 'MEDIUM':
                report['summary']['medium_severity'] += 1
            else:
                report['summary']['low_severity'] += 1
    
    # Analyze Trivy results
    if os.path.exists('trivy-report.json'):
        with open('trivy-report.json', 'r') as f:
            trivy_data = json.load(f)
        
        total_vulns = 0
        if 'Results' in trivy_data:
            for result in trivy_data['Results']:
                if 'Vulnerabilities' in result:
                    total_vulns += len(result['Vulnerabilities'])
        
        trivy_summary = {
            'tool': 'Trivy',
            'type': 'Container Security Scan',
            'vulnerabilities_found': total_vulns
        }
        
        report['scans_performed'].append(trivy_summary)
    
    # Add recommendations
    if report['summary']['high_severity'] > 0:
        report['recommendations'].append("Immediately fix all high severity security issues before deployment")
    
    if report['summary']['medium_severity'] > 5:
        report['recommendations'].append("Review and fix medium severity issues")
    
    report['recommendations'].extend([
        "Implement regular security scanning in CI/CD pipeline",
        "Set up automated dependency updates",
        "Enable security monitoring and alerting",
        "Conduct regular security training for development team"
    ])
    
    # Save report
    with open('security-report.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    # Print summary
    print("=== SECURITY REPORT SUMMARY ===")
    print(f"Generated: {report['timestamp']}")
    print(f"Total Issues Found: {report['summary']['total_issues']}")
    print(f"  High Severity: {report['summary']['high_severity']}")
    print(f"  Medium Severity: {report['summary']['medium_severity']}")
    print(f"  Low Severity: {report['summary']['low_severity']}")
    print(f"\nScans Performed: {len(report['scans_performed'])}")
    for scan in report['scans_performed']:
        print(f"  - {scan['tool']} ({scan['type']})")
    
    print(f"\nRecommendations: {len(report['recommendations'])}")
    for i, rec in enumerate(report['recommendations'], 1):
        print(f"  {i}. {rec}")
    
    print(f"\nDetailed report saved to: security-report.json")

if __name__ == '__main__':
    generate_security_report()
