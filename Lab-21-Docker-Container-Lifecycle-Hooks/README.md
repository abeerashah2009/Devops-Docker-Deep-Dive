# Lab 21 - Docker Container Lifecycle Hooks

## 1. Lab Overview

This lab demonstrates Docker container lifecycle startup configuration using ENTRYPOINT and CMD instructions.

**LMS Score: 100 / 100 — Passed**

## 2. Objectives

- Understand Docker ENTRYPOINT and CMD.
- Learn how ENTRYPOINT and CMD work together.
- Pass runtime arguments to containers.
- Override CMD and ENTRYPOINT at runtime.

## 3. Environment

- OS: Ubuntu 24.04 LTS
- Docker Engine: 29.9.0
- Docker Buildx: v0.38.0
- Docker Compose: v5.6.0
- Base Image: Alpine 3.20

## 4. Project Structure

```text
Lab-21-Docker-Container-Lifecycle-Hooks/
├── Dockerfile
└── README.md
```

## 5. Dockerfile

```dockerfile
FROM alpine:3.20

ENTRYPOINT ["echo"]

CMD ["Hello, world!"]
```

## 6. Build Docker Image

Command:

```bash
sudo docker build -t my-echo-app .
```

Result: Docker image built successfully.

Image name: `my-echo-app:latest`

## 7. Run Container with Default CMD

Command:

```bash
sudo docker run --rm my-echo-app
```

Output:

```text
Hello, world!
```

The default ENTRYPOINT and CMD worked successfully.

## 8. Override CMD at Runtime

Command:

```bash
sudo docker run --rm my-echo-app "Docker is awesome!"
```

Output:

```text
Docker is awesome!
```

The runtime argument replaced the default CMD while ENTRYPOINT remained active.

## 9. Override ENTRYPOINT at Runtime

Command:

```bash
sudo docker run --rm --entrypoint sh my-echo-app \
-c 'echo "Entrypoint replaced; running as: $(whoami)"'
```

Output:

```text
Entrypoint replaced; running as: root
```

The `--entrypoint` option replaced the default ENTRYPOINT.

## 10. Inspect Docker Image Configuration

Command:

```bash
sudo docker inspect --format '{{.Config.Entrypoint}} {{.Config.Cmd}}' my-echo-app
```

Output:

```text
[echo] [Hello, world!]
```

The image contains the expected ENTRYPOINT and CMD settings.

## 11. Important Concepts

### ENTRYPOINT

Defines the main executable that runs when a container starts.

### CMD

Provides default arguments or a default command.

### Runtime Arguments

Arguments supplied after the image name replace the default CMD when ENTRYPOINT is configured.

### ENTRYPOINT Override

The `--entrypoint` option replaces the executable defined in the Dockerfile.

### --rm

Automatically removes a container after it exits.

## 12. Final Verification

- Docker image built successfully.
- Default CMD output verified.
- Runtime CMD override verified.
- Runtime ENTRYPOINT override verified.
- Docker image configuration inspected.
- All practical tests passed.

## 13. LMS Result

**Final Score: 100 / 100**

**Status: PASSED**

## 14. Conclusion

I successfully completed Docker Container Lifecycle Hooks.

I learned how ENTRYPOINT and CMD work together, how to override CMD using runtime arguments, and how to replace ENTRYPOINT when starting a container.
