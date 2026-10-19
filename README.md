# CloudScope

## Project Overview

CloudScope is a Python-based IT endpoint diagnostics platform designed to help IT technicians troubleshoot Windows computers more efficiently. Instead of manually checking each computer for system information, network settings, running processes, and other diagnostics, CloudScope aims to collect that information through a lightweight agent and make it available to authorized technicians in one place.

The goal is to reduce repetitive troubleshooting tasks, speed up issue investigation, and give IT teams a clearer view of managed computers.

## Features

The following features are planned and are not yet implemented:

- **Windows diagnostic agent:** Collect system information such as CPU and memory usage, disk capacity, operating system details, and uptime.
- **Network diagnostics:** Gather network adapter, IP address, DNS, and connectivity information.
- **Processes and services:** Report running processes and Windows service statuses to assist troubleshooting.
- **Azure backend:** Receive diagnostic reports from registered agents through a secure API.
- **Diagnostic storage:** Store recent system information and historical reports in a database.
- **Technician dashboard:** Allow authorized technicians to search for a computer by hostname and review its diagnostics.
- **Access controls:** Protect endpoint information using agent authentication, technician sign-in, and appropriate permissions.

## Architecture

CloudScope is planned to use a client-agent and cloud-backend architecture:

```text
Windows Computer
       |
       v
  Python Agent
       |
       v
  Azure Backend
       |
       v
    Database
       ^
       |
  Azure Backend API
       ^
       |
Technician Dashboard
```

1. A Python agent runs on a managed Windows computer and collects approved diagnostic information.
2. The agent securely sends diagnostic reports to an API hosted in Microsoft Azure.
3. The backend validates the incoming data and stores it in a database.
4. An authorized technician searches for an endpoint using the dashboard.
5. The dashboard requests the endpoint's stored diagnostic information through the backend API rather than directly accessing the database.

The initial implementation will focus on local diagnostic collection before introducing cloud services and the dashboard.

## Technologies

Planned technologies include:

- **Python:** Endpoint agent and backend development.
- **FastAPI:** HTTP API for receiving and retrieving diagnostic information.
- **pytest:** Automated tests for application behavior.
- **Microsoft Azure:** Cloud hosting and related services.
- **Git and GitHub:** Version control and project management.
- **Future DevOps tools:** CI/CD workflows, containers, infrastructure as code, and deployment automation as the project grows.

The technology choices may change during development.

## Installation

CloudScope is under active development and is not yet ready for end-user installation. To set up the development repository locally:

1. Install Python and Git.
2. Clone the repository and navigate into the project folder:

   ```bash
   git clone <repository-url>
   cd CloudScope
   ```

3. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate the environment:

   **Windows (PowerShell):**
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   **macOS/Linux:**
   ```bash
   source .venv/bin/activate
   ```

5. Once dependencies and a package configuration have been added, installation and test commands will be documented here.

> Replace `<repository-url>` with the actual GitHub repository URL before following these steps.

## Project Status

**Under active development.** CloudScope is being rebuilt around Windows endpoint diagnostics, an Azure-hosted backend, and a technician-facing dashboard. The first development phase will focus on building and testing the local Python diagnostic agent.
