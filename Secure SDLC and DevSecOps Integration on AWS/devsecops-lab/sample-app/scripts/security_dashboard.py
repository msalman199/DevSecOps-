#!/usr/bin/env python3
"""
Security Dashboard - Aggregate security findings from AWS services
"""
import boto3
import json
from datetime import datetime, timedelta

def get_security_hub_findings():
    """Get Security Hub findings"""
    client = boto3.client('securityhub', region_name='us-east-1')
    
    try:
        response = client.get_findings(
            Filters={
                'RecordState': [{'Value': 'ACTIVE', 'Comparison': 'EQUALS'}]
            },
            MaxResults=50
        )
        return response.get('Findings', [])
    except Exception as e:
        print(f"Error getting Security Hub findings: {e}")
        return []

def get_guardduty_findings():
    """Get GuardDuty findings"""
    client = boto3.client('guardduty', region_name='us-east-1')
    
    try:
        detectors = client.list_detectors()
        if not detectors['DetectorIds']:
            return []
        
        detector_id = detectors['DetectorIds'][0]
        findings = client.list_findings(DetectorId=detector_id)
        
        if findings['FindingIds']:
            detailed_findings = client.get_findings(
                DetectorId=detector_id,
                FindingIds=findings['FindingIds'][:10]  # Get first 10
            )
            return detailed_findings.get('Findings', [])
        return []
    except Exception as e:
        print(f"Error getting GuardDuty findings: {e}")
        return []

def get_config_compliance():
    """Get Config compliance status"""
    client = boto3.client('config', region_name='us-east-1')
    
    try:
        response = client.describe_compliance_by_config_rule()
        return response.get('ComplianceByConfigRules', [])
    except Exception as e:
        print(f"Error getting Config compliance: {e}")
        return []

def generate_dashboard():
    """Generate security dashboard"""
    print("=" * 60)
    print("DEVSECOPS SECURITY DASHBOARD")
    print("=" * 60)
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Security Hub findings
    print("🔍 SECURITY HUB FINDINGS")
    print("-" * 30)
    sh_findings = get_security_hub_findings()
    
    if sh_findings:
        severity_counts = {}
        for finding in sh_findings:
            severity = finding.get('Severity', {}).get('Label', 'UNKNOWN')
            severity_counts[severity] = severity_counts.get(severity, 0) + 1
        
        for severity, count in severity_counts.items():
            print(f"{severity}: {count}")
    else:
        print("No active findings")
    print()
    
    # GuardDuty findings
    print("🛡️  GUARDDUTY FINDINGS")
    print("-" * 30)
    gd_findings = get_guardduty_findings()
    
    if gd_findings:
        for finding in gd_findings[:5]:  # Show first 5
            print(f"• {finding.get('Title', 'Unknown threat')}")
            print(f"  Severity: {finding.get('Severity', 'Unknown')}")
    else:
        print("No threats detected")
    print()
    
    # Config compliance
    print("📋 CONFIG COMPLIANCE")
    print("-" * 30)
    config_rules = get_config_compliance()
    
    if config_rules:
        compliant = sum(1 for rule in config_rules if rule.get('Compliance', {}).get('ComplianceType') == 'COMPLIANT')
        total = len(config_rules)
        print(f"Compliant rules: {compliant}/{total}")
        
        non_compliant = [rule for rule in config_rules if rule.get('Compliance', {}).get('ComplianceType') == 'NON_COMPLIANT']
        if non_compliant:
            print("Non-compliant rules:")
            for rule in non_compliant[:3]:  # Show first 3
                print(f"• {rule.get('ConfigRuleName', 'Unknown rule')}")
    else:
        print("No Config rules found")
    print()
    
    print("=" * 60)
    print("Dashboard generation complete!")

if __name__ == "__main__":
    generate_dashboard()
