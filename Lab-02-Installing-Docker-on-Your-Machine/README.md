# Lab 02 - Installing Docker on Your Machine

## Overview
This lab covers installing, configuring, and verifying Docker Engine on Ubuntu 24.04 LTS.

The practical uses the official Docker APT repository and installs Docker Engine, Docker CLI, containerd, Docker Buildx, and Docker Compose.

## Environment
- Operating System: Ubuntu 24.04.5 LTS
- Architecture: x86_64
- Platform: AWS EC2
- Docker Engine: 29.10.0
- Docker Compose: 5.8.0
- Docker Buildx: 0.39.0

## Task 1 - Docker Installation

### 1.1 Windows Installation
Not applicable. This practical was performed on an Ubuntu Linux environment.

### 1.2 macOS Installation
Not applicable. This practical was performed on an Ubuntu Linux environment.

### 1.3 Linux Installation
Verified the official Docker APT repository configuration and signing key.

Installed the required packages:

- docker-ce
- docker-ce-cli
- containerd.io
- docker-buildx-plugin
- docker-compose-plugin

Updated package lists and installed the latest available packages from the official Docker repository.

## Task 2 - Docker Verification

Verified the following commands:

```bash
docker --version
docker compose version
docker buildx version
docker info
```

All commands completed successfully.

Added the current Ubuntu user to the Docker group to allow Docker commands without `sudo`.

## Task 3 - Docker Daemon Verification

Enabled and started Docker:

```bash
sudo systemctl enable --now docker
```

Verified the service:

```bash
sudo systemctl is-active docker
systemctl status docker --no-pager
```

Result: Docker service was active and running, and enabled at startup.

## Hello World Container Test

Executed:

```bash
docker run --rm hello-world
```

The Docker image was downloaded successfully and the container ran successfully.

Expected verification output:

```text
Hello from Docker!
```

## Learning Outcomes

- Installed Docker Engine using the official Docker repository.
- Understood Docker package components.
- Verified Docker CLI, Compose, and Buildx.
- Enabled and started the Docker daemon.
- Configured Docker group membership.
- Inspected Docker system information.
- Successfully executed the Hello World container.

## Result

All applicable practical installation and verification tasks were completed successfully on Ubuntu 24.04.5 LTS.

Windows and macOS installation tasks were not applicable to this Linux-based environment.

LMS score: Pending confirmation.
