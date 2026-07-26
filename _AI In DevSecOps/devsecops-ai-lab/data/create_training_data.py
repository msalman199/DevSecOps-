#!/usr/bin/env python3
import pandas as pd
import numpy as np
import json
import random
from datetime import datetime, timedelta

class VulnerabilityDataGenerator:
    def __init__(self):
        self.vulnerability_types = [
            'SQL_INJECTION', 'XSS', 'CSRF', 'BUFFER_OVERFLOW', 
            'HARDCODED_SECRETS', 'INSECURE_CRYPTO', 'PATH_TRAVERSAL',
            'COMMAND_INJECTION', 'LDAP_INJECTION', 'XXE'
        ]
        
        self.code_patterns = {
            'SQL_INJECTION': ['SELECT * FROM', 'INSERT INTO', 'UPDATE', 'DELETE FROM'],
            'XSS': ['innerHTML', 'document.write', 'eval(', 'render_template_string'],
            'HARDCODED_SECRETS': ['password =', 'api_key =', 'secret =', 'token ='],
            'PATH_TRAVERSAL': ['open(', 'file_get_contents', 'readFile', 'include'],
            'COMMAND_INJECTION': ['system(', 'exec(', 'shell_exec', 'subprocess.call']
        }
    
    def generate_code_features(self, has_vulnerability=False, vuln_type=None):
        """Generate code-based features"""
        features = {
            'lines_of_code': random.randint(10, 1000),
            'cyclomatic_complexity': random.randint(1, 20),
            'number_of_functions': random.randint(1, 50),
            'number_of_classes': random.randint(0, 10),
            'external_dependencies': random.randint(0, 20),
            'user_input_handling': random.randint(0, 10),
            'database_interactions': random.randint(0, 15),
            'file_operations': random.randint(0, 8),
            'network_operations': random.randint(0, 5),
            'crypto_operations': random.randint(0, 3)
        }
        
        if has_vulnerability and vuln_type:
            # Adjust features to make vulnerability more likely
            if vuln_type == 'SQL_INJECTION':
                features['database_interactions'] = random.randint(5, 15)
                features['user_input_handling'] = random.randint(3, 10)
            elif vuln_type == 'XSS':
                features['user_input_handling'] = random.randint(5, 10)
            elif vuln_type == 'HARDCODED_SECRETS':
                features['crypto_operations'] = random.randint(1, 3)
        
        return features
    
    def generate_metadata_features(self):
        """Generate metadata-based features"""
        return {
            'author_experience_months': random.randint(1, 120),
            'code_review_count': random.randint(0, 5),
            'time_since_last_commit_hours': random.randint(1, 168),
            'commit_size_changes': random.randint(1, 500),
            'is_weekend_commit': random.choice([0, 1]),
            'is_late_night_commit': random.choice([0, 1])
        }
    
    def generate_training_sample(self, has_vulnerability=False):
        """Generate a single training sample"""
        vuln_type = None
        if has_vulnerability:
            vuln_type = random.choice(self.vulnerability_types)
        
        sample = {}
        sample.update(self.generate_code_features(has_vulnerability, vuln_type))
        sample.update(self.generate_metadata_features())
        
        # Target variables
        sample['has_vulnerability'] = 1 if has_vulnerability else 0
        sample['vulnerability_type'] = vuln_type if has_vulnerability else 'NONE'
        sample['severity_score'] = random.uniform(0.1, 1.0) if has_vulnerability else 0.0
        
        return sample
    
    def generate_dataset(self, num_samples=1000, vulnerability_ratio=0.3):
        """Generate complete training dataset"""
        samples = []
        num_vulnerable = int(num_samples * vulnerability_ratio)
        num_clean = num_samples - num_vulnerable
        
        # Generate vulnerable samples
        for _ in range(num_vulnerable):
            samples.append(self.generate_training_sample(has_vulnerability=True))
        
        # Generate clean samples
        for _ in range(num_clean):
            samples.append(self.generate_training_sample(has_vulnerability=False))
        
        # Shuffle the dataset
        random.shuffle(samples)
        
        return pd.DataFrame(samples)

if __name__ == '__main__':
    generator = VulnerabilityDataGenerator()
    
    # Generate training dataset
    print("Generating training dataset...")
    train_data = generator.generate_dataset(num_samples=2000, vulnerability_ratio=0.3)
    train_data.to_csv('data/vulnerability_training_data.csv', index=False)
    
    # Generate test dataset
    print("Generating test dataset...")
    test_data = generator.generate_dataset(num_samples=500, vulnerability_ratio=0.3)
    test_data.to_csv('data/vulnerability_test_data.csv', index=False)
    
    print(f"Training data shape: {train_data.shape}")
    print(f"Test data shape: {test_data.shape}")
    print(f"Vulnerability distribution in training: {train_data['has_vulnerability'].value_counts()}")
    
    # Display sample data
    print("\nSample training data:")
    print(train_data.head())
