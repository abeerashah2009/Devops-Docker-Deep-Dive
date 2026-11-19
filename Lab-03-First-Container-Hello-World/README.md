# Lab 03 - First Container: Hello World

## 1. Lab Overview

**Topic:** First Container - Hello World
**Platform:** Ubuntu 24.04 LTS
**Tool:** Docker
**LMS Score:** 100 / 100
**Result:** PASSED

### Objectives

- Understand the basics of Docker containers.
- Pull images from Docker Hub.
- Run and execute Docker containers.
- Verify container execution through output.
- Remove containers and images after testing.

---

## 2. Docker Installation Verification

Docker was already installed on the lab VM. I verified the official Docker APT repository, signing key, installed packages, and running service.

### Commands

```bash
docker --version
sudo docker compose version
systemctl is-active docker
```

### Important Notes

- `docker --version` displays the installed Docker version.
- `docker compose version` checks Docker Compose.
- `systemctl is-active docker` checks whether Docker is running.

**Verified:** Docker service was active.

---

## 3. Pull the Hello World Image

Docker Hub is a public registry where Docker images are stored and shared.

### Command

```bash
sudo docker pull hello-world
```

### Verify the Image

```bash
sudo docker images hello-world
```

### Result

- Image downloaded successfully.
- Repository: `hello-world`
- Tag: `latest`
- Image ID: `1e4c05b897a7`

### Important Notes

- `docker pull` downloads an image from a registry.
- `hello-world` is the image name.
- `latest` is the default image tag.

---

## 4. Run the First Docker Container

### Command

```bash
sudo docker run hello-world
```

### Expected Output

```text
Hello from Docker!
```

Docker displayed the successful execution message.

### What Happened?

1. Docker client contacted the Docker daemon.
2. Docker daemon used the Hello World image.
3. Docker created a container from the image.
4. The container executed its program.
5. Docker displayed the output in the terminal.

---

## 5. Verify the Container

### Command

```bash
sudo docker ps -a
```

### Verified Result

| Item | Value |
|---|---|
| Container ID | bf69d9956a92 |
| Image | hello-world |
| Command | /hello |
| Status | Exited (0) |

### Important Notes

- `docker ps` displays running containers.
- `docker ps -a` displays all containers, including stopped containers.
- `Exited (0)` means the container completed successfully.

---

## 6. Verify the Exact Output

### Command

```bash
sudo docker run --rm hello-world | grep 'Hello from Docker!'
```

### Output

```text
Hello from Docker!
```

### Explanation

- `--rm` automatically removes the container after execution.
- `grep` searches for the required text.
- The expected message appeared successfully.

---

## 7. Clean Up Docker Resources

After completing the practical, I removed the stopped container and the Hello World image.

### Remove the Container

```bash
sudo docker rm $(sudo docker ps -aq --filter ancestor=hello-world)
```

### Remove the Image

```bash
sudo docker image rm hello-world
```

### Verify Cleanup

```bash
sudo docker images hello-world
```

### Result

- Container removed successfully.
- Image untagged and deleted successfully.
- Final image listing showed no Hello World image.

---

## 8. Important Docker Commands - Quick Revision

| Command | Purpose |
|---|---|
| `docker --version` | Check Docker version |
| `docker pull IMAGE` | Download an image |
| `docker images` | List local images |
| `docker run IMAGE` | Create and run a container |
| `docker ps` | List running containers |
| `docker ps -a` | List all containers |
| `docker rm CONTAINER` | Remove a container |
| `docker image rm IMAGE` | Remove an image |

---

## 9. What I Learned

- Docker images are used to create containers.
- Docker Hub stores and distributes images.
- A container runs an application from an image.
- Docker client communicates with the Docker daemon.
- `Exited (0)` indicates successful container execution.
- Containers and images can be removed after testing.

---

## 10. Final Lab Result

**LMS Evaluation:** Al Baari
**Score:** 100 / 100
**Status:** PASSED

The Hello World container executed successfully. Image pulling, container execution, output verification, and cleanup were completed.

**Lab 03 successfully completed.**
