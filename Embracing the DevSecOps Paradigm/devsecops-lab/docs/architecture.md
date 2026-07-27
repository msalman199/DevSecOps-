# DevSecOps Lab Application Architecture

## Overview
This document describes the architecture of our DevSecOps demonstration application.

## System Architecture

### Components

1. **Web Application Layer**
   - Flask-based Python web application
   - RESTful API endpoints
   - Static content serving

2. **Security Layer**
   - Authentication and authorization
   - Input validation
   - Security headers

3. **Data Layer**
   - Configuration management
   - Secret storage (Vault integration)

4. **Infrastructure Layer**
   - Containerized deployment (Docker)
   - Network security
   - Monitoring and logging

### Data Flow

1. User Request → Web Application
2. Application → Vault (for secrets)
3. Application → Data Processing
4. Response → User

### Security Boundaries

- Network boundary (firewall/security groups)
- Application boundary (authentication)
- Data boundary (encryption at rest/transit)

## Threat Model Scope

### Assets
- User data
- Application secrets
- Infrastructure configuration
- Source code

### Trust Boundaries
- Internet ↔ Application
- Application ↔ Vault
- Application ↔ Infrastructure

### Entry Points
- HTTP/HTTPS endpoints
- API endpoints
- Configuration files
- Environment variables
