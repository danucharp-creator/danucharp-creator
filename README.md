# 🐋 Production-Ready Python DevSecOps CI/CD Pipeline

A robust, enterprise-grade DevSecOps Continuous Integration and Continuous Deployment (CI/CD) pipeline. This project automates code quality analysis, enforces stringent security vulnerability gates, and handles automated deployments to a home server infrastructure upon code changes in the main branch.

## 🏗️ System Architecture & Workflow

```text
[ VS Code ] --(git push)--> [ GitHub Repository ]
                                   │
                      ┌────────────┴────────────┐
                      ▼                         ▼
         [ Job 1: SonarQube Scan ]   [ Job 2: Trivy Security Scan ]
         (Code Quality & Smells)       (FS Vulnerability Scanning)
                      │                         │
                      └────────────┬────────────┘
                                   ▼
                   [ Job 3: Build & Push Image ]
                    (Artifacts hosted on GHCR)
                                   │
                                   ▼
                    [ Job 4: Automated Deploy ]
               (Self-hosted Runner triggers Compose)
