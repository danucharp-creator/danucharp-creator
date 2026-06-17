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

🛠️ Technology Stack & Infrastructure
CI/CD Orchestrator: GitHub Actions
Code Quality Platform: SonarQube Server (LTS Community Edition)
Security Scanner: Aquasecurity Trivy
Container Registry: GitHub Container Registry (GHCR)
Containerization: Docker & Docker Compose
Runner Environment: Linux Ubuntu via WSL2 (Self-hosted Runner)

⚡ Key Automation & Engineering Features
Strict Security Gate: The pipeline automatically terminates (Fail Pipeline) if Trivy detects any CRITICAL vulnerability within the source files. This acts as a security gate to ensure zero vulnerable code reaches the compilation/build stage.

Automated Resource Optimization: The deployment stage executes docker image prune -f immediately post-deployment. This guarantees that dangling/legacy images are purged, maintaining tight storage control on the host server.

Optimized Container Lifecycle: Tailored docker-compose.yml logic to suit specific script behaviors, ensuring containers exit smoothly with status Exited (0) rather than falling into an infinite crash-restart loop.

🎯 Project Roadmap (Next Milestones)
[x] Phase 1: Dockerization & Basic CI/CD Pipeline Configuration
[x] Phase 2: Integration of Automated Code Quality (SonarQube) and Security Gate (Trivy)
[ ] Phase 3: Centralized Monitoring (Prometheus & Grafana Dashboard) to track host and container metrics
[ ] Phase 4: Real-time Incident Notification via Chat Webhook (LINE / Discord Notification Gate)

🚀 How to Run & Setup Local Server
1. Spin up SonarQube on Local Host
Bash
docker run -d --name sonarqube -p 9000:9000 sonarqube:lts-community
Note: Ensure Linux kernel parameters are adjusted using sysctl -w vm.max_map_count=262144 before initial execution. Generate a User Token and map it to GitHub Secrets as SONAR_TOKEN.

2. Configure and Initialize Self-hosted Runner
Bash
# Install mandatory extraction utility for CLI binaries
sudo apt update && sudo apt install -y unzip

# Start the listener daemon
./run.sh
💡 Designed, architected, and maintained by a dedicated System Engineer specialized in Infrastructure & Automation.
