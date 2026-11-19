# Lab 01 - Introduction to Docker Concepts

## 1. Overview

This lab introduces Docker and its role in modern DevOps workflows.

I installed Docker Engine, explored Docker images and containers, checked Docker Hub connectivity, compared containers with virtual machines, tested a container-based DevOps task, and performed cleanup.

## 2. Environment

- Cloud Platform: AWS EC2
- Operating System: Ubuntu 24.04.5 LTS
- Docker Engine: 29.10.0
- Docker Image: Ubuntu 24.04
- Git Branch: main

## 3. Objectives

- Understand basic Docker concepts.
- Install and configure Docker Engine.
- Explore Docker images and containers.
- Connect to Docker Hub.
- Understand containers versus virtual machines.
- Run a simple container-based test.
- Perform Docker resource cleanup.

## 4. Docker Installation

Docker Engine was installed using the official Docker Ubuntu package repository.

Commands:

```bash
docker --version
sudo systemctl enable --now docker
sudo systemctl is-active docker
groups
docker info
```

**Verification:**
- Docker version: 29.10.0
- Docker service: active
- User successfully added to the Docker group.

## 5. Docker Images

A Docker image is a read-only template used to create containers.

Commands:

```bash
docker images
docker pull hello-world
docker images hello-world
docker pull ubuntu:24.04
docker images ubuntu
```

Images explored:
- hello-world
- ubuntu:24.04

## 6. Docker Containers

A container is an instance of a Docker image.

Commands:

```bash
docker run hello-world
docker run --rm hello-world
docker ps -a
docker system df
```

**Result:** The `Hello from Docker!` message appeared successfully.

## 7. Docker Hub Registry

Docker Hub is a public registry for finding and downloading Docker images.

Commands:

```bash
docker search --limit 5 ubuntu
curl -I --max-time 10 https://hub.docker.com
```

**Result:**
- Ubuntu image search successful.
- Docker Hub connectivity confirmed with HTTP 200.

## 8. Docker vs Virtual Machines

Virtual machines run their own guest operating systems and kernels. Linux containers share the host's kernel while providing process and environment isolation.

Kernel verification:

```bash
uname -r
docker run --rm ubuntu:24.04 uname -r
```

**Verified output:**

- Host kernel: `7.0.0-1014-aws`
- Container kernel: `7.0.0-1014-aws`

Both versions matched.

### Container Startup Test

```bash
time docker run --rm ubuntu:24.04 echo "container started"
```

Output: `container started`

Observed real time: **0.724 seconds**

## 9. DevOps Pipeline Test

A disposable Ubuntu container was used to execute a basic test:

```bash
docker run --rm ubuntu:24.04 bash -c 'echo "tests passed" && cat /etc/os-release | head -n 2'
```

Output:

```text
tests passed
PRETTY_NAME="Ubuntu 24.04.5 LTS"
NAME="Ubuntu"
```

The test completed successfully.

## 10. Docker Cleanup

Commands:

```bash
docker rm $(docker ps -aq --filter ancestor=hello-world)
docker rmi hello-world
docker images hello-world
docker ps -a
docker system df
```

**Cleanup results:**
- Hello-world container removed.
- Hello-world image removed.
- No containers remained.
- Ubuntu 24.04 image retained.

## 11. Skills Learned

- Docker Engine installation and configuration.
- Docker image and container management.
- Docker Hub registry access.
- Container lifecycle management.
- Linux kernel sharing.
- Container-based testing.
- Docker cleanup.

## 12. LMS Assessment Result

**Score: 100 / 100**

**Status: PASSED**

Evaluated by Al Baari.

## 13. Evidence

Verification details are available in:

`evidence/verification.txt`
