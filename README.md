# Hoder

Secure Cloud Backend login system for college project
A production-grade backend system built using FastAPI, PostgreSQL, Docker, AWS, and Linux security practices.

**Features**
- JWT Authentication
- Role-Based Access Control (RBAC)
- Secure REST APIs
- Dockerized Deployment
- Cloud Hosting (AWS EC2)
- Server Hardening & Security Scanning
- Monitoring & Logging

** Tech Stack**
- Backend: FastAPI (Python)
- Database: PostgreSQL
- Cloud: AWS EC2
- Security: JWT, Fail2ban, UFW, Nmap
- DevOps: Docker, GitHub Actions

**Architecture**
Client → API → Auth → Database → Cloud → Monitoring
cd secure-cloud-backend
docker-compose up -d
