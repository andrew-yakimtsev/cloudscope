# CloudScope — Project Progress

## Current Milestone
Milestone 3 — Device Diagnostics and Data Collection

## Completed Tasks
- Milestone 1: Project Foundation
  - Created project structure and Python virtual environment.
  - Configured Python packaging and editable installations.
  - Set up Git, GitHub, and `.gitignore`.
  - Created README.md and project documentation.
  - Configured pytest for automated testing.

- Milestone 2: System Information Collection
  - Implemented `get_system_info()` to collect hostname, operating system, processor, CPU cores, and RAM.
  - Implemented `get_disk_info()` to collect disk capacity, used space, free space, and usage percentage.
  - Implemented `get_uptime_info()` to collect system boot time and calculate uptime.
  - Added automated tests for system, disk, and uptime information.

- Milestone 3: Device Diagnostics and Data Collection
  - Created the `DeviceInfo` dataclass with 17 diagnostic fields.
  - Implemented `collect_device_info()` to combine system, disk, and uptime information into a structured object.

## Current Task
- Create automated tests for `collect_device_info()` using pytest's `monkeypatch` fixture.
- Verify that the collector correctly combines simulated diagnostic information.
- Run the complete pytest test suite.

## Technologies Learned
- Python virtual environments
- Git branching and pull requests
- Python packaging and editable installations
- pytest and automated testing
- Python `platform` module
- `psutil` library
- Python `datetime` module
- Dictionaries and dictionary merging (`|`)
- Dictionary unpacking (`**`)
- Dataclasses and type annotations
- Modular Python project organization
- System resource and uptime monitoring

## Known Issues
- No confirmed issues reported.
- Collector tests have not yet been verified as passing.

## Upcoming Milestones
- Complete Milestone 3: Device Diagnostics and Data Collection
- Performance and Network Diagnostics
  - CPU and memory utilization
  - Network adapter information
  - IP addresses and DNS configuration
  - Network connectivity diagnostics
- Azure Backend Integration
- Technician Dashboard Development
- DevOps Automation and Deployment

## Project Status
CloudScope is under active development. Milestones 1 and 2 are complete, and Milestone 3 is in progress. The project is focused on building a Python-based IT endpoint diagnostics platform that will eventually send diagnostic information to Microsoft Azure for authorized IT technicians to access.