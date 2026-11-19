# Lab 07 – Dockerfile Basics

## 1. Objective

Understand Dockerfile structure, use a base image, install packages, build a custom Docker image, and run containers from that image.

## 2. Environment

- Host OS: Ubuntu 24.04
- Docker Version: 29.9.0
- Base Image: ubuntu:24.04
- Custom Image: my-ubuntu

## 3. Introduction to Dockerfile

A Dockerfile is a text file containing instructions to build a Docker image.

Each instruction defines a step in the image-building process.

Important instructions:

- `FROM` – selects the base image.
- `ENV` – sets environment variables.
- `RUN` – executes commands during image building.
- `CMD` – defines the default command when a container starts.

## 4. Create Dockerfile

**Command:**

```bash
cat > Dockerfile <<'EOF'
# Use Ubuntu 24.04 as the base image
FROM ubuntu:24.04

# Avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install curl and certificates, then clean package lists
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates && rm -rf /var/lib/apt/lists/*

# Create a file inside the image
RUN echo "built with Dockerfile Basics" > /etc/lab-info

# Default command when the container starts
CMD ["curl", "--version"]
EOF
```

**Result:** Dockerfile created successfully.

## 5. Pull Base Image

**Command:**

```bash
sudo docker pull ubuntu:24.04
```

**Result:** Ubuntu 24.04 image downloaded successfully.

## 6. Build Custom Docker Image

**Command:**

```bash
sudo docker build -t my-ubuntu .
```

**Result:** Image built successfully.

Image name: `my-ubuntu:latest`

## 7. Inspect Docker Image

**Commands:**

```bash
sudo docker images my-ubuntu
sudo docker history my-ubuntu | head
```

**Verified:**

- Custom image was created.
- Docker image layers were displayed.
- Docker history showed the `ENV`, `RUN`, and `CMD` instructions.

## 8. Run Container Using Default CMD

**Command:**

```bash
sudo docker run --rm my-ubuntu
```

**Output:**

```text
curl 8.5.0
```

**Result:** Default CMD executed successfully and displayed curl version information.

## 9. Verify Curl Installation

**Command:**

```bash
sudo docker run --rm my-ubuntu curl --version | head -1
```

**Verified Output:**

```text
curl 8.5.0 (x86_64-pc-linux-gnu)
```

**Result:** Curl was installed successfully inside the custom image.

## 10. Verify File Created by RUN

**Command:**

```bash
sudo docker run --rm my-ubuntu cat /etc/lab-info
```

**Output:**

```text
built with Dockerfile Basics
```

**Result:** File was created successfully inside the image.

## 11. Key Learnings

1. A Dockerfile contains instructions to build an image.
2. `FROM` defines the base image.
3. `ENV` configures environment variables.
4. `RUN` executes commands during image building.
5. Multiple `RUN` instructions can create separate image layers.
6. `CMD` defines the default container command.
7. `docker build` creates a custom image.
8. `docker history` displays image layers and build instructions.
9. `docker run --rm` removes a container after it exits.

## 12. LMS Assessment Result

**Score: 100/100 – PASSED**

All Dockerfile Basics practical tasks were completed and evaluated successfully.
