# Privacy Threat Model for Sample Web Application

## System Overview
- Web application with user registration and login
- SQLite database for user storage
- Session management for authentication

## LINDDUN Privacy Threats Analysis

### L - Linking
**Threat**: User activities can be linked across sessions
**Impact**: High - User behavior tracking
**Mitigation**: Implement session rotation, use pseudonymization

### I - Identifying
**Threat**: Users can be identified through email addresses
**Impact**: Medium - Personal identification possible
**Mitigation**: Hash email addresses, implement data minimization

### N - Non-repudiation
**Threat**: User actions are logged and cannot be denied
**Impact**: Low - Standard application behavior
**Mitigation**: Implement selective logging policies

### D - Detecting
**Threat**: User presence and activity patterns detectable
**Impact**: Medium - Privacy invasion through monitoring
**Mitigation**: Implement privacy-preserving analytics

### D - Data Disclosure
**Threat**: Sensitive user data exposed through database
**Impact**: High - Personal data breach
**Mitigation**: Encrypt sensitive data, implement access controls

### U - Unawareness
**Threat**: Users unaware of data collection practices
**Impact**: High - Lack of informed consent
**Mitigation**: Implement clear privacy notices, consent mechanisms

### N - Non-compliance
**Threat**: Application may violate privacy regulations
**Impact**: High - Legal and regulatory violations
**Mitigation**: Implement GDPR/CCPA compliance measures
