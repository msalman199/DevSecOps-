#!/usr/bin/env python3
import json
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import os
import pickle

class DevSecOpsPredictiveAnalytics:
    def __init__(self):
        self.historical_data = []
        self.model_path = 'models/vulnerability_predictor.pkl'
        
    def load_historical_data(self):
        """Load historical security scan data"""
        # Simulate historical data for demonstration
        historical_data = [
            {'date': '2024-01-01', 'vulnerabilities': 5, 'code_changes': 20, 'team_size': 3, 'deployment_frequency': 2},
            {'date': '2024-01-02', 'vulnerabilities': 3, 'code_changes': 15, 'team_size': 3, 'deployment_frequency': 1},
            {'date': '2024-01-03', 'vulnerabilities': 7, 'code_changes': 35, 'team_size': 4, 'deployment_frequency': 3},
            {'date': '2024-01-04', 'vulnerabilities': 2, 'code_changes': 10, 'team_size': 3, 'deployment_frequency': 1},
            {'date': '2024-01-05', 'vulnerabilities': 8, 'code_changes': 40, 'team_size': 5, 'deployment_frequency': 4},
        ]
        
        self.historical_data = pd.DataFrame(historical_data)
        self.historical_data['date'] = pd.to_datetime(self.historical_data['date'])
        
    def analyze_vulnerability_trends(self):
        """Analyze vulnerability trends over time"""
        if len(self.historical_data) == 0:
            self.load_historical_data()
            
        # Calculate moving average
        self.historical_data['vulnerability_trend'] = self.historical_data['vulnerabilities'].rolling(window=3).mean()
        
        # Calculate correlation between code changes and vulnerabilities
        correlation = self.historical_data['code_changes'].corr(self.historical_data['vulnerabilities'])
        
        return {
            'trend_analysis': {
                'average_vulnerabilities': self.historical_data['vulnerabilities'].mean(),
                'vulnerability_trend': 'increasing' if self.historical_data['vulnerabilities'].iloc[-1] > self.historical_data['vulnerabilities'].mean() else 'decreasing',
                'code_vulnerability_correlation': correlation
            }
        }
    
    def predict_deployment_risk(self, code_changes, team_size, deployment_frequency):
        """Predict deployment risk based on current metrics"""
        # Simple risk calculation based on historical patterns
        base_risk = 0.1
        
        # Risk increases with code changes
        change_risk = min(code_changes * 0.01, 0.5)
        
        # Risk decreases with larger team (more reviews)
        team_risk_reduction = max(0, (team_size - 2) * 0.05)
        
        # Risk increases with deployment frequency
        frequency_risk = deployment_frequency * 0.05
        
        total_risk = base_risk + change_risk + frequency_risk - team_risk_reduction
        total_risk = max(0, min(1, total_risk))  # Clamp between 0 and 1
        
        risk_level = 'LOW' if total_risk < 0.3 else 'MEDIUM' if total_risk < 0.7 else 'HIGH'
        
        return {
            'risk_score': total_risk,
            'risk_level': risk_level,
            'recommendations': self.generate_recommendations(total_risk, code_changes, team_size)
        }
    
    def generate_recommendations(self, risk_score, code_changes, team_size):
        """Generate recommendations based on risk analysis"""
        recommendations = []
        
        if risk_score > 0.7:
            recommendations.append("HIGH RISK: Consider additional security reviews before deployment")
            recommendations.append("Implement staged rollout strategy")
            
        if code_changes > 30:
            recommendations.append("Large number of code changes detected - increase testing coverage")
            
        if team_size < 3:
            recommendations.append("Small team size - consider peer reviews for all changes")
            
        if risk_score < 0.3:
            recommendations.append("Low risk deployment - proceed with standard pipeline")
            
        return recommendations
    
    def generate_predictive_report(self):
        """Generate comprehensive predictive analytics report"""
        trend_analysis = self.analyze_vulnerability_trends()
        
        # Simulate current deployment metrics
        current_metrics = {
            'code_changes': 25,
            'team_size': 3,
            'deployment_frequency': 2
        }
        
        risk_prediction = self.predict_deployment_risk(
            current_metrics['code_changes'],
            current_metrics['team_size'],
            current_metrics['deployment_frequency']
        )
        
        report = {
            'timestamp': datetime.now().isoformat(),
            'trend_analysis': trend_analysis,
            'current_deployment_risk': risk_prediction,
            'current_metrics': current_metrics
        }
        
        # Save report
        with open('ci-cd/predictive_report.json', 'w') as f:
            json.dump(report, f, indent=2)
            
        return report
    
    def display_dashboard(self, report):
        """Display predictive analytics dashboard"""
        print("\n" + "="*60)
        print("DEVSECOPS PREDICTIVE ANALYTICS DASHBOARD")
        print("="*60)
        
        print(f"\nCURRENT DEPLOYMENT RISK: {report['current_deployment_risk']['risk_level']}")
        print(f"Risk Score: {report['current_deployment_risk']['risk_score']:.2f}")
        
        print(f"\nCURRENT METRICS:")
        print(f"  Code Changes: {report['current_metrics']['code_changes']}")
        print(f"  Team Size: {report['current_metrics']['team_size']}")
        print(f"  Deployment Frequency: {report['current_metrics']['deployment_frequency']}")
        
        print(f"\nTREND ANALYSIS:")
        trend = report['trend_analysis']['trend_analysis']
        print(f"  Average Vulnerabilities: {trend['average_vulnerabilities']:.1f}")
        print(f"  Vulnerability Trend: {trend['vulnerability_trend']}")
        print(f"  Code-Vulnerability Correlation: {trend['code_vulnerability_correlation']:.2f}")
        
        print(f"\nRECOMMENDATIONS:")
        for rec in report['current_deployment_risk']['recommendations']:
            print(f"  • {rec}")
        
        print("\n" + "="*60)

if __name__ == '__main__':
    analytics = DevSecOpsPredictiveAnalytics()
    report = analytics.generate_predictive_report()
    analytics.display_dashboard(report)
