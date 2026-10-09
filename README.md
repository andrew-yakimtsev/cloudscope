# CloudScope

## Overview

CloudScope is a Python-based cloud monitoring and automation project designed to help monitor websites, services, and cloud infrastructure. Its goal is to make it easier to track system health, identify potential problems, and reduce manual monitoring tasks.

## Features

The following features are planned for future development:

- **Monitoring:** Monitor websites and APIs to check their availability and response status.
- **Incident Detection:** Identify service failures and other potential issues.
- **Azure Integration:** Connect with Microsoft Azure to monitor cloud resources.
- **Automation:** Automate monitoring tasks and reduce manual work.
- **Incident Tracking:** Record detected issues for troubleshooting and analysis.

## Technology Stack

CloudScope plans to use the following technologies:

- **Python:** Main programming language for backend development and automation.
- **FastAPI:** Framework for building APIs.
- **Microsoft Azure:** Cloud platform for hosting and monitoring services.
- **Terraform:** Infrastructure as Code for managing cloud resources.
- **Docker:** Containerization for consistent application deployment.
- **GitHub Actions:** Automated testing and deployment through CI/CD pipelines.
- **Pytest:** Framework for writing and running automated tests.

## Getting Started

To set up CloudScope locally:

1. Clone the repository:

   ```bash
   git clone https://github.com/andrew-yakimtsev/cloudscope.git
   cd cloudscope
   ```

2. Create a Python virtual environment:

   ```bash
   python3 -m venv .venv
   ```

3. Activate the virtual environment on macOS or Linux:

   ```bash
   source .venv/bin/activate
   ```

4. Install the project (once its package configuration is ready):

   ```bash
   python -m pip install -e .
   ```

5. Install pytest if needed and run the existing tests:

   ```bash
   python -m pip install pytest
   python -m pytest -v
   ```

## Project Status

CloudScope is currently in the **early stages of development**.

The initial project setup, Git version control, and basic Python testing have been completed. The first automated test verifies whether an HTTP status code represents a successful response.

Core monitoring functionality, Azure integration, containerization, and automated deployment are planned for future development.